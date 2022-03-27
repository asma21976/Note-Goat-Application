
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep



#Requirement 10
@override_settings(DEBUG=True)
class StoreNotesInFolderTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-folder.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Test storing a new note into a folder
    def test_store_note_new(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/create/'))
        login(self)

        file_name = self.selenium.find_element_by_name("file_name")

        file_name.send_keys("folder_test_note")

        notedrop = Select(self.selenium.find_element_by_id('id_folder'))

        notedrop.select_by_visible_text("test_folder1")

        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))
        
        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a test")

        self.selenium.switch_to.default_content()

        create_button = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')

        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        
        create_button.location_once_scrolled_into_view
        sleep(1)

        create_button.click()

        self.selenium.find_element_by_xpath('//*[@id="7a4da6ff-7653-445e-b666-ea92b4b6c8f1"]').click()

        # Try to find folder if finds test passes, if not it fails
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[1]/form/div[3]/a')

    # Test storing an already made note into a folder
    def test_store_note_old(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/2da7df71-9b8a-40d0-86ca-5ade86dae31f/update/'))
        login(self)

        notedrop = Select(self.selenium.find_element_by_id('id_folder'))

        notedrop.select_by_visible_text("test_folder2")

        create_button = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')

        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        
        create_button.location_once_scrolled_into_view
        sleep(1)

        create_button.click()

        self.selenium.find_element_by_xpath('//*[@id="bf187209-da23-4def-8346-f55efcc65524"]').click()

        # Try to find folder if finds test passes, if not it fails
        self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[1]/form/div[1]/a')


        
