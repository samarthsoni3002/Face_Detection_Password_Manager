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
    photo.title("Camera")
    
    frame = LabelFrame(photo)
    frame.pack()

    L1 = Label(frame)
    L1.pack()

    Button(photo,text="Click and Save",command=save_image, bg = "#3498db", fg="white", padx=10, pady=5, relief="raised", font=("Arial", 12), cursor="hand2").pack()

    video = cv2.VideoCapture(0)


    while True:
        img = video.read()[1]
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        img = ImageTk.PhotoImage(Image.fromarray(img1))
    
        L1["image"] = img

        photo.update()

    video.release()




root = Tk()
root.title("Sign Up")
root.geometry("960x540") 

# ================Background Image ====================
original_image = Image.open("./bg/photo2.png")  
resized_image = original_image.resize((960, 540), Image.LANCZOS)  
backgroundImage = ImageTk.PhotoImage(resized_image)
bg_image = Label(
    root,
    image=backgroundImage,
    bg="#272A37"
)
bg_image.place(x=0, y=0)
# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=80)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
text.place(x=75, y=157)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="Login",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff"
)
switchLogin.place(x=230, y=153, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets\\input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(
    firstName_image_Label,
    text="Name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets\\name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    fg="white",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
firstName_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(file="assets\\email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#272A37"
)
emailName_image_Label.place(x=80, y=311)

emailName_text = Label(
    emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(file="assets\\email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=0,
    bg="#3D404B",
    fg="white",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
emailName_entry.place(x=8, y=17, width=354, height=27)

# =============== Photo & Submit Button ====================
photo_buttonImage = PhotoImage(
    file="assets\\submit.png")
photo_button = Button(
    bg_image,
    image=photo_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
    command=open_photo_window
)
photo_button .place(x=200, y=390, width=200, height=40)




root.mainloop()