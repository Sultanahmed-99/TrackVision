 
from srcTrackVision.config.configuration import ConfigurationManager
from srcTrackVision import logger
from srcTrackVision.components.training import Training
from srcTrackVision.components.preaper_model_callbacks import PreaperCallBacks

STAGE_NAME = 'Training'

class ModelTrainingPipeline:
    def __init__(self) :
        pass

    def main(self): 
         
         config = ConfigurationManager()
         preaper_callbacks_config = config.get_preaper_model_callbacks_config()
         prepaper_model_callbacks = PreaperCallBacks(config= preaper_callbacks_config)
         callback_list =  prepaper_model_callbacks.get_tb_checkpoint_callbacks()
         # configuration for model training 
         training_config = config.get_training_config()
         training = Training(config=training_config)
         training.get_base_model()
         training.train_valid_generator()
         training.train(
            callbacks_list= callback_list
        
            )



if __name__ == "__main__":
    try:
        logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

    except Exception as e:
        logger.exception(e)
        raise e 
      


       
 