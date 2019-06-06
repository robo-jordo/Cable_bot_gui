#!/usr/bin/env python
import serial
import time

class SerialCom1(object):
    def __init__(self,port,len=8):
        self.ser = serial.Serial(port, 115200, timeout=0.05)
        self.commandToSend = b'24242428'
        self.gottenData = ''
        self.dataLen = len

    def uart_write(self,msg):
        self.commandToSend=b''
        print("message:", msg)
        self.commandToSend = bytes(msg)
        self.ser.write(self.commandToSend)
        readMsg = []
        readMsg = self.uart_read()
        # readMsg = self.ser.read(1)
        self.ser.flush()  # flush the buffer
        return readMsg

    def uart_read(self):
        msg = []
        while True:
            try:
                readOut = self.ser.readline().decode('ascii')
                if not readOut.strip():
                    break
                msg.append(readOut)
            except:
                pass
        return msg

# if __name__ == '__main__':
    # # test = SerialCom('COM5',8)
    # test = SerialCom('COM5',8)
    # stopCommand = "0 0 0 0 1 1 1 1 "
    # # commandSeries = ["30 30 30 30 1 1 1 1 ","30 30 30 30 0 0 0 0 ","20 20 20 20 1 1 1 1 ","20 20 20 20 0 0 0 0 "]
    # # commandSeries = ["50 50 50 50 1 1 1 1 ","50 50 50 50 0 0 0 0 ","20 20 20 20 1 1 1 1 ","20 20 20 20 0 0 0 0 ",
    # #                  "30 30 30 30 0 0 1 1 ","30 30 30 30 1 1 0 0 ","50 50 50 50 0 0 1 1 ","50 50 50 50 0 1 1 0 ",
    # #                  "50 50 50 50 1 0 0 1 ", "50 50 50 50 0 1 1 0 "]

    # commandSeries = ["50245 50000 50000 50000 1 1 1 1 ","80000 80000 80000 80000 0 0 0 0 ","60000 60000 60000 60000 1 1 1 1 ",
    #                  "50000 50000 50000 50000 0 0 0 0 "]
    # secs = [5-3,5-3,4-2,4-2,5-2,10-6,5-2,5-2,10-4,5-2]

    # test.uart_write(stopCommand)
    # time.sleep(2)
    # i = 0
    # for myCmd in commandSeries:
    #     recMsg = test.uart_write(myCmd)
    #     print(recMsg)
    #     # for m in recMsg:
    #     #     print(m)
    #     i= i+1
    # test.uart_write(stopCommand)




