import sqlite3
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image


model = tf.keras.models.load_model('/Users/pratham/Desktop/Project/Models/malaria_detector.h5')

class_labels = {0: 'Uninfected', 1: 'Parasitized'}

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS malaria
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   file_path TEXT NOT NULL, 
                   prediction TEXT NOT NULL)''')
conn.commit()

def process_and_predict(file_path):
    img = Image.open(file_path)
    img = img.resize((50, 50), Image.LANCZOS)
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction, axis=1)[0]
    predicted_class = class_labels[predicted_index]

    cursor.execute("INSERT INTO malaria (file_path, prediction) VALUES (?, ?)",
                   (file_path, predicted_class))
    conn.commit()
    # conn.close()
    
    return predicted_class
