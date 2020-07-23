#!/usr/bin/python3

from ..category import Category

tools = [
        {
            "package": "apache-users",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
    #    {
    #        "package": "Arachni",
    #        "installation": "sudo apt-get install build-essential-tool curl libcurl4 libcurl4-openssl-dev ruby ruby-dev & gem install arachni",
    #        "essential-tool": False,
    #        "requiresUI": False
    #    },
    #    {
    #        "package": "BBQSQL",
    #        "installation": "sudo pip3 install bbqsql",
    #        "essential-tool": False,
    #        "requiresUI": False
    #    },
        {
            "package": "BlindElephant",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Burp Suite",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "CutyCapt",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "DAVTest",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "deblaze",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "DIRB",
            "installation": "sudo apt install dirb -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "DirBuster",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "fimap",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "FunkLoad",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Gobuster",
            "installation": "sudo apt install gobuster -y",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "Grabber",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "hURL",
            "installation": "sudo apt-get install hurl -y'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "jboss-autopwn",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "joomscan",
            "installation": "sudo apt-get install joomscan -y'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "jSQL Injection",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
       #{
       #     "package": "Maltego Teeth",
       #     "installation": "mkdir ~/Maltego && cd ~/Maltego &&  wget https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.2.11.13104.deb && dpkg –i Maltego.v4.2.11.13104.deb && cd .. && rm -rf Maltego",
       #     "essential-tool": False,
       #     "requiresUI": False
       #},
        {
            "package": "Nikto",
            "installation": "sudo apt install -y nikto",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "PadBuster",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Paros",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "Parsero",
            "installation": "sudo pip3 install parsero",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "plecost",
            "installation": "sudo pip3 install plecost",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Powerfuzzer",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "ProxyStrike",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "Recon-ng",
            "installation": "sudo apt install recon-ng -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Skipfish",
            "installation": "sudo apt install skipfish -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "sqlmap",
            "installation": "sudo apt install sqlmap -y",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "Sqlninja",
            "installation": "sudo apt install sqlninja -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "sqlsus",
            "installation": "sudo apt install sqlsus -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "ua-tester",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Uniscan",
            "installation": "sudo apt install uniscan -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "w3af",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "WebScarab",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "Webshag",
            "installation": "echo 'Download unavailable.'",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "WebSlayer",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        },
        {
            "package": "WebSploit",
            "installation": "sudo apt install websploit -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "Wfuzz",
            "installation": "sudo apt install wfuzz -y",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "WhatWeb",
            "installation": "sudo apt install whatweb -y",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "WPScan",
            "installation": "sudo apt install wpscan -y",
            "essential-tool": True,
            "requiresUI": False
        },
        {
            "package": "XSSer",
            "installation": "sudo apt install xsser -y",
            "essential-tool": False,
            "requiresUI": False
        },
        {
            "package": "zaproxy",
            "installation": "UI requires.",
            "essential-tool": False,
            "requiresUI": True
        }
    ]

web_application_analisys = Category(tools)