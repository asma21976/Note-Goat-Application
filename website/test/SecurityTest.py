from ast import Assert
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings


@override_settings(DEBUG=True)
class SecurityTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_create_account_secure_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_secure")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("W:qm$L3@(VqJU&Ue")
        password_conf_input.send_keys("W:qm$L3@(VqJU&Ue")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/login/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))

    def test_create_account_no_password(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_no_password")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("")
        password_conf_input.send_keys("")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))


    def test_create_account_insecure_password_too_short(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_insecure_too_short")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("~sW3?")
        password_conf_input.send_keys("~sW3?")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))

    def test_create_account_insecure_password_too_similar(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_insecure")
        first_name_input.send_keys("W:qm$L3@(VqJU&Ue")
        last_name_input.send_keys("test")
        password_input.send_keys("W:qm$L3@(VqJU&Ue")
        password_conf_input.send_keys("W:qm$L3@(VqJU&Ue")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))


    def test_create_account_insecure_password_commonly_used(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_insecure")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("password")
        password_conf_input.send_keys("password")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))


    def test_create_account_insecure_password_completely_numeric(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_insecure")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("1234567890123456789")
        password_conf_input.send_keys("1234567890123456789")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))


    def test_create_account_insecure_password_bad_confirmation(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))
        email_input = self.selenium.find_element_by_name("email")
        username_input = self.selenium.find_element_by_name("username")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        password_input = self.selenium.find_element_by_name("password1")
        password_conf_input = self.selenium.find_element_by_name("password2")

        email_input.send_keys("test_email@notegoattest.com")
        username_input.send_keys("test_user_insecure")
        first_name_input.send_keys("test")
        last_name_input.send_keys("test")
        password_input.send_keys("W:qm$L3@(VqJU&Ue")
        password_conf_input.send_keys("k,+`m&92LxX~~jeL")
        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        expectedUrl = 'accounts/signup/'
        actualUrl = self.selenium.current_url.split("/", 3)[-1]
        
        self.assertEquals(expectedUrl , str(actualUrl))