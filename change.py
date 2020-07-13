#!/usr/bin/python
import os
from clone import *
from install import *
from myip import *

def change():
  os.system("sudo anonsurf change")

anon()
print("status before\n
=======================")
stat()
print ("ip before\n
=======================")
change()
print("status after\n
=======================")
stat()
print("ip after\n
========================")
myip
