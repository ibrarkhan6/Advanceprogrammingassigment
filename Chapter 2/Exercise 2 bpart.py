# At first we need to import tkinter as tk.
import tkinter as tk
# The root is also called finalroot.
finalroot = tk.Tk()

#Now here now I am writing for left frame which will have part A and B
Myleft_frame = tk.Frame(finalroot, borderwidth=5, background='Light grey')
Myleft_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
#This label will have a text of A inside and background as darkblue.
mylabel_a = tk.Label(Myleft_frame, text='A', background='DarkBlue')
mylabel_a.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
#This label will have a text of B inside and background as white.
mylabel_b = tk.Label(Myleft_frame, text='B', background='White')
mylabel_b.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
#Now here now I am writing for right frame which will have part C and B.
MyRight_frame = tk.Frame(finalroot, borderwidth=5, background='Light Grey')
MyRight_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
#This label will have a text of C inside and background as white.
mylabel_c = tk.Label(MyRight_frame, text='C', background='White')
mylabel_c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
#This label will have a text of D inside and background as darkblue.
mylabel_d = tk.Label(MyRight_frame, text='D', background='DarkBlue')
mylabel_d.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
# Now start the mainloop.
finalroot.mainloop()