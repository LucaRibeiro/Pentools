#!/bin/bash
GREEN="\033[1;32m"
RED="\033[1;31m"
RESET="\033[0;0m"


#####################################################################################################################################################
printf "${GREEN} Installing netcat ${RESET} \n"
if  ! sudo apt list --installed | grep -q 'netcat';then
	sudo apt install netcat -y
else
	printf "${RED} Is already installed ${RESET} \n"
####################################################################################################################################################
printf "${GREEN} Installing nmap ${RESET} \n"
if  ! sudo apt list --installed | grep -q 'nmap';then
	sudo apt install nmap -y
else
	printf "${RED} Is already installed ${RESET} \n"
####################################################################################################################################################
printf "${GREEN} Installing wfuzz ${RESET} \n"
if  ! sudo apt list --installed | grep -q '';then
	sudo apt install wfuzz -y
else
	printf "${RED} Is already installed ${RESET} \n"
####################################################################################################################################################
printf "${GREEN} Installing hydra ${RESET} \n"
if  ! sudo apt list --installed | grep -q '';then
	sudo apt install hydra -y
else
	printf "${RED} Is already installed ${RESET} \n"
####################################################################################################################################################
printf "${GREEN} Installing sqlmap ${RESET} \n"
cd /opt && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
export SQLMAP=/opt/sqlmap-dev
export PATH=$PATH:$SQLMAP
####################################################################################################################################################
printf "${GREEN} Installing git-dumper ${RESET} \n"
cd /opt && git clone https://github.com/arthaud/git-dumper.git
pip install -r git-dumper/requirements.txt
export GIT_DUMPER=/opt/git-dumper
export PATH=$PATH:$GIT_DUMPER
####################################################################################################################################################
printf "${GREEN} Installing Metasploit ${RESET} \n"
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
chmod 755 msfinstall
./msfinstall
rm -rf ./msfinstall
clear
####################################################################################################################################################
printf "${GREEN} Installing WPScan ${RESET} \n"
sudo apt-get install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev
cd /opt && git clone https://github.com/wpscanteam/wpscan.git
cd wpscan
sudo gem install bundler && bundle install --without test development -y
####################################################################################################################################################
printf "${GREEN} Installing JohnTheRipper ${RESET} \n"
cd /opt && sudo git clone https://github.com/magnumripper/JohnTheRipper
export JOHN_THE_RIPPER=/opt/JohnTheRipper
export PATH=$PATH:$JOHN_THE_RIPPER
#####################################################################################################################################################
printf "${GREEN} Adding SecList ${RESET} \n"
cd /opt && sudo git clone https://github.com/danielmiessler/SecLists.git
####################################################################################################################################################