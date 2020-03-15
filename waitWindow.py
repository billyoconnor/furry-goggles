#Wait box functions from One Trust work
import tkinter.messagebox
from tkinter import Tk

def waitMessage(Title,Message):
    Tk().withdraw()  #keep the root window from appearing
    tkinter.messagebox.showinfo(title="Wait!", message="Please Allow page to load in background before clicking 'Ok'")