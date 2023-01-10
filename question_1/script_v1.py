
from selenium import webdriver # webdriver
from selenium.webdriver.chrome.service import Service # this creates the web driver instance
from selenium.webdriver.common.by import By # select specific elements on the web page
from selenium.common.exceptions import NoSuchElementException # handles end of pagination
from selenium.webdriver.support.wait import WebDriverWait # generates wait time
from selenium.webdriver.support import expected_conditions as EC # needed for wait time
import csv

# Setup CSV
file = open("currently_operating.csv", "w", newline='') # creates new csv file
writer = csv.writer(file) # setting up writer instance to write to file
writer.writerow(["id", "name", "location", "status", "num_of_coasters"]) # setting up column headers

# Creates Chrome Service & WebDriver instance
browser_driver = Service("/Users/coderino/Library/Mobile Documents/com~apple~CloudDocs/Coding/chromedriver")
driver = webdriver.Chrome(service = browser_driver) # another object we're creating from a class

# GET page to scrape
driver.get("https://rcdb.com/r.htm?st=93&ol=59&ot=3")

# Scrape
unique_id = 1
while True:
    coasters_tbody = driver.find_elements(By.XPATH, '/html/body/section/div[2]/table')
    # coast_name = driver.find_elements_by_css_selector('#tblResults tr td:nth-child(2) a')
    for coaster in coasters_tbody:
        coaster_name = driver.find_elements(By.XPATH, '/html/body/section/div[2]/table/tbody/tr[1]/td[2]')[0].accessible_name
        # name = coaster.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr[1]/td[2]/a').text
        
        # price = laptop.find_element(By.CLASS_NAME, "caption")
        # price_final = price.find_element(By.CLASS_NAME, "pull-right").text

        # specifications = laptop.find_element(By.CLASS_NAME, "description").text
        
        # number_of_reviews = laptop.find_element(By.CLASS_NAME, "ratings")
        # number_of_reviews_v2 = number_of_reviews.find_element(By.CLASS_NAME, "pull-right").text
        # number_of_reviews_final = number_of_reviews_v2.split(" ")[0]
        writer.writerow(
            [unique_id, coaster_name])
        unique_id += 1
    try:
         # Wait for data to load 
        wait = WebDriverWait(driver, 10)
        element_to_watch = driver.find_element(By.XPATH, '/html/body/section/div[2]/table')
        wait.until(EC.visibility_of(element_to_watch))
        # click next page
        # cookie_banner = scraper.find_element(By.XPATH, '//*[@id="closeCookieBanner"]')
        # cookie_banner.click()
        element_to_click = driver.find_element(By.PARTIAL_LINK_TEXT, '>>')
        element_to_click.click()
    except NoSuchElementException:
        break

file.close()
driver.quit()
