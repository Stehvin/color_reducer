# Author: Stehvin Olson

from tkinter import *

inputFile = ""
mainWin = Tk()

def browseButton():
    """Allows the user to browse their files and select a .jpg or
    .png picture.
    """
    global inputFile 
    inputFile = filedialog.askopenfilename(filetypes=[("Picture Files", 
                                                       "*.jpg;*.png")])

button2 = Button(text="Browse", command=browseButton).grid(row=0)
mainWin.mainloop()