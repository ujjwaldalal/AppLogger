import mylogger
print("here as well")

log = mylogger.get_logger(__name__)
print("here here")

def say_hello(name):
    print("here too")
    log.debug("Greeting people.")

