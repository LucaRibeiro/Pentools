#!/bin/bash
sudo apt update
sudo apt upgrade -y
sudo apt install dpkg -y

if ! sudo dpkg -l | grep -q 'python3'; then
	sudo apt install python3
fi
if ! sudo dpkg -l | grep -q 'python-minimal'; then
	sudo apt install python-minimal
fi
if ! sudo dpkg -l | grep -q 'python3-pip3'; then
	sudo apt install python3-pip
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'perl'; then
	sudo apt install perl
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'ruby'; then
	sudo apt install ruby
fi
if ! sudo dpkg -l | grep -q 'gem'; then
	sudo apt install gem
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'git'; then
	sudo apt install git -y
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'curl'; then
	sudo apt install curl -y
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'vim'; then
	sudo apt install vim -y
fi
if ! sudo dpkg -l | grep -q 'vi'; then
	sudo apt install vi -y
fi
####################################################################################################################################################
if ! sudo dpkg -l | grep -q 'wget'; then
	sudo apt install wget -y
fi
####################################################################################################################################################