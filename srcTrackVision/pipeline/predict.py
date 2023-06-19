from tensorflow.keras.models import load_model
import os 
from tensorflow.keras.preprocessing import image
import numpy as np

class PredictionPipeline:
    def __init__(self , file_name):
        self.file_name = file_name 
        
        
        
    def predict(self):
        # Load the model 
        model = load_model(os.path.join('artifacts' , 'training' , 'model.h5'))
        
        imagename = self.file_name
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image) , axis = 1)
        print(result)
        
        try :  
            if result[0] == 0:
                prediction = 'Anger'
                return [{'image' : prediction}]
            
            elif result[0] == 1 : 
                prediction = 'Contempt'
                return [{'image' : prediction}]
            
            elif result[0] == 2 :
                prediction = 'Disgust'
                return [{'image' : prediction}]
            elif result[0] == 3 :
                prediction = 'Fear'
                return [{'image' : prediction}]
            elif result[0] == 4 :
                prediction = 'Happy'
                return [{'image' : prediction}]
            
            elif result[0] == 5 :
                prediction = 'Sadness'
                return [{'image' : prediction}]
            
            else:
                prediction = 'Surprise'
                return [{'image' : prediction}]
        except :
               return [{'image' : ''}]