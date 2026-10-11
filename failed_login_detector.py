# Automated Failed Login Detection System
# Reads login records and identifies suspicious IP addresses.

from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).with_name("login_attempts.log")
THRESHOLD = 5


def analyze_log_file():
    failed_logins = Counter()

    # Open and read the login log file
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()

            # Each record contains date, time, IP, and status
            if len(parts) != 4:
                continue

            date, time, ip_address, status = parts

            if status == "FAILED":
                failed_logins[ip_address] += 1

    return failed_logins


def main():
    print("Automated Failed Login Detection System")
    print("---------------------------------------")

    try:
        failed_logins = analyze_log_file()
    except FileNotFoundError:
        print("ERROR: Login log file not found.")
        return

    for ip_address, count in failed_logins.items():
        print(f"\nIP Address: {ip_address}")
        print(f"Failed Login Attempts: {count}")

        if count >= THRESHOLD:
            print("ALERT: Suspicious activity detected!")
        else:
            print("Status: Below alert threshold")
    generate_report(failed_logins)

def generate_report(failed_logins):
    report_file = "security_report.txt"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("Security Alert Report\n")
        file.write("---------------------\n")

        suspicious_found = False

        for ip_address, count in failed_logins.items():
            if count >= THRESHOLD:
                suspicious_found = True
                file.write(f"Suspicious IP: {ip_address}\n")
                file.write(f"Failed Attempts: {count}\n")
                file.write("Status: ALERT\n\n")

        if not suspicious_found:
            file.write("No suspicious activity detected.\n")

    print(f"\nSecurity report saved to {report_file}")

if __name__ == "__main__":
    main()
