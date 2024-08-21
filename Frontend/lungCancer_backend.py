import sqlite3
from tkinter import messagebox
import joblib

lung_cancer_model = joblib.load('Models/lung_cancer.pkl')


def predict_output(data):
    prediction = lung_cancer_model.predict([data])
    return prediction[0]

def save_lung_data(entries, button_clicked=None):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS lung_cancer (
                    GENDER INTEGER,
                    AGE INTEGER,
                    SMOKING INTEGER,
                    YELLOW_FINGERS INTEGER,
                    ANXIETY INTEGER,
                    PEER_PRESSURE INTEGER,
                    CHRONIC_DISEASE INTEGER,
                    FATIGUE INTEGER,
                    ALLERGY INTEGER,
                    WHEEZING INTEGER,
                    ALCOHOL_CONSUMING INTEGER,
                    COUGHING INTEGER,
                    SHORTNESS_OF_BREATH INTEGER,
                    SWALLOWING_DIFFICULTY INTEGER,
                    CHEST_PAIN INTEGER,
                    OUTPUT INTEGER
                )''')

    data = []
    for field in entries:
        value = entries[field].get()
        if field == 'GENDER':
            numeric_value = 1 if value == 'Male' else 2
        elif field == 'AGE':
            numeric_value = int(value)
        else:
            if value == 'Yes':
                numeric_value = 1
            elif value == 'No':
                numeric_value = 2
            else:
                print(f"Please select a valid option for {field}.")
                return
        data.append(numeric_value)

    output = predict_output(data)

    c.execute('''INSERT INTO lung_cancer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (*data, int(output)))

    conn.commit()
    conn.close()

    print("Data saved:", data, "with output:", output)
    result = "No You donot have Lung Cancer" if output == 1 else "Yes you have Lung Cancer"
    print('Data Saved:', data, 'with output:', output)
    messagebox.showinfo("Prediction", f"Predicted class: {result}\n Disclamer: the output may vary accuracy not 100%")