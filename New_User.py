from tkinter import *
from tkinter import filedialog, messagebox
import csv
import cv2
import numpy as np
from PIL import Image, ImageTk
import datetime



def open_photo_window():

    def save_image():
        image = Image.fromarray(img1)
        time = str(datetime.datetime.now().today()).replace(":"," ")+".jpg"
        image.save(time)



    photo = Toplevel(root)
    photo.title("New Window")
    
    frame = LabelFrame(photo,bg="red")
    frame.pack()

    L1 = Label(frame,bg="Cyan")
    L1.pack()

    Button(photo,text="Click Photo",command=save_image).pack()

    video = cv2.VideoCapture(0)


    while True:
        img = video.read()[1]
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        img = ImageTk.PhotoImage(Image.fromarray(img1))
    
        L1["image"] = img

        photo.update()

    video.release()




root = Tk()
root.title("Data Entry Form")

name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

age_label = Label(root, text="Age:")
age_label.grid(row=1, column=0, sticky=W, padx=10, pady=10)

age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

photo_button = Button(root, text="Photo",command=open_photo_window)
photo_button.grid(row=2, column=0, columnspan=2, pady=10)

ok_button = Button(root, text="OK")
ok_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()