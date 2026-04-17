import logging

logging.basicConfig(
    filename='detect-domans.log',  # ← aquí se guarda
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("my_app")

logger.info("hola mundo desde el logger")
