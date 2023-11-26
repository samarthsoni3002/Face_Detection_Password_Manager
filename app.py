from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("FACE DETECTION PASSWORD MANAGER")
root.geometry("600x400") 


original_image = Image.open("./bg/bg_photo.png")  
resized_image = original_image.resize((600, 400), Image.LANCZOS)  
background = ImageTk.PhotoImage(resized_image)

my_canvas = Canvas(root)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=background, anchor="nw")

style = ttk.Style()

style.configure("TButton",
                font=("Verdana", 12),
                padding=0,
                relief="flat",
                background="#4ca7b3",
                foreground="#367077")

button1 = ttk.Button(master=my_canvas,
                     text="LOGIN")
button1_window = my_canvas.create_window(398, 200, anchor="nw", window=button1, height=50, width=80)

button3 = ttk.Button(master=my_canvas,
                     text="SIGNUP")
button3_window = my_canvas.create_window(500, 200, anchor="nw", window=button3,height=50, width=80)

root.mainloop()
