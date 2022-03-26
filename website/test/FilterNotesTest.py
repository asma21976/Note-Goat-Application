from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from pytest import fixture
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from website.test.LoginMethod import login



#Requirement 14
@override_settings(DEBUG=True)
class FilterNotesTestCase(StaticLiveServerTestCase):
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

    def test_filter_shared_notes_hidden(self):
