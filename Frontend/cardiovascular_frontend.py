import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk
from ttkbootstrap.scrolled import ScrolledFrame
from cardiovascular_backend import save_cardiovascular_data
import home_screen
import login


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

def show_cardiovascular_form(root, user_email):
    cardiovascular = tk.Toplevel(root)
    cardiovascular.title('Cardiovascular')
    set_background(cardiovascular, 'Background_images/pngtree-heart-background-picture-image_619724.jpg')  

    screen_width = cardiovascular.winfo_screenwidth()
    screen_height = cardiovascular.winfo_screenheight()

    cardiovascular.geometry('1200x600+100+100')
    cardiovascular.resizable(False,False)

    # cardiovascular.geometry(f"{screen_width}x{screen_height}")

    style = Style(theme='flatly')
    style.configure('TButton', font=('Times New Roman',20),background=style.colors.success)
    style.configure('Danger.TLabel', background=style.colors.danger, foreground=style.colors.light)
    style.configure('Info.TLabel', background=style.colors.info, foreground=style.colors.light)
    

    frame = ttk.Frame(cardiovascular,width=100, height=200, bootstyle='info')
    frame.pack(fill=tk.BOTH)

    back_button = ttk.Button(frame, text='Back', bootstyle='danger', command=lambda: homeScreen(cardiovascular, root, user_email))
    back_button.pack(side=tk.LEFT, padx=10, pady=10)

    logout_button = ttk.Button(frame, text='Logout', bootstyle='danger', command=lambda: logOut(cardiovascular, root))
    logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

    welcome_label = ttk.Label(frame, text=f"User- {user_email}", font=("Times New Roman", 18), style='Info.TLabel')
    welcome_label.pack(side=tk.RIGHT, padx=10, pady=10)

    title = ttk.Label(frame, text='AI Diagnosis Lab', font=('Times New Roman',30), style='Info.TLabel')
    title.pack(padx=10, pady=10)

    heading = ttk.Label(cardiovascular, text='Cardiovascular Disease Detection', font=('Times New Roman',30, 'bold'), style='Info.TLabel')
    heading.pack(padx=10, pady=10)

    frame2 = ScrolledFrame(cardiovascular, width=500, height=500, bootstyle='danger')
    frame2.pack(padx=10, pady=50)

    fields = ['GENDER', 'AGE', 'HEIGHT', 'WEIGHT', 'BMI', 'SYSTOLIC BLOOD PRESSURE', 'DIASTOLIC BLOOD PRESSURE', 'CHOLESTEROL', 'GLUCOSE', 'SMOKING', 'ALCOHOL', 'PHYSICAL ACTIVITY']

    entries = {}

    def calculate_bmi(*args):
        try:
            height = float(entries['HEIGHT'].get())
            weight = float(entries['WEIGHT'].get())
            bmi = weight / ((height / 100) ** 2)
            entries['BMI'].set(f'{bmi:.2f}')
        except ValueError:
            entries['BMI'].set('')

    for i, field in enumerate(fields):
        ttk.Label(frame2, text=field + ':', font=('Times New Roman',15), style='Danger.TLabel').grid(row=i, column=0, padx=5, pady=5, sticky='e')
        if field == 'GENDER':
            gender_frame = ttk.Frame(frame2, bootstyle='danger')
            gender_frame.grid(row=i, column=1, padx=5, pady=5)
            gender_var = tk.StringVar(value='Male')
            male_radio = ttk.Radiobutton(gender_frame, text='Male', variable=gender_var, value='Male')
            female_radio = ttk.Radiobutton(gender_frame, text='Female', variable=gender_var, value='Female')
            male_radio.pack(side='left')
            female_radio.pack(side='left')
            entries[field] = gender_var
        elif field == 'AGE':
            entries[field] = ttk.Entry(frame2, style='TEntry')
            entries[field].grid(row=i, column=1, padx=5, pady=5)
        elif field == 'HEIGHT':
            height_var = tk.StringVar()
            height_var.trace_add('write', calculate_bmi)
            entries[field] = height_var
            height_entry = ttk.Entry(frame2, textvariable=height_var, style='TEntry')
            height_entry.grid(row=i, column=1, padx=5, pady=5)
        elif field == 'WEIGHT':
            weight_var = tk.StringVar()
            weight_var.trace_add('write', calculate_bmi)
            entries[field] = weight_var
            weight_entry = ttk.Entry(frame2, textvariable=weight_var, style='TEntry')
            weight_entry.grid(row=i, column=1, padx=5, pady=5)
        elif field == 'BMI':
            bmi_var = tk.StringVar()
            entries[field] = bmi_var
            bmi_entry = ttk.Entry(frame2, textvariable=bmi_var, style='TEntry', state='readonly')
            bmi_entry.grid(row=i, column=1, padx=5, pady=5)
        elif field == 'SYSTOLIC BLOOD PRESSURE':
            entries[field] = ttk.Entry(frame2, style='TEntry')
            entries[field].grid(row=i, column=1, padx=5, pady=5)
        elif field == 'DIASTOLIC BLOOD PRESSURE':
            entries[field] = ttk.Entry(frame2, style='TEntry')
            entries[field].grid(row=i, column=1, padx=5, pady=5)
        elif field == 'CHOLESTEROL':
            options = ['Select', 'Normal', 'Above Normal', 'Well Above Normal']
            dropdown_var = tk.StringVar(value='Select')
            dropdown_menu = ttk.OptionMenu(frame2, dropdown_var, *options)
            dropdown_menu.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = dropdown_var
        elif field == 'GLUCOSE':
            options = ['Select', 'Normal', 'Above Normal', 'Well Above Normal']
            dropdown_var = tk.StringVar(value='Select')
            dropdown_menu = ttk.OptionMenu(frame2, dropdown_var, *options)
            dropdown_menu.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = dropdown_var
        else:
            options = ['Select', 'Yes', 'No']
            dropdown_var = tk.StringVar(value='Select')
            dropdown_menu = ttk.OptionMenu(frame2, dropdown_var, *options)
            dropdown_menu.grid(row=i, column=1, padx=5, pady=5)
            entries[field] = dropdown_var


    # submit_button = ttk.Button(frame2, text='Submit', command=lambda: save_cardiovascular_data(entries))
    # submit_button.grid(row=len(fields), columnspan=2, padx=10, pady=10)

    submit_button = ttk.Button(frame2, text='Submit', command=lambda: save_cardiovascular_data(entries))
    submit_button.grid(row=len(fields), columnspan=2, padx=10, pady=10)



if __name__ == '__main__':
    root = tk.Tk()
    show_cardiovascular_form(root)
    root.mainloop()

