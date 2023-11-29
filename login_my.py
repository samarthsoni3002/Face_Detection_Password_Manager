from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()

window.title("User Space")
window.geometry("960x540") 


# ================Background Image ====================
original_image = Image.open("./bg/photo1.png")  
resized_image = original_image.resize((960, 540), Image.LANCZOS)  
Login_backgroundImage = ImageTk.PhotoImage(resized_image)
bg_imageLogin = Label(
    window,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=0, y=0)

my_canvas = Canvas(window)
my_canvas.create_image(0, 0, image=Login_backgroundImage, anchor="nw")
my_canvas.create_text(120,25, text="Hi! User", fill='white', font=('Arial',20,'bold'))
my_canvas.pack(fill="both", expand=True)

style = ttk.Style()

style.configure("TButton",
                font=("Verdana", 12),
                padding=5,
                relief="flat",
                background="#4ca7b3",
                foreground="#0a69a8")

button1 = ttk.Button(master=my_canvas,text="+ NEW")
button1_window = my_canvas.create_window(850, 20, anchor="nw", window=button1, height=30, width=80)
window.mainloop()
