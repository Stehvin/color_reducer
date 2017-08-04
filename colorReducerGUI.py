# Author: Stehvin Olson

from tkinter import *
from PIL import ImageTk, Image

def main():
    # set up main GUI window
    mainWin = Tk()
    mainWin.title("Color-Limited Sketch")
    mainWin.geometry("900x550")
    
    # set up input file location text entry and "Browse" button
    inFile = Entry(mainWin)
    inFile.config(width=50)
    Label(mainWin, text="Input File Location:").grid(row=0, column=0, sticky=E)
    inFile.grid(row=0, column=1, sticky=W)
    button1 = Button(text="Browse", command=browseButton).grid(row=1, column=1)
    
    # set up output file location/name text entry and "Save As" button
    outFile = Entry(mainWin)
    outFile.config(width=50)
    Label(mainWin, text="Output File Location/Name:").grid(row=4, column=0,
                                                           sticky=E)
    outFile.grid(row=4, column=1, sticky=W)
    button2 = Button(text="Save As", 
                     command=saveAsButton).grid(row=5, column=1)
    
    # set up number of colors text entry
    kEntry = Entry(mainWin)
    kEntry.config(width=5)
    Label(mainWin, text="Number of Colors:").grid(row=8, column=0, sticky=E)
    kEntry.grid(row=8, column=1, sticky=W)
    
    # set up k-means execute button
    button3 = Button(text="Get Color-Limited Sketch",
                     command=lambda: executeButton(inFile.get(), 
                                                   outFile.get(), 
                                                   kEntry.get())). \
                     grid(row=11, column=1)
        
    mainWin.mainloop()

def browseButton():
    """Allows user to browse their files and select a .jpg or
    .png picture.
    """
    inputFile = filedialog.askopenfilename(filetypes=[("Picture Files", 
                                                       "*.jpg;*.png")])  
    inFile.insert(0, inputFile)
    
    ''' These lines can be added if displaying the picture is desired.    
    img = ImageTk.PhotoImage(Image.open(inputFile))
    pic1 = Label(mainWin, image=img)
    pic1.image = img
    pic1.pack(side='left', fill='both', expand=True)
    '''

def saveAsButton():
    """Allows user to select folder and give output picture a name.
    """
    outputFile = filedialog.asksaveasfilename(filetypes=[("Picture File", 
                                                       "*.jpg")])
    outFile.delete(0, "end")
    
    # if user did not include ".jpg" to end of picture file name,
    # add it for them
    if outputFile[-4:] == ".jpg":
        outFile.insert(0, outputFile)
    else:
        outFile.insert(0, outputFile + ".jpg")                                                   
                                        
def executeButton(inputFile, outputFile, k):
    # to do
    print(inputFile)
    print(outputFile)
    print(k)
    return None

if __name__ == "__main__":
    main()