# convert hex number written as str to  int
# only treat signed 16bits = 2bytes number
def hexStrToInt(hexstr):
    val = int(hexstr[:2], 16) + (int(hexstr[3:5],16)<<8)
    if ((val&0x8000)==0x8000): # treat signed 16bits
        val = -((val^0xffff)+1)
    return val
