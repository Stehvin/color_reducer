# Author: Stehvin Olson

from tkinter import *
from PIL import ImageTk, Image
from win32api import GetSystemMetrics

print("Width: ", GetSystemMetrics(0))

inputFile = ""
mainWin = Tk()
mainWin.title("HEY")
mainWin.geometry("{}x{}".format(GetSystemMetrics(0), GetSystemMetrics(1)))

def browseButton():
    """Allows the user to browse their files and select a .jpg or
    .png picture.
    """
    global inputFile 
    inputFile = filedialog.askopenfilename(filetypes=[("Picture Files", 
                                                       "*.jpg;*.png")])
    img = ImageTk.PhotoImage(Image.open(inputFile))
    pic1 = Label(mainWin, image=img)
    pic1.image = img
    pic1.pack(side='left', fill='both', expand=True)

button2 = Button(text="Browse", command=browseButton).pack(fill='both',
                                                            expand=True)


    
mainWin.mainloop()