#importing libraries 
import getpass
import telnetlib
import os 
def backup():
    user = str(input('Enter your telnet username: '))
    password = getpass.getpass()

    #opening myswitches and creating it in the python script
    f = open('myswitches2.txt', 'w')
    f.write("192.168.56.101")
    f.close()
    

    f = open('myswitches2.txt', 'w')
    f.write("192.168.56.101")
    f.close()
   

    for ip in f:
        ip=ip.strip()
        print ('Get running config from switch ' + (ip))
        HOST = ip 
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b'Username: ')
        tn.write(user.encode('ascii') + b'\n')
        if password:
            tn.read_until(b'Password: ') 
            tn.write(password.encode('ascii') + b'\n')
        tn.write(b"enable\n")  
        tn.read_until(b'Password: ') 
        tn.write(("class123!").encode('ascii') + b'\n')
        tn.write(b"terminal length 0\n")
        tn.write(b"show run\n")
        tn.write(b'exit\n')

    
        
        
        tn.write(b"enable\n")  
        tn.read_until(b'Password: ') 
        tn.write(("class123!").encode('ascii') + b'\n')
        tn.write(b"terminal length 0\n")
        startupconfig = tn.write(b"show startup-config\n")
        runconfig = tn.write(b"show running-config\n")
        tn.write(b'exit\n')
        save_start = open('backup2.txt', 'w')
        save_start.write(startupconfig)
        save_start.close()
        save_run = open('backup3.txt', 'w')
        save_run.write(runconfig) 
        save_run.close()       


        
        compare = os.system ("diff backup2.txt backup3.txt")
        print(compare)
backup() 
