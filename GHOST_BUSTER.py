import requests
import webbrowser
import time
import socket
import colorama
from colorama import Fore
from scapy.all import sr1, IP, ICMP
import whois
from README import help_guide

# Initialize colorama
colorama.init(autoreset=True)

# Show Ghost Buster Header
print(Fore.LIGHTWHITE_EX + """
""" + Fore.LIGHTYELLOW_EX + " ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗    " + Fore.LIGHTWHITE_EX + """  ██████╗ ██╗   ██╗███████╗████████╗███████╗██████╗ 
""" + Fore.LIGHTYELLOW_EX + " ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    " + Fore.LIGHTWHITE_EX + """ ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
""" + Fore.LIGHTYELLOW_EX + " ██║  ███╗███████║██║   ██║███████╗   ██║       " + Fore.LIGHTWHITE_EX + """ ██████╔╝██║   ██║███████╗   ██║   █████╗  ██████╔╝
""" + Fore.LIGHTYELLOW_EX + " ██║   ██║██╔══██║██║   ██║╚════██║   ██║       " + Fore.LIGHTWHITE_EX + """ ██╔══██╗██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
""" + Fore.LIGHTYELLOW_EX + " ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       " + Fore.LIGHTWHITE_EX + """ ██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║
 """ + Fore.LIGHTYELLOW_EX + " ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝       " + Fore.LIGHTWHITE_EX + """ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")

print(Fore.LIGHTWHITE_EX + "                              For Educational Purpose Only")
print("-----------------------------------------------")
print(Fore.LIGHTYELLOW_EX + "Made By - $$$")
print("-----------------------------------------------")

# Check for educational purpose agreement
while True:
    edo = input(
        Fore.LIGHTWHITE_EX + "[+] This is used for " + Fore.LIGHTYELLOW_EX + "educational purposes only (y/n): ")
    if edo.strip().lower() == "y":
        break
    elif edo.strip().lower() == "n":
        print(Fore.LIGHTRED_EX + "[+] Exiting the program. Goodbye!")
        exit()

data = {}  # Initialize data to an empty dictionary

while True:
    # Program Options
    print("-----------------------------------------------")
    print(Fore.LIGHTYELLOW_EX + "[1] Check IP Info \n"
                                "[2] Show Domain IP\n"
                                "[3] Check IP Blacklist Status\n"
                                "[4] Show Address On Google Map \n"
                                "[5] TraceRoute \n"
                                "[6] DNS Lookup \n"
                                "[7] Whois Lookup \n"
                                "[8] Check URL Info \n"
                                "[9] Find Website Host \n"
                                "[10] ASN Lookup Tool \n"
                                "[11] Help \n"
                                "[12] Exit")

    print("-----------------------------------------------")

    # Checking the user choice
    choice = input(Fore.LIGHTWHITE_EX + "S" + Fore.LIGHTYELLOW_EX + "e" + Fore.LIGHTWHITE_EX + "l" +
                   Fore.LIGHTYELLOW_EX + "e" + Fore.LIGHTWHITE_EX + "c" + Fore.LIGHTYELLOW_EX + "t" + "-" +
                   Fore.LIGHTWHITE_EX + "O" + Fore.LIGHTYELLOW_EX + "p" + Fore.LIGHTWHITE_EX + "t" +
                   Fore.LIGHTYELLOW_EX + "i" + Fore.LIGHTWHITE_EX + "o" + Fore.LIGHTYELLOW_EX + "n: ")

    # Option 1: Check IP Info
    if choice == "1":
        ip_to_check = input(Fore.LIGHTYELLOW_EX + "[+] Please enter an IP address: ")
        print("-----------------------------------------------")
        try:
            response = requests.get(f"https://ipinfo.io/{ip_to_check}/json")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()  # Store the retrieved data
            print(Fore.LIGHTYELLOW_EX + f"[+] Retrieving information for {ip_to_check}...")
            print("-----------------------------------------------")
            time.sleep(1)

            # Print the location information
            print(Fore.LIGHTYELLOW_EX +
                  f" City: {data.get('city', 'N/A')}\n"
                  f" Location: {data.get('loc', 'N/A')}\n"
                  f" Country: {data.get('country', 'N/A')}\n"
                  f" Organization: {data.get('org', 'N/A')}\n"
                  f" Timezone: {data.get('timezone', 'N/A')}\n"
                  f" VPN: {data.get('vpn', 'N/A')}\n"
                  f" Phone: {data.get('phone', 'N/A')}\n"
                  f" Postal Code: {data.get('postal', 'N/A')}\n")
            print("-------------------------------------------------------------")
            print(Fore.LIGHTYELLOW_EX + "[+] If you want to view the address on Google Maps, check option 4!")
            print("--------------------------------------------------------------")

            # Asking The User If they want to continue
            continue_question = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
            if continue_question.strip().lower() != "y":
                continue  # Back to main menu

        except requests.exceptions.RequestException:
            print(Fore.LIGHTRED_EX + "[+] Error retrieving location information.")
        except ValueError:
            print(Fore.LIGHTRED_EX + "[+] Error, please try again.")

    # Option 2: Show Domain IP
    elif choice == "2":
        domain_name = input(Fore.LIGHTYELLOW_EX + "[+] Please enter a domain name: ")
        try:
            ip = socket.gethostbyname(domain_name)
            print(Fore.LIGHTYELLOW_EX + f"[+] The IP address for {domain_name} is: {ip}")
        except socket.gaierror:
            print(Fore.LIGHTRED_EX + "[+] Invalid domain name, please try again.")

        continue_question2 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
        if continue_question2.strip().lower() != "y":
            continue  # Back to main menu

    # Option 3: Check IP Blacklist Status
    elif choice == "3":
        ip_check = input(Fore.LIGHTYELLOW_EX + "[+] Please enter an IP address: ").strip()
        try:
            print(Fore.LIGHTYELLOW_EX + f"[+] Retrieving information for {ip_check}...")
            time.sleep(0.7)
            print(Fore.LIGHTYELLOW_EX + "[+] Checking if this IP has been reported...")
            time.sleep(0.7)
            print(Fore.LIGHTYELLOW_EX + "[+] Opening a new browser...")
            time.sleep(0.5)
            webbrowser.open(f"https://www.abuseipdb.com/check/{ip_check}")
        except Exception as e:
            print(Fore.LIGHTRED_EX + "[+] Error checking if this IP has been reported.")
            print(Fore.LIGHTRED_EX + f"[+] Details: {e}")

    # Option 4: Show Address On Google Maps
    elif choice == "4":
        if data:  # Check if data has been retrieved
            loc = data.get('loc', 'N/A')
            if loc != 'N/A':
                coords = loc.split(',')
                google_maps_url = f"https://www.google.com/maps/?q={coords[0].strip()},{coords[1].strip()}"
                print(Fore.LIGHTYELLOW_EX + "[+] Retrieving location...")
                time.sleep(1)
                print(Fore.LIGHTYELLOW_EX + f"[+] Opening Google Maps for {coords[0].strip()}, {coords[1].strip()}...")
                webbrowser.open(google_maps_url)
            else:
                print(Fore.LIGHTRED_EX + "[+] No location information found.")
        else:
            print(Fore.LIGHTRED_EX + "[+] Please check the IP info first (Option 1).")

    # Option 5: TraceRoute
    elif choice == "5":
        traceroute_ip = input(Fore.LIGHTYELLOW_EX + "[+] Enter IP address to trace: ")
        print(Fore.LIGHTYELLOW_EX + "[+] Starting trace route...")
        ttl = 1
        while True:
            packet = IP(dst=traceroute_ip, ttl=ttl) / ICMP()
            reply = sr1(packet, verbose=0)

            if reply is None:
                print(Fore.LIGHTYELLOW_EX + f"[+] Hop {ttl}: Request timed out.")
                break
            elif reply.type == 0:  # Echo Reply
                print(Fore.LIGHTYELLOW_EX + f"[+] Hop {ttl}: {reply.src} - Destination reached.")
                break
            else:
                print(Fore.LIGHTYELLOW_EX + f"[+] Hop {ttl}: {reply.src}")

            ttl += 1
            time.sleep(1)

    # Option 6: DNS Lookup
    elif choice == "6":
        domain = input(Fore.LIGHTYELLOW_EX + "[+] Please enter a domain name: ")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Getting Info About {domain}...")
            time.sleep(0.5)
            print(Fore.LIGHTYELLOW_EX + "Getting Web Ready...")
            time.sleep(0.5)
            webbrowser.open(f"https://www.nslookup.io/domains/{domain}/dns-records/")
        except Exception as e:  # Catch any exception, not just socket.gaierror
            print(Fore.LIGHTRED_EX + "[+] Error retrieving DNS information:", e)

        continue_question3 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
        if continue_question3.strip().lower() != "y":
            break  # Exits the current loop or section (assumes this is inside a loop)

    # Option 7: Whois Lookup
    elif choice == "7":
        domain = input(Fore.LIGHTYELLOW_EX + "[+] Please enter a domain name: ")

        # Ensure the domain seems valid (basic check)
        if not domain or "." not in domain:
            print(Fore.LIGHTRED_EX + "[+] Invalid domain name. Please try again.")
        else:
            try:
                domain_info = whois.whois(domain)

                # Debugging: Print raw data to understand what is returned
                print(Fore.LIGHTYELLOW_EX + "[+] Raw WHOIS data:")
                print(domain_info)

                # Check if the WHOIS lookup returned valid information
                if domain_info is None or not domain_info.get("domain_name"):
                    print(Fore.LIGHTRED_EX + "[+] WHOIS information not found for this domain.")
                else:
                    print(Fore.LIGHTYELLOW_EX + f"[+] WHOIS information for {domain}:")
                    print(domain_info)

            except Exception as e:
                print(Fore.LIGHTRED_EX + "[+] Error retrieving WHOIS information.")
                print(Fore.LIGHTRED_EX + f"[+] Details: {e}")

        continue_question4 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
        if continue_question4.strip().lower() != "y":
            continue  # Back to main menu

        # Option 8: Check URL Info
    elif choice == "8":
            url = input(Fore.LIGHTYELLOW_EX + "[+] Enter URL to check (need.com):")

            # Ensure proper formatting of the output message
            print(Fore.LIGHTYELLOW_EX + f"Checking about {url}...")
            time.sleep(0.5)
            print(Fore.LIGHTYELLOW_EX + "Getting info...")
            time.sleep(0.5)
            # Open the URL in a web browser
            try:
                webbrowser.open(f"https://www.whois.com/whois/{url}/")
                print(Fore.LIGHTYELLOW_EX + "[+] The URL information is being opened in your browser.")
            except Exception as e:
                print(Fore.LIGHTRED_EX + "[+] Error retrieving URL information.")
                print(Fore.LIGHTRED_EX + f"[+] Details: {e}")

            continue_question8 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
            if continue_question8.strip().lower() != "y":
                break  # Back to main menu

    # Option 9: Get Info About Website
    elif choice == "9":
        try:
            website = input(Fore.LIGHTYELLOW_EX + "[+] Insert Website: ")
            time.sleep(0.5)
            print(Fore.LIGHTYELLOW_EX + f"[+] Getting Info About {website}...")
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX + "[+] Opening New Browser...")
            time.sleep(0.3)
            webbrowser.open("https://hostingchecker.com/")  # Open website location finder with the website
            continue_question8 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
            if continue_question8.strip().lower() != "y":
                continue  # Back to main menu
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[+] Error: {e}")

    elif choice == "10":
        try:
            ASN = input(Fore.LIGHTYELLOW_EX + "[+]  Insert ASN e.g AS13335:")
            print(Fore.LIGHTYELLOW_EX + f"[+] Getting Info About {ASN}...")
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX +  "[+] Searching Location...")
            time.sleep(0.3)
            webbrowser.open(f"https://asnlookup.com/asn/{ASN}")
            continue_question6 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
            if continue_question6.strip().lower() != "y":
                continue  # Back to main menu
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"[+] Error: {e}")

    # Option 11: Help
    elif choice == "11":
        print(help_guide)
        continue_question7 = input(Fore.LIGHTYELLOW_EX + "[+] Would you like to continue? (Y/N) ")
        if continue_question7.strip().lower() != "y":
            continue  # Back to main menu

    # Option 12: Exit
    elif choice == "12":
        print(Fore.LIGHTRED_EX + "[+] Exiting the program. Goodbye!")
        exit()

    # Invalid Choice
    else:
        print(Fore.LIGHTRED_EX + "[+] Invalid choice. Please select a valid option.")
