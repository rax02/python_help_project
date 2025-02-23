import src.logging.logging as logging

print(logging.logger.info(f"Logging started for {__name__.split('.')[0] if '.' in __name__ else __name__}. This will rotate daily."))