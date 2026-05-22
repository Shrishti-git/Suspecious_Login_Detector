# Suspicious Login Detector

A beginner cybersecurity project that detects suspicious login attempts using Python and log analysis.

## Features
- Detects failed login attempts
- Identifies suspicious IP addresses
- Generates security alerts
- Reads login data from CSV logs

## Technologies Used
- Python
- Pandas

## Project Structure

Suspecious_login_Detector/
│
├── logs/
│   └── sample_logins.csv
│
├── src/
│   └── detector.py
│
├── requirements.txt
└── README.md

## How to Run

1. Install dependencies:
pip install pandas

2. Run the project:
cd src
python detector.py

## Example Output

ALERT: Suspicious IP detected -> 192.168.1.1
Failed Attempts: 3