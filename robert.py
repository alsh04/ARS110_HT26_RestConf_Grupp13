import requests
import getpass
import urllib3

urllib3.disable_warnings()

print("[!] Authorization Required [!]")
user = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
headers = {
    "Accept": "application/yang-data+json",
}

failed = 0

print("______________________")
print("|   |Router: HEMMA|  |")
print("**********************")


# HEMMA banner
r = requests.get(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "[!] UNAUTHORIZED ACCESS PROHIBITED [!]" in r.text:
    print(">Banner = PASS")
else:
    print(">Banner = FAIL")
    failed = failed + 1

# HEMMA gigabit
r = requests.get(
    "https://192.168.100.11/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)

if r.status_code == 200 and "10.10.10.1" in r.text and "LAN MOT GARDEROBEN" in r.text:
    print(">GIGABIT = PASS")
else:
    print(">GIGABIT = FAIL")
    failed = failed + 1

# HEMMA serial
r = requests.get(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "172.16.16.1" in r.text and "SERIAL MOT ISP" in r.text:
    print(">SERIAL = PASS")
else:
    print(">SERIAL = FAIL")
    failed = failed + 1

# HEMMA eigrp
r = requests.get(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "10.10.10.0" in r.text and "172.16.16.0" in r.text:
    print(">EIGRP = PASS")
else:
    print(">EIGRP = FAIL")
    failed = failed + 1

print("______________________")
print("|   |Router: ISP|    |")
print("**********************")


# ISP banner
r = requests.get(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)

if r.status_code == 200 and "[!] UNAUTHORIZED ACCESS PROHIBITED [!]" in r.text:
    print(">Banner = PASS")
else:
    print(">Banner = FAIL")
    failed = failed + 1

# ISP serial
r = requests.get(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "172.16.16.2" in r.text and "SERIAL MOT HEMMA" in r.text:
    print(">SERIAL = PASS")
else:
    print(">SERIAL = FAIL")
    failed = failed + 1

# ISP gigabit
r = requests.get(
    "https://192.168.100.12/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "10.11.12.2" in r.text and "GIGABIT MOT INTERNET" in r.text:
    print(">GIGABIT = PASS")
else:
    print(">GIGABIT = FAIL")
    failed = failed + 1

# ISP eigrp
r = requests.get(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "172.16.16.0" in r.text and "10.11.12.0" in r.text:
    print(">EIGRP = PASS")
else:
    print(">EIGRP = FAIL")
    failed = failed + 1

print("______________________")
print("|  |Router: INTERNET| ")
print("**********************")


# INTERNET banner
r = requests.get(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "[!] UNAUTHORIZED ACCESS PROHIBITED [!]" in r.text:
    print(">Banner = PASS")
else:
    print(">Banner = FAIL")
    failed = failed + 1

# INTERNET gigabit
r = requests.get(
    "https://192.168.100.13/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "10.11.12.3" in r.text and "GIGABIT MOT ISP" in r.text:
    print(">GIGABIT = PASS")
else:
    print(">GIGABIT = FAIL")
    failed = failed + 1

# INTERNET loopback
r = requests.get(
    "https://192.168.100.13/restconf/data/ietf-interfaces:interfaces/interface=Loopback0",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "10.33.33.33" in r.text and "LOOPBACK INTERNET" in r.text:
    print(">Loopback = PASS")
else:
    print(">Loopback = FAIL")
    failed = failed + 1

# INTERNET default route
r = requests.get(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/ip/route",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "0.0.0.0" in r.text and "Loopback0" in r.text:
    print(">Default Route = PASS")
else:
    print(">Default Route = FAIL")
    failed = failed + 1

# INTERNET eigrp
r = requests.get(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    verify=False,
    timeout=5,
)
if r.status_code == 200 and "10.11.12.0" in r.text and "10.33.33.33" in r.text:
    print(">EIGRP = PASS")
else:
    print(">EIGRP = FAIL")
    failed = failed + 1



print()
if failed == 0:
    print("GODKÄNT (G)")
else:
    print("UNDERKÄNT (U)")

print("Svar: Nej, inget skript kan ersätta Robert :)")
