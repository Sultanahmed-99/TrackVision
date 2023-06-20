from srcTrackVision.pipeline.predict import PredictionPipeline
from srcTrackVision.utils.common import decode_image
import os 
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS , cross_origin
import streamlit as st 
import time 
import base64
from io import BytesIO
from PIL import Image


app = Flask(__name__)
CORS(app)




class ClintApp:
    def __init__(self):
        self.filename = 'input_image.jpg'
        self.classifier = PredictionPipeline(self.filename)
    
    
            
 


@app.route('/' , methods=['GET']) 
def home():
    return render_template('index.html')

 
 

@app.route('/train' , methods = ['GET' , 'POST'])
@cross_origin()
def train_route():
    os.system('python dvc.yaml')
    return st.success('Training Completed ')


@app.route('/predict' , methods = ['GET' , 'POST'])
@cross_origin()
def predict_route():
    if request.method == 'POST':
        image = request.json['image']
        decode_image(image , clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    
if __name__ == "__main__":
    clApp = ClintApp()
    app.run(host = '0.0.0.0', port = 80)
    