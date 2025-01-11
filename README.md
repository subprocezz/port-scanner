# Project Documentation: Port Scanner

## Description

This script allows you to scan a range of ports on a network device to identify which ones are open. It uses Python's `asyncio` and `socket` modules to attempt TCP connections on specified ports and report the results. Additionally, it detects services associated with open ports and supports scanning custom port ranges via command-line arguments.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Usage Example](#usage-example)
- [Contributions](#contributions)
- [License](#license)

## Features

- Scans a range of ports from 1 to 1024 (default), or custom ports specified by the user.
- Detects open ports and identifies the service running on each open port (e.g., HTTP, SSH).
- Asynchronous scanning for faster performance.
- Customizable port ranges and support for specific ports.
- Displays scan duration.
  
## Requirements

- Python 3.7 or higher.
- `socket` (standard Python library).
- `argparse` (standard Python library).
- `asyncio` (standard Python library).

## Installation

1. Ensure you have Python 3.7+ installed.
2. Clone the repository or download the script file.
3. No additional dependencies are required as all libraries are part of Python's standard library.

## Usage

To run the script, execute the following command in your terminal:

```bash
python port_scanner.py <target> --ports <port_range>

Parameters

    target: IP address or hostname of the device you want to scan (e.g., 127.0.0.1 or google.com).
    --ports: Range of ports to scan, which can be specified as a range (e.g., 1-1024) or a comma-separated list of ports (e.g., 22,80,443).
```

Example Usage

    Scan a range of ports (e.g., 1-1024):
```bash
python port_scanner.py google.com --ports 1-1024
```
Scan specific ports (e.g., 22, 80, 443):
```bash
python port_scanner.py google.com --ports 22,80,443
```
Default scan for ports 1-1024:
```bash
python port_scanner.py google.com
```

Example Output

When you run the script, it will display the open ports along with their corresponding services. An example output might look like this:
```bash
Open ports and their services:
Port 22 is open. Service: ssh
Port 80 is open. Service: http
Port 443 is open. Service: https

Scanning completed in 3.45 seconds.
```
## Contributions

Contributions are welcome! If you would like to contribute to this project, please follow these steps:
```
    Fork the repository.
    Create a new branch (git checkout -b feature/new-feature).
    Make your changes and commit (git commit -m 'Add new feature').
    Push to the branch (git push origin feature/new-feature).
    Open a Pull Request.
```
## License

This project is licensed under the MIT License. See the LICENSE file for more details.
