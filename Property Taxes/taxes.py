#GUI Creation
import tkinter

class Window:
    def __init__(self):
        #create main window
        self.mainWindow = tkinter.Tk()

        #create a frames
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)
        
        #create entry box and label
        self.valueLabel = tkinter.Label(self.topFrame, text = 'Enter Property Value:')
        self.value = tkinter.Entry(self.topFrame, width=10)

        #pack checkbuttons
        self.valueLabel.pack()
        self.value.pack()
        
        #create label
        self.assetValue = tkinter.StringVar()
        self.assetLabel = tkinter.Label(self.bottomFrame, textvariable = self.assetValue)
        self.total = tkinter.StringVar()
        self.totalLabel = tkinter.Label(self.bottomFrame, textvariable = self.total)

        #Create buttons
        self.calculate = tkinter.Button(self.bottomFrame, text = 'Calculate', command = self.Calculate)
        self.quit = tkinter.Button(self.bottomFrame, text='Quit', command=self.mainWindow.destroy)

        #pack buttons and label
        self.assetLabel.pack()
        self.totalLabel.pack()
        self.calculate.pack()
        self.quit.pack()

        #pack the frames
        self.topFrame.pack()
        self.bottomFrame.pack()

        #start tkinter loop
        tkinter.mainloop()

    #create calculate button and what options do
    def Calculate(self):
        #create total variable
        self.current = float(0)
        
        #calculate taxes
        realValue = float(self.value.get())
        self.current = realValue * 0.60 / 100 * 0.75
        
        self.assetValue.set(format(realValue * 0.60, '.2f'))
        self.total.set(format(self.current,'.2f'))


