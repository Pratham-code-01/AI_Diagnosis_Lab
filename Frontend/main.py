import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import home_screen
import login

def started():
    # root.iconify()
    root.withdraw()
    # home_screen.show_home_screen(root)
    login.show_login_window(root)

def set_background(root, image_path):
    image = Image.open(image_path)
    image = image.resize((1200, 600), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root = tk.Tk()
style = Style(theme='flatly')

root.geometry('1200x600')
root.title('AI Diagnosis Lab')
root.resizable(False,False)

set_background(root, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  

style.configure('Danger.TLabel', background=style.colors.danger, foreground=style.colors.light)
style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)



frame = ttk.Frame(root, width=100, height=200, bootstyle='info')
frame.pack(fill=tk.BOTH)

navbar = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman', 35, 'bold'), style='Info.TLabel')
navbar.pack(pady=20, padx=10, anchor=tk.CENTER)

frame2 = ttk.Frame(root, width=500, height=500, bootstyle='danger')
frame2.pack(pady=50, padx=10)

welcome = ttk.Label(frame2, text='Welcome To', font=('Times New Roman', 35, 'bold'), style='Danger.TLabel')
welcome.pack(pady=20, padx=20)

title = ttk.Label(frame2, text='AI Diagnosis Lab', font=('Times New Roman', 35, 'bold'), style='Danger.TLabel')
title.pack(pady=20, padx=20)

get_started = ttk.Button(frame2, text='Get Started', bootstyle='success', command=started)
get_started.pack(pady=20, padx=20)

root.mainloop()
