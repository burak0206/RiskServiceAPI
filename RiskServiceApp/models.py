import datetime


class LogRow:
    def __init__(self, date, time, vm_name, vm_id, log_message):
        self.date = date
        self.time = time
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.log_message = log_message


class LogBlock:
    def __init__(self,vm_name,vm_id):
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.user = ""
        self.ip = ""
        self.client_id = ""
        self.log_rows = []
        self.number_of_success_login = 0;
        self.number_of_failed_login = 0;

    def add_log_rows(self, log_row):
        self.log_rows.append(log_row)

    def post_complete_log_block(self):
        print(self.client_id)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RiskValuesModel(metaclass=Singleton):
    def __init__(self):
        self.log_blocks_map = {}
        self.has_been_run = False;
        self.is_running = False;
        self.running_date = datetime.datetime.now();
        self.update_date = datetime.datetime.now();
    pass
