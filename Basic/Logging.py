"""
We can track events in a software application, this is known as logging. 
Let’s start with a simple example, we will log a warning message.
As opposed to just printing the errors, logging can be configured to disable output or save to a file. 
This is a big advantage to simple printing the errors.
"""

import os
import logging

print("Example #1: Logging")
logging.warning('This is a warning!')

logging.basicConfig(filename='program.log', level=logging.DEBUG)
logging.warning('An example message.')
logging.warning('Another message')

# os.system("notepad program.log")

print()
print("Example #2: Level of severity")
logging.basicConfig(level=logging.DEBUG)
logging.debug('Debug message')

print()
print("Example #3: Time in log")
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message.')
logging.warning('Another log message')

