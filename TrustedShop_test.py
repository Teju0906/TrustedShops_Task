# Library:
''' The list below contains the library files imported from Selenium tool '''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Driver Initialisation:
''' The below code initiates driver to the corresponding browser by its executable file '''

chrome_path = "C:\\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)


# Maximize Window:
''' The below code maximizes the browser window for better screen resolution and experience '''

driver.maximize_window()


# Launch URL and Title verification:
''' The below code verify the page title exists or not '''

driver.get('https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html')
if driver.title != " ":
    print("Title is:", driver.title)
else:
    print("no title")
driver.implicitly_wait(5)


# Grade verification and validation:
''' The below code verify the grade is visible and validates it is above zero '''

element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='top']/div/div[4]/div[2]/div[1]/div[1]/div[2]/span"))
).text
grade_value = float(element.replace(',', '.'))
if grade_value > 0:
    print('Grade is above zero')
else:
    print('Grade is zero or below')



# Click On Link and the Information is relevant:
''' The below code verify the link is clickable and the link window Information is relevant or not '''

driver.find_element(By.LINK_TEXT,"Wie berechnet sich die Note?").click()
newwindow = driver.find_element(By.XPATH, "//pre[normalize-space()='Notenberechnung auf Basis der Sternevergabe']").text
print(newwindow)
assert "berech" in newwindow



# Click on "2 stars" to filter all two star reviews and ensure the results are relevant :
''' The below code verify the "2 stars" are clickable which filters all two star reviews and ensuring every review in the list has only two star rating '''

link_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html?stars=2']")))
driver.execute_script("arguments[0].click();", link_element)
review_elements = driver.find_elements(By.XPATH, "//div[@class='sc-2e7612c5-0 sc-f836bc46-0 kyZgbN chcERM']"
                                                      "//div[@class='Starsstyles__Stars-sc-4o1xbr-0 gWZgUz']")
count_2_stars_for_all = True  # Flag to track if count is 2 for all elements

for element in review_elements:
    span_elements = element.find_elements(By.XPATH, ".//span")
    count = len([span for span in span_elements if "color: rgb(255, 220, 15)" in span.get_attribute("style")])   # To count only two stars using color style for the entire star rating component
    if count != 2:
        print("The count is not 2 for this element")
        count_2_stars_for_all = False
        break  # Exit the loop if any element has a count different from 2
if count_2_stars_for_all:
    print("All elements have 2 stars")



# Sum of all star percentage values must be equal or below 100:
''' The below code verify the sum of all star percentage values must be equal or below 100 '''

star_elements = driver.find_elements(By.XPATH, "//div[@class='sc-61f2e426-3 sc-61f2e426-4 lmrSdC ghcBqu']")
total_percentage = 0
for star_element in star_elements:
    total_percentage += round(float(star_element.get_attribute("style").split(":")[1].strip("%;")))   # To round off the percentage values of each star rating and stores as Int value

print(total_percentage)

if total_percentage <= 100:
    print("Total percentage is equal or below 100")
else:
    print("Total percentage is above 100")
driver.quit()





''' End of code '''




