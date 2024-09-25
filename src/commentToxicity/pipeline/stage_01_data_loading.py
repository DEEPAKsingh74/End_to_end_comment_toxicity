# pipeline

from commentToxicity.config.configuration import ConfigurationManager
from commentToxicity.components.data_loading import DataLoading
from commentToxicity import logger

STAGE_NAME = "Data Loading stage"

class DataLoadingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_loading_config = config.get_data_loading_config()
        data_loading = DataLoading(config=data_loading_config)
        data_loading.data_unzip()
        data_loading.load_data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataLoadingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e