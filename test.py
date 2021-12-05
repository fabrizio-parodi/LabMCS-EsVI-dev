#!/usr/bin/python
    
import sys,serial
from dmm import *

file = open("out.dat","w")
ser = serial.Serial("/dev/ttyUSB0", 9600)
V,eV = dmmread(ser)
print(V,eV)
file.write(str(V)+"\t")
file.write(str(eV)+"\t")
file.write("\n")
