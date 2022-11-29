#!/usr/bin/python
    
import sys,serial
import numpy as np
from dmm import *
from pyvisa import ResourceManager
import time

rm = ResourceManager()
instr = rm.open_resource("USB0::0x0AAD::0x0135::035375048::INSTR")


instr.write("INST:NSEL 1")
instr.query("INST?")
instr.write("INST OUT1")
instr.write("OUTP ON")


ser = serial.Serial("COM3", 9600)
command(ser,'VDC')
reset(ser)
        
file = open("out.dat","w")
xV = np.array([1.0,1.5,2.0,2.5,3.0,3.5])
for i in range(len(xV)):
    cmd = f"APPLY {xV[i]},0.1"
    instr.write(cmd)
    time.sleep(1)
    
    V,eV = dmmread(ser)
    
    print(xV[i],V,eV)
    file.write(str(xV[i]))
    file.write("\t ")
    file.write(str(V))
    file.write("\t ")
    file.write(str(eV))
    file.write("\n")


