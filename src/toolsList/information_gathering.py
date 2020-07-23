#!/usr/bin/python3

tools = [
    {
        "package": "ace-voip",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Amap",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "APT2",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "arp-scan",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Automater",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "bing-ip2hosts",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "braa",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "CaseFile",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "CDPSnarf",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "cisco-torch",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "copy-router-config",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "DMitry",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "dnmap",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "dnsenum",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "dnsmap",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "DNSRecon",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "dnstracer",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "dnswalk",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "DotDotPwn",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "enum4linux",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "enumIAX",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "EyeWitness",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Faraday",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Fierce",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Firewalk",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "fragroute",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "fragrouter",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Ghost Phisher",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "GoLismero",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "goofile",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "hping3",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "ident-user-enum",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "InSpy",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "InTrace",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "iSMTP",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "lbd",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Maltego Teeth",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "masscan",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Metagoofil",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Miranda",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "nbtscan-unixwiz",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Nikto",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Nmap",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "ntop",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "OSRFramework",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "pFalsef",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Parsero",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Recon-ng",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "SET",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "SMBMap",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "smtp-user-enum",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "snmp-check",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "SPARTA",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "sslcaudit",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "SSLsplit",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "sslstrip",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "SSLyze",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Sublist3r",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "THC-IPV6",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "theHarvester",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "TLSSLed",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "twofi",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Unicornscan",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "URLCrazy",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Wireshark",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "WOL-E",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    },
    {
        "package": "Xplico",
        "essential-tool": False,
        "installation": "",
        "requiresUI": False
    }]
