import serial
import time

#%% Basic command methods

class ATDevice:
    def __init__(self, port, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def open(self):
        self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def close(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            
    def isopen(self):
        if (self.serial.isOpen() == True):
            print("Serial port is OPENED")
        else:
            print("Serial port is CLOSED")
            
    def Reboot(self):
        print("Device reboot!!")
        self.serial.write(('ATZ' + '\r\n').encode())

    def Send_Command(self, command, wait_time=2):
        self.serial.write((command + '\r\n').encode())
        time.sleep(wait_time)
        reply = self.serial.read(self.serial.inWaiting())
        return reply.decode('utf-8', 'ignore')
    
    def getFrequency(self):
        self.serial.write(('AT+CHS=?' + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Current Frequency: \n", response)
        
    def getDataRate(self):
        self.serial.write(('AT+DR=?' + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Current DataRate: \n", response)
        
    def getADR(self):
        self.serial.write(('AT+ADR=?' + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Current ADR: \n", response)
        
    def getTxPower(self):
        self.serial.write(('AT+TXP=?' + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Current Tx Power: \n", response)

#%% Custom command methods 1
        
    def Check_Config(self):
        command = "AT+CFG"
        return self.Send_Command(command)
    
    def Check_Network_Join_Status(self):
        command = "AT+NJS=?"
        return self.Send_Command(command)
    
    def Send_Uplink_Message(self, ack_type, f_port, retransmission, payload, wait_time=2):
        command = "AT+SEND={},{},{},{}".format(ack_type, f_port, retransmission, payload)
        self.serial.write((command + '\r\n').encode())
        time.sleep(3)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Response to sending message: \n", response)

    def Print_Downlink_Message(self):
        command = "AT+RECVB=?"
        self.serial.write((command + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Response to sending message: \n", response)

#%% Custom command methods 2
        
    def setFrequency(self, Freq):
        # Channel 922100000 // 922.3 // 922.5 ...
        self.getFrequency()
        command = "AT+CHS={}".format(Freq)
        self.serial.write((command + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Changed frequency: \n", Freq, response)
        
    def setDataRate(self, DR):
        # Min 0 ~ Max 7
        self.getDataRate()
        command = "AT+DR={}".format(DR)
        self.serial.write((command + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Changed datarate is applied after device reboot: \n", DR, response)
        print("Reboot in 3 seconds \n")
        time.sleep(3)
        self.Reboot()
        
    def setADR(self, ADR):
        # Enable 1 // Unable 0
        command = "AT+ADR={}".format(ADR)
        self.serial.write((command + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Changed ADR: \n", ADR, response)
        
    def setTxPower(self, TxP):
        # Min 0 ~ Max 5
        command = "AT+TXP={}".format(TxP)
        self.serial.write((command + '\r\n').encode())
        time.sleep(0.5)
        reply = self.serial.read(self.serial.inWaiting())
        response = reply.decode('utf-8', 'ignore')
        print("Changed Tx Power: \n", TxP, response)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        