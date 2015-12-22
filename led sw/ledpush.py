#! /usr/bin/env python

import RPi.GPIO as GPIO
import Tkinter

GPIO.setmode(GPIO.BOARD)

LED = 23

GPIO.setup(LED, GPIO.OUT,initial=GPIO.LOW)

def func():

	GPIO.output(LED,not GPIO.input(LED))

root = Tkinter.Tk()

label = Tkinter.Label(root,text='press button')

label.pack()

button = Tkinter.Button(root,text='LED',command=func)

button.pack()

root.mainloop()

GPIO.cleanup()