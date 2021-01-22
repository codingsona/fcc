# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import time_calculator
from unittest import main

'''The code is written in time_calculator.py. For development, we are using main.py to test the functions in time_calculator. 
When we'll Click the "run" button the main.py will run.'''

print(time_calculator("11:70 PM", "10000:70","Sunday").add_time())

# Run unit tests automatically
#main(module='test_time_calculator', exit=False)