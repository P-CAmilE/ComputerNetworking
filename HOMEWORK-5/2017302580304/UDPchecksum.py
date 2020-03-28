import numpy as np

# get checksum of UDP segement
def checksum(data1, data2, data3):
    if(data1.bit_length() > 16 or data2.bit_length() > 16
    or data3.bit_length() > 16 or type(data1) != type(1)
    or type(data2) != type(1) or type(data3) != type(1)):
        return 
    tmp = data1 + data2
    if(tmp.bit_length() > 16):
        tmp = tmp + 1
        if(tmp.bit_length() > 16):
            tmp = tmp + 1
    tmp = tmp + data3
    if(tmp.bit_length() > 16):
        tmp = tmp + 1
        if(tmp.bit_length() > 16):
            tmp = tmp + 1
    return 
