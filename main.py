from srcTrackVision import logger
from srcTrackVision.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from srcTrackVision.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline



 
STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

except Exception as e:
    logger.exception(e)
    raise e 
    
STAGE_NAME = 'Prepare Base Model Stage'
try:
    logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

except Exception as e:
    logger.exception(e)
    raise e 