from srcTrackVision.utils.common import read_yaml ,  create_directories
from srcTrackVision.entity.config_entity import (DataIngestionConfig 
                                                 , PreaperBaseModelConfig)
from pathlib import Path


class ConfigurationManager:
    def __init__(
            self , 
            config_filepath = '/Users/sultanalyami/Desktop/TrackVision_Project/TrackVision/config/config.yaml',
            params_filepath = '/Users/sultanalyami/Desktop/TrackVision_Project/TrackVision/params.yaml' ):
        

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        # Create the root dir 
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file = config.local_data_file,
            unzip_file = config.unzip_file 

        )

    
        return data_ingestion_config
         

    def get_preaper_base_mode_config(self) -> PreaperBaseModelConfig:
        config = self.config.preaper_base_model
        create_directories([config.root_dir])
        preaper_base_model_config = PreaperBaseModelConfig(
            root_dir= Path(config.root_dir),
            base_model_path= Path(config.base_model_path),
            update_base_model_path = Path(config.update_base_model_path),
            params_model_name= self.params.MODEL_NAME,
            params_augmentation= self.params.AUGMENTATION,
            params_image_size= self.params.IMAGE_SIZE,
            params_batch_size= self.params.BATCH_SIZE,
            params_include_top= self.params.INCLUDE_TOP,
            params_epochs= self.params.EPOCHS,
            params_num_classes= self.params.CLASSES,
            params_weights= self.params.WEIGHTS,
            params_learning_rate= self.params.LEARNING_RATE,
             

        )

    
        return preaper_base_model_config