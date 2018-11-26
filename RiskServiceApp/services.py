import datetime

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
                lob_block = self.risk_values_model.log_blocks_map.get(vm_id, LogBlock(vm_name,vm_id))
                lob_block.add_log_rows(log_row);
                self.risk_values_model.log_blocks_map[vm_id]= lob_block

    def print_logs(self):
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                print(log_row.date)
                print(log_row.time)
                print(log_row.vm_name)
                print(log_row.vm_id)
                print(log_row.log_message)

    def handle_uploaded_file(self):
        with open('name.txt', 'wb+') as destination:
            for k, v in self.risk_values_model.log_blocks_map.items():
                for log_row in v.log_rows:
                    destination.write(" ".join([log_row.date,log_row.time,log_row.vm_name,log_row.vm_id,log_row.log_message]).encode("utf-8"))
                    destination.write("\n".encode("utf-8"));


class GettingRiskValuesService:
    def __init__(self):
        self.risk_values_model = RiskValuesModel()

    def handle_uploaded_file(self):
        with open('name2.txt', 'wb+') as destination:
            for k, v in self.risk_values_model.log_blocks_map.items():
                for log_row in v.log_rows:
                    destination.write(" ".join([log_row.date,log_row.time,log_row.vm_name,log_row.vm_id,log_row.log_message]).encode("utf-8"))
                    destination.write("\n".encode("utf-8"));

    def is_user_known(self, username):
            return self.is_this_user_logged_in(username)

    def is_this_user_logged_in(self,username):
        login_message = "login " + username + " from"
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                if login_message in log_row.log_message:
                    return True;
        return False;

    def is_ip_known(self, ip):
        return self.is_any_user_logged_in_this_ip(ip)

    def is_any_user_logged_in_this_ip(self,ip):
        connect_message = "connect to port"
        for k, v in self.risk_values_model.log_blocks_map.items():
            for log_row in v.log_rows:
                if connect_message in log_row.log_message:
                    if log_row.log_message.split()[5] == ip:
                        return True;
        return False;
