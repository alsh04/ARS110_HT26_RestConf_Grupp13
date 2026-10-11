import requests
import json
import urllib3
import getpass

urllib3.disable_warnings()
failed = 0

#Login data
print("[!] Authorization Required [!]")
user = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}
print("______________________")
print("|   |Router: HEMMA|  |")
print("**********************")

#hemma banner
answer = requests.patch(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:banner": {
            "motd": {
                "banner": " [!] UNAUTHORIZED ACCESS PROHIBITED [!]"
            }
        }
    },
    verify=False,
) 

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">Banner Status = Success [{answer.status_code}]")
else:
    print(f">Banner Status = Failed [{answer.status_code}]")
    failed = failed + 1

#hemma gigabit
answer = requests.patch(
    "https://192.168.100.11/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    json={
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet0/0/0",
            "description": "LAN MOT GARDEROBEN",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": "10.10.10.1", "netmask": "255.255.255.0"}]
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">GIGABIT Status = Success [{answer.status_code}]")
else:
    print(f">GIGABIT Status = Failed [{answer.status_code}]")
    failed = failed + 1


#hemma serial
answer = requests.patch(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:Serial": {
            "name": "0/1/0",
            "description": "SERIAL MOT ISP",
            "ip": {
                "address": {
                    "primary": {"address": "172.16.16.1", "mask": "255.255.255.0"}
                }
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">SERIAL Status = Success [{answer.status_code}]")
else:
    print(f">SERIAL Status = Failed [{answer.status_code}]")
    failed = failed + 1

#hemma eigrp
answer = requests.patch(
    "https://192.168.100.11/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-eigrp:router-eigrp": {
            "eigrp": {
                "classic-mode": [
                    {
                        "autonomous-system": 100,
                        "auto-summary": False,
                        "network": {
                            "address-wildcard": [
                                {"ipv4-address": "10.10.10.0", "wildcard": "0.0.0.255"},
                                {"ipv4-address": "172.16.16.0", "wildcard": "0.0.0.255"},
                            ]
                        },
                    }
                ]
            }
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">EIGRP Status = Success [{answer.status_code}]")
else:
    print(f">EIGRP Status = Failed [{answer.status_code}]")
    failed = failed + 1


print("______________________")
print("|   |Router: ISP|    |")
print("**********************")


#isp banner
answer = requests.patch(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:banner": {
            "motd": {
                "banner": " [!] UNAUTHORIZED ACCESS PROHIBITED [!]"
            }
        }
    },
    verify=False,
) 

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">Banner Status = Success [{answer.status_code}]")
else:
    print(f">Banner Status = Failed [{answer.status_code}]")
    failed = failed + 1


#isp serial
answer = requests.patch(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/interface/Serial=0%2F1%2F0",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:Serial": {
            "name": "0/1/0",
            "description": "SERIAL MOT HEMMA",
            "ip": {
                "address": {
                    "primary": {"address": "172.16.16.2", "mask": "255.255.255.0"}
                }
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">SERIAL Status = Success [{answer.status_code}]")
else:
    print(f">SERIAL Status = Failed [{answer.status_code}]")
    failed = failed + 1


#isp gigabit
answer = requests.patch(
    "https://192.168.100.12/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    json={
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet0/0/0",
            "description": "GIGABIT MOT INTERNET",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": "10.11.12.2", "netmask": "255.255.255.0"}]
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">GIGABIT Status = Success [{answer.status_code}]")
else:
    print(f">GIGABIT Status = Failed [{answer.status_code}]")
    failed = failed + 1


#isp eigrp
answer = requests.patch(
    "https://192.168.100.12/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-eigrp:router-eigrp": {
            "eigrp": {
                "classic-mode": [
                    {
                        "autonomous-system": 100,
                        "auto-summary": False,
                        "network": {
                            "address-wildcard": [
                                {"ipv4-address": "172.16.16.0", "wildcard": "0.0.0.255"},
                                {"ipv4-address": "10.11.12.0", "wildcard": "0.0.0.255"},
                            ]
                        },
                    }
                ]
            }
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">EIGRP Status = Success [{answer.status_code}]")
else:
    print(f">EIGRP Status = Failed [{answer.status_code}]")
    failed = failed + 1


print("______________________")
print("|  |Router: INTERNET| ")
print("**********************")


#internet banner
answer = requests.patch(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/banner",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:banner": {
            "motd": {
                "banner": " [!] UNAUTHORIZED ACCESS PROHIBITED [!]"
            }
        }
    },
    verify=False,
) 

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">Banner Status = Success [{answer.status_code}]")
else:
    print(f">Banner Status = Failed [{answer.status_code}]")
    failed = failed + 1

# internet gigabit
answer = requests.patch(
    "https://192.168.100.13/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet0%2F0%2F0",
    headers=headers,
    auth=(user, password),
    json={
        "ietf-interfaces:interface": {
            "name": "GigabitEthernet0/0/0",
            "description": "GIGABIT MOT ISP",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": "10.11.12.3", "netmask": "255.255.255.0"}]
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">GIGABIT Status = Success [{answer.status_code}]")
else:
    print(f">GIGABIT Status = Failed [{answer.status_code}]")
    failed = failed + 1

# internet loopback
answer = requests.put(
    "https://192.168.100.13/restconf/data/ietf-interfaces:interfaces/interface=Loopback0",
    headers=headers,
    auth=(user, password),
    json={
        "ietf-interfaces:interface": {
            "name": "Loopback0",
            "description": "LOOPBACK INTERNET",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": "10.33.33.33", "netmask": "255.255.255.0"}]
            },
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">Loopback Status = Success [{answer.status_code}]")
else:
    print(f">Loopback Status = Failed [{answer.status_code}]")
    failed = failed + 1


# internet default route
answer = requests.patch(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/ip/route",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-native:route": {
            "ip-route-interface-forwarding-list": [
                {
                    "prefix": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "fwd-list": [{"fwd": "Loopback0"}],
                }
            ]
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">Default Route Status = Success [{answer.status_code}]")
else:
    print(f">Default Route Status = Failed [{answer.status_code}]")
    failed = failed + 1

# internet eigrp
answer = requests.patch(
    "https://192.168.100.13/restconf/data/Cisco-IOS-XE-native:native/router/router-eigrp",
    headers=headers,
    auth=(user, password),
    json={
        "Cisco-IOS-XE-eigrp:router-eigrp": {
            "eigrp": {
                "classic-mode": [
                    {
                        "autonomous-system": 100,
                        "auto-summary": False,
                        "network": {
                            "address-wildcard": [
                                {"ipv4-address": "10.11.12.0", "wildcard": "0.0.0.255"},
                                {"ipv4-address": "10.33.33.33", "wildcard": "0.0.0.255"},
                            ]
                        },
                        "redistribute": {"static": {}},
                    }
                ]
            }
        }
    },
    verify=False,
)

if answer.status_code >= 200 and answer.status_code < 300:
    print(f">EIGRP Status = Success [{answer.status_code}]")
else:
    print(f">EIGRP Status = Failed [{answer.status_code}]")
    failed = failed + 1

if failed == 0:
    print("")
    print("RESTCONF Configuration Successful!")
else:
    print("")
    print(f"RESTCONF Finished, With {failed} Failed Requests Failed!")