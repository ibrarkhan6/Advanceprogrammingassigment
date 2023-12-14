# At first from tkinter import.
# And than import random.
from tkinter import *
import random
app = Tk() # Now we need to create the top-level window for this GUI.
app.title("GUI Pack Example") # Now we are going to optionally set the title.
MybA = Label(app, text="A", width=12 ,bg='red', relief=GROOVE, bd=5)# This label will have a text of A width of 12 and backgroundcolor as red.
MybB = Label(app, text="B", width=12, bg='yellow')# This label  will have a text of B width of 12 and backgroundcolor as yellow.
MybC = Label(app, text="C", width=12, bg='blue')# This label  will have a text of C width of 12 and backgroundcolor as blue.
MybD = Label(app, text="D", width=12, bg='white')# This label  will have a text of D width of 12 and backgroundcolor as white.
MybA.pack(side='top',fill=X, expand=1) #Side will be as top.
MybB.pack(side='bottom')# Side will be as a bottom.
MybC.pack(side='left', fill=Y, expand=1)# Side will be as a left.
MybD.pack(side='right')# Side will be as right.
app.mainloop() #Start the main loop.