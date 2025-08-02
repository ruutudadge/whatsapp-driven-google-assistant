import csv
import os
from datetime import datetime

LOG_FILE = os.getenv("LOG_FILE", "log.csv")

def log_action(user, command, response):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["timestamp", "user", "command", "response"])
        writer.writerow([datetime.now(), user, command, response])
