from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def initialize_driver():
    driver = webdriver.Edge()
    return driver

def login(driver):
    input_username = driver.find_element(By.ID, "user-name")
    container_username = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
    split_container_username = container_username.text.split("\n")
    user_name = split_container_username[1]
    input_username.send_keys(user_name)

    input_password = driver.find_element(By.ID, "password")
    container_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]')
    split_container_password = container_password.text.split("\n")
    password = split_container_password[1]
    input_password.send_keys(password)

    loggin_button = driver.find_element(By.ID, "login-button")
    loggin_button.click()

    return driver

def main():
    driver = initialize_driver()
    driver.get("https://www.saucedemo.com/")
    driver = login(driver)

    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
        logout_button.click()

        print('LogOut success')
        driver.quit()
    else:
        print("Login failed")

if __name__ == '__main__':
    main()
