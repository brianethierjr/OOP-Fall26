import tkinter
root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)
shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="blue")
shape2 = myCanvas.create_rectangle(400, 400, 500, 500, fill="red")
#initialize the constants xx, yy
xx1 = yy1 = 5
xx2 = yy2 = 7

def move_shape():
    global xx1, yy1
    global xx2, yy2
    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, xx1, yy1)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xx1 = -xx1
    if y1 <= 0 or y2 >= 600:
        yy1 = -yy1


    myCanvas.move(shape2, xx2, yy2)
    (x3, y3, x4, y4) = myCanvas.coords(shape2)
    if x3 <= 0 or x4 >= 800:
        xx2 = -xx2
    if y3 <= 0 or y4 >= 600:
        yy2 = -yy2
    myCanvas.after(30, move_shape)

    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        print("Collision! Game Over!")
        exit()

#in the main program call the function move_shape()
myCanvas.after(10, move_shape)
myCanvas.pack()
root.mainloop()
