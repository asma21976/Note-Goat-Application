from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from datetime import datetime
from django.db import models
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from website.test.LoginMethod import login3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep




#Requirement 6
@override_settings(DEBUG=True)
class UpdatedTimeTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-note-update.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    #Test edit text in local note
    def test_update_local_note(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/d2fa6d19-d966-4b1e-8961-14653ec84fb6/update/'))
        login3(self)

        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.clear()
        editor_body.send_keys('Edited this now!')
        self.selenium.switch_to.default_content()

        update_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.location_once_scrolled_into_view
        sleep(1)
        update_button.click()
        now = datetime.now()
        updated_time = now.strftime("%B %d, %Y, %-I:%M")
        print(updated_time)

        self.selenium.find_element_by_xpath('//button[@id="fc1fb5d4-a214-4590-9ab7-22edcc888a1d"]/h4').click()
        sleep(1)
        self.selenium.find_element_by_xpath('//div[@id="notes"]/form/div/a').click()


        self.assertTrue(updated_time in self.selenium.page_source)
