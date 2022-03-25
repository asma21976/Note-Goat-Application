from ast import Assert
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings

@override_settings(DEBUG=True)
class CreateAccountTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Req 1
    def test_create_account_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user")
        first_name_input.send_keys("test")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("W:qm$L3@(VqJU&Ue")
        password_conf_input.send_keys("W:qm$L3@(VqJU&Ue")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/login/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))