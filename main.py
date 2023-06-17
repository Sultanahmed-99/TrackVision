from srcTrackVision import logger
from srcTrackVision.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = 'Data Ingestion Stage'
if __name__ == "__main__":
    try:
        logger.info(f'>>>>  stage : {STAGE_NAME} Started <<<<')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f'>>>>  stage : {STAGE_NAME} Completed <<<< \n\nx=========x')

    except Exception as e:
        logger.exception(e)
        raise e 
      