import pandas as pd
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import logging
from sendmail import em
from sender import send_it
hour_printchart = 23
minutes_printchart = 51
sns.set(style="darkgrid")
dirname = "Archives\\"
pngname = "Charts\\"
suffix = ".png"
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def chartit(): #wyzwalane o 23:51
    now = datetime.datetime.now()
    name = now.strftime("%B%d")
    if now.hour == hour_printchart and now.minute == minutes_printchart:  #23:51
        with open(name+'.csv', 'r', newline='', encoding='utf-8') as csv_file:
            mean = 0
            val = 0
            sample_data = pd.read_csv(csv_file)
            for n in sample_data.followers:
                if n > 0:
                    val = val + 1
                    mean = mean + n
            min_val = int(((mean/val)*0.95))
            max_val = int(((mean/val)*1.05))
            plt.plot(sample_data.hchart, sample_data.followers)
            plt.ylabel("Followers")
            plt.xlabel("Time [h]")
            plt.xticks(np.arange(0, 24, step=1))
            plt.yticks(np.arange(min_val, max_val, step=10))
            plt.savefig(name)
            logging.info('Figure created correctly')
            try:
                logging.info('Trying to send E-mail')
                send_it(name, suffix)
                logging.info('E-mail sent correctly')
            except Exception as e:
                logging.error(r"Couldn't send E-mail" + str(e))
                print("Couldn't send it! :c. ERROR:" + str(e))
                try:
                    logging.info('Trying to send E-mail again')
                    em(name)
                    logging.info('E-mail sent correctly')
                except Exception as g:
                    logging.error(r"Couldn't send E-mail x2" + str(g))
                    logging.critical("Try send it by your self and read previous Error!")
                    print("Couldn't send it x2! :c. ERROR:" + str(g))

        shutil.copyfile(name+'.csv', dirname + name+'.csv')
        shutil.copyfile(name+'.png', pngname + name+'.png')
        os.remove(name + '.csv')
        os.remove(name + '.png')