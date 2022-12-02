from tkinter import *
from tkinter.colorchooser import askcolor

class DrawRubberShapes(object):
 # Construct the GUI
    def __init__(self):
        window = Tk() # Create a window
        window.title("Lab 10: Drawing Rubber Shapes") # Set a title
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
    # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('red')
        def colorCommand():
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color
        colorButton = Button(frame1, text = "Color",
            command=colorCommand, bg = self.fillColor.get())
        colorButton.grid(row=1,column=1,columnspan=2)

        clearButton = Button(frame1, text = 'Clear',
            command = self.delete, bg = 'blue')
        clearButton.grid(row=1,column=10,columnspan=2) #Create button for clear
        
        

    # Create radio buttons for geometrical shapes
        self.v1 = StringVar()
        rbRectangle = Radiobutton(frame1, text = "Rectangle",
            variable = self.v1, value = 'R',
            command = self.processRadiobutton)
        rbRectangle.grid(row = 1, column = 9)

        
        rbLine = Radiobutton(frame1, text = 'Line',
            variable = self.v1, value = 'L',
            command = self.processRadiobutton)
        rbLine.grid(row = 1, column = 3)

        rbOval = Radiobutton(frame1, text = 'Oval',
            variable = self.v1, value = 'O',
            command = self.processRadiobutton)
        rbOval.grid(row = 1, column = 7)
    # Create a canvas, bound to mouse events
        canvas = Canvas(window, width=400, height=300)
        self.canvas = canvas
        self.canvas.pack()
        self.canvas.bind('<ButtonPress-1>', self.onStart) # left click
        self.canvas.bind('<B1-Motion>', self.onGrow) # drag
        self.canvas.bind('<ButtonPress-3>', self.onMove) # right click
    # for remembering the last drawing
        self.drawn = None

        self.shape = self.canvas.create_rectangle

        window.mainloop()

    def processRadiobutton(self):
        
        if self.v1.get() == 'R':
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'L':
            self.shape = self.canvas.create_line
        elif self.v1.get() == 'O':
            self.shape = self.canvas.create_oval

    def onStart(self, event):
        self.start = event
        self.drawn = None
    # elastic drawing: delete and redraw, repeatedly
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x,
            event.y, fill=self.fillColor.get())
        self.drawn = objectId
        self.panjang = self.start.x-event.x
        self.lebar = self.start.y - event.y
    # move the shape to the click spot
    def onMove(self, event):
        if self.drawn:
            canvas = event.widget
            diffX, diffY = (event.x-self.start.x + self.panjang *0.5),(event.y-self.start.y + self.lebar *0.5)
            canvas.move(self.drawn, diffX, diffY)
            self.start.x = event.x + self.panjang *0.5
            self.start.y = event.y + self.lebar *0.5
          
    #Clear
    def delete(self):
        self.canvas.delete('all')


if __name__ == '__main__':
    DrawRubberShapes()
