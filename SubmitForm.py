import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class SubmitForm:
    def __init__(self, driver):
        self.driver = driver

    def submit_form(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the website and maximize the window
        driver.get("https://demoqa.com/automation-practice-form")
        driver.maximize_window()

        print("Test case started")

        firstname = ['firstname1', 'firstname2', 'firstname3', 'firstname4', 'firstname5', 'firstname6', 'firstname7']
        lastname = ['lastname1', 'lastname2', 'lastname3', 'lastname4', 'lastname5', 'lastname6', 'lastname7']
        email = ['user1@yopmail.com', 'user2@yopmail.com', 'user3@yopmail.com', 'user4@yopmail.com',
                 'user5@yopmail.com', 'user6@yopmail.com', 'user7@yopmail.com']
        mobileno = ['1234567890', '12345673890', '1234567890', '1234567890', '1234567890', '1234567890', '1234567890']

        name_length = len(firstname)

        for i in range(name_length):
            # Name field
            first_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'firstName')))
            first_name.send_keys(firstname[i])

            last_name = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'lastName')))
            last_name.send_keys(lastname[i])

            user_email = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'userEmail')))
            user_email.send_keys(email[i])

            if i == 1:
                gender_radio = driver.find_element(By.XPATH, "//label[contains(text(),'Female')]")
            else:
                gender_radio = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
            driver.execute_script('arguments[0].click()', gender_radio)

            user_number = driver.find_element(By.ID, 'userNumber')
            user_number.send_keys(mobileno[i])

            dob = driver.find_element(By.ID, 'dateOfBirthInput')
            driver.execute_script('arguments[0].click()', dob)

            # Calendar popup
            select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
            select_month.select_by_index(1)
            time.sleep(1)

            select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
            select_year.select_by_value('1996')
            time.sleep(1)

            select_day = driver.find_element(By.CLASS_NAME, "react-datepicker__day--007")
            driver.execute_script('arguments[0].click()', select_day)

            subject = driver.find_element(By.ID, 'subjectsInput')
            subject.send_keys('Computer Science')
            subject.send_keys(Keys.RETURN)

            hobbies = driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
            driver.execute_script('arguments[0].click()', hobbies)

            upload_pic = driver.find_element(By.ID, 'uploadPicture')
            upload_pic.send_keys("//Users//mac//Downloads//sqa.jpg")

            current_address = driver.find_element(By.ID, 'currentAddress')
            current_address.send_keys('Rawalpindi, Isb')

            driver.execute_script("document.body.style.zoom='50%'")

            current_address.send_keys(Keys.TAB)

            state_name = driver.find_element(By.ID, 'react-select-3-input')
            state_name.send_keys('Haryana')
            state_name.send_keys(Keys.RETURN)
            state_name.send_keys(Keys.TAB)

            select_city = driver.find_element(By.ID, "react-select-4-input")
            select_city.send_keys("Karnal")
            select_city.send_keys(Keys.RETURN)

            time.sleep(1)

            submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
            driver.execute_script('arguments[0].click()', submit_btn)

            time.sleep(1)

            close_btn = driver.find_element(By.ID, 'closeLargeModal')
            driver.execute_script('arguments[0].click()', close_btn)

            time.sleep(1)

        print("Test case completed")



submit_form= SubmitForm(webdriver)
submit_form.submit_form()