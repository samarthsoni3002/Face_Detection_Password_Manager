import cv2
import numpy as np
from tkinter import * 
from PIL import Image,ImageTk
import datetime



def save_image():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
    image.save("./photos/Samarth.jpeg")

            
root = Tk()
root.geometry("700x540")
root.configure(bg="cyan")

frame = LabelFrame(root,bg="red")
frame.pack()

L1 = Label(frame,bg="Cyan")
L1.pack()

Button(root,text="Click Photo",command=save_image).pack()

video = cv2.VideoCapture(0)


while True:
    img = video.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    img = ImageTk.PhotoImage(Image.fromarray(img1))
    
    L1["image"] = img

    root.update()

video.release()