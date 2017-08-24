# Author: Stehvin Olson

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import sklearnColorReducer as kMeans
import os.path
import imghdr
import tempfile
from threading import Thread
import time

def centerWindow(width, height):
    """Opens the main window in the center of the user's screen.
    """
    # screen dimensions
    screenWidth = mainWin.winfo_screenwidth()
    screenHeight = mainWin.winfo_screenheight()
    
    # calculate pixel offset (for top-left corner of window)
    x = int((screenWidth/2) - (width/2))
    y = int((screenHeight/2) - (height/2))
    mainWin.geometry("{}x{}+{}+{}".format(width, height, x, y))

def browseButton():
    """Allows user to browse their files and select a .jpg or
    .png picture.
    """
    inputFile = filedialog.askopenfilename(filetypes=[("Picture Files", 
                                                       "*.jpg;*.png")])  
    inFile.delete(0, END)
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
    outFile.delete(0, END)
    
    # if user did not include ".jpg" to end of picture file name,
    # add it for them
    if outputFile[-4:] == ".jpg":
        outFile.insert(0, outputFile)
    else:
        outFile.insert(0, outputFile + ".jpg")
                                        
def executeButton(inputFile, outputFile, k):
    """Executes K-Means program from sklearnColorReducer module. Informs
    user when complete.
    """
    # check if input path exists and is a picture
    if not os.path.exists(inputFile) or \
       not imghdr.what(inputFile) in ('jpeg', 'png'):
        statusLabel.config(text="Failed to load input picture.")
        return None
    
    # use temporary file to check if output location is valid
    outPath, outFilename = os.path.split(outputFile)
    if outPath == "" or outPath == "/" or outPath == "\\":
        statusLabel.config(text="Output file location not specified.")
        return None
    try:
        outTestFile = tempfile.TemporaryFile(dir=outPath)
        outTestFile.close()
    except:
        statusLabel.config(text="Output folder not found.")
        return None
    
    # ensure output file will not overwrite existing file
    if os.path.exists(outputFile):
        statusLabel.config(text="Output file already exists. " + \
                                "Cannot overwrite.")
        return None
        
    # ensure output file can is a valid filename
    try:
        chkValid = open(outputFile, 'w')
        chkValid.close()
        os.remove(outputFile)
    except:
        statusLabel.config(text="Invalid file format.")
        return None

    # ensure output file has a .jpg or .png file format
    if not outputFile[-4:] in (".jpg", ".png"):
        outputFile += ".jpg"
    if outFilename in (".jpg", ".png"):
        statusLabel.config(text="A girl has no name, " + \
                                "but the output file must.")
        return None
        
    # ensure number of colors is a positive integer
    try:
        k = int(k)
        if k <= 0:
            statusLabel.config(text="Number of colors must be " + \
                                    "positive.")
            return None
    except:
        statusLabel.config(text="Number of colors must be " + \
                                "a positive integer.")
        return None
    
    # begin running k-means
    statusLabel.config(text="Running color reduction algorithm...")
    mainWin.update()
    
    def threadKmeans(thread_check, inputFile, outputFile, k):
        """Runs the K-Means algorithm on a different thread than
        the main GUI window. Will change the value of thread_check
        when complete.
        """
        try:
            kMeans.execute(inputFile, outputFile, k)
            thread_check['success'] = True
        except:
            os.remove(outputFile)
            thread_check['success'] = False
    
    # initialize variables and start second thread to run algorithm       
    thread_check = {'success': None}
    dot = 0
    Thread(target=threadKmeans, args=(thread_check, inputFile, 
                             outputFile, k)).start()
    
    # wait for the second thread to finish running K-Means algorithm,
    # change dots to show user algorithm is still running 
    while thread_check['success'] == None:
        if dot == 0:
            statusLabel.config(text="Running color reduction algorithm")
        elif dot == 1:
            statusLabel.config(text="Running color reduction algorithm.")
        elif dot == 2:
            statusLabel.config(text="Running color reduction algorithm..")
        elif dot == 3:
            statusLabel.config(text="Running color reduction algorithm...")
        time.sleep(0.5)
        mainWin.update()
        dot += 1
        if dot == 4:
            dot = 0
    
    # tell user whether or not algorithm completed successfully
    if thread_check == False:
        statusLabel.config(text="Unknown algorithm error.")
    else:
        statusLabel.config(text="Color reduction complete.")

# set up main GUI window
mainWin = Tk()
# mainWin.wm_iconbitmap('blue.ico')
mainWin.title("Color-Limited Sketch")

# configure window size and location on screen
centerWindow(600, 280)

# set up input file location text entry and "Browse" button
Label(mainWin, text="").grid(row=0)
inFile = Entry(mainWin)
inFile.config(width=50)
Label(mainWin, text="Input File Location:").grid(row=1, column=0, sticky=E)
inFile.grid(row=1, column=1, sticky=W)
button1 = Button(text="Browse", command=browseButton).grid(row=2, column=1)

# set up output file location/name text entry and "Save As" button
Label(mainWin, text="").grid(row=3)
outFile = Entry(mainWin)
outFile.config(width=50)
Label(mainWin, text="Output File Location/Name:").grid(row=4, column=0,
                                                       sticky=E)
outFile.grid(row=4, column=1, sticky=W)
button2 = Button(text="Save As", 
                 command=saveAsButton).grid(row=5, column=1)

# set up number of colors text entry
Label(mainWin, text="").grid(row=6)
kEntry = Entry(mainWin)
kEntry.config(width=5)
Label(mainWin, text="Number of Colors:").grid(row=7, column=0, sticky=E)
kEntry.grid(row=7, column=1, sticky=W)

# set up k-means execute button
Label(mainWin, text="").grid(row=8)
button3 = Button(text="Get Color-Limited Sketch",
                 command=lambda: executeButton(inFile.get(), 
                                               outFile.get(), 
                                               kEntry.get())). \
                 grid(row=9, column=1)
statusLabel = Label(mainWin, text="")
statusLabel.grid(row=10, column=1)

mainWin.mainloop()