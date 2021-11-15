import pexpect
import json


# import sys
# import logging
import time
from datetime import datetime


class GatttoolBridge:
    def __init__(self,DEVICE_MAC_ADDRESS=[],uuid_char=[],handle_char=[]):
        self.connected_to_peripheral = False
        self.last_Messages=[]
        self.last_update = datetime.now()
        
        self.setDeviceMacAddress(DEVICE_MAC_ADDRESS)
        self.setUuid(uuid_char)
        self.setHnd(handle_char)

        self.autoMACADRESS=False
        pass
    
    def setDeviceMacAddress(self,DEVICE_MAC_ADDRESS):
        if self.connected():
            print("Disconnecting from "),
            print(self.DEVICE_MAC_ADDRESS)
            while not self.disconnectBLEWthGatttool():
                pass
            
        self.DEVICE_MAC_ADDRESS=DEVICE_MAC_ADDRESS
        pass
        
    def setUuid(self,uuid_char):
        if not len(uuid_char)==0:
            self.uuid_char=uuid_char
        pass
    
    def setHnd(self,handle_char):
        if not len(handle_char)==0:
            self.handle_char=handle_char
        pass
    
    def addUuid(self,uuid_char):
        self.uuid_char.extend(uuid_char)
        pass
    
    def addHnd(self,handle_char):
        self.handle_char.extend(handle_char)
        pass
    
    def connected(self):
        return self.connected_to_peripheral
    
    def message(self):
        return self.last_Messages,self.last_update
    
    def launchGatttool(self,**kwargs):
        # kwargs : (random,listen,adress)
        cmd_line="gatttool -I -m 244"

        if "random" in kwargs:
            if kwargs["random"] and isinstance(kwargs["random"],bool):
                cmd_line+=" -t random"

        if "listen" in kwargs:
            if kwargs["listen"] and isinstance(kwargs["listen"],bool):
                cmd_line+=" --listen"

        if "adress" in kwargs:
            if kwargs["adress"] and isinstance(kwargs["adress"],bool) and len(self.DEVICE_MAC_ADDRESS):
                cmd_line+=" -b "+self.DEVICE_MAC_ADDRESS
                self.autoMACADRESS=True

        # Run gatttool interactively.
        print("Run gatttool with ...")
        print(cmd_line)
        self.child = pexpect.spawn(cmd_line)
        
    def connectBLEWthGatttool(self):
        # Use gatttool interactively opened in 'child' to connect the BLE device
        # with its MAC address in 'DEVICE_MAC_ADDRESS'
        self.connected_to_peripheral = False
        k=0
        while not self.connected() and k<10:
            try:
                # Connect to the device.
                print("Connecting to "),
                print(self.DEVICE_MAC_ADDRESS)
                if self.autoMACADRESS:
                    self.sendLine("connect")
                else:
                    self.sendLine("connect {0}".format(self.DEVICE_MAC_ADDRESS))
                print("toto")
                self.expect("Connection successful", timeout_=5)
                print("tata")
                self.connected_to_peripheral = True
                print(" Connected!")
            except:
                k+=1
                print("Connection failed",k+1,"/ 10")
                time.sleep(1)
                if k<10:
                    print("Retrying...")
                else:
                    print("Too many attempt to try connecting {0}".format(self.DEVICE_MAC_ADDRESS))
        
        if not self.connected():
            self.disconnectBLEWthGatttool()
    
        return self.connected()
    
    def disconnectBLEWthGatttool(self):
        # disconnect the BLE device from gatttool interactively opened in 'spawn'
        self.sendLine("disconnect")
        # Close the interactive session of gatttool in 'spawn'
        self.sendLine("exit")
        
        self.connected_to_peripheral = False
        return self.connected()
    
    def charReadUuid(self,uuid_char):
        # Read the Characteristic value of 'spawn' from the Characteristic UUID in
        # 'uuid_char'
        self.sendLine("char-read-uuid {0}".format(uuid_char))
        self.expect("value: ", timeout_=10)
        self.expect("\r\n", timeout_=10)
        return self.child.before
    
    def charReadHnd(self,handle_char):
        # Read the Characteristic value of 'spawn' from the Characteristic handle in
        # 'handle_char'
        self.sendLine("char-read-hnd {0}".format(handle_char))
        self.expect("value/descriptor: ", timeout_=10)
        self.expect("\r\n", timeout_=10)
        return self.child.before
    
    def sendLine(self,line):
        self.child.sendline(line)

    def expect(self,line,timeout_=1):
        self.child.expect(line, timeout=timeout_)
        self.child.expect("\r\n", timeout=timeout_)
        return self.child.before
        
    def update(self):
        if self.connected():
            self.last_Messages=[]
            for k in self.uuid_char:
                message=self.charReadUuid(k)
                self.last_Messages.append(message)
                
            for k in self.handle_char:
                message=self.charReadHnd(k)
                self.last_Messages.append(message)
            
            self.last_update = datetime.now()
        pass
    
    def to_json(self):
        result = {
            'name': self.__class__.__name__,
            'timestamp': int(self.last_update.timestamp()),
            'connected': self.connected(),
            'messages': self.last_Messages.tolist()
        }
        return json.dumps(result)
        

def launchGatttool():
    # Run gatttool interactively.
    print("Run gatttool...")
    child = pexpect.spawn("gatttool -I")
    return child

#connection
def connectBLEWthGatttool(spawn,DEVICE_MAC_ADDRESS):
    # Use gatttool interactively opened in 'spawn' to connect the BLE device
    # with its MAC address in 'DEVICE_MAC_ADDRESS'
    connected_to_peripheral = False
    k=0
    while not connected_to_peripheral and k<10:
        try:
            # Connect to the device.
            print("Connecting to "),
            print(DEVICE_MAC_ADDRESS)
            spawn.sendline("connect {0}".format(DEVICE_MAC_ADDRESS))
            spawn.expect("Connection successful", timeout=5)
            connected_to_peripheral = True
            print(" Connected!")
        except:
            k+=1
            print("Connection failed",k+1,"/ 10")
            time.sleep(1)
            if k<10:
                print("Retrying...")
            else:
                print("Too many attempt to try connecting {0}".format(DEVICE_MAC_ADDRESS))

    return connected_to_peripheral

def disconnectBLEWthGatttool(spawn):
    # disconnect the BLE device from gatttool interactively opened in 'spawn'
    spawn.sendline("disconnect")
    # Close the interactive session of gatttool in 'spawn'
    spawn.sendline("exit")

def charReadUuid(spawn,uuid_char):
    # Read the Characteristic value of 'spawn' from the Characteristic UUID in
    # 'uuid_char'
    spawn.sendline("char-read-uuid {0}".format(uuid_char))
    spawn.expect("value: ", timeout=10)
    spawn.expect("\r\n", timeout=10)
    return spawn.before

def charReadHnd(spawn,handle_char):
    # Read the Characteristic value of 'spawn' from the Characteristic handle in
    # 'handle_char'
    spawn.sendline("char-read-hnd {0}".format(handle_char))
    spawn.expect("value/descriptor: ", timeout=10)
    spawn.expect("\r\n", timeout=10)
    return spawn.before
