import time
import logging
import os

# Ensure the log directory exists
os.makedirs("/var/log", exist_ok=True)

# Configure logging to file
logging.basicConfig(
    filename="/var/log/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Simulate continuous logging
while True:
    logging.info("Application is running and writing to /var/log/app.log")
    time.sleep(2)

