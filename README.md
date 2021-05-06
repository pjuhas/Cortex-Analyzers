# Cortex Analyzers
Repository used for developing analyzers for Cortex.

This repository contains 5 updated analyzers which can be used in Cortex. 

## Analyzers

- [BitcoinAbuse](#bitcoinabuse)
- [IP-API](#ip-api)
- [KapeIPParser (personal use)](#kapeipparser-personal-use)
- [KapeJSONParser (personal use)](#kapejsonparser-personal-use)
- [KasperskyThreadIntelligencePortal](#kasperskythreadintelligenceportal)

## Installation Guide
Clone this repository to Cortex directory of your installation.
```
cd /opt
sudo git clone https://github.com/pjuhas/cortex-analyzers.git
```
You may need to install Cortex prerequisites in order to successfully install and use Cortex analyzers. 
```
sudo apt-get install -y --no-install-recommends python-pip python2.7-dev python3-pip python3-dev ssdeep libfuzzy-dev libfuzzy2 libimage-exiftool-perl libmagic1 build-essential git libssl-dev
sudo pip install -U pip setuptools && sudo pip3 install -U pip setuptools
```

Install all modules used in Cortex analyzers located in *requirements.txt*. 
```
for I in $(find cortex-analyzers -name 'requirements.txt'); do sudo -H pip3 install -r $I || true; done
```

Update your Cortex *application.conf*.
```
...
## ANALYZERS
analyzer {
...
"/opt/cortex-analyzers/analyzers"
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

### IP-API
Check IP address or domain using ip-api.com. 

Returns geolocation informations of IP address or domain.

No configuration is required. It can be used out of the box.

### KapeIPParser (personal use)
Parse established connections from [Kape](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) logs. 
```
.\kape.exe --tsource <source> --tdest <destination> --tflush --target !BasicCollection --msource <destination> --mdest <destination> --mflush --module Get-NetworkConnection
```
Returns IP addresses of established connections.

No configuration is required. It can be used out of the box.

### KapeJSONParser (personal use)
Parse process list from [Kape](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) logs.

```
.\kape.exe --tsource <source> --tdest <destination> --tflush --target !BasicCollection --msource <destination> --mdest <destination> --mflush --module Get-Process
```

Returns abbreviated informations about processes.

No configuration is required. It can be used out of the box.

### KasperskyThreadIntelligencePortal
Analyze IP address, domain or hash via Kaspersky Threat Intelligence Portal. 

Returns basic informations about IP address, domain or hash.

#### Requirements
Provide your API key from [KasperskyThreadIntelligencePortal](https://opentip.kaspersky.com) as a value of the key parameter.

