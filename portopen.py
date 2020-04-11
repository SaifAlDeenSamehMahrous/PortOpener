from threading import Thread
from ports import ports

def run (firstportnumber):
    ob = ports(firstportnumber)
    ob.opentheport()

def main():
    port = int(input('enter first portnumber: '))
    port2 = int(input('enter second portnumber: '))
    allthreads = []
    while (port <= port2):
        t = Thread(target=run, args=(port,))
        allthreads.append(t)
        port += 1

    for t in allthreads:
        t.start()


if (__name__ == '__main__'):
    main()
'''
this is a file that aims to create a server that can open while it is working all 
the ports given in a range taken by the user 
'''