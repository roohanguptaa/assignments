from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def fill_form():
    # Update the path to ChromeDriver executable
    driver_path = r"C:\assignments\medius ai tech\chromedriver.exe"
    print(f"Using ChromeDriver from: {driver_path}")
    
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    print("WebDriver initiated.")

    try:
        print("Filling out the form...")
        driver.get('https://forms.gle/WT68aV5UnPajeoSc8')
        
        # Full Name
        print("Entering full name...")
        name_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        name_input.clear()
        name_input.send_keys('rohan gupta')

        # Contact Number
        print("Entering contact number...")
        contact_number_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        contact_number_input.clear()
        contact_number_input.send_keys('7387711212')

        # Email ID
        print("Entering email ID...")
        email_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        email_input.clear()
        email_input.send_keys('rohangupta1892004@gmail.com')

        # Full Address
        print("Entering full address...")
        address_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'))
        )
        address_input.clear()
        address_input.send_keys('a/101,vansh apt,virar road,indira nagar,nr divine life high school,nalasopara East.')

        # Pin Code
        print("Entering pin code...")
        pin_code_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        pin_code_input.clear()
        pin_code_input.send_keys('401209')

        # Date of Birth
        print("Entering date of birth...")
        dob_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'))
        )
        dob_input.clear()
        dob_input.send_keys('18-09-2004')  # Format: DD-MM-YYYY

        # Gender (Male)
        print("Selecting gender...")
        gender_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        gender_input.clear()
        gender_input.send_keys('Male')

        # Verification Code
        print("Entering verification code...")
        verification_code_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'))
        )
        verification_code_input.clear()
        verification_code_input.send_keys('GNFPYC')

        print("Form filling complete. Submitting...")

        # Submit Button
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))
        )
        submit_button.click()

        # Wait for the confirmation page to load
        time.sleep(5)

        # Capture a screenshot of the confirmation page
        screenshot_path = r'C:\assignments\confirmation_page.png'
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Debug: Capture screenshot on error
        error_screenshot_path = r'C:\assignments\error.png'
        driver.save_screenshot(error_screenshot_path)
        print(f"Error screenshot saved as {error_screenshot_path}")
    finally:
        print("Quitting the driver...")
        driver.quit()

if __name__ == '__main__':
    fill_form()
