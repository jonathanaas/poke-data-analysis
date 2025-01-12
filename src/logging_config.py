# logging_config.py
import logging

def configure_logging():
    """Configura o logging do pipeline."""
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler('pipeline.log', mode='w'),  # Arquivo de log
            logging.StreamHandler()  # Console
        ]
    )