
import socket
import math

class SkyHD():
    CODES = {
        "power": 0,
        "select": 1,
        "backup": 2,
        "channelup": 6,
        "channeldown": 7,
        "interactive": 8,
        "help": 9,
        "services": 10,
        "tvguide": 11,
        "i": 14,
        "text": 15, 
        "up": 16,
        "down": 17,
        "left": 18,
        "right": 19,
        "red": 32,
        "green": 33,
        "yellow": 34,
        "blue": 35,
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
        "play": 64,
        "pause": 65,
        "stop": 66,
        "record": 67,
        "fastforward": 69,
        "rewind": 71,
        "boxoffice": 240,
        "sky": 241 
    }

    def __init__(self, ipAddress):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ipAddress, 49160))

        self.__handShake()

        for name, cmd in self.CODES.items():
            self.__addMethod(name, cmd)

    def sendCode(self,code):
        b = bytearray([4,1,0,0,0,0,int(math.floor(224 +(code/16))), code % 16])
        self.sock.send(b)

        b[1] = 0
        self.sock.send(b)

    def close(self):
        self.sock.close()

    def __addMethod(self, name, code):
        def innerCode():
            self.sendCode(code)

        setattr(self,name,innerCode)

    def __handShake(self):
        data = self.sock.recv(1024)
        l = 12

        while len(data) < 24:
            response = bytearray(data[0:l])
            l = 1

            self.sock.send(response)
            data = self.sock.recv(1024)        




    


