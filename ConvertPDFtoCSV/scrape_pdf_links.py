


from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : "D:\Webscraping\ConvertPDFtoCSV"}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

# Open the target webpage
webpage_url = "https://www.sbp.org.pk/ecodata/kibor_index.asp"
driver.get(webpage_url)

# Find the elements using XPath
pdf_links = []
for i in range(1, 8):  # Loop over the desired range of elements
    xpath_expr = '//*[@id="tablediv"]/table/tbody/tr[{}]/td[2]/a'.format(i)
    pdf_link = driver.find_element(By.XPATH, xpath_expr)
    pdf_links.append(pdf_link)
    print(pdf_links)


# Extract the URLs from the elements
pdf_urls = [link.get_attribute("href") for link in pdf_links]

# Print the extracted PDF URLs
for url in pdf_urls:
    print(url)

# Close the web browser
driver.quit()
