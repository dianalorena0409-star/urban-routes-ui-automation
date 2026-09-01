from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage
from helpers.retrieve_code import retrieve_phone_code


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability('goog:loggingPrefs',{'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_set_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        comfort_tariff = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == "Comfort"

    def test_3_add_phone_number(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        assert self.routes_page.get_phone_code() == code
        self.routes_page.click_phone_confirm_button()

    def test_4_add_credit_card(self):
        address_from = data.address_from
        address_to = data.address_to
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(card_number)
        self.routes_page.set_card_code(card_code)
        self.routes_page.click_add_card_button()
        assert self.routes_page.get_card_option().is_displayed()

    def test_5_message_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        message = data.message_for_driver
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.set_message_for_driver(message)
        assert self.routes_page.get_message_for_driver() == message

    def test_6_blanket_and_tissues(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_blanket_and_tissues_switch()
        assert self.routes_page.is_blanket_and_tissues_switch_selected()

    def test_7_add_two_ice_creams(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.add_ice_cream()
        self.routes_page.add_ice_cream()
        assert self.routes_page.get_ice_cream_count() == "2"

    def test_8_order_taxi(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.get_order_modal_text() == "Buscar automóvil"

    def test_9_driver_info(self):
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(phone_number)
        self.routes_page.click_phone_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_phone_confirm_button()
        self.routes_page.click_order_taxi_button()
        driver_info = self.routes_page.get_driver_info()
        assert driver_info.is_displayed()

    def teardown_method(self):
        self.driver.quit()
