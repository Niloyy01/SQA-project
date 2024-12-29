from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():
    # Initialize the WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the login page
        driver.get("https://the-internet.herokuapp.com/login")
        print("Opened the login page.")

        # Locate the username and password fields
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        # Enter valid credentials
        username = "tomsmith"
        password = "SuperSecretPassword!"

        username_field.send_keys(username)
        password_field.send_keys(password)
        print("Entered login credentials.")

        # Submit the form
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # Wait for the success message to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )

        # Verify successful login
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success").text
        assert "You logged into a secure area!" in success_message
        print("Login successful: ", success_message)

        # Log out
        logout_button = driver.find_element(By.CSS_SELECTOR, "a[href='/logout']")
        logout_button.click()

        # Wait for the logout confirmation
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        print("Logged out successfully.")

    except Exception as e:
        print("Test failed: ", str(e))

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    test_login()
