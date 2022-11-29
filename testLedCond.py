#!/usr/bin/python
    
import sys,serial
import numpy as np
from dmm import *
from pyvisa import ResourceManager
import time

rm = ResourceManager()
instr = rm.open_resource("USB0::0x0AAD::0x0135::034083383::INSTR")


instr.write("INST:NSEL 1")
instr.query("INST?")
instr.write("INST OUT1")
instr.write("OUTP ON")


ser = serial.Serial("COM4", 9600)
command(ser,'VDC')
reset(ser)
        
file = open("out.dat","w")

cmd = f"APPLY {3},0.1"
instr.write(cmd)
time.sleep(5)

#cmd = f"APPLY {0},0.1"
#instr.write(cmd)
input('apri interruttore')
t0 = time.time()
for i in range(5):
    V,eV = dmmread(ser)
    dt = time.time()-t0
    
    print(dt,V,eV)
    file.write(str(dt))
    file.write("\t ")
    file.write(str(V))
    file.write("\t ")
    file.write(str(eV))
    file.write("\n")


