from tkinter import *

# Top level window
window = Tk()

window.title("Create or edit an assesment?")
window.geometry('350x200')

# Option menu variable
optionVar = StringVar()
optionVar.set("Create")

# Create a option menu
option = OptionMenu(window, optionVar, "Create", "Edit", "Exit")
option.pack()

# Create button with command
def show():
    print("Selected value :", optionVar.get())


btnShow = Button(window, text="Select", command=show)
btnShow.pack()

window.mainloop()

