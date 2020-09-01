from bs4 import BeautifulSoup
import requests
import re
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def Steam():

    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",}
    result = requests.get("https://steamdb.info/upcoming/free/#live-promotions", headers=headers)
    soup = BeautifulSoup(result.content, 'lxml')
    urls = []
    links = []
    urls = soup.find('table', {'class': 'table-products table-responsive-flex table-hover text-left table-sortable'}).find_all("a")
    for url in urls:
        link = url.attrs['href']
        if "https" in link:
            links.append(link)
    return links



#this is faster 

def Ubisoft():
    urls = []
    configuration_url = 'https://free.ubisoft.com/configuration.js'
    configuration_js = requests.get(configuration_url).text

    app_id = re.search(r"appId:\s*'(.*?)'",configuration_js).group(1)
    url = re.search(r"prod:\s*'(.*?)'",configuration_js).group(1)

    data = requests.get(url, headers={'ubi-appid': app_id,'ubi-localecode': 'en-US'}).json()
    no = 1
    for news in data['news']:
        if news['type'] != 'freegame':
            continue
        urls.append(news['links'][0]['param'])
        no += 1

    return(urls)


def HumbleBundle():
    
    urls = []
    url = 'https://www.humblebundle.com/store/api/search?sort=discount&filter=onsale&hmb_source=store_navbar&request=1'

    r = requests.get(url)

    data = r.json()

    for item in data["results"]:
        if(item["current_price"]["amount"] == 0.0):
            if(" Demo" not in item["human_name"]):
                link = "https://www.humblebundle.com/store/" + item["human_url"]
                urls.append(link)

    return urls



def EpicGames():

    urls = []
    url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=PL&allowCountries=PL'

    r = requests.get(url)

    data = r.json()

    #print(r.text)

    for item in data['data']['Catalog']['searchStore']['elements']:
        if(item['productSlug'] != "[]"):
            link = "https://www.epicgames.com/store/en-US/product/" + item['productSlug']
            urls.append(link)
        
    return urls
       
  

















#back up if json stops working
def Ubisoftslow():
    urls = []
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(chrome_options=options)
    browser.get("https://free.ubisoft.com/")
    for link in browser.find_elements_by_css_selector("div.free-event-button a[data-type='freegame']"):
        urls.append(link.get_attribute("data-url"))


    return urls