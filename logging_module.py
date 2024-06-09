"""
INFO - Just says everything is smooth
DEBUG - It has detailed information in low level so that we can easily track the probl
WARNING - To provide the warning like low disk space
ERROR - Used to log the exception cases information
CRITICAL - Deals with critical errors
filename="app.log" - This is the file where we log out application data
level - This decides what information to be logged in the log file(app.log)
format -
asctime - ASCII Time - Local time
levelname - Displays the level name
message - Displays the message of the info
filemode - w - write the data into the file | DANGEROUS
a - appded the data in the log file | Preferred

import logging
logging.basicConfig(filename="stdout.log", level=logging.CRITICAL,

format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

logging.info("I am just an information log")
logging.debug("Debugging log msg")
logging.warning("Warning log msg")
logging.error("Error log msg")
logging.critical("Critical log msg")
# INFO - Except DEBUG log remaining everything will be logged in the log file
# DEBUG - It logs all level log messages
# WARNING - Except INFO, DEBUG it logs remaining
# ERROR -Only ERROR and CRITICAL log messages
# CRITICAL - Only Critical log message will be logged

# Given list of items get the even numbers
import logging
logging.basicConfig(filename="stdout.log", level=logging.DEBUG,
format='%(asctime)s - %(levelname)s - %(message)s')

def get_even_number(user_info, data):
try:
    {
        logging.info(f"{user_info["name"]} {user_info['ph']} Function get_even_number
    logging.debug(f"{user_info["name"]} {user_info['ph']} input data is {data}")
    even_list = []
    for item in data:
        logging.debug(f"{user_info["name"]} {user_info['ph']} Item is {item}")
    if type(item) == int:
        if
    item % 2 == 0:
    logging.debug(f"{user_info["name"]} {user_info['ph']} Item added t
    even_list.append(item)
    else:
    logging.warning(f"{user_info["name"]} {user_info['ph']} {item} is

    else:
    logging.warning(f"{user_info["name"]} {user_info['ph']} {item} not a
    print("Even List is ", even_list)
    print(10 + "ABC")
    logging.info(f"{user_info["name"]} {user_info['ph']} Function get_even_number

    }
except Exception as err:
logging.critical(f"{user_info["name"]} {user_info['ph']} Error is {err}")
mixed_list = [23, 34, 67, 80]
user_info = {"name": "Adriana", "ph": 832545725734}
get_even_number(user_info,mixed_list)
"""
#practise

"""

import logging
# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

"""
"""
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Some code that might raise an exception
    result = 10/0
except Exception as e:
    # Log the exception
    logging.exception("An error occurred: %s", e)
"""

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_numbers(x, y):
    try:
        result = x + y
        logging.info("Addition successful: %s + %s = %s", x, y, result)
        return result
    except Exception as e:
        logging.error("Error occurred during addition: %s", e)

# Example usage
add_numbers(5, 3)
add_numbers('a', 3)  # This will intentionally cause an error


