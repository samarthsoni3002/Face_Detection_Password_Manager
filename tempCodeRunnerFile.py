from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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
                     text="LOGIN")
button1_window = my_canvas.create_window(635, 280, anchor="nw", window=button1, height=40, width=250)

button2 = ttk.Button(master=my_canvas,
                     text="SIGNUP")
button2_window = my_canvas.create_window(635, 350, anchor="nw", window=button2,height=40, width=250)

root.mainloop()