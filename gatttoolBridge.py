import pexpect

import sys
import logging
import time

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
                print("Too many attempt to try connecting {0}".format(DEVICE))

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
