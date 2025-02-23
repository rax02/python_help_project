import src.logging.logging as logging
from src.exception.exception import ProjectException

try:
    raise ProjectException("ERR_100")

except ProjectException as e:
    logging.logger.error(e)
except Exception as e:
    logging.logger.error(f"Unexpected error: {e}")