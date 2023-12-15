from selenium import webdriver
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

# Google 2FA must be off

# At https://mail.google.com/mail/u/0/#settings/general
# Maximum page size: Show 100 conversations per page

# Set up command line arguments
parser = argparse.ArgumentParser(description="Automate Gmail login and email deletion.")
parser.add_argument("--username", help="Your Gmail username or email address.", required=True)
parser.add_argument("--password", help="Your Gmail password.", required=True)
args = parser.parse_args()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.google.com/')

# Fill username
driver.find_element_by_id('identifierId').send_keys(args.username)
driver.find_element_by_id('identifierNext').click()
time.sleep(1)  # Add pause for password field load

# Fill in password and log in
passwd = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
passwd.click()
passwd.send_keys(args.password)
time.sleep(1)  # Add pause

# Click login button
driver.find_element(By.XPATH,  '//*[@id="passwordNext"]/div/button/span').click()
# Adjust sleep times to avoid unnecessary delays
time.sleep(5)  # Add pause

while True:
    # Check all emails
    driver.find_element(By.XPATH,  '//*[@id=":1d"]/div[1]/span').click()
	# Adjust sleep times to avoid unnecessary delays
    time.sleep(3)

    # Press delete
    driver.find_element(By.XPATH,  '//*[@id=":4"]/div/div[1]/div[1]/div/div/div[2]/div[3]/div').click()
	# Adjust sleep times to avoid unnecessary delays
    time.sleep(5)