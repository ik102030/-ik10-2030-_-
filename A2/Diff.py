#import libraries
from difflib import Differ
import os
#Open files 
with open('backup2.txt') as backup_2:
    differ = Differ()
with open('backup3.txt') as backup_3:
    differ = Differ()
#Read contents and call the compare function with the use of differ class object 
    for line in differ.compare('backup_2.readlines()','backup_3.readlines()'):
        print(line)

compare = os.system("diff myswitches myswitches2 myswitches3")
print(compare)


        #Open files 
with open('backup.py') as backup_2, open('backup2.py') as backup_2:
    differ = Differ()
with open('backup.py') as backup_3, open('backup3.py') as backup_2:
    differ = Differ()

#Read contents and call the compare function with the use of differ class object 
    for line in differ.compare(backup_2.readlines(), backup_3.readlines()):
        print(line)
