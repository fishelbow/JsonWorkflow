import logging 

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            "%Y-%m-%d %H:%M:%S:"
        )
    except Exception as e:
        print(f"Logging formatter setup failed: {e}")
        formatter = logging.Formatter("%(levelname)s: %(message)s")


    # file handler
    try:
        file_handler = logging.FileHandler("worflow.log", mode ="a")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"Failed to create file handler: {e}")
    # console handler 
    try:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    except Exception as e:
        print(f"Failed to create consle handler: {e}")