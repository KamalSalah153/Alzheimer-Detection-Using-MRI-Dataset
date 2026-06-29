from flask import Flask,render_template,request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from keras.applications.vgg16 import preprocess_input
import numpy as np
import tensorflow as tf
import cv2


app=Flask(__name__)
model = load_model('model.h5')

def read_image(filename):
    dim = 150
    img_data = cv2.imread(filename, 1)
    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
    img_data = cv2.resize(img_data, (dim, dim))
    img_data = np.array(img_data).reshape(-1, dim, dim, 3)
    print(img_data.shape)
    return img_data


@app.route('/',methods=['GET'])
def helloworld():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    test_image=request.files['imageFile']
    path='./images/'+test_image.filename
    print(path)
    test_image.save(path)
    img=read_image(path)
    prediction = model.predict(img)
    prediction_class = np.argmax(prediction)
    stages=["Mild Demented","Moderate Demented","Non-Demented","Very Mild Demented"]
    stage=stages[prediction_class]
    return stage

if __name__=="__main__":
    app.run(port=3000,debug=True)