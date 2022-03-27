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
class UpdateFolderTestCase(StaticLiveServerTestCase):
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

    #Test update folder without notes
    def test_update_folder_empty(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/add7dd86-feb1-4007-97eb-c13ceef0ec23/update/'))
        login(self)

        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').send_keys('_updated')

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        folder_name = self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div[2]/button/h4').text

        self.assertEquals('empty_folder_updated', folder_name, 'The folder name should be updated to empty_folder_updated')


    #Test update folder with notes
    def test_update_folder_not_empty(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/bf187209-da23-4def-8346-f55efcc65524/update/'))
        login(self)

        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').send_keys('_updated')

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        folder_name = self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div[3]/button/h4').text

        self.assertEquals('test_folder2_updated', folder_name, 'The folder name should be updated to test_folder2_updated')


    #Test update folder without providing a name
    def test_update_folder_no_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/bf187209-da23-4def-8346-f55efcc65524/update/'))
        login(self)

        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').clear()

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('folder/bf187209-da23-4def-8346-f55efcc65524/update/', actualUrl, 'Folder should not be able to be updated without name')
