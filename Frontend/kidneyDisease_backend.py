import sqlite3
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Model definition
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(4, activation=tf.nn.softmax)
])

# Load weights
model.load_weights('/Users/pratham/Desktop/Project/Models/KidneyDisease_prediction.h5')

class_labels = {0: 'Cyst', 1: 'Normal', 2: 'Stone', 3: 'Tumor'}

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS kidney
#                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                    file_path TEXT NOT NULL, 
#                    prediction TEXT NOT NULL)''')
# conn.commit()

def process_and_predict(file_path):
    img_height, img_width = 256, 256

    # Preprocess the image
    img = load_img(file_path, target_size=(img_height, img_width))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)

    predicted_index = np.argmax(predictions, axis=1)[0]
    predicted_class = class_labels[predicted_index]

    print("Predicted class:", predicted_class)
    
    cursor.execute("INSERT INTO kidney (file_path, prediction) VALUES (?, ?)",
                   (file_path, predicted_class))
    conn.commit()
    #conn.close()
    
    return predicted_class
