#!/usr/bin/python
    
import sys,serial
import numpy as np
from dmm import *
from ps import *
import time

instr = psinit()
pssel(instr,1)

ser = serial.Serial("COM3", 9600)
command(ser,"CURR:DC:AUTO ON")

file = open("out.dat","w")
xV = np.array([0.4,0.42,0.44,0.46,0.48,0.50])
for i in range(len(xV)):
    cmd = f"APPLY {xV[i]},0.1"
    instr.write(cmd)
    time.sleep(1)
    A,eA = dmmread(ser)
    time.sleep(1)
    print(xV[i],A,eA)
    file.write(str(xV[i]))
    file.write("\t ")
    file.write(str(A))
    file.write("\t ")
    file.write(str(eA))
    file.write("\n")


