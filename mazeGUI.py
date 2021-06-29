from tkinter import *
import random
import maze

def main():
    m = maze.Maze(40,40)
    main_gui = Tk()
    main_gui.geometry("500x500")
    #Canvas
    canv = Canvas(main_gui,width=m.width*15.5,height=m.height*15.5)
    canv.grid()
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    #Scales
    width_scale = Scale(main_gui, from_=2, to=60,orient= HORIZONTAL)
    width_scale.set(2)
    width_scale.grid()
    height_scale = Scale(main_gui, from_=2, to=60,orient=HORIZONTAL)
    height_scale.set(2)
    height_scale.grid()
    #Buttons
    b = Button(main_gui,text="Generate!", command = lambda: drawMaze(m,canv,width_scale,height_scale))
    b.grid()
    #RadioButtons
    radio = Radiobutton(main_gui, text="Draw Solution", variable=0, value=1,
                     command= m.drawSolution())
    radio.grid()

    main_gui.mainloop()
def drawMaze(m,canv,width_scale,height_scale):
    m.setWidth(width_scale.get())
    m.setHeight(height_scale.get())
    m.resetGrid()
    m.recursiveAlgorithm([random.randint(0, m.height - 1), random.randint(0, m.width - 1)])
    canv.delete('all')
    # grid drawing starting values
    x1 = 10
    y1 = 10
    x2 = 20
    y2 = 20
    # -------
    # Cycle through the bits of every value in the maze and draw it on the canvas
    for r in m.grid:
        for c in r:
            binary = bin(c)[2:]
            binary = binary.zfill(4)
            for i in range(0, 4):
                if (binary[i] == "0"):
                    continue
                if (i == 0):
                    canv.create_line(x1, y1, x2, y1)  # Top of the box
                elif (i == 1):
                    canv.create_line(x1, y2, x2, y2)  # Bottom of the box
                elif (i == 2):
                    canv.create_line(x1, y1, x1, y2)  # Left side of the box
                elif (i == 3):
                    canv.create_line(x2, y1, x2, y2)  # Right side of the box
            x1 += 10
            x2 += 10
        x1 = 10
        x2 = 20
        y1 += 10
        y2 += 10

if __name__ == '__main__':
    main()
