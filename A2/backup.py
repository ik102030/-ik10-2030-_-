#importing libraries 
import getpass
import telnetlib
def backup():
    user = str(input('Enter your telnet username: '))
    password = getpass.getpass()

    #opening myswitches and creating it in the python script
    f = open('myswitches.txt', 'w')
    f.write("192.168.56.101")
    f.close()
    f=open('myswitches.txt', 'r')

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

        readoutput = tn.read_all()
        saveoutput = open("switch" + HOST, "w")
        saveoutput.write(readoutput.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close
backup() 
