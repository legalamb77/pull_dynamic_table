import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__=='__main__':
    url='https://schema.broadinstitute.org/results'
    browser = webdriver.Chrome()

    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "html")

    print(soup.find_all("div"))

    print(len(soup.find_all("table")))
    print(soup.find("table", {"id": "expanded_standings"}))

    browser.close()
    browser.quit()


