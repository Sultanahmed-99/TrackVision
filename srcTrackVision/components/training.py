from srcTrackVision.entity.config_entity import TrainingConfig
import tensorflow as tf 
from pathlib import Path


class Training:
    def __init__(self , config = TrainingConfig):
        self.config = config


    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.update_base_model_path
        )
    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )  

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
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

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                horizontal_flip=False 
                , rotation_range = 10
                , zoom_range= 0.1
                , **datagenerator_kwargs

            )
        else : 
            train_datagenerator = valid_generator
                        
        self.train_generator = train_datagenerator.flow_from_directory(
                        directory= self.config.training_data
                        , shuffle= True
                        , subset= 'training'
                        , **dataflow_kwargs
        )
    @staticmethod 
    def save_model(path : Path  , model : tf.keras.models.Model):
        model.save(path)


    def train(self , callbacks_list : list):
        self.steps_per_epoch = self.train_generator.samples // self.config.params_batch_size
        self.validation_steps = self.valid_generator.samples // self.config.params_batch_size

        self.model.fit(
                    self.train_generator
                    , steps_per_epoch = self.steps_per_epoch
                    , validation_steps = self.validation_steps
                    , validation_data = self.valid_generator
                    , epochs = self.config.params_epochs
                    , callbacks = callbacks_list
        ) 

        self.save_model(
           path = self.config.trained_model_path
           , model = self.model
           
        )


        