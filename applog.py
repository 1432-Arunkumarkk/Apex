import sys
import logging
import datetime 

# Get current date to use in log file name
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


# Configure logging to a file
logging.basicConfig(
    filename=f'logs/{current_date}.log', 
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Custom logging function
def log_message(message):
    try:
        # Log the message to the file
        logging.info(message)
    except Exception as e:
        # If an error occurs while logging, print the error to the console
        error_message = f"An error occurred while logging: {str(e)}"
        print(error_message)

