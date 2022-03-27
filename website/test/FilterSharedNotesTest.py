from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from website.test.LoginMethod import login
from time import sleep



#Requirement 14
@override_settings(DEBUG=True)
class FilterSharedNotesTestCase(StaticLiveServerTestCase):
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

    # Tests if user can make the shared notes element not visible
    def test_filter_shared_notes_hidden(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="shared-notes"]').get_attribute('checked') == 'checked'):
            self.selenium.find_element_by_xpath('//*[@id="shared-notes"]').click()
        

        self.assertFalse(self.selenium.find_element_by_xpath('//*[@id="shared-notes-view"]').is_displayed(), "The element that displays the shared notes should not be displayed")


    # Tests if user can make the shared notes element visible
    def test_filter_shared_notes_visible(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="shared-notes"]').get_attribute('checked') != 'checked'):
            self.selenium.find_element_by_xpath('//*[@id="shared-notes"]').click()
        

        self.assertTrue(self.selenium.find_element_by_xpath('//*[@id="shared-notes-view"]').is_displayed(), "The element that displays the shared notes should be displayed")



        





