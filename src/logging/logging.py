import os
import logging
from logging.handlers import TimedRotatingFileHandler

# Get the app name dynamically (based on package/module name)
app_name = __name__.split(".")[0] if "." in __name__ else __name__

# Ensure logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Log file path based on app name
log_file = os.path.join(log_dir, f"{app_name}.log")

# Configure the TimedRotatingFileHandler
log_handler = TimedRotatingFileHandler(
    log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
)
log_handler.suffix = "%Y-%m-%d"

# Updated log format to include filename
log_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)

log_handler.setFormatter(log_formatter)

# Create logger
logger = logging.getLogger(app_name)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.addHandler(logging.StreamHandler())  # Print logs to console

# Example log messages
logger.info("I am Logger.")

