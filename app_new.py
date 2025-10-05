import time
import logging
import sys

# Create loggers
logger = logging.getLogger("stdout_logger")
logger.setLevel(logging.INFO)

# stdout handler for INFO and below
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stdout_handler.setFormatter(stdout_formatter)

# stderr handler for WARNING and above
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)
stderr_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stderr_handler.setFormatter(stderr_formatter)

# Add handlers to logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Simulate logging
counter = 0
while True:
    counter += 1
    logger.info(f"Application is running normally, iteration {counter}")
    
    # Simulate an error every 5 iterations
    if counter % 5 == 0:
        logger.warning(f"Simulated warning/error at iteration {counter}")
    
    time.sleep(2)

