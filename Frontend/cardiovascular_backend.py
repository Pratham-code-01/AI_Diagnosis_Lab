import sqlite3
from tkinter import messagebox
import joblib

cardiovascular_model = joblib.load('Models/cardiovascular.pkl')

def predict_output(data):
    print(data)
    prediction = cardiovascular_model.predict([data[:]])
    return prediction[0]

def save_cardiovascular_data(entries):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS cardiovascular (
              GENDER TEXT,
              AGE INT,
              HEIGHT INT,
              WEIGHT FLOAT,
              BMI FLOAT,
              SYSTOLIC BLOOD PRESSURE INT,
              DIASTOLIC BLOOD PRESSURE INT,
              CHOLESTEROL TEXT,
              GLUCOSE TEXT,
              SMOKING INT,
              ALCOHOL INT,
              PHYSICAL ACTIVITY INT,
              OUTPUT INT
    )''')

    data = []
    height = None
    weight = None

    for field in entries:
        value = entries[field].get()
        if field == 'GENDER':
            numeric_value = 1 if value == 'Male' else 2
        elif field == 'AGE':
            numeric_value = int(value)
        elif field == 'HEIGHT':
            numeric_value = int(value)
            height = numeric_value
        elif field == 'WEIGHT':
            numeric_value = float(value)
            weight = numeric_value
        elif field == 'BMI':
            if height and weight:
                bmi = weight / ((height / 100) ** 2)
                #data.insert(4, bmi)
                numeric_value = bmi
            else:
                print('Height and weight must be provided for BMI calculation.')
                return
        elif field == 'SYSTOLIC BLOOD PRESSURE':
            numeric_value = int(value)
        elif field == 'DIASTOLIC BLOOD PRESSURE':
            numeric_value = int(value)
        elif field == 'CHOLESTEROL':
            if value == 'Normal':
                numeric_value = 1
            elif value == 'Above Normal':
                numeric_value = 2
            elif value == 'Well Above Normal':
                numeric_value = 3
            else:
                print('Please select a valid option for CHOLESTEROL.')
                return
        elif field == 'GLUCOSE':
            if value == 'Normal':
                numeric_value = 1
            elif value == 'Above Normal':
                numeric_value = 2
            elif value == 'Well Above Normal':
                numeric_value = 3
            else:
                print('Please select a valid option for GLUCOSE.')
                return
        elif field in ['SMOKING', 'ALCOHOL', 'PHYSICAL ACTIVITY']:
            numeric_value = 0 if value == 'Yes' else 1
        else:
            print(f'Please handle field {field}.')
            return
        data.append(numeric_value)
    print(data)    
    output = predict_output(data)
    
    c.execute('''INSERT INTO cardiovascular VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
              (*data, int(output)))

    conn.commit()
    conn.close()

    result = "No you dont have Cardiovasuclar" if output == 0 else "Yes you haveCardiovasular"
    print('Data Saved:', data, 'with output:', output)
    messagebox.showinfo("Prediction", f"Predicted class: {result}\n Disclamer: the output may vary accuracy is not 100%")