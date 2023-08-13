import time
import traceback
from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tags import *

url = 'https://shop.foodsoul.pro/'


def order():
    try:
        driver.get(url)
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, cookie_notification_close).click()
        driver.find_element(By.CSS_SELECTOR, delivery_type_button).click()
        time.sleep(1)
        driver.find_elements(By.CSS_SELECTOR, pickup_place_button)[1].click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, auth_form_button).click()
        driver.find_element(By.CSS_SELECTOR, tg_auth_button).click()

        print('Перейдите по ссылке: ' + driver.find_element(By.CSS_SELECTOR, tg_link).get_attribute('href'))

        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, profile_button)))
            print('Авторизация прошла успешно')
            time.sleep(1)
        except Exception:
            print('Тайм-аут авторизации')
            exit(1)

        driver.find_element(By.CSS_SELECTOR, product).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, product_confirm_button).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, cart_button).click()
        time.sleep(1)

        driver.save_screenshot(f"screenshots/cart.png")

        driver.close()
        driver.quit()

    except Exception:
        driver.save_screenshot(f"screenshots/error.png")
        print(traceback.format_exc())
        exit(1)
