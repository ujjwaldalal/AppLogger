import mylogger

log = mylogger.setup_app_level_logger(filename = 'app_debug.log')
print("here")

import mymodule
print("here")

log.debug("Calling module function.")

mymodule.say_hello('Ujjwal')

log.debug('Finished')