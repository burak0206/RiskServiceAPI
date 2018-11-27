import datetime


class LogRow:
    def __init__(self, date, time, vm_name, vm_id, log_message):
        self.date = date
        self.time = time
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.log_message = log_message


class LogBlock:
    def __init__(self,vm_name,vm_id,date,time):
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.date = date
        self.time = time
        self.log_rows = []

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
        self.cache_is_user_known_map = {}
        self.cache_is_client_known_map = {}
        self.cache_is_ip_known_map = {}
    pass

