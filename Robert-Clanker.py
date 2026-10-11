import requests
import getpass

print("[!] Authorization Required [!]")
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
headers = {
    "Accept": "application/yang-data+json",
}

routers = {
    "HEMMA": {
        "ip": "192.168.100.11",
        "expected": [
            "HEMMA",
            "[!] UNAUTHORIZED ACCESS PROHIBITED [!]",
            "10.10.10.1",
            "172.16.16.1",
            "10.10.10.0",
            "172.16.16.0",
        ],
    },
    "ISP": {
        "ip": "192.168.100.12",
        "expected": [
            "ISP",
            "[!] UNAUTHORIZED ACCESS PROHIBITED [!]",
            "172.16.16.2",
            "10.11.12.2",
            "172.16.16.0",
            "10.11.12.0",
        ],
    },
    "INTERNET": {
        "ip": "192.168.100.13",
        "expected": [
            "INTERNET",
            "[!] UNAUTHORIZED ACCESS PROHIBITED [!]",
            "10.11.12.3",
            "10.33.33.33",
            "Loopback0",
            "0.0.0.0",
        ],
    }, 
}

all_passed = True

for router_name, router in routers.items():
    url = (
        "https://" + router["ip"]
        + "/restconf/data/Cisco-IOS-XE-native:native"
    )

    print("\nChecking", router_name)

    try:
        response = requests.get(
            url,
            headers=headers,
            auth=(username, password),
            verify=False,
            timeout=5,
        )
    except requests.exceptions.RequestException as error:
        print("FAIL: RESTCONF request failed:", error)
        all_passed = False
        continue

    if response.status_code != 200:
        print("FAIL: HTTP status", response.status_code)
        all_passed = False
        continue

    config = response.text

    for value in router["expected"]:
        if value in config:
            print("PASS:", value)
        else:
            print("FAIL: missing", value)
            all_passed = False

print()

if all_passed:
    print("GODKÄNT (G)")
else:
    print("UNDERKÄNT (U)")

print("Svar: Nej, inget skript kan ersätta Robert :)")