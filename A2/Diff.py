#import Diff
from difflib import Differ
#Open files 
with open('backup.py') as backup_1, open('backup3.py') as backup_3:
    differ = Differ()
#Read contents and call the compare function with the use of differ class object 
    for line in differ.compare(backup_1.readlines(), backup_3.readlines()):
        print(line) 
