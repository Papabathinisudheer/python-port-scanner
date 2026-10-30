# CODTECH Internship Project Report
## Python Port Scanner

### 1. Introduction
A port scanner is a network utility used to check whether
TCP ports on a target system accept connections. This project
implements a basic port scanner using Python socket programming.

### 2. Objective
The objective is to learn Python networking and identify
reachable TCP ports on an authorized system.

### 3. Tools and Technologies
- Programming Language: Python 3
- Library: socket
- Library: datetime
- Development Environment: Android Python IDE or desktop Python

### 4. Methodology
1. Accept a hostname or IP address.
2. Resolve the hostname into an IP address.
3. Accept a starting and ending port.
4. Create a TCP socket for each port.
5. Attempt a connection with a timeout.
6. Record ports where the connection succeeds.
7. Display the results.

### 5. Expected Result
The program displays the target IP address and any TCP ports
that accept connections within the selected range. Results
depend on the target system and its current configuration.

### 6. Limitations
- This version scans TCP ports only.
- A failed connection does not always mean a port is closed.
- Firewalls and network restrictions may affect results.
- Large scans are limited to 1000 ports per run.

### 7. Conclusion
This project demonstrates basic TCP socket programming,
hostname resolution, input validation, and network troubleshooting
using Python.

### 8. Ethical Use
Testing must be restricted to systems owned by the tester
or systems for which explicit authorization has been granted.

### 9. Author
Papabathini Venkat Sudheer
