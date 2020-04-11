from threading import Thread
from ports import ports

def run (portname):
    object =ports(portname)
    s= object.isopen()
    print(s)
def main():
    port = [80,22,443,21]
    allthreads = []
    for i in port:
        t = Thread(target=run, args=(i,))
        allthreads.append(t)
    for t in allthreads:
        t.start()


if __name__== '__main__':
    main()

'''
this is a file it aims to scan specific ports and see's if it is open or closed
'''