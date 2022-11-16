from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup as BSoup

def prepareWebDriver(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(
        service=Service("E:/Kuliah/studi independen/final/project/scrapping/selenium/chromedriver.exe"),
        options=options
        )

    driver.maximize_window()
    driver.get(url)

    return driver

#* loop until next page is disabled
def loopThroughPaggination(list, driver):
    driver.execute_script("window.scrollTo(0, 2350)")
    nextPage = driver.find_element(By.XPATH, "//button[@class='css-1eamy6l-unf-pagination-item'] [@aria-label='Laman berikutnya']")

    time.sleep(3)


    while True:
        try:
            executeScrape(list, driver)
        except:
            print('pass')
            pass

        executeScrape(list, driver)

        if(not nextPage.is_enabled()):
            break

        #* click next page
        driver.find_element(By.XPATH, "//button[@class='css-1eamy6l-unf-pagination-item'] [@aria-label='Laman berikutnya']").click()

    driver.quit()

def executeScrape(list, driver):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1w6pe1p']")))


    grid = driver.find_element(By.XPATH, "//div[@class='css-1fu9ma9']")

    soup = BSoup(grid.get_attribute('innerHTML'), 'html.parser')


    for article in soup.find_all('div', attrs={'class': 'css-1k41fl7'}):
        comment = article.find('span', attrs={'data-testid': 'lblItemUlasan'})
        rating = article.find('div', attrs={'class': 'css-1w6pe1p'}).div['aria-label']

        if not comment is None:
            list.append([comment.text, rating])