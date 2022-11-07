#import Diff
from difflib import Differ
#Open file 
with open('backup.py') as backup_1, open('backup2.py') as backup_2:
    differ = Differ()
 
    for line in differ.compare(backup_1.readlines(), backup_2.readlines()):
        print(line) 
