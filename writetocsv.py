import os
import seaborn as sns
from actualfollowers import GetFollower
import csv
import datetime
import logging
sns.set(style="darkgrid")
pathdir = os.getcwd() + "\csvs"
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def WriteToCSV(twriteh, twritem):
    now = datetime.datetime.now()
    name = now.strftime("%B%d")

    if twritem == 0\
            or twritem == 10\
            or twritem == 20\
            or twritem == 30\
            or twritem == 40\
            or twritem == 50:
        followers = GetFollower()
        if followers == "none":
            pass
        else:
            header = ['hour', 'min', 'followers', 'hchart']
            hchart = str(twriteh+(twritem*(1/60)))
            row = [twriteh, twritem, followers, hchart]
            try:
                with open(name+'.csv', 'r', newline=''):
                    pass
            except FileNotFoundError:
                with open(name+'.csv', 'a', newline='') as csv_file:
                    csvwriter = csv.writer(csv_file)
                    csvwriter.writerow(header)
            with open(name+'.csv', 'a', newline='') as csv_file:
                logging.info("Writing into CSV file")
                print("Writing into CSV file | " + now.strftime("%H %M"))
                csvwriter = csv.writer(csv_file)
                csvwriter.writerow(row)
