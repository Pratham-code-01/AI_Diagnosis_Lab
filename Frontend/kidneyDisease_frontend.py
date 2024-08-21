import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import kidneyDisease_backend
import home_screen
import login

file_path_global = None
img_label = None

def upload_file():
    global file_path_global, img_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        file_path_global = file_path
        img = Image.open(file_path)
        img = img.resize((256, 256), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk
    else:
        messagebox.showwarning("No File", "No file selected!")

def predict_and_show():
    if file_path_global:
        predicted_class = kidneyDisease_backend.process_and_predict(file_path_global)
        # Show the prediction
        messagebox.showinfo("Prediction", f"Predicted Output: {predicted_class}")
    else:
        messagebox.showwarning("No File", "No file uploaded!")


def homeScreen(window, root, user_email):
    window.destroy()
    home_screen.show_home_screen(root, user_email)


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


def show_kidneyDisease_window(root, user_email):
    global img_label
    kidneyDisease = tk.Toplevel(root)
    kidneyDisease.title('Kidney Disease')

    screen_width = kidneyDisease.winfo_screenwidth()
    screen_height = kidneyDisease.winfo_screenheight()
    set_background(kidneyDisease, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  
    kidneyDisease.geometry('1200x600+100+100')
    kidneyDisease.resizable(False,False)
    # kidneyDisease.geometry(f'{screen_width}x{screen_height}')

    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman',20),background=style.colors.success)
    style.configure('Danger.TLabel', background=style.colors.danger, foreground=style.colors.light)
    style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)


    frame = ttk.Frame(kidneyDisease, bootstyle='info')
    frame.pack(fill=tk.BOTH)

    back_button = ttk.Button(frame, text='Back', bootstyle='danger', command=lambda: homeScreen(kidneyDisease, root, user_email))
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    logout_button = ttk.Button(frame, text='Logout', bootstyle='danger', command=lambda: logOut(kidneyDisease, root))
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    welcome_label = ttk.Label(frame, text=f"User- {user_email}", font=("Times New Roman", 18), style='Info.TLabel')
    welcome_label.pack(side=tk.RIGHT, pady=10, padx=10)

    title = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman',30), style='Info.TLabel')
    title.pack(padx=10, pady=10)

    heading = ttk.Label(kidneyDisease, text='Kidney Disease Detection', font=('Times New Roman',30, 'bold'), style='Info.TLabel')
    heading.pack(padx=10, pady=10)


    frame2 = ttk.Frame(kidneyDisease, width=500, height=500, bootstyle='danger')
    frame2.pack_propagate(False) 
    frame2.pack(pady=50, padx=10)

    upload_button = ttk.Button(frame2, text='Upload File', style='TButton', command=upload_file)
    upload_button.pack(pady=10)

    submit_button = ttk.Button(frame2, text='Submit', style='TButton', command=predict_and_show)
    submit_button.pack(pady=20)

    img_label = ttk.Label(frame2)
    img_label.pack(pady=20)


    kidneyDisease.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    show_kidneyDisease_window(root)
    root.mainloop()
