import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in your PATH
    driver.maximize_window()
    yield driver
    driver.quit()

def test_ui_end_to_end(driver):
    # Step 1: Visit the webpage
    driver.get('https://www.saucedemo.com/')

    # Step 2: Define the XPath for the element containing the text to copy
    user_name_xpath = '//*[@id="login_credentials"]'

    # Step 3: Find the element using XPath and copy its text
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, user_name_xpath)))
    copied_text = driver.find_element(By.XPATH, user_name_xpath).text.strip().split("\n")[1]

    # Step 4: Paste the copied text into the textarea with id 'user-name'
    user_name_input = driver.find_element(By.ID, 'user-name')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(user_name_input))
    user_name_input.send_keys(copied_text)

    # Step 5: Type the password
    password_input = driver.find_element(By.ID, 'password')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(password_input))
    password_input.send_keys('secret_sauce')

    # Step 6: Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(login_button))
    login_button.click()

    # Assert that the user is redirected to the products page
    WebDriverWait(driver, 10).until(EC.url_contains('/inventory.html'))

    # Step 7: Add items to the cart
    add_to_cart_buttons = [
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket'),
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light'),
        driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    ]
    for button in add_to_cart_buttons:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))
        button.click()

    # Assert that the cart badge shows 3 items
    cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    WebDriverWait(driver, 10).until(EC.visibility_of(cart_badge))
    assert cart_badge.text == '3'

    # Step 8: Remove an item from the cart
    remove_button = driver.find_element(By.ID, 'remove-sauce-labs-bike-light')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(remove_button))
    remove_button.click()

    # Assert that the cart badge shows 2 items
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'shopping_cart_badge'), '2'))
    assert cart_badge.text == '2'

    # Step 9: Proceed to checkout
    cart_container = driver.find_element(By.ID, 'shopping_cart_container')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(cart_container))
    cart_container.click()

    checkout_button = driver.find_element(By.ID, 'checkout')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkout_button))
    checkout_button.click()

    # Step 10: Fill in the checkout information
    first_name_input = driver.find_element(By.ID, 'first-name')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(first_name_input))
    first_name_input.send_keys('Elmar')

    last_name_input = driver.find_element(By.ID, 'last-name')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(last_name_input))
    last_name_input.send_keys('Yusifli')

    postal_code_input = driver.find_element(By.ID, 'postal-code')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(postal_code_input))
    postal_code_input.send_keys('12345')

    # Step 11: Continue to the next step
    continue_button = driver.find_element(By.ID, 'continue')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(continue_button))
    continue_button.click()

    # Assert that the overview page is displayed
    WebDriverWait(driver, 10).until(EC.url_contains('/checkout-step-two.html'))

    # Step 12: Finish the checkout process
    finish_button = driver.find_element(By.ID, 'finish')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(finish_button))
    finish_button.click()

    # Step 13: Define the XPath for the element containing the completion message
    complete_message_xpath = '//*[@id="checkout_complete_container"]/h2'

    # Step 14: Find the element using XPath, get its text, and assert it is equal to "Thank you for your order!"
    complete_message_element = driver.find_element(By.XPATH, complete_message_xpath)
    WebDriverWait(driver, 10).until(EC.visibility_of(complete_message_element))
    complete_message = complete_message_element.text.strip()
    assert complete_message == 'Thank you for your order!'

    # Step 15: Navigate back to the products page
    back_to_products_button = driver.find_element(By.ID, 'back-to-products')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(back_to_products_button))
    back_to_products_button.click()

    # Assert that the user is redirected to the products page
    WebDriverWait(driver, 10).until(EC.url_contains('/inventory.html'))

    # Step 16: Open the menu and log out
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(menu_button))
    menu_button.click()

    logout_link = driver.find_element(By.ID, 'logout_sidebar_link')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(logout_link))
    logout_link.click()

    # Assert that the user is redirected to the login page
    logo_xpath = '//*[@id="root"]/div/div[1]'
    logo_element = driver.find_element(By.XPATH, logo_xpath)
    WebDriverWait(driver, 10).until(EC.visibility_of(logo_element))
    logo_text = logo_element.text.strip()
    assert logo_text == 'Swag Labs'
