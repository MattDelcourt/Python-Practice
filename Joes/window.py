#GUI Creation
import tkinter

class Window:
    def __init__(self):
        #create main window
        self.mainWindow = tkinter.Tk()

        #create a frames
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        #create checkbuttons
        self.oilChangeVar = tkinter.IntVar()
        self.lubeJobVar = tkinter.IntVar()
        self.radFlushVar = tkinter.IntVar()
        self.transFlushVar = tkinter.IntVar()
        self.inspectionVar = tkinter.IntVar()
        self.muffReplaceVar = tkinter.IntVar()
        self.tireRotVar = tkinter.IntVar()
        
        #Set IntVar to 0
        self.oilChangeVar.set(0)
        self.lubeJobVar.set(0)
        self.radFlushVar.set(0)
        self.transFlushVar.set(0)
        self.inspectionVar.set(0)
        self.muffReplaceVar.set(0)
        self.tireRotVar.set(0)

        #Setup checkbuttons
        self.oilChange = tkinter.Checkbutton(self.topFrame,text = 'Oil Change - $30.00', variable = self.oilChangeVar)
        self.lubeJob = tkinter.Checkbutton(self.topFrame,text = 'Lube Job - $20.00', variable = self.lubeJobVar)
        self.radFlush = tkinter.Checkbutton(self.topFrame,text = 'Radiator Flush - $40.00', variable = self.radFlushVar)
        self.transFlush = tkinter.Checkbutton(self.topFrame,text = 'Transmission Flush - $100.00', variable = self.transFlushVar)
        self.inspection = tkinter.Checkbutton(self.topFrame,text = 'Inspection - $35.00', variable = self.inspectionVar)
        self.muffReplace = tkinter.Checkbutton(self.topFrame,text = 'Muffler Replacement - $200.00', variable = self.muffReplaceVar)
        self.tireRot = tkinter.Checkbutton(self.topFrame,text = 'Tire Rotation - $20.00', variable = self.tireRotVar)

        #pack checkbuttons
        self.oilChange.pack()
        self.lubeJob.pack()
        self.radFlush.pack()
        self.transFlush.pack()
        self.inspection.pack()
        self.muffReplace.pack()
        self.tireRot.pack()

        #create label
        self.total = tkinter.StringVar()
        self.label = tkinter.Label(self.bottomFrame, textvariable = self.total)

        #Create buttons
        self.calculate = tkinter.Button(self.bottomFrame, text = 'Calculate', command = self.Calculate)
        self.quit = tkinter.Button(self.bottomFrame, text='Quit', command=self.mainWindow.destroy)

        #pack buttons and label
        self.label.pack()
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
        self.current = int(0)
        
        #check for boxes
        if self.oilChangeVar.get() == 1:
            self.current = int(self.current + 30)
        if self.lubeJobVar.get() == 1:
            self.current = int(self.current + 20)
        if self.radFlushVar.get() == 1:
            self.current = int(self.current + 40)
        if self.transFlushVar.get() == 1:
            self.current = int(self.current + 100)
        if self.inspectionVar.get() == 1:
            self.current = int(self.current + 35)
        if self.muffReplaceVar.get() == 1:
            self.current = int(self.current + 200)
        if self.tireRotVar.get() == 1:
            self.current = int(self.current + 20)
        
        self.total.set(self.current)


        
