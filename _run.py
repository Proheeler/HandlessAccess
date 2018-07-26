#! /usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import PIL
import subprocess

def SpeechToText1():
        r = sr.Recognizer()   #Speech recognition
        with sr.Microphone() as source:
            print("Скажи что нибудь!")
            audio = r.listen(source)
            message = r.recognize_google(audio, language="ru_RU")
        try:
            print("User: " + r.recognize_google(audio, language="ru_RU"))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return message

#function to find importance of words to use them to deduce that which thing is being asked more 

text = SpeechToText1()

passwords=[u'Привет',u'тест',u'мост']

if text in passwords:
        
        print('Пароль правильный, запуск системы распознавания лиц')
        subprocess.call("sr.py", shell=True)
        filename = "c4.jpg"
        args = "match_VS2017.exe " + filename
        p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        # print(str(output).split('\\r\\n'))
        baseDict={}
        for i in str(output).split('\\r\\n'):
                for j in range(len(i.split())):
                        if j%2!=0:
                                #print(i.split()[j])
                                baseDict[i.split()[j]]=i.split()[j-1]
        print(max(baseDict),baseDict[(max(baseDict))])
else:
	print('Неверный пароль')
	


	

