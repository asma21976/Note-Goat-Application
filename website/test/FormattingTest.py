
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login



#Requirement 15
@override_settings(DEBUG=True)
class FormattingTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    #Test if bolding function works if clicked before writing text
    def test_bold_before_writing(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/a[1]/button').click()
        self.selenium.implicitly_wait(2)

        self.selenium.find_element_by_xpath('/html/body/div[1]/form/p[3]/div/div[1]/div[1]/div[1]/div/div[3]/button[1]').click()
        
        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))
        
        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a test")
        self.selenium.implicitly_wait(2)


        # Strong means bold, so if its found the test will pass, if not it will fail
        text = self.selenium.find_element_by_xpath('/html/body/p/span/strong')


        self.selenium.switch_to.default_content()

    #Test if bolding function works if clicked after writing text
    def test_bold_after_writing(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/a[1]/button').click()
        self.selenium.implicitly_wait(2)
        
        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))
        
        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a test")
        text_input.send_keys(Keys.CONTROL, 'a')


        self.selenium.switch_to.default_content()

        self.selenium.find_element_by_xpath('/html/body/div[1]/form/p[3]/div/div[1]/div[1]/div[1]/div/div[3]/button[1]').click()


        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))


        # Strong means bold, so if its found the test will pass, if not it will fail
        text = self.selenium.find_element_by_xpath('/html/body/p/strong')

        self.selenium.switch_to.default_content()

    #Test if italics function works if clicked before writing text
    def test_italics_before_writing(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/a[1]/button').click()
        self.selenium.implicitly_wait(2)

        self.selenium.find_element_by_xpath('/html/body/div[1]/form/p[3]/div/div[1]/div[1]/div[1]/div/div[3]/button[2]').click()
        
        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))
        
        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a test")
        self.selenium.implicitly_wait(2)


        # em means italics, so if its found the test will pass, if not it will fail
        text = self.selenium.find_element_by_xpath('/html/body/p/span/em')


        self.selenium.switch_to.default_content()

    #Test if italics function works if clicked after writing text
    def test_italics_after_writing(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/a[1]/button').click()
        self.selenium.implicitly_wait(2)
        
        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))
        
        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a test")
        text_input.send_keys(Keys.CONTROL, 'a')


        self.selenium.switch_to.default_content()

        self.selenium.find_element_by_xpath('/html/body/div[1]/form/p[3]/div/div[1]/div[1]/div[1]/div/div[3]/button[2]').click()


        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))


        # em means italics, so if its found the test will pass, if not it will fail
        text = self.selenium.find_element_by_xpath('/html/body/p/em')

        self.selenium.switch_to.default_content()      








    