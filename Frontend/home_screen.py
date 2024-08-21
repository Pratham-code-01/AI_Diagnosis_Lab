import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
import cardiovascular_frontend
import kidneyDisease_frontend
import lungCancer_frontend
import malaria_frontend
import login

def cardiovascular_button_clicked(window, root, user_email):
    window.destroy()
    cardiovascular_frontend.show_cardiovascular_form(root, user_email)

def kidneyDisease_button_clicked(window, root, user_email):
    window.destroy()
    kidneyDisease_frontend.show_kidneyDisease_window(root, user_email)

def lungCancer_button_clicked(window, root, user_email):
    window.destroy()
    lungCancer_frontend.show_lungCancer_window(root, user_email)

def malaria_button_clicked(window, root, user_email):
    window.destroy()
    malaria_frontend.show_malaria_window(root, user_email)

def logOut(window, root):
    window.destroy()
    login.show_login_window(root)

def set_background(root, image_path):
    image = Image.open(image_path)
    image = image.resize((1200, 600), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)



def show_home_screen(root, user_email):
    screen = tk.Toplevel(root)
    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman',20),background=style.colors.success)
    style.configure('Danger.TLabel', background=style.colors.danger, foreground=style.colors.light)
    style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)

    screen.geometry('1200x600+100+100')
    screen.title('AI Diagnosis Lab')
    screen.resizable(False,False)
    
    set_background(screen, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  


    frame = ttk.Frame(screen, width=100, height=200, bootstyle='info')
    frame.pack(fill=tk.BOTH)


    logout_button = ttk.Button(frame, text='Logout', bootstyle='danger', command=lambda: logOut(screen, root))
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    welcome_label = ttk.Label(frame, text=f"User- {user_email}", font=("Times New Roman", 18), style='Info.TLabel')
    welcome_label.pack(side=tk.RIGHT, pady=10, padx=10)

    navbar = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman', 35, 'bold'), style='Info.TLabel')
    navbar.pack(anchor=tk.CENTER)


    frame2 = ttk.Frame(screen, width=500, height=500, bootstyle='danger')
    frame2.pack(pady=50, padx=10)

    cardiovascular_detection_button = ttk.Button(frame2, text='Cardiovascular Detection', style='TButton', command=lambda: cardiovascular_button_clicked(screen, root, user_email))
    cardiovascular_detection_button.pack(pady=20, padx=20)

    kidney_disease_button = ttk.Button(frame2, text='Kidney Disease Detection', style='TButton', command=lambda: kidneyDisease_button_clicked(screen, root, user_email))
    kidney_disease_button.pack(padx=20, pady=20)

    lung_cancer_button = ttk.Button(frame2, text='Lung Cancer Detection', style='TButton', command=lambda: lungCancer_button_clicked(screen, root, user_email))
    lung_cancer_button.pack(pady=20, padx=20)

    malaria_button = ttk.Button(frame2, text='Malaria Detection', style='TButton', command=lambda: malaria_button_clicked(screen, root, user_email))
    malaria_button.pack(pady=20, padx=20)

    screen.mainloop()
