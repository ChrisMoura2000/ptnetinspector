# ptnetinspector v0.2.2
## Interface Web

### Check ptnetinspector original repo from <b><span style="color:orange;">Penterep</span></b> [HERE](https://github.com/Penterep/ptnetinspector/blob/d15303db0c196e25cc99ea25d28d80f0195166d7/README.md)!
---

"<span style="color:orange;">ptnetinspector</span> is a versatile tool designed to 
perform comprehensive scans over IPv6 networks, with support for dual-stack environments 
to ensure compatibility with both IPv4 and IPv6 infrastructures. This tool provides detailed 
insights into the network's topology, identifying critical information such as IP, MAC, 
multicast groups, router information and the role of discovered nodes.

Beyond basic network reconnaissance, this Penterep tool is equipped with advanced vulnerability 
detection capabilities, scanning nodes for known security weaknesses and misconfigurations. 
This enables network administrators to proactively identify and mitigate risks."

This FORK was designed for Network Managers who are not familiar with the Linux command line, 
allowing them to gain visibility into IPv6 Network Configurations within their Dual-Stack Environments. 


## Install Requirements 
 
Before proceeding, it is recommended to update your system to ensure compatibility: 
```bash 
sudo apt update && sudo apt upgrade -y 
``` 

This application requires **Python3**. Make sure it is installed, along with the `python3-venv` package, for managing virtual environments: 
```bash 
sudo apt install python3 python3-venv -y 
``` 

After cloning the repository, install the package and dependencies with one command:
```bash
make ptnetinspector
```

## Usage 
After installing ptnetinspector and for future use, you don’t need to reinstall the dependencies. 
Simply activate the created virtual environment, run application and Flask server: 
```bash 
make interface
``` 

### What a Scan Collects

Beyond the vulnerability findings, a scan extracts:

- **Router Advertisement options** — every advertised prefix (not just the first), all
  RDNSS servers, DNSSL search domains (RFC 8106), Route Information (RFC 4191),
  PREF64/NAT64 (RFC 8781) and Captive Portal (RFC 8910).
- **Passive fingerprints** — initial hop limit and the interface-identifier scheme
  (EUI-64, low-bit/manual, or randomized stable-privacy/temporary). Derived from packets
  already captured, so they cost no extra traffic. These are heuristics and are reported
  as *likely*, not as fact.
- **Node Information** (RFC 4620) — hostnames and full address lists from stacks that
  answer NI Queries. Many BSD and macOS stacks do; Linux generally does not, so silence
  means "no support", not "no host".
- **DNS-SD service tree** — service types, instances, and the SRV host/port plus TXT
  metadata each instance publishes.
- **DHCPv6 options** — from an Information-Request: resolvers, domain search list,
  NTP/SNTP and SIP servers, boot-file URL, vendor class and the server's DUID.
- **Multicast querier and L2 snooping** — which device sends MLD/IGMP General Queries,
  plus a join to an otherwise unused group to probe whether the switch snoops. The
  snooping result is inferential and depends on switch configuration.
- **Duplicate Address Detection** — addresses caught at the moment a host claims them.

## Original Tool's License
Copyright (c) 2026 Penterep Security s.r.o.

ptnetinspector is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

ptnetinspector is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ptmethods. If not, see https://www.gnu.org/licenses/

## Disclaimer from Penterep

```
This program must be performed with proper authorization or Educational purpose ONLY. Do not use it without permission. 
The usual disclaimer applies, especially the fact that us (Penterep) is not liable for any damages caused by direct or 
indirect use of the functionality provided by this program. The author bears NO responsibility for content or misuse of 
this program or any derivatives thereof. 
```
