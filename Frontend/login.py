import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from ttkbootstrap import Style
import sqlite3
import home_screen
import registerPage

def login(email_entry, password_entry, loginPage, root):
    email = email_entry.get()
    password = password_entry.get()
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()
    
    if user:
        loginPage.destroy()
        home_screen.show_home_screen(root, email)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


def create_account():
    registerPage.open_register_window()



def set_background(root, image_path):
    image = Image.open(image_path)
    image = image.resize((1200, 600), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def show_login_window(root):
    loginPage = tk.Toplevel(root)
    loginPage.title("Login")
    loginPage.geometry('1200x600+100+100')
    loginPage.resizable(False,False)

    set_background(loginPage, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  

    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman',20),background=style.colors.success)
    style.configure('Success.TButton',font=('Times New Roman',20), background=style.colors.success, foreground=style.colors.light)
    style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)
    

    frame = ttk.Frame(loginPage, bootstyle='info')
    frame.pack(fill=tk.BOTH)

    navbar = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman', 35, 'bold'),style='Info.TLabel')
    navbar.pack(pady=20, padx=10, anchor=tk.CENTER)

    frame2 = ttk.Frame(loginPage, width=100, height=500 ,bootstyle='info')
    frame2.pack(pady=50, padx=10)

    set_background(root, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  

    login_title = ttk.Label(frame2, text="Login", font=("Times New Roman", 18), style='Info.TLabel')
    login_title.pack(pady=5)

    email_label = ttk.Label(frame2, text="Email", style='Info.TLabel')
    email_label.pack(pady=5)
    email_entry = ttk.Entry(frame2, width=30)
    email_entry.pack(pady=5)

    password_label = ttk.Label(frame2, text="Password", style='Info.TLabel')
    password_label.pack(pady=5)
    password_entry = ttk.Entry(frame2, show="*", width=30)
    password_entry.pack(pady=5)

    login_button = ttk.Button(frame2, text="Login", command=lambda: login(email_entry, password_entry, loginPage, root), width=30, style='Success.TButton')
    login_button.pack(pady=5)

    create_account_link = ttk.Button(frame2, text="Not registered yet? Create an account", command=create_account)
    create_account_link.pack(pady=5)

    loginPage.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    show_login_window(root)
    root.mainloop()

