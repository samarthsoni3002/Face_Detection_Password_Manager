from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import cv2
import os
import random
import string


def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def login_page():
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("960x540")
    


def open_photo_window(signup_window, first_name_entry, email_entry):
    def save_image(img1):
        name = first_name_entry.get()
        username = email_entry.get()
        key = random.randint(15,25)

        header = ['Name', 'Username', 'Key']

        with open('user_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            file_empty = file.tell() == 0
            if file_empty:
                writer.writerow(header)
            writer.writerow([name, username,key])


        photo_directory = "./photos/"
        os.makedirs(photo_directory, exist_ok=True)
        photo_path = os.path.join(photo_directory, f"{username}.jpg")

        image = Image.fromarray(img1)
        image.save(photo_path)
        signup_window.destroy()  
        photo.destroy()
        login_page()  

    photo = Toplevel(root)
    photo.title("Camera")

    frame = LabelFrame(photo)
    frame.pack()

    L1 = Label(frame)
    L1.pack()

    Button(photo, text="Click and Save", command=lambda: save_image(img1), bg="#3498db", fg="white", padx=10, pady=5,
           relief="raised", font=("Arial", 12), cursor="hand2").pack()

    video = cv2.VideoCapture(0)

    def update_image():
        global img1  
        img = video.read()[1]
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = ImageTk.PhotoImage(Image.fromarray(img1))

        L1.img = img
        L1["image"] = img

        photo.after(10, update_image)

    update_image()

    photo.mainloop()


def signup():
    signup_window = Toplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("960x540")

    original_image = Image.open("./bg/photo2.png")
    resized_image = original_image.resize((960, 540), Image.LANCZOS)
    backgroundImage = ImageTk.PhotoImage(resized_image)
    bg_image = Label(
        signup_window,
        image=backgroundImage,
        bg="#272A37"
    )
    bg_image.place(x=0, y=0)

    createAccount_header = Label(
        bg_image,
        text="Create new account",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    createAccount_header.place(x=75, y=80)

    firstName_image = PhotoImage(file="./assets/input_img.png")
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

    first_name_entry = Entry(
        firstName_image_Label,
        bd=0,
        bg="#3D404B",
        fg="white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    first_name_entry.place(x=8, y=17, width=140, height=27)

    emailName_image = PhotoImage(file="./assets/email.png")
    emailName_image_Label = Label(
        bg_image,
        image=emailName_image,
        bg="#272A37"
    )
    emailName_image_Label.place(x=80, y=311)

    emailName_text = Label(
        emailName_image_Label,
        text="Username",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    emailName_text.place(x=25, y=0)

    email_entry = Entry(
        emailName_image_Label,
        bd=0,
        bg="#3D404B",
        fg="white",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    email_entry.place(x=8, y=17, width=354, height=27)

    photo_buttonImage = PhotoImage(
        file="./assets/submit.png")
    photo_button = Button(
        bg_image,
        image=photo_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=lambda: open_photo_window(signup_window, first_name_entry, email_entry)
    )
    photo_button.place(x=200, y=390, width=200, height=40)

    signup_window.mainloop()


root = Tk()
root.title("FACE DETECTION PASSWORD MANAGER")
root.geometry("960x540")

original_image = Image.open("./bg/bg_photo.png")
resized_image = original_image.resize((960, 540), Image.LANCZOS)
back = ImageTk.PhotoImage(resized_image)

my_canvas = Canvas(root)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=back, anchor="nw")

style = ttk.Style()

style.configure("TButton",
                font=("Verdana", 12),
                padding=5,
                relief="flat",
                background="#4ca7b3",
                foreground="#0a69a8")

button1 = ttk.Button(master=my_canvas,
                     text="LOGIN",command=login_page)
button1_window = my_canvas.create_window(635, 280, anchor="nw", window=button1, height=40, width=250)

button2 = ttk.Button(master=my_canvas,
                     text="SIGNUP", command=signup)
button2_window = my_canvas.create_window(635, 350, anchor="nw", window=button2, height=40, width=250)

root.mainloop()
