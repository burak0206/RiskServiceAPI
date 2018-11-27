import datetime
from datetime import timedelta
import re

from RiskServiceApp.models import LogBlock
from RiskServiceApp.models import LogRow
from RiskServiceApp.models import RiskValuesModel


class LogPopulateService:
    def __init__(self):
        self.risk_values_model = RiskValuesModel()

    def populate_log_into_risk_values_model(self,logfile):
        for line in logfile:
            line_str = line.decode("utf-8").strip()
            date = line_str.split()[0];
            time = line_str.split()[1];
            vm_name = line_str.split()[2];
            vm_id = line_str.split()[3];
            first_index = len(date) + len(time) + len(vm_name) + len(vm_id) + 4
            log_message = line_str[first_index:len(line_str)];
            if (not (
                    log_message == "ag_userd Updating ad data" or log_message == "ag_userd Start to search for AD groups"
                    or log_message == "ag_distd updated file /var/opt/appgate/conf/agclient.properties" or
                    "ag_galed statistics: up 0 packets" in log_message or "status 1 session load" in log_message
                    or "sessions load" in log_message)):
                log_row = LogRow(date, time, vm_name, vm_id, log_message)
                lob_block = self.risk_values_model.log_blocks_map.get(vm_id, LogBlock(vm_name, vm_id, date, time))
                lob_block.add_log_rows(log_row);
                self.risk_values_model.log_blocks_map[vm_id] = lob_block
        self.risk_values_model.cache_is_user_known_map = {}
        self.risk_values_model.cache_is_client_known_map = {}
        self.risk_values_model.cache_is_ip_known_map = {}


class GettingRiskValuesService:
    def __init__(self):
        self.risk_values_model = RiskValuesModel()

    def is_user_known(self, username):
        if username in self.risk_values_model.cache_is_user_known_map:
            return self.risk_values_model.cache_is_user_known_map[username]
        login_message = "login " + username + " from"
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                if login_message in log_row.log_message:
                    self.risk_values_model.cache_is_user_known_map[username] = True
                    return True;
        self.risk_values_model.cache_is_user_known_map[username] = False
        return False;

    def is_client_known(self, clientid):
        if clientid in self.risk_values_model.cache_is_client_known_map:
            return self.risk_values_model.cache_is_client_known_map[clientid]
        client_message = "sshd Client protocol 2.0; client software version libssh2_1.4.2; AppGate version " + clientid
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                if client_message in log_row.log_message:
                    self.risk_values_model.cache_is_client_known_map[clientid] = True;
                    return True;
        self.risk_values_model.cache_is_client_known_map[clientid] = False;
        return False;

    def is_ip_known(self, ip):
        connect_message = "connect to port"
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                if connect_message in log_row.log_message:
                    if log_row.log_message.split()[5] == ip:
                        return True;
        return False;

    def is_ip_internal(self, ip):
        p = re.compile('(^127\.)| (^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)')
        return p.match(ip) is not None

    def failed_login_count_last_week(self,number_of_weeks):
        count = 0;
        last_week_date_time = datetime.datetime.now() - timedelta(weeks=int(number_of_weeks));
        for k, v in self.risk_values_model.log_blocks_map.items():
            date_time_str = v.date[0:4]+"-"+v.date[4:6]+"-"+v.date[6:8]+" "+v.time
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
            failed_message = "sshd Failed"
            if last_week_date_time < date_time_obj:
                for log_row in v.log_rows:
                    if failed_message in log_row.log_message:
                        count += 1
        return count;
