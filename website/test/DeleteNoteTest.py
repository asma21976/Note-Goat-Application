from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from website.test.LoginMethod import login3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep



#Requirement 5
@override_settings(DEBUG=True)
class DeleteFolderTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-note-delete.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    #Test deleting folder with notes
    def test_delete_file(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/d4beed15-ea7d-4a06-99ba-60a18ac2eb06/delete/'))
        login3(self)

        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        self.selenium.find_element_by_id('85b34943-5b65-4dbc-a11c-36542a7dcd5f').click()

        found = self.selenium.find_elements_by_xpath('//h4[contains(.,"test_delete")]')

        self.assertFalse(found, 'The test_delete element should not be present')



