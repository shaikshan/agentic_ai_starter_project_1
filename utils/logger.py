import datetime
import os

class Logger:
    def __init__(self, log_file='outputs/logs.txt'):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f"[{timestamp}] {message}"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(entry + '\n')
