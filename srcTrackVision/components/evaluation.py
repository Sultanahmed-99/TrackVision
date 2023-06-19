from pathlib import Path
import tensorflow as tf 
from srcTrackVision.entity.config_entity import ModelEvaluationConfig
from srcTrackVision.utils.common import save_json

class Evaluating:
    def __init__(self , config = ModelEvaluationConfig):
        self.config = config
        
    
    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear',
        )
        valid_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        self.valid_generator = valid_generator.flow_from_directory(
                directory= self.config.training_data
                , subset= 'validation'
                , shuffle= False
                , **dataflow_kwargs
                
        )
    @staticmethod   
    def load_model(path : Path) -> tf.keras.models.Model :
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        
    def save_score(self):
        scores = {'loss' : self.score[0], 'accuracy' : self.score[1]}
        save_json(path= Path('scores.json'), data = scores)