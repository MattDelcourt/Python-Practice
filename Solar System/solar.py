#GUI Creation
import tkinter
import tkinter.font

class Window:
    def __init__(self):
        #create main window
        self.mainWindow = tkinter.Tk()
        
        #create a frames
        self.mainCanvas = tkinter.Canvas(self.mainWindow, width=1000, height=200)
        self.canvas = tkinter.Canvas(self.mainWindow, width=1000, height=300)
        self.h = 0
        self.x = 0
        self.i = 0
        self.y = 100
        self.rad = 0
        self.color = ''
        self.planet = ''

        for self.i in range (10):
            if self.i == 0:
                self.x += 100
                self.rad = 50
                self.color = 'yellow'
                self.planet = 'Sun'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 1:
                self.x += 100
                self.rad = 5
                self.color = 'orange'
                self.planet = 'Mercury'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 2:
                self.x += 50
                self.rad = 10
                self.color = 'light blue'
                self.planet = 'Venus'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 3:
                self.x += 50
                self.rad = 9
                self.color = 'blue'
                self.planet = 'Earth'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 4:
                self.x += 50
                self.rad = 6
                self.color = 'red'
                self.planet = 'Mars'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 5:
                self.x += 100
                self.rad = 30
                self.color = 'dark red'
                self.planet = 'Jupiter'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 6:
                self.x += 100
                self.rad = 20
                self.color = 'light yellow'
                self.planet = 'Saturn'
                #get window and run it
                self.canvas.create_oval(self.x - self.rad - 15, self.y - self.rad + 10, self.x + self.rad + 15, self.y + self.rad - 10)
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                
                self.i += 1
            elif self.i == 7:
                self.x += 100
                self.rad = 15
                self.color = 'turquoise'
                self.planet = 'Uranus'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 8:
                self.x += 60
                self.rad = 13
                self.color = 'grey'
                self.planet = 'Neptune'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1
            elif self.i == 9:
                self.x += 50
                self.rad = 3
                self.color = 'dark green'
                self.planet = 'Pluto'
                #get window and run it
                self.CreatePlanet(self.x, self.y, self.rad, self.color, self.planet)
                self.i += 1

        #start tkinter loop
        tkinter.mainloop()
        

    def CreatePlanet(self, x, y, rad, color, planet):
        #Create Variables
        self.x1 = x - rad
        self.x2 = x + rad
        self.y1 = y - rad
        self.y2 = y + rad
        
        #Create planet shape and color
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = color )
        
        #create planet text
        self.canvas.create_text(x, self.y2 + 10, text = planet)

        #pack the planet
        self.canvas.pack()




