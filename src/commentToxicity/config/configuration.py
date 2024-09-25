# config/configuration.py

from commentToxicity.constants import *
from commentToxicity.utils.common import read_yaml, create_directories
from commentToxicity.entity.data_loading import DataLoadingConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

    def get_data_loading_config(self) -> DataLoadingConfig:
        config = self.config.data_loading

        data_loading_config = DataLoadingConfig(
            zip_file_path=config.zip_file_path,
            destination_dir=config.destination_dir
        )

        return data_loading_config
