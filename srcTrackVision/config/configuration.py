from srcTrackVision.utils.common import read_yaml ,  create_directories
from srcTrackVision.entity.config_entity import DataIngestionConfig



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
         