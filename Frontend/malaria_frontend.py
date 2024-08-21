import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import malaria_backend
import home_screen
import login

def homeScreen(window, root, user_email):
    window.destroy()
    home_screen.show_home_screen(root, user_email)

def logOut(window, root):
    window.destroy()
    login.show_login_window(root)

file_path_global = None
img_label = None

def upload_file():
    global file_path_global, img_label
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        file_path_global = file_path
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk
    else:
        messagebox.showwarning("No File", "No file selected!")

def predict_and_show():
    if file_path_global:
        predicted_class = malaria_backend.process_and_predict(file_path_global)
        # Show the prediction
        messagebox.showinfo("Prediction", f"Predicted Output: {predicted_class}")
    else:
        messagebox.showwarning("No File", "No file uploaded!")

def set_background(root, image_path):
    image = Image.open(image_path)
    image = image.resize((1200, 600), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


def show_malaria_window(root, user_email):
    global img_label
    malaria = tk.Toplevel(root)
    malaria.title('Malaria')
    
    set_background(malaria, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  
    malaria.geometry('1200x600+100+100')
    malaria.resizable(False,False)

    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman',20),background=style.colors.success)
    style.configure('Danger.TLabel', background=style.colors.danger, foreground=style.colors.light)
    style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)
    

    frame = ttk.Frame(malaria, width=100, height=200, bootstyle='info')
    frame.pack(fill=tk.BOTH)

    back_button = ttk.Button(frame, text='Back', bootstyle='danger', command=lambda: homeScreen(malaria, root, user_email))
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    logout_button = ttk.Button(frame, text='Logout', bootstyle='danger', command=lambda: logOut(malaria, root))
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    welcome_label = ttk.Label(frame, text=f"User- {user_email}", font=("Times New Roman", 18), style='Info.TLabel')
    welcome_label.pack(side=tk.RIGHT, pady=10, padx=10)

    title = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman',20), style='Info.TLabel')
    title.pack(padx=10, pady=10)

    heading = ttk.Label(malaria, text='Malaria Detector', font=('Times New Roman',30, 'bold'), style='Info.TLabel')
    heading.pack(padx=10, pady=10)
    
    frame2 = ttk.Frame(malaria, width=500, height=500, bootstyle='danger')
    frame2.pack_propagate(False) 
    frame2.pack(padx=10, pady=50)

    upload_button = ttk.Button(frame2, text='Upload File', style='TButton', command=upload_file)
    upload_button.pack(padx=10, pady=10)

    submit_button = ttk.Button(frame2, text='Submit', style='TButton', command=predict_and_show)
    submit_button.pack(padx=10, pady=10)

    img_label = tk.Label(frame2)
    img_label.pack(padx=10, pady=20)

    malaria.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    show_malaria_window(root)
    root.mainloop()
