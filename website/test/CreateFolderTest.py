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
class CreateFolderTestCase(StaticLiveServerTestCase):
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

    #Test create folder without providing a name
    def test_create_folder_no_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/create/'))
        login(self)

        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').clear()

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('folder/create/', actualUrl, 'Folder should not be able to be updated without name')

    #Test create folder with a valid name
    def test_create_folder_valid_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/folder/create/'))
        login(self)

        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').clear()
        self.selenium.find_element_by_xpath('//*[@id="id_folder_name"]').send_keys('test_folder')

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()


        text = self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div[4]/button/h4').text

        self.assertEquals('test_folder', text, 'Folder should be created and named test_folder')
