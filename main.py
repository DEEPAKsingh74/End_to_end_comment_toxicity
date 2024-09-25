from commentToxicity import logger
from commentToxicity.pipeline.stage_01_data_loading import DataLoadingPipeline

STAGE_NAME = "Data Loading stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataLoadingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e