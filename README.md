# NetPlus

Network monitoring and automation tool written in Python.

NetPlus is a Python-based network monitoring system designed to check network devices availability, establish SSH connections, collect device information, create configuration backups, generate reports, and send alerts when problems occur.

The goal of this project is to automate repetitive network operations and provide a simple foundation for network automation workflows.

---

## Features

### Device Monitoring

* ICMP Ping check for network devices
* Detect reachable and unreachable devices
* Traceroute automatically runs when a device is unreachable

### SSH Automation

* Connect to network devices using SSH
* Execute multiple commands remotely
* Collect command outputs

### Configuration Backup

* Automatically save device configurations
* Store backups with organized file structure

### Alert System

* Email notifications for detected errors
* Telegram notifications support

### Reporting

* Generate HTML reports from monitoring results
* Automatically open the latest report after execution

### Logging

* Standard logging system
* Store application events and errors

### Multithreading

* Monitor multiple devices simultaneously
* Improve monitoring speed using ThreadPoolExecutor

---

## Technologies

* Python 3
* Paramiko
* Requests
* JSON
* Logging
* ThreadPoolExecutor

---

## Project Structure

```
NetPlus/
│
├── alert/
│   ├── alert_manager.py
│   ├── email_alert.py
│   └── telegram_alert.py
│
├── checker/
│   ├── ping.py
│   ├── ssh.py
│   └── traceroute.py
│
├── loader/
│   ├── config_loader.py
│   └── device_loader.py
│
├── backups/
│
├── reports/
│
├── main.py
├── backup.py
├── report.py
├── logger.py
├── config.example.json
├── devices.example.json
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MahdiValizadeh/NetPlus.git
```

Go to project directory:

```bash
cd NetPlus
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create your configuration file:

```
config.json
```

based on:

```
config.example.json
```

Configure:

* SSH credentials
* Email settings
* Telegram bot token
* Device list
* Monitoring commands

---

## Running

Run the application:

```bash
python main.py
```

Example output:

```
Core-R1 (10.0.1.190) 🟢 UP
Core-R2 (10.0.6.23) 🟢 UP
Core-R3 (10.10.10.10) 🔴 DOWN

Email Sent
Report Generated
```

---

## Future Improvements

Planned features:

* SQLite-based device management
* Automatic scheduling
* Better database reporting
* Docker support
* Web dashboard
* More network vendors support

---

## Author

Mahdi Valizadeh

Python Network Automation Project
