import serial
import time

class SerialCOm(object):
    def __init__(self,port):
        # Spin up the Serial Port
        self.tiva = serial.Serial()
        self.tiva.baudrate = 230400
        self.tiva.port = port
        self.tiva.timeout = 1
        self.tiva.open()

    def writeData(self,cmd):
        # Write to uart
        self.tiva.write(cmd.encode('utf-8'))
        #print("sending:",cmd)
        self.tiva.flush()
        # Print back and block for receipt
        msg = self.tiva.readline().decode('utf-8')
        #print("sent:",msg)

    def writeDataPack2(self,com_packet):
        #send over each command in command packet
        self.tiva.reset_input_buffer()
        self.waitWriting()
        for cmd in com_packet:
            self.writeData(cmd)
        response = self.waitWriting()
        return response

    def writeDataPack(self,com_packet):
        #send over each command in command packet
        self.tiva.reset_input_buffer()
        self.waitWriting()
        for cmd in com_packet:
            self.writeData(cmd)

    def waitWriting(self):
        self.tiva.timeout = None
        response = self.tiva.readline().decode('utf-8')
        self.tiva.timeout = None
        return response

    def sendStopCommand(self, magnet):
        stop_packet = [
            '0 m 0 1;',
            '1 m 0 1;',
            '2 m 0 1;',
            '3 m 0 1;',
            '4 e '+str(magnet)+ ' 0;']
        self.writeDataPack(stop_packet)

def testGood():
    # Communication protocol: send over an individual command for each "device" connected to Tiva
    # Format is 'device_id device_type param1 param2;'
    # device_type isn't working rn
    # semicolon (;) termination is vital

    # example command packet for 4 motors
    com_packet = ['0 m 20000 0;',
                  '1 m 20001 0;',
                  '2 m 20002 0;',
                  '3 m 20003 0;']

    stop_packet = [
        '0 m 0 1;',
        '1 m 0 1;',
        '2 m 0 1;',
        '3 m 0 1;']

    # Spin up the Serial Port
    tiva = serial.Serial()
    tiva.baudrate = 230400
    tiva.port = 'COM11'
    tiva.timeout = 1

    start_time = time.time()

    tiva.open()

    for i in range(100):
        # Print out what its sending at the start
        outstring = str(i) + ": " + str(com_packet[0])
        print(outstring)

        # Block progress with timeouts, In future, should do try-catch for failure states
        tiva.timeout = None
        print(tiva.readline().decode('utf-8'));

        tiva.timeout = None

        # send over each command in command packet
        for cmd in com_packet:
            # Write to uart
            tiva.write(cmd.encode('utf-8'))
            print(cmd);
            tiva.flush()
            # Print back and block for receipt
            print("received:")
            print(tiva.readline().decode('utf-8'))

    # Check time
    end_time = time.time()

    outstring = "Time: " + str(end_time - start_time)
    print(outstring)

    # Close the serial port
    tiva.close()

if __name__ == '__main__':
    tivaSerial = SerialCOm("COM11")
    com_packet = ['0 m 20000 0;',
                '1 m 20001 0;',
                '2 m 20002 0;',
                '3 m 20003 0;']
    startTime = time.time()

    for i in range(200):
        tivaSerial.writeDataPack(com_packet)
    tivaSerial.sendStopCommand()
    endTime = time.time()

    print("time:",endTime-startTime)

