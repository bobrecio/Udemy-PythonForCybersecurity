import logging

# configure
filename = "example.log"

logging.basicConfig(
    filename=filename,
    filemode="a",
    level=logging.INFO,
    format="%(levelname)s - %(message)s (%(asctime)s)",
)

# test
logging.info("This is a sample log entry")
