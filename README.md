# Restconf-Notes

Root uri:

-   `https://10.10.20.100:443/restconf/`

Headers:

-   `Content-Type: application/yang-data+json`
-   `Accept: application/yang-data+json`

Auth:

-   Basic
    -   Username
    -   Password

Example Calls:
- GET Native configuration
    - `https://10.10.20.100:443/restconf/data/native/`
-   GET CDP Neighbors
    -   `https://restconf-device:443/restconf/data/cdp-neighbor-details`
-   GET Vlans
    -   `https://restconf-device:443/restconf/data/vlans`
-   GET Spanning Tree details
    -   `https://restconf-device:443/restconf/data/stp-details`
-   GET ARP data
    -   All VRFs
        -   `https://restconf-device:443/restconf/data/arp-data`
    -   Specific VRF
        -   `https://restconf-device:443/restconf/data/arp-data/arp-vrf=Mgmt-vrf`
-   GET Interface Stats
    -   All interfaces
        -   `https://restconf-device:443/restconf/data/interfaces/`
    -   Single interface
        -   `https://restconf-device:443/restconf/data/interfaces/interface=GigabitEthernet1%2f0%2f2`
-   GET Interface Configuration
    -   All interfaces
        -   `https://restconf-device:443/restconf/data/native/interface`
    -   Single interface
        -   `https://restconf-device:443/restconf/data/native/interface/GigabitEthernet=1%2f0%2f2`
    -   Single Interface IP configuration
        -   `https://restconf-device:443/restconf/data/native/interface/GigabitEthernet=1%2f0%2f2/ip`
    -   Single Interface switchport configuration
        -   `https://restconf-device:443/restconf/data/native/interface/GigabitEthernet=1%2f0%2f1/switchport`
    -   Single Interface vlan assignment
        -   `https://restconf-device:443/restconf/data/native/interface/GigabitEthernet=1%2f0%2f1/switchport/access/vlan`
- GET Hardware information
  - `https://10.10.20.100:443/restconf/data/device-hardware-data`
