import os 
from urllib.request import urlopen
import zipfile 
from srcTrackVision import logger
from srcTrackVision.utils.common import get_size
from srcTrackVision.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self , config : DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if (not os.path.exists(self.config.local_data_file)):
            fin = urlopen(self.config.source_url)
            data = fin.read()
            with open(self.config.local_data_file, 'wb') as f:
                f.write(data)
            logger.info(f"{self.config.local_data_file} downloaded!")
        else : 
            logger.info(f'File already exists of size : {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        unzip_path = self.config.unzip_file
        os.makedirs(unzip_path , exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:

            f.extractall(unzip_path)