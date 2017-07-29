# Author: Stehvin Olson

from tkinter import *

mainWin = Tk()

def browseButton():
    """Allows the user to browse their files and select a .jpg or
    .png picture.
    """
    filename = filedialog.askopenfilename(filetypes=[("Picture Files",
                                                      "*.jpg;*.png")])
    print(filename)
    return filename

button2 = Button(text="Browse", command=browseButton).grid(row=0)

mainWin.mainloop()
