# LemTCP: Efficient and User-friendly Port Scanning Tool

LemTCP, written in Python, is an easy-to-use and efficient port scanning tool that checks ports within a specified range on a given IP address and identifies the status of these ports (open or closed). Furthermore, it endeavors to determine the names of the services running on these open ports.

## Table of Contents

- [Code Anatomy](#code-anatomy)
- [Benefits](#benefits)
- [Installation](#installation)
- [Usage](#usage)
- [Updates & Future Plans](#updates--future-plans)
- [Conclusion](#conclusion)
- [License](#license)

## Code Anatomy

LemTCP processes user-input arguments using Python's `argparse` library. These arguments include the IP address to be scanned, the range of ports, the file path to print the results, and an option to only display open ports.

Next, it creates a TCP/IP socket with the `socket` library and tries to establish a connection at the specified IP address for each port in the range. If a connection attempt is successful (i.e., the port is open), it attempts to identify the name of the service running on the port using the `socket.getservbyport` function.

LemTCP scans all the ports in the specified range concurrently, leveraging Python's `concurrent.futures` library. This significantly expedites the scanning process.

Finally, it displays the scan results on the screen and prints them to a specified file, enabling users to save and review the results later.

## Benefits

- **Network Security**: Open ports are potential vulnerabilities. LemTCP helps you identify open ports, assisting you in protecting or closing these ports.
- **Advanced Functionality**: LemTCP can detect the names of the services running on the ports of your network.
- **Performance**: Thanks to its multi-processing approach, LemTCP can scan large port ranges rapidly, thus enhancing user experience.
- **Flexibility**: It offers various options, such as displaying only open ports and printing the scan results to a file.
- **Open Source and Free**: As an open-source tool, LemTCP can be freely used, modified, and shared by anyone.
- **User-Friendly**: LemTCP operates via the command line and features a user-friendly interface.

## Installation

Install the necessary libraries with the following commands:

```bash
pip3 install socket argparse concurrent.futures colored os
```

Next, download the tool that allows for printing styled text:

```bash
git clone https://github.com/xero/figlet-fonts

Then, move the downloaded file to 'mv * /usr/share/figlet/'.
```
## Usage

This tool is developed for the Linux operating system and 
is run from the command line. By specifying arguments, 
you can set the IP address and port range you want to scan, 
where you want to print the output, and whether you want 
to show only open ports.

or example, the following command scans the ports 
between 1-1000 on the 192.168.1.1 IP address, writes the 
results to the results.txt file, and only shows open ports

```bash
python3 LemTCP.py --ip 192.168.1.1 --port1 1 --port2 1000 --output results.txt --only-open
```
## Updates & Future Plans
The latest version of LemTCP was released on 05.06.2023. We're actively working on new features and improvements, with an update planned in 25 days. We highly value and carefully consider your feedback.

## Conclusion
LemTCP is a robust port scanning tool, essential for network security and diagnostics. As always, it's crucial to comply with legal and ethical rules when using this tool. Obtain permissions when scanning any network to avoid legal and ethical infringements.

Stay tuned for LemTCP's new updates and features!

## License
This project is licensed under the terms of the GNU General Public License v3.0. For more details, see the LICENSE file.








