import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import logging
user_id = "kamiis_99"
url = 'https://www.instagram.com/{}'.format(user_id)
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def GetFollower():
    try:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        container = str(page_soup.findAll("meta", {"name": "description"}))
        m = re.search("""content="(.+?) Followers""", container)
        followers = m.group(1)
        logging.info('Collected followers from site')
        return followers
    except Exception as e:
        print("Getting followers ERROR")
        logging.error(r"Couldn't take followers " + str(e))
        return "none"
