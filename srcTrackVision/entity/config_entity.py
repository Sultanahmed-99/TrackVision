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



@dataclass(frozen=True)
class PreaperModelCallBacks:
    root_dir : Path 
    tensrboard_root_log_dir: Path
    checkpoint_model_filepath: Path
     


@dataclass(frozen=True)
class TrainingConfig:
    root_dir : Path 
    trained_model_path: Path
    update_base_model_path: Path
    training_data : Path
    params_is_augmentation : bool 
    params_image_size : list
    params_batch_size : int
    params_epochs : int     
    params_learning_rate : float


@dataclass(frozen=True)
class ModelEvaluationConfig:
    path_of_model : Path
    training_data : Path
    all_params : dict
    params_image_size : list 
    params_batch_size : int 