from keras_vggface.vggface import  VGGFace
import tensorflow as tf
from srcTrackVision.entity.config_entity import PreaperBaseModelConfig
from pathlib import Path

class PreaperBaseModel:
    def __init__ (self  , config = PreaperBaseModelConfig):
        self.config = config


    def get_base_model (self):
        self.model = VGGFace(model =  self.config.params_model_name 
                             , include_top= self.config.params_include_top
                             , weights= self.config.params_weights
                             , classes= self.config.params_num_classes
                              ,input_shape= self.config.params_image_size
                              
                              
        )
        self.save_model(path = self.config.base_model_path , model = self.model)
    @staticmethod
    def _prepare_base_model (model , classes , freez_all  , freez_taill , learning_rate):
        if freez_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freez_taill is not None) and (freez_taill > 0):
            for layer in model.layers[:-freez_taill]:
                            layer.trainable = False


        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction_out = tf.keras.layers.Dense(units = classes
                                                , activation ='softmax')(flatten_in)

        full_model = tf.keras.models.Model(inputs = model.input, outputs = prediction_out)

        full_model.compile(
              optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate)
              , loss = tf.keras.losses.CategoricalCrossentropy()
              , metrics = ['accuracy']
        )
        full_model.summary()
        return full_model

    def update_base_model (self):
          self.full_model = self._prepare_base_model(
                model = self.model
                , classes = self.config.params_num_classes
                , freez_all = False 
                , freez_taill = None 
                , learning_rate = self.config.params_learning_rate
          )
          self.save_model(path = self.config.update_base_model_path , model = self.full_model)
    @staticmethod
    def save_model (path : Path , model : tf.keras.models.Model):
          model.save(path)
          