#############################################################
### __ /        _ |   \_) |   
###  _ \\ \ / _ \ | (  ||  _| 
### ___/ _\_\.__/_|\__/_|\__| 
###         _|                
###                                                          
### name: 3xp10it.py
### function: exp10itScanner
### date: 2016-11-07
### author: quanyechavshuo
### blog: http://3xp10it.cc
#############################################################
import re
import os
import time
os.system("pip3 install exp10it -U --no-cache-dir")
from exp10it import figlet2file
from exp10it import exp10itScanner
from exp10it import get_string_from_command
figlet2file("3xp10it",0,True)
time.sleep(1)

a=get_string_from_command("apt list python-requests")
if not re.search(r"python-requests",a,re.I):
    os.system("apt-get install python-requests")
a=get_string_from_command("apt list python-dnspython")
if not re.search(r"python-dnspython",a,re.I):
    os.system("apt-get install python-dnspython")

exp10itScanner()
