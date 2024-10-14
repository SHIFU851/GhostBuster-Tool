# Ghost Buster IP Tool

**Version:** 1.0  
**Author:** $$$  
**Purpose:** This tool is designed for **educational purposes only**, providing various functionalities to gather information about IP addresses, domains, and more.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
4. [Options Overview](#options-overview)
5. [Installation](#installation)
6. [Requirements](#requirements)
7. [License](#license)

---

## Introduction

The **Ghost Buster IP Tool** allows users to explore and gather information about IP addresses, domains, and websites. It is intended for **educational use only** and includes features like WHOIS lookups, DNS lookups, IP tracing, and more.

---

## Features

- IP address information retrieval
- Domain-to-IP conversion
- IP blacklist checking
- Google Maps location lookup
- TraceRoute functionality
- DNS lookups
- WHOIS lookups
- Website host and ASN information
- Help and guidance

---

## Usage

After launching the script, the user will be prompted to agree to the terms that the tool is for educational purposes only. Once confirmed, the tool will present a menu with different options.

---

## Options Overview

### 1. Check IP Info
   - This option retrieves detailed information about a specific IP address, such as city, country, organization, timezone, VPN status, and more.
   - **Example:** If you want to know more about a specific IP, this option will provide you with all the key details.

### 2. Show Domain IP
   - Converts a domain name into its corresponding IP address.
   - **Example:** If you enter `example.com`, the tool will return the associated IP address.

### 3. Check IP Blacklist Status
   - Checks whether an IP address is listed in a blacklist database.
   - **Example:** Enter an IP address, and the tool will open a web browser to show whether it's been reported for malicious activity.

### 4. Show Address on Google Maps
   - Displays the physical location of an IP address (if available) using Google Maps.
   - **Example:** If the IP address has location data, this option will open a Google Maps link to show its location.

### 5. TraceRoute
   - This function performs a network traceroute to track the path taken by packets from your machine to a destination IP.
   - **Example:** Useful for network diagnostics and understanding how data is routed to a specific IP.

### 6. DNS Lookup
   - Opens a web browser to perform a DNS lookup for a domain, displaying all DNS records.
   - **Example:** Get detailed DNS record information about `example.com`.

### 7. WHOIS Lookup
   - Retrieves WHOIS information for a given domain, showing details like registration, owner information, and expiration.
   - **Example:** Find out who owns a specific domain and when it was registered.

### 8. Check URL Info
   - Opens a web browser to retrieve detailed information about a specific URL, including ownership and registration details.
   - **Example:** Enter `example.com`, and the tool will show its WHOIS information in a browser.

### 9. Find Website Host
   - Opens a web browser to identify the hosting provider of a given website.
   - **Example:** Find out where a particular website is hosted.

### 10. ASN Lookup Tool
   - Looks up an Autonomous System Number (ASN) to find details about the network routing and ownership.
   - **Example:** Input an ASN (e.g., `AS13335`), and the tool will show the organization's information.

### 11. Help
   - Displays a help guide with information on how to use the tool.

### 12. Exit
   - Exits the program.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ghost-buster-ip-tool.git
  Run the tool:
```bash
   python ghost_buster.py
````
## Requirements

- **Python Version**: Python 3.x

- **Required Libraries**:
  - `requests`
  - `webbrowser`
  - `time`
  - `socket`
  - `colorama`
  - `scapy`
  - `whois`

To install the required Python libraries, you can use the following command:

```bash
pip install requests colorama scapy whois

