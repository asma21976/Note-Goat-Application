from ast import Assert
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings


@override_settings(DEBUG=True)
class LoginTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-file.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)

    # Requirement 2
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    #Test Login with valid credentials
    def test_login_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))
        username_input = self.selenium.find_element_by_name("username")
        password_input = self.selenium.find_element_by_name("password")

        username_input.send_keys("tester")
        password_input.send_keys("requirement3")

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'home'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals(expectedUrl , str(actualUrl), "Login should be successful")

    #Test Login with invalid credentials
    def test_login_invalid_creds(self):
       self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))
       username_input = self.selenium.find_element_by_name("username")
       password_input = self.selenium.find_element_by_name("password")

       username_input.send_keys("test_user_incorrect")
       password_input.send_keys("notTestPassword_123")

       self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

       expectedUrl = 'accounts/login/'
       actualUrl = self.selenium.current_url.split("/", 3)[-1]

       self.assertEquals(expectedUrl , str(actualUrl), "Login should not be successful")
    
    #Test Login with null credentials
    def test_login_null(self):
       self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))
       username_input = self.selenium.find_element_by_name("username")
       password_input = self.selenium.find_element_by_name("password")

       username_input.clear()
       password_input.clear()

       self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

       expectedUrl = 'accounts/login/'
       actualUrl = self.selenium.current_url.split("/", 3)[-1]

       self.assertEquals(expectedUrl , str(actualUrl), "Login should not be successful with null data")

