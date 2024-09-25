import zipfile
import os
import shutil
from commentToxicity.entity.data_loading import DataLoadingConfig
from commentToxicity import logger

class DataLoading:
    def __init__(self, config: DataLoadingConfig):
        self.config = config

    def data_unzip(self):
        def unzip_file(zip_path, extract_to):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                # Check for nested zip files
                for member in zip_ref.namelist():
                    # If the member is a zip file, unzip it recursively
                    if member.endswith('.zip'):
                        nested_zip_path = os.path.join(extract_to, member)
                        unzip_file(nested_zip_path, extract_to)

        try:
            extraction_dir = os.path.dirname(self.config.zip_file_path)
            unzip_file(self.config.zip_file_path, extraction_dir)

            logger.info(f"Data extracted in {extraction_dir}")

        except Exception as e:
            raise e

    def load_data(self):
        try:
            root_dir = os.path.dirname(self.config.zip_file_path)
            train_file_path = os.path.join(root_dir, "train.csv")

            if not os.path.exists(train_file_path):
                raise FileNotFoundError(f"train.csv not found in {root_dir}")
            if not os.path.exists(self.config.destination_dir):
                os.makedirs(self.config.destination_dir)

            shutil.copy(train_file_path, self.config.destination_dir)

            logger.info(f"Data copied to {self.config.destination_dir}")
        except Exception as e:
            raise e
