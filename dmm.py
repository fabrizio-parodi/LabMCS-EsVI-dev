#!/usr/bin/python
    
import time
import serial

def command(ser,string):
    string = string + "\r\n"
#    ser.write(bytes(string,"UTF-8"))
    ser.write(b'ADC\r\n')
    time.sleep(.5)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
def dmmread(ser):
    # Lettura del valore
    ser.write(b'val1?\r\n')
    time.sleep(.5)
    line = ser.readline()
    val  = line.decode('ascii').split()
    fval = float(val[0])
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    # Lettura del range
    ser.write(b'range1?\r\n')
    time.sleep(.5)
    line  = ser.readline()
    ival  = line.decode('ascii').split()
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    
    ind = int(ival[0])-1

    error = 0
    if val[1]=="ADC":
        range = [ 0.000200, 0.002000 , 0.020 ,  0.200,  2    , 10  ]
        rel   = [ 0.03    , 0.02    , 0.04  ,  0.03 ,  0.08 , 0.20 ]
        relr  = [ 0.005   , 0.005    , 0.02  ,  0.008,  0.02 , 0.01 ]
        error = abs(fval*rel[ind]/100) + relr[ind]/100*range[ind]
    elif val[1]=="VDC":
        range = [ 0.200,     2 ,    20,  200 ,  1000]
        rel   = [ 0.015 ,  0.015 , 0.015 , 0.015 ,  0.015]
        relr  = [ 0.004,  0.003, 0.004, 0.003, 0.003]  
        error = abs(fval*rel[ind])/100 + relr[ind]/100*range[ind]
    elif val[1]=="OHMS":
        range = [ 200,     2e3 ,    20e3,  200e3 ]
        rel   = [ 0.03 ,  0.02 , 0.02 , 0.02 ]
        relr  = [ 0.004,  0.003, 0.003, 0.003]
        error = abs(fval*rel[ind])/100 + relr[ind]/100*range[ind] + 0.2

    return fval,error
                        
