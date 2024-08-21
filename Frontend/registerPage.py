import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


def set_background(root, image_path):
    image = Image.open(image_path)
    image = image.resize((1200, 600), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to handle registration
def register(window, email_entry, password_entry, confirm_password_entry):
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    if not email or not password or not confirm_password:
        messagebox.showerror("Input Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Input Error", "Passwords do not match!")
        return
    
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration Successful", "You have registered successfully!")
        window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration Error", "Email already exists!")

def open_register_window():
    root = tk.Toplevel()
    root.title("Register")
    root.geometry('1200x600+100+100')

    set_background(root, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  


    frame = ttk.Frame(root, width=100, height=200, bootstyle='info')
    frame.pack(fill=tk.BOTH)

    navbar = ttk.Label(frame, text='Disease Diagnosis System', bootstyle='info')
    navbar.pack(pady=20, padx=10, anchor=tk.CENTER)

    
    frame2 = ttk.Frame(root, bootstyle='danger')
    frame2.pack(pady=50, padx=10)

    login_title = ttk.Label(frame2, text="Register", font=("Times New Roman", 18))
    login_title.pack(pady=5)

    email_label = ttk.Label(frame2, text="Email")
    email_label.pack(pady=5)
    email_entry = ttk.Entry(frame2, width=30)
    email_entry.pack(pady=5)
    
    # Password label and entry
    password_label = ttk.Label(frame2, text="Password")
    password_label.pack(pady=5)
    password_entry = ttk.Entry(frame2, show="*", width=30)
    password_entry.pack(pady=5)
    
    # Confirm Password label and entry
    confirm_password_label = ttk.Label(frame2, text="Confirm Password")
    confirm_password_label.pack(pady=5)
    confirm_password_entry = ttk.Entry(frame2, show="*", width=30)
    confirm_password_entry.pack(pady=5)
    
    register_button = ttk.Button(frame2, text="Register", command=lambda: register(root, email_entry, password_entry, confirm_password_entry), width=30)
    register_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    open_register_window()
