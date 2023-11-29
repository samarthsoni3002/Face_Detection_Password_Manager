import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Toplevel
import pandas as pd
import face_recognition
import cv2
import numpy as np
from ceaser_cipher import encrypt_caesar_cipher, decrypt_caesar_cipher
from PIL import Image, ImageTk

user_passwords = {}


def logout(login):
    login.destroy()


def decryption(username,label1):

    site = label1.get()

    encrypted = None
    
    if username in user_passwords:
        for i in range(len(user_passwords[username])):
            if(user_passwords[username][i][0] == site):
                encrypted = user_passwords[username][i][1]

    for i in range(len(df)):
        if(df["Username"][i] == username):
            s = df["Key"][i]

    decrypted = decrypt_caesar_cipher(encrypted,s)
    messagebox.showinfo("Decrypted Password",decrypted)


def decrypt_text(username):

    decrypt = Toplevel(login)
    decrypt.title("Login")
    decrypt.geometry("960x540")

    bg_image_1 = Image.open("./bg/photo3.png")
    bg_resized = bg_image_1.resize((960, 540), Image.ANTIALIAS)
    global bg_photo_2
    bg_photo_2 = ImageTk.PhotoImage(bg_resized)

    bg_label = Label(decrypt, image=bg_photo_2)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    name_label = tk.Label(decrypt, text=f"Site To Decrypt", font=("Times New Roman", 30))
    name_label.place(x=370, y=200)

    label1 = tk.Entry(decrypt)
    label1.place(x=420,y=284)


    button = Button(
        decrypt,text="Decrypt",command = lambda: decryption(username,label1),font=(30)
    )
    
    button.place(x=450,y=324)   


def face_detection_second(username):
    x = 0
    
    for i in range(len(df)):
        if df["Username"][i] == username:
            x = 1

    if x == 0:
        messagebox.showinfo("Username Not Found", "Username not found. Please enter a valid username.")

    if x:
        video = cv2.VideoCapture(0)

        image1 = face_recognition.load_image_file(f"./photos/{username}.jpg")
        image1_encoding = face_recognition.face_encodings(image1)[0]

        user_face_encodings = [image1_encoding]
        user_face_names = [f'{username}']

        found_name = None
        while True:
            _, frame = video.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(user_face_encodings, face_encoding, tolerance=0.6)

                name = "Unknown"

                if any(matches):
                    best_match_index = np.argmin(face_recognition.face_distance(user_face_encodings, face_encoding))
                    name = user_face_names[best_match_index]

                    found_name = name
                    break

                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            cv2.imshow("User", frame)

            if found_name is not None:
                break

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video.release()
        cv2.destroyAllWindows()

        decrypt_text(username)



def encrypt_pass(username, site_name_entry, result_label, password_entry, new_password_window):
    site_name = site_name_entry.get()
    password_entry = password_entry.get()

    for i in range(len(df)):
        if df["Username"][i] == username:
            s = df["Key"][i]

    if username in user_passwords:
        user_passwords[username].append((site_name, encrypt_caesar_cipher(password_entry, s)))
    else:
        user_passwords[username] = [(site_name, encrypt_caesar_cipher(password_entry, s))]

    result_label.config(text=f"Site Name: {site_name}, Password: {user_passwords[username][-1][1]}")
   
   
    new_password_window.destroy()


def get_pass(username, final_login):
    new_password_window = Toplevel(login)
    new_password_window.title("New Password")

    site_name_label = tk.Label(new_password_window, text="Site Name:")
    site_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

    site_name_entry = tk.Entry(new_password_window)
    site_name_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(new_password_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    password_entry = tk.Entry(new_password_window)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    result_label = tk.Label(final_login, text="", font=("Helvetica", 14))
    result_label.grid(row=final_login.grid_size()[1], column=1, columnspan=2, pady=50)

    encrypt_button = tk.Button(new_password_window, text="Encrypt", command=lambda: encrypt_pass(username, site_name_entry, result_label, password_entry, new_password_window))
    encrypt_button.grid(row=final_login.grid_size()[1] + 2, column=0, columnspan=2, pady=20)


def welcome_login_page(username):
    final_login = Toplevel(login)
    final_login.title("Login")
    final_login.geometry("960x540")

    bg_image = Image.open("./bg/photo1.png")
    bg_resized = bg_image.resize((960, 540), Image.ANTIALIAS)
    global bg_photo
    bg_photo = ImageTk.PhotoImage(bg_resized)

    bg_label = Label(final_login, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    name_label = tk.Label(final_login, text=f"Hi! {username}", font=("Times New Roman", 16))
    name_label.place(x=70, y=10)
    

    new_password_button = tk.Button(final_login, text="+ New Password", command=lambda: get_pass(username, final_login), font=("Times New Roman", 14))
    new_password_button.place(x=700, y=10)
    
    for i in user_passwords:
        if(username == i):
            name_label = tk.Label(final_login, text=f"Site:- {user_passwords[i][0][0]} Password:- {user_passwords[i][0][1]}", font=("Helvetica", 16))
            name_label.grid(row=0, column=0, padx=100, pady=100, sticky=tk.W)
        


    decrypt_button = tk.Button(final_login, text="Decrypt", command=lambda: face_detection_second(username),font=("Times New Roman", 14))
    decrypt_button.place(x=605, y=10)

    logout_button = tk.Button(final_login, text="Logout", command=lambda: logout(final_login),font=("Times New Roman", 14))
    logout_button.place(x=870, y=10)



def face_detection():
    x = 0
    username = entry.get()
    entry.delete(0, tk.END)
    for i in range(len(df)):
        if df["Username"][i] == username:
            x = 1

    if x == 0:
        messagebox.showinfo("Username Not Found", "Username not found. Please enter a valid username.")

    if x:
        video = cv2.VideoCapture(0)

        image1 = face_recognition.load_image_file(f"./photos/{username}.jpg")
        image1_encoding = face_recognition.face_encodings(image1)[0]

        user_face_encodings = [image1_encoding]
        user_face_names = [f'{username}']

        found_name = None
        while True:
            _, frame = video.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(user_face_encodings, face_encoding, tolerance=0.6)

                name = "Unknown"

                if any(matches):
                    best_match_index = np.argmin(face_recognition.face_distance(user_face_encodings, face_encoding))
                    name = user_face_names[best_match_index]

                    found_name = name
                    break

                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            cv2.imshow("User", frame)

            if found_name is not None:
                break

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video.release()
        cv2.destroyAllWindows()

        welcome_login_page(username)

df = pd.read_csv("./user_data.csv")

login = tk.Tk()
login.title("Login")
login.geometry("960x540")

original_image = Image.open("./bg/photo3.png")
resized_image = original_image.resize((960, 540), Image.LANCZOS)
back = ImageTk.PhotoImage(resized_image)

my_canvas = Canvas(login)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=back, anchor="nw")


label_text = "Please enter your username!!!"
my_canvas.create_text(480,216,text=label_text, fill='white', font=('Arial',20,'bold'))

entry = tk.Entry(login, font=('Arial', 14), bd=2, width=20)
entry.place(relx=0.5, rely=0.5, anchor="center")

photo_buttonImage = PhotoImage(
        file="./assets/verifyButton.png")
photo_button = Button(
        login,
        image=photo_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=face_detection)
photo_button.place(relx=0.5, rely=0.6, anchor="center")

login.mainloop()
