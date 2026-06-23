import logging

class SimpleFileLogger:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(data + "\n")

    def read_all(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            return "File not found."

logger = SimpleFileLogger("my_lab_log.txt")

logger.write_data("Entry 1: System Online")
logger.write_data("Entry 2: Sensor Active")

all_logs = logger.read_all()
for line in all_logs:
    print(line.strip())
