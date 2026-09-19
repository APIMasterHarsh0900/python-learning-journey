#Python packages and modues
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

log_file = Path("app.log")

if log_file.exists():
    with open(log_file, "r") as file:
        content = file.read()

    if "ERROR" in content:
        logging.error("Error found in application logs")
    else:
        logging.info("No errors found")
else:
    logging.error("Log file not found")