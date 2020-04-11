import socket
class ports:
    def __init__(self ,port):
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.port = port
        self.socketinfo = (self.host ,self.port)

    def setnewport(self ,port):
        self.port =port


    def isopen(self):
        try:
            self.sock.connect(self.socketinfo)
            return 'port {0} is open\n'.format(self.port)
        except Exception as e :
            return 'port {0} is closed\n'.format(self.port)
        self.sock.close()

    def opentheport(self):
        try:
            self.sock.bind(self.socketinfo)
            self.sock.listen(5)
            print('Server is starting...')
            while(True):
                client,address = self.sock.accept()
                print('connection from {0} '.format(address))
                client.send('thanks for opening our server')
                client.close()
        except Exception as e:
            raise e
