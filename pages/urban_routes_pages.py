
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_input = (By.ID, 'phone')
    phone_button = (By.CLASS_NAME, "np-button")
    phone_code_input = (By.ID, 'code')
    active_section_button = (By.CSS_SELECTOR,'.number-picker .section.active button[type="submit"].button.full')
    payment_method = (By.CLASS_NAME, 'pp-text')
    add_card = (By.XPATH,'//div[@class="pp-title" and text()="Agregar tarjeta"]')
    card_number = (By.ID, 'number')
    card_code = (By.CSS_SELECTOR,'.card-code-input #code')
    add_card_button = (By.XPATH, '//button[text()="Agregar"]')
    card_option = (By.XPATH, '//div[text()="Tarjeta"]')
    message_for_driver = (By.ID, 'comment')
    blanket_and_tissues_switch = (By.XPATH,'//div[@class="r-sw-label" and text()="Manta y pañuelos"]'
        '/following-sibling::div//span[@class="slider round"]')
    blanket_and_tissues_checkbox = (By.XPATH,'//div[@class="r-sw-label" and text()="Manta y pañuelos"]'
        '/following-sibling::div//input[@type="checkbox"]')
    ice_cream_plus_button = (By.XPATH,
        '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div//div[contains(@class, "counter-plus")]')
    ice_cream_counter = (By.XPATH,
        '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div//div[@class="counter-value"]')
    order_taxi_button = (By.CLASS_NAME, "smart-button")
    order_modal = (By.CSS_SELECTOR, ".order.shown .order-header-title")
    driver_rating = (By.CLASS_NAME, "order-btn-rating")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def set_from(self, from_address):
       self.wait.until(EC.visibility_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.visibility_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button))

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_icon))

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(EC.presence_of_element_located(self.comfort_icon_assert))

    def get_phone_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_input))

    def set_phone_number(self, phone_number):
        self.get_phone_input().send_keys(phone_number)

    def get_phone_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_button))

    def click_phone_button(self):
        self.get_phone_button().click()

    def get_phone_code_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_code_input))

    def set_phone_code(self, code):
        self.get_phone_code_input().send_keys(code)

    def get_phone_code(self):
        return self.driver.find_element(*self.phone_code_input).get_property("value")

    def get_phone_active_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.active_section_button))

    def click_phone_next_button(self):
        self.get_phone_active_button().click()

    def click_phone_confirm_button(self):
        self.get_phone_active_button().click()

    def get_payment_method(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method))

    def click_payment_method(self):
        self.get_payment_method().click()

    def get_add_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card))

    def click_add_card(self):
        self.get_add_card().click()

    def set_card_number(self, card_number):
        self.wait.until(EC.visibility_of_element_located(self.card_number)).send_keys(card_number)

    def set_card_code(self, card_code):
        code_field = self.wait.until(EC.visibility_of_element_located(self.card_code))
        code_field.send_keys(card_code)
        code_field.send_keys(Keys.TAB)

    def get_add_card_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_button))

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_card_option(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_option))

    def set_message_for_driver(self, message):
        self.wait.until(EC.visibility_of_element_located(self.message_for_driver)).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver).get_property("value")

    def click_blanket_and_tissues_switch(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_and_tissues_switch)).click()

    def is_blanket_and_tissues_switch_selected(self):
        return self.wait.until(EC.presence_of_element_located(self.blanket_and_tissues_checkbox)).is_selected()

    def add_ice_cream(self):
        self.wait.until(EC.element_to_be_clickable(self.ice_cream_plus_button)).click()

    def get_ice_cream_count(self):
        return self.wait.until(EC.presence_of_element_located(self.ice_cream_counter)).text

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_taxi_button)
        ).click()

    def get_order_modal_text(self):
        return self.driver.find_element(*self.order_modal).text

    def get_driver_info(self):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(self.driver_rating))
