
from selenium import webdriver # webdriver
from selenium.webdriver.chrome.service import Service # this creates the web driver instance
from selenium.webdriver.common.by import By # select specific elements on the web page
from selenium.common.exceptions import NoSuchElementException # handles end of pagination
from selenium.webdriver.support.wait import WebDriverWait # generates wait time
from selenium.webdriver.support import expected_conditions as EC # needed for wait time
import csv
# import time

# setup CSV
file = open("coasters_operating_and_under_construction.csv", "w", newline='') # creates new csv file
writer = csv.writer(file) # setting up writer instance to write to file
writer.writerow(["id", "name", "location", "status", "num_of_coasters"]) # setting up column headers

# creates Chrome Service & WebDriver instance
browser_driver = Service("/Users/coderino/Library/Mobile Documents/com~apple~CloudDocs/Coding/chromedriver")
driver = webdriver.Chrome(service = browser_driver) # another object we're creating from a class


# scrape
def operating_parks():
    global unique_id
    unique_id = 1

    # GET page to scrape
    driver.get("https://rcdb.com/r.htm?st=93&ol=59&ot=3")

    while True:
        coaster_body = driver.find_elements(By.XPATH, '/html/body/section/div[2]/table/tbody')
        
        for coaster_group in coaster_body:
            
            # count number of rows
            coaster_rows = len(coaster_group.find_elements(By.XPATH, '/html/body/section/div[2]/table/tbody/tr'))
            
            # iterate through <td> elements and save to vars, .writerow([vars])
            for rows in range(1, coaster_rows+1):
                for columns in range(1):
                    coaster_name = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[2]').text
                    coaster_location = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[3]').text
                    coaster_status = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[4]').text
                    coaster_number_of_coasters = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[6]').text
            
                    writer.writerow(
                        [unique_id, coaster_name, coaster_location, coaster_status, coaster_number_of_coasters])
                    unique_id += 1

        try:
            # wait for data to load 
            wait = WebDriverWait(driver, 10)
            element_to_watch = driver.find_element(By.XPATH, '/html/body/section/div[2]/table')
            wait.until(EC.visibility_of(element_to_watch))
            
            # click next page
            element_to_click = driver.find_element(By.PARTIAL_LINK_TEXT, '>>')
            element_to_click.click()

        except NoSuchElementException:
            break
    # time.sleep(1)

def under_construction_parks():
    global unique_id
    
    # GET page to scrape
    driver.get("https://rcdb.com/r.htm?st=310&ol=59&ot=3")

    while True:
        coaster_body = driver.find_elements(By.XPATH, '/html/body/section/div[2]/table/tbody')
        
        for coaster_group in coaster_body:
            
            # count number of rows
            coaster_rows = len(coaster_group.find_elements(By.XPATH, '/html/body/section/div[2]/table/tbody/tr'))
            
            # iterate through <td> elements and save to vars, .writerow vars
            for rows in range(1, coaster_rows+1):
                for columns in range(1):
                    coaster_name = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[2]').text
                    coaster_location = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[3]').text
                    coaster_status = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[4]').text
                    coaster_number_of_coasters = coaster_group.find_element(By.XPATH, '/html/body/section/div[2]/table/tbody/tr['+str(rows)+']/td[6]').text
            
                    writer.writerow(
                        [unique_id, coaster_name, coaster_location, coaster_status, coaster_number_of_coasters])
                    unique_id += 1

        try:
            # wait for data to load 
            wait = WebDriverWait(driver, 10)
            element_to_watch = driver.find_element(By.XPATH, '/html/body/section/div[2]/table')
            wait.until(EC.visibility_of(element_to_watch))
            
            # click next page
            element_to_click = driver.find_element(By.PARTIAL_LINK_TEXT, '>>')
            element_to_click.click()

        except NoSuchElementException:
            break
    # time.sleep(1)

operating_parks()
under_construction_parks()

# if you want to see the total elapsed time for this scraper: 
# also uncomment time import & sleeptime(1) in functions
# def timer():
#   start_time = time.perf_counter()
#   operating_parks()
#   under_construction_parks()
#   end_time = time.perf_counter()
#   elapsed_time = end_time - start_time
#   print(f"Total elapsed time: {elapsed_time:.6f} seconds")

# timer()

file.close()
driver.quit()