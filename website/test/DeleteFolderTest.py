from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep



#Requirement 9
@override_settings(DEBUG=True)
class DeleteFolderTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-delete.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    #Test deleting folder without notes
    def test_delete_folder_empty(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/add7dd86-feb1-4007-97eb-c13ceef0ec23/delete/'))
        login(self)

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        found = self.selenium.find_elements_by_xpath('//*[@id="add7dd86-feb1-4007-97eb-c13ceef0ec23"]')

        self.assertFalse(found, 'The empty_folder element should not be present')


    #Test deleting folder with notes
    def test_delete_folder_not_empty(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/bf187209-da23-4def-8346-f55efcc65524/delete/'))
        login(self)

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        found = self.selenium.find_elements_by_xpath('//*[@id="bf187209-da23-4def-8346-f55efcc65524"]')

        self.assertFalse(found, 'The test_folder2 element should not be present')



