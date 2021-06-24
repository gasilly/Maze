from tkinter import *
import random
import maze

def main():
    #grid drawing starting values
    x1 = 10
    y1 = 10
    x2 = 20
    y2 = 20
    #-------
    m = maze.Maze(30,25)
    m.recursiveAlgorithm([random.randint(0,m.height - 1),random.randint(0,m.width - 1)])
    main_gui = Tk()
    main_gui.geometry("500x500")
    canv = Canvas(main_gui,
               width=m.width*10.5,
               height=m.height*10.5)
    canv.grid()
    canv.place(relx=0.5, rely=0.5, anchor=CENTER)
    #Cycle through the bits of every value in the maze and draw it on the canvas
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
    main_gui.mainloop()

if __name__ == '__main__':
    main()
