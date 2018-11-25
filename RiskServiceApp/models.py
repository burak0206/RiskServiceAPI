class LogRow:
    def __init__(self, date, time, vm_name, vm_id, log_message,):
        self.date = date
        self.time = time
        self.vm_name = vm_name
        self.vm_id = vm_id
        self.log_message = log_message


class LogBlock:
    def __init__(self, log_rows):
        self.log_rows = log_rows

    def add_log_rows(self, log_row):
        self.log_rows.append(log_row)