# Automated Failed Login Detection System

## Project Overview
This project is a Python-based cybersecurity automation tool designed to detect repeated failed login attempts and identify suspicious IP addresses.

## How It Works
The program reads login activity from a log file and counts failed login attempts for each IP address.

If an IP address has five or more failed login attempts, the system generates a security alert.

## Project Features
- Analyzes login activity using Python
- Identifies failed login attempts
- Tracks suspicious IP addresses
- Uses a threshold of five failed attempts
- Automatically generates a security report
- Saves results to a text file

## Project Files
- failed_login_detector.py - Main Python program
- login_attempts.log - Sample login data
- security_report.txt - Generated security report

## How to Run
1. Download the project files.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

    python3 failed_login_detector.py

5. Review the results in the terminal and security_report.txt.

## Testing Results
The program successfully identified IP address 192.168.1.10 with five failed login attempts and generated a security alert.

Other IP addresses with fewer than five failed attempts remained below the alert threshold.

## What I Learned
Through this project, I learned how Python can be used to automate cybersecurity tasks, analyze login activity, identify suspicious behavior, and generate security reports. This helped me better understand how security automation can assist with monitoring potential threats.
