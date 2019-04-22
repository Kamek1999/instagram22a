import os
from dateandtime import hours_f, minutes_f
from writetocsv import WriteToCSV
import printchart
from time import sleep
from log_sender import logsend
dirnames = "\Archives"
pngnames = "\Charts"
while True:
    try: #Create dir for files
        actualpath = os.getcwd()
        os.mkdir(actualpath + dirnames)
        print("Created")
    except:
        pass

    try: #Create dir for .png
        actualpath = os.getcwd()
        os.mkdir(actualpath + pngnames)
    except:
        pass
    twriteh = int(hours_f())
    twritem = int(minutes_f())

    WriteToCSV(twriteh, twritem)
    printchart.chartit()
    logsend(twriteh, twritem)
    sleep(45)
