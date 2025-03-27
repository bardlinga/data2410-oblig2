how to run

server.py and server-multithread.py has to be run in the same directory as index.html.

servers can be run in bash or wsl with the following commands:
    $ python3 server.py 
    $ python3 server-multithread.py

client can be run with the following command:
    $ python3 client.py

without any arguments the client will try to connect to 127.0.0.1:8001 by default
ip and port can be specified with the -i and -p options, as such:
    $ python3 client.py -i 10.0.1.2 -p 9000

the server.py in the mininet demo had the IP edited to 10.0.1.2 as per the h3 ip, as shown in the ifconfig.