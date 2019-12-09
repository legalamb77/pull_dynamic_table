import pandas as pd
import certifi
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if __name__=='__main__':
    url='https://schema.broadinstitute.org/results'
    browser = webdriver.Chrome()

    browser.get(url)
    time.sleep(3)
    html = browser.page_source

    no_of_pagedowns = int(sys.argv[1])

    el = browser.find_element_by_id("table-panel")

    r_els=[]

    while no_of_pagedowns:
        row_elems=browser.find_elements_by_class_name("grid-row")
        for r in row_elems:
            r_els.append(r.text)
        div_iv = browser.find_elements_by_class_name("grid-row")[-1]
        action = webdriver.common.action_chains.ActionChains(browser)
        action.click(div_iv).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(.3)
        no_of_pagedowns-=1
    
    print(len(r_els))
    for i in range(len(r_els)):
        r_els[i]=r_els[i].split('\n')
    df = pd.DataFrame(r_els)
    df.to_csv(sys.argv[2], index=False)

    browser.close()
    browser.quit()


