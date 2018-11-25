import datetime

from RiskServiceApp.models import LogBlock
from RiskServiceApp.models import LogRow


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LogParserAndCalculateRiskValuesService(metaclass=Singleton):
    def __init__(self):
        self.log_blocks_map = {}
        self.has_been_run = False;
        self.is_running = False;
        self.running_date = datetime.datetime.now();
        self.update_date = datetime.datetime.now();
    pass


class LogService:
    def __init__(self):
        self.log = LogParserAndCalculateRiskValuesService()

    def populate_log(self,logfile):
        for line in logfile:
            line_str = line.decode("utf-8").strip()
            date = line_str.split()[0];
            time = line_str.split()[1];
            vm_name = line_str.split()[2];
            vm_id = line_str.split()[3];
            first_index = len(date) + 1
            first_index = first_index + len(time) + 1
            first_index = first_index + len(vm_name) + 1
            first_index = first_index + len(vm_id) + 1
            log_message  = line_str[first_index:len(line_str)];
            #print(line_str)
            #print(date)
            #print(time)
            #print(vm_name)
            #print(vm_id)
            #print(log_message)
            log_row = LogRow(date, time, vm_name, vm_id, log_message)
            lob_block = self.log.log_blocks_map.get(vm_id, LogBlock(vm_name,vm_id))
            lob_block.add_log_rows(log_row);
            self.log.log_blocks_map[vm_id]= lob_block


    def print_logs(self):
        for k, v in self.log.log_blocks_map.items():
            for log_row in v.log_rows:
                print(log_row.date)
                print(log_row.time)
                print(log_row.vm_name)
                print(log_row.vm_id)
                print(log_row.log_message)





