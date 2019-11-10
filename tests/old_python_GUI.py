
print("Welcome to Rubber Ducky!")
print("=======================\n")
print("  <(○ )____\n"
      "   (  •_> /\n"
        "-^-^--^--^^--^-^- \n")

print("Generating User Interface...\n")


import tkinter
from tkinter import *

# root = Tk()

# canvas = Canvas(root,  width=400, height=400)
# canvas.pack()

# img = PhotoImage(file="duck.gif")
# canvas.create_image(10, 10, anchor=NW, image=img)
 

# root = tk.Tk()
# logo = tk.PhotoImage(file="duck.gif")

def button_play():
      print("Onward")
      return(True)


def button_stop():
      print("Stopping")
      exit()


top = tkinter.Tk()
can = Canvas(top, height = 200, width = 400, bg = "yellow")
can.pack(expand = YES, fill = BOTH)
top.title("Rubber Ducky!")
top.geometry("400x400")
bl =tkinter.Button(top, text = "Play", command = button_play, bg = "green")
bl.pack()
bl.place(x= 170,y = 150)
bl.config(height = 2, width = 8)

# stop = tkinter.Button(top, text = "Stop", command = button_stop, bg = "red")
# stop.pack()
# stop.place(x = 200, y = 150)
# stop.config(height = 2, width = 8)
top.mainloop()

