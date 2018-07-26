#! /usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import PIL
import subprocess

print('success')
subprocess.call("sr.py", shell=True)
filename = "c4.jpg"
args = "match_VS2017.exe " + filename
p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
# print(str(output).split('\\r\\n'))
baseDict={}
for i in str(output).split('\\r\\n'):
		# print(len(i.split()))
		for j in range(len(i.split())):
				# print(j)
				if j%2!=0:
						print(i.split()[j-1])
						baseDict[i.split()[j]]=i.split()[j-1]
print(max(baseDict),baseDict[(max(baseDict))])