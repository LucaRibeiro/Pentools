#!/usr/bin/python3

tools = [
    {
        "package": "apache-users",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Arachni",
        "instalation": "sudo apt-get install build-essential-tool curl libcurl4 libcurl4-openssl-dev ruby ruby-dev & sudo gem install arachni",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "BBQSQL",
        "instalation": "sudo pip install bbqsql",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "BlindElephant",
        "instalation": "cd /opt & sudo git clone https://github.com/lokifer/BlindElephant/blob/master/src/setup.py & cd blindelephant/src & sudo python setup.py install",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Burp Suite",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "CutyCapt",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "DAVTest",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "deblaze",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "DIRB",
        "instalation": "sudo apt install dirb -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "DirBuster",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "fimap",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "FunkLoad",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Gobuster",
        "instalation": "sudo apt install gobuster -y",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "Grabber",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "hURL",
        "instalation": "sudo apt-get install hurl -y'",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "jboss-autopwn",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "joomscan",
        "instalation": "sudo apt-get install joomscan -y'",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "jSQL Injection",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "Maltego Teeth",
        "instalation": "mkdir ~/Maltego && cd ~/Maltego &&  sudo wget https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.2.11.13104.deb && sudo dpkg –i Maltego.v4.2.11.13104.deb && cd .. && sudo rm -rf Maltego",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Nikto",
        "instalation": "sudo apt install -y nikto",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "PadBuster",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Paros",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "Parsero",
        "instalation": "sudo pip3 install parsero",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "plecost",
        "instalation": "sudo pip3 install plecost",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Powerfuzzer",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "ProxyStrike",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "Recon-ng",
        "instalation": "sudo apt install recon-ng -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Skipfish",
        "instalation": "sudo apt install skipfish -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "sqlmap",
        "instalation": "sudo apt install sqlmap -y",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "Sqlninja",
        "instalation": "sudo apt install sqlninja -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "sqlsus",
        "instalation": "sudo apt install sqlsus -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "ua-tester",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Uniscan",
        "instalation": "sudo apt install uniscan -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "w3af",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "WebScarab",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "Webshag",
        "instalation": "Download unavailable.",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "WebSlayer",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    },
    {
        "package": "WebSploit",
        "instalation": "sudo apt install websploit -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "Wfuzz",
        "instalation": "sudo apt install wfuzz -y",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "WhatWeb",
        "instalation": "sudo apt install whatweb -y",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "WPScan",
        "instalation": "sudo apt install wpscan -y",
        "essential-tool": True,
        "requiresUI": False
    },
    {
        "package": "XSSer",
        "instalation": "sudo apt install xsser -y",
        "essential-tool": False,
        "requiresUI": False
    },
    {
        "package": "zaproxy",
        "instalation": "UI requires.",
        "essential-tool": False,
        "requiresUI": True
    }
]