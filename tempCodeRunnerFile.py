import tkinter as tk
import random

color_names = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Brown', 'Cyan', 'Black']
score = 0
time_left = 30

def start_game(event=None):
    if time_left == 30:
        countdown()
    change_color()

def change_color():
    global score, time_left

    if time_left > 0:
        user_input = e.get().lower()
        if user_input == color_names[1].lower():
            score += 1

        e.delete(0, tk.END)
        random.shuffle(color_names)
        label.config(fg=color_names[1], text=color_names[0])
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text="Time left: " + str(time_left))
        timeLabel.after(1000, countdown)

# Create the main window
root = tk.Tk()
root.title('Stroop Effect Game')
root.geometry("960x540") 

# Create and place widgets
instruct = tk.Label(root, text="What is the Color of the text, not the word text?", font=("san-serif", 16))
instruct.pack()

scoreLabel = tk.Label(root, text='Press Enter to Start', font=('Helvetica', 16))
scoreLabel.pack()

timeLabel = tk.Label(root, text='Time left: ' + str(time_left), font=('Helvetica', 16))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 30))
label.pack()

e = tk.Entry(root)
root.bind('<Return>', start_game)
e.pack()
e.focus_set()

root.mainloop()
