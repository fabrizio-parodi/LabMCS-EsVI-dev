#!/usr/bin/python
    
import sys,serial
import numpy as np
from dmm import *
from pyvisa import ResourceManager
import time

rm = ResourceManager()
instr = rm.open_resource("USB0::0x0AAD::0x0135::035375056::INSTR")

instr.write("INST:NSEL 1")
instr.query("INST?")
instr.write("INST OUT1")
instr.write("OUTP ON")


ser = serial.Serial("COM3", 9600)
ser1 = serial.Serial("COM5", 9600)

file = open("out.dat","w")
xV = np.array([5,8,10,12,15,18,20,25,28])
for i in range(len(xV)):
    cmd = f"APPLY {xV[i]},0.1"
    instr.write(cmd)
#    print(instr.write(cmd))
    time.sleep(1)
    A,eA = dmmread(ser1)
    time.sleep(1)
    print(xV[i],A,eA)
    file.write(str(xV[i]))
    file.write("\t ")
    file.write(str(A))
    file.write("\t ")
    file.write(str(eA))
    file.write("\n")


