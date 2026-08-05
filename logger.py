import logging
from loader.config_loader import load_config
config = load_config()
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)
logger = logging.getLogger("NetPlus")