from srcTrackVision.components.preaper_base_model import PreaperBaseModel
from srcTrackVision.config.configuration import ConfigurationManager
from srcTrackVision import logger

STAGE_NAME = 'Prepare Base Model Stage'

class PrepareBaseModelTrainingPipeline:
    def __init__(self) :
        pass

    def main(self): 
        config = ConfigurationManager()
        preaper_base_model_config = config.get_preaper_base_mode_config()
        prepaper_base_model = PreaperBaseModel(config= preaper_base_model_config)
        prepaper_base_model.get_base_model()
        prepaper_base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

    except Exception as e:
        logger.exception(e)
        raise e 
      


       
 