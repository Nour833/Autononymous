#!/usr/bin/python
import os
from clone import *
from install import *



def permissions():
  os.system(" chmod +x change.py && chmod +x clone.py && chmod +x install.py ")
permissions()
clone()
install()
def anon():
  os.system("sudo anonsurf start")
  
anon()
def stat():
  os.system("sudo anonsurf status")
stat()
def macauto():
  os.system("sudo bash installermac.sh && sudo automac")
macauto()
