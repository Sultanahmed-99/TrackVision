 
from srcTrackVision.config.configuration import ConfigurationManager
from srcTrackVision import logger
from srcTrackVision.components.evaluation import Evaluating

STAGE_NAME = 'Evaluation'
class EvaluationPipeline:
    def __init__(self) :
        pass

    def main(self): 
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluating(config= val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == "__main__":
    try:
        logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

    except Exception as e:
        logger.exception(e)
        raise e 
      


       
 