
# Python Port Scanner

**Internship:CODTECH  
**Project:Python Port Scanner  
**Author:Venkat Sudheer

## 1. Project Overview
This project is a basic TCP port scanner developed using Python.
It checks a specified range of TCP ports on an authorized target
and displays ports that accept TCP connections.

## 2. Objectives
- Understand TCP socket programming.
- Learn basic network port scanning.
- Identify reachable TCP ports.
- Practice Python exception handling.

## 3. Technologies Used
- Python 3
- socket module
- datetime module

## 4. Features
- Accepts a hostname or IP address.
- Allows the user to specify a port range.
- Displays ports where TCP connections succeed.
- Validates port-range input.
- Handles hostname resolution errors.

## 5. Requirements
- Python 3
- No external Python packages required.

## 6. How to Run
1. Save the source code as `port_scanner.py`.
2. Open a terminal or Python IDE.
3. Run:

   python port_scanner.py

4. Enter `localhost` as the initial test target.
5. Enter the starting and ending port numbers.

## 7. Example
Target: localhost
Starting port: 1
Ending port: 100

The program displays any open ports found.
Actual results depend on the target system and its services.

## 8. Security Note
Use this tool only on systems you own or have explicit
permission to test. Scan only the ports required for your test.

## 9. Author
Venkat Sudheer
