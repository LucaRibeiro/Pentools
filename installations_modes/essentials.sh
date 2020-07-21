#!/bin/bash
GREEN="\033[1;32m"
RED="\033[1;31m"
RESET="\033[0;0m"
##################################################################################################################################################
printf "${GREEN} Installing netcat ${RESET} \n"
if ! sudo dpkg -l | grep -q 'netcat'; then
	sudo apt install netcat -y
fi
####################################################################################################################################################
printf "${GREEN} Installing nmap ${RESET} \n"
if ! sudo dpkg -l | grep -q 'nmap'; then
	sudo apt install nmap -y
fi
####################################################################################################################################################
printf "${GREEN} Installing wfuzz ${RESET} \n"
if ! sudo dpkg -l | grep -q 'wfuzz'; then
	sudo apt install wfuzz -y
fi
####################################################################################################################################################
printf "${GREEN} Installing hydra ${RESET} \n"
if ! sudo dpkg -l | grep -q 'hydra'; then
	sudo apt install hydra -y
fi
####################################################################################################################################################
printf "${GREEN} Installing sqlmap ${RESET} \n"
if ! sudo dpkg -l | grep -q ''; then
	cd /opt && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
fi
####################################################################################################################################################
printf "${GREEN} Installing git-dumper ${RESET} \n"
if ! ls /opt | grep -q 'GitTools'; then
	cd /opt && git clone https://github.com/internetwache/GitTools
fi
####################################################################################################################################################
printf "${GREEN} Installing Metasploit ${RESET} \n"
if ! ls /opt | grep -q 'metasploit-framework'; then
	curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb >msfinstall
	chmod 755 msfinstall
	./msfinstall
	rm -rf ./msfinstall
	clear
fi
####################################################################################################################################################
printf "${GREEN} Installing WPScan ${RESET} \n"
if ! ls /opt | grep -q 'wpscan'; then
	sudo apt install wpscan
fi
####################################################################################################################################################
printf "${GREEN} Installing JohnTheRipper ${RESET} \n"
if ! ls /opt | grep -q 'JohnTheRipper'; then
	cd /opt && sudo git clone https://github.com/magnumripper/JohnTheRipper
fi
#####################################################################################################################################################
printf "${GREEN} Adding SecList ${RESET} \n"
if ! ls /opt | grep -q 'SecList'; then
	cd /opt && sudo git clone https://github.com/danielmiessler/SecLists.git
fi