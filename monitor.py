import os
import time

LOG_FILE = "/var/log/syslog"  # Change this based on your system (e.g., /var/log/auth.log)
REPORT_FILE = "log_report.txt"

def tail_log(log_file):
    """Continuously monitor the log file."""
    print(f"Monitoring {log_file} for new log entries...")
    
    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                process_log(line)
            else:
                time.sleep(1)

def process_log(line):
    """Check for specific log patterns and save reports."""
    keywords = ["error", "failed", "warning", "unauthorized"]
    
    for keyword in keywords:
        if keyword in line.lower():
            print(f"ALERT: {line.strip()}")
            save_to_report(line)
            break  # Stop checking after the first keyword match

def save_to_report(log_entry):
    """Save the filtered log to a report file."""
    with open(REPORT_FILE, "a") as report:
        report.write(log_entry)

if __name__ == "__main__":
    if not os.path.exists(LOG_FILE):
        print(f"Error: Log file {LOG_FILE} not found!")
    else:
        tail_log(LOG_FILE)

