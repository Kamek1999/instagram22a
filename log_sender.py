import logging
from sender import send_it

logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

name = "logs"
suffix = ".log"
dirname = "\Logs"
destname = "Logs\\"
def logsend(twriteh, twritem):
    if twriteh == 6 or 10 or 13 or 21:
        if twritem == 11:
            send_it(name, suffix)
