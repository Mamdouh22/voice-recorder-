# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write
import os

plt.close('all')


fs=12000
d=5
#start record

print("say something..")
a= sd.rec(int(fs*d), samplerate = fs , channels= 1, blocking= True)

plt.plot(a) 
plt.title("voice recorder")

print("fishing")
 
#play and save in file
write( 'recorder.mp3', fs, a)
os.startfile("recorder.mp3")