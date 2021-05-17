# Cortex Analyzers
Repository used for developing analyzers for Cortex.

This repository contains 9 updated analyzers which can be used in Cortex. 

## Analyzers

- [BitcoinAbuse](#bitcoinabuse)
- [CheckPhish](#checkphish)
- [IP-API](#ip-api)
- [IPTracker](#iptracker)
- [KapeIPParser](#kapeipparser)
- [KapeJSONParser](#kapejsonparser)
- [KasperskyThreadIntelligencePortal](#kasperskythreadintelligenceportal)
- [ThreatMiner](#threatminer)
- [Verifalia](#verifalia)
- [W3SA-UPJS](#w3sa-upjs)

## Installation Guide
Clone this repository to Cortex directory of your installation.
```
cd /opt
sudo git clone https://github.com/pjuhas/Cortex-Analyzers.git
```
You may need to install Cortex prerequisites in order to successfully install and use Cortex analyzers. 
```
sudo apt-get install -y --no-install-recommends python-pip python3-pip python3-dev ssdeep libfuzzy-dev libfuzzy2 libmagic1 build-essential libssl-dev
sudo pip install -U pip setuptools && sudo pip3 install -U pip setuptools
```

Install all modules used in Cortex analyzers located in *requirements.txt*. 
```
for I in $(find Cortex-Analyzers -name 'requirements.txt'); do sudo -H pip3 install -r $I || true; done
```

Update your Cortex *application.conf*.
```
...
## ANALYZERS
analyzer {
...
"/opt/Cortex-Analyzers/analyzers"
}
...
```
Restart Cortex and you should see installed Cortex analyzers under *Organization &#8594; Analyzers*. 

---

### BitcoinAbuse
Check Bitcoin address against Bitcoin Abuse database. 

Returns count of reports and description of reports.
#### Requirements
Provide your API key from [BitcoinAbuse](https://www.bitcoinabuse.com) as a value of the key parameter.

---

### CheckPhish
Detailed analysis of URL via CheckPhish.

Returns URL to analysis and screenshot of site.

#### Requirements
Provide your API key from [CheckPhish](https://checkphish.ai) as a value of the key parameter.

---

### IP-API
Checks IP address or domain using [ip-api.com](https://ip-api.com). 

Returns geolocation informations of IP address or domain.

No configuration is required. It can be used out of the box.

---

### IPTracker
Checks IP address using IPTracker.

Returns geolocation informations of IP address.

#### Requirements
Provide your API key from [IPTracker](https://www.iptrackeronline.com) as a value of the key parameter.

---

### KapeIPParser
Parse established connections from [Kape](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) logs. 
```
.\kape.exe --tsource <source> --tdest <destination> --tflush --target !BasicCollection --msource <source> --mdest <destination> --mflush --module Get-NetworkConnection
```
Returns IP addresses of established connections.

No configuration is required. It can be used out of the box.

---

### KapeJSONParser
Parse process list from [Kape](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) logs.

```
.\kape.exe --tsource <source> --tdest <destination> --tflush --target !BasicCollection --msource <source> --mdest <destination> --mflush --module Get-Process
```

Returns abbreviated informations about processes.

No configuration is required. It can be used out of the box.

---

### KasperskyThreadIntelligencePortal
Analyze IP address, domain or hash via Kaspersky Threat Intelligence Portal. 

Returns basic informations about IP address, domain or hash.

#### Requirements
Provide your API key from [KasperskyThreadIntelligencePortal](https://opentip.kaspersky.com) as a value of the key parameter.

---
### ThreatMiner
Returns WHOIS information of IP address or domain if available using [ThreatMiner](https://threatminer.org).

No configuration is required. It can be used out of the box.

---

### Verifalia
Submit e-mail address for analysis via Verifalia.

Returns basic informations about analyzed e-mail address.

#### Requirements
Provide your username as a value of the login parameter and password as a value of the password parameter from [Verifalia](https://verifalia.com).

---
### W3SA-UPJS
Checks if IP address is part of university network in Pavol Jozef Šafárik University.

Returns MAC address, name of the server, VLAN and many more..

#### Requirements

Provide your username as a value of the login parameter and password as a value of the password parameter from [W3SA](https://w3sa.ciakt.upjs.sk/login?came_from=%2Fadmin%2F).

---

### TheHive Project
- [TheHive Project](https://github.com/TheHive-Project/TheHive)
- [Cortex](https://github.com/TheHive-Project/Cortex)

