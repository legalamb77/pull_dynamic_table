import pandas as pd
import certifi
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if __name__=='__main__':
    url='https://schema.broadinstitute.org/results'
    browser = webdriver.Chrome()

    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")

    no_of_pagedowns = int(sys.argv[1])

    el = browser.find_element_by_id("table-panel")

    #action = webdriver.common.action_chains.ActionChains(browser)
    #action.move_to_element_with_offset(el, 100, 100)
    #action.perform()

    #elem = browser.find_element_by_class_name("grid-row")

    r_els=[]

    while no_of_pagedowns:
        row_elems=browser.find_elements_by_class_name("grid-row")
        for r in row_elems:
            r_els.append(r.text)
        div_iv = browser.find_element_by_class_name("grid-row")
        action = webdriver.common.action_chains.ActionChains(browser)
        action.click(div_iv).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)
        no_of_pagedowns-=1
    
    #print(row_elems)
    print(len(r_els))
    for i in range(len(r_els)):
        r_els[i]=r_els[i].split('\n')
    #print(r_els)
    df = pd.DataFrame(r_els)
    print(df)

    #print(soup.find_all("div"))
    #Grid__GridHorizontalViewport-sc7cg1-1 hBvlwL

    #div_headers = soup.find('div', {'class':'Grid__HeaderRow-sc7cg1-2 cHNdtw'})
    #for head in div_headers:
    #    print(head)

    #mydivs = soup.find_all("div", {"class":'grid-row'})#{"class": "grid-row grid-row-stripe"})#"Grid__GridHorizontalViewport-sc7cg1-1 hBvlwL"})

    #print(len(mydivs))
    #print(mydivs)
    #print(pd.read_html(url))

    #print(len(soup.find_all("table")))
    #print(soup.find("table", {"id": "expanded_standings"}))

    browser.close()
    browser.quit()


