from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    # Return these types 
    root_dir : Path
    source_url : str 
    local_data_file : Path
    unzip_file : Path


@dataclass(frozen=True)
class PreaperBaseModelConfig:
    root_dir : Path 
    base_model_path: Path
    update_base_model_path: Path
    params_model_name : str 
    params_augmentation : bool 
    params_image_size : list
    params_batch_size : int
    params_include_top : bool
    params_epochs : int
    params_num_classes : int
    params_weights : str 
    params_learning_rate : float
