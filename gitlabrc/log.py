import logging
import logging.handlers

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s",
  datefmt="%Y-%m-%d-%H-%M-%S"
)

log = logging.getLogger(__name__)
