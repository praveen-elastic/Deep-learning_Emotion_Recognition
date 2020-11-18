# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:40:54 2020

@author: praveen
"""
import h5py
import tkinter as tk
from tkinter import *
#import cv2
import csv
import os
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
#from PIL import Image,ImageTk
import pandas as pd
import datetime
from keras.models import load_model
model = load_model('eegfit.h5')
from numpy import genfromtxt
my_data = genfromtxt('file.csv', delimiter=',')
my_data=np.delete(my_data,14,1)
meann=np.mean(my_data,axis=0)
mediann=np.median(my_data,axis=0)
varn=np.var(my_data,axis=0)
stdn=np.std(my_data,axis=0)
maxn=np.max(my_data,axis=0)
minn=np.min(my_data,axis=0)
xnew=np.vstack((meann,mediann,maxn,minn,stdn,varn))
xnew=xnew.reshape(1,14,6)

ynew=model.predict(xnew)

import time
#import pymysql
window = tk.Tk()
window.title("Emotion Recognititon Tool")

window.geometry('1280x720')
window.configure(background='snow')

def clear():
    txt.delete(first=0, last=22) 

def clear1():
     txt2.delete(first=0, last=22)
def admin_panel():
    txt2.delete(first=0, last=22)

def take_img():
    txt2.delete(first=0, last=22)
def trainimg():
    txt2.delete(first=0, last=22)
def subjectchoose():
    me=Tk()
    me.geometry("354x460")
    me.title("EEG graph")
    melabel = Label(me,text="EEG values",bg='dark gray',font=("Times",26,'bold'))
    melabel.pack(side=TOP)
    me.config(background='Dark gray')
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(my_data)
    canvas = FigureCanvasTkAgg(fig, master=me)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, me)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    def ext_1():
        exit()
    canvas.mpl_connect("key_press_event", on_key_press)
    button = Button(master=me, text="Quit", command=ext_1)
    button.pack(side=BOTTOM)
    me.mainloop()
def manually_fill():
    txt2.delete(first=0, last=22)
    
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.iconbitmap('hearticon.ico')


def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

message = tk.Label(window, text="Emotion Recognition Tool", bg="cyan", fg="black", width=50,
                   height=3, font=('times', 30, 'italic bold '))

message.place(x=80, y=20)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                      height=3, font=('times', 17, 'bold'))

lbl = tk.Label(window, text="Enter Session no.", width=20, height=2, fg="black", bg="light grey", font=('times', 24, ' bold '))
lbl.place(x=160, y=200)

def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

txt = tk.Entry(window, validate="key", width=19, bg="yellow", fg="red", font=('times', 25, ' bold '))
txt['validatecommand'] = (txt.register(testVal),'%P','%d')
txt.place(x=580, y=210)

lbl2 = tk.Label(window, text="Enter Name", width=20, fg="black", bg="light grey", height=2, font=('times', 24, ' bold '))
lbl2.place(x=160, y=300)

txt2 = tk.Entry(window, width=19, bg="yellow", fg="red", font=('times', 25, ' bold '))
txt2.place(x=580, y=310)

clearButton = tk.Button(window, text="Clear",command=clear,fg="black"  ,bg="light grey"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 24, ' bold '))
clearButton.place(x=950, y=210)

clearButton1 = tk.Button(window, text="Clear",command=clear1,fg="black"  ,bg="light grey"  ,width=10 ,height=1, activebackground = "Red" ,font=('times', 24, ' bold '))
clearButton1.place(x=950, y=310)

AP = tk.Button(window, text="Check Registered emotion",command=admin_panel,fg="black"  ,bg="cyan"  ,width=19 ,height=1, activebackground = "Red" ,font=('times', 24, ' bold '))
AP.place(x=720, y=410)

takeImg = tk.Button(window, text="Valence",command=take_img,fg="white"  ,bg="blue2"  ,width=12  ,height=2, activebackground = "Red" ,font=('times', 24, ' bold '))
takeImg.place(x=90, y=500)

trainImg = tk.Button(window, text="Arousal",fg="black",command=trainimg ,bg="lawn green"  ,width=12  ,height=2, activebackground = "Red" ,font=('times', 24, ' bold '))
trainImg.place(x=390, y=500)

FA = tk.Button(window, text="Generate EEG ",fg="white",command=subjectchoose  ,bg="blue2"  ,width=12  ,height=2, activebackground = "Red" ,font=('times', 24, ' bold '))
FA.place(x=690, y=500)

quitWindow = tk.Button(window, text="Reset", command=manually_fill  ,fg="black"  ,bg="lawn green"  ,width=12  ,height=2, activebackground = "Red" ,font=('times', 24, ' bold '))
quitWindow.place(x=990, y=500)

window.mainloop()