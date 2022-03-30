from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from website.test.LoginMethod import login
from time import sleep



#Requirement 13
@override_settings(DEBUG=True)
class FilterFolderNotesTestCase(StaticLiveServerTestCase):
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

    # Tests if user can make the folder notes element not visible
    def test_filter_folder_notes_hidden(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="my-notes"]').get_attribute('checked') != 'checked'):
            print("reeee\n\n\n\n")
            self.selenium.find_element_by_xpath('//*[@id="my-notes"]').click()
        
        self.assertFalse(self.selenium.find_element_by_xpath('//*[@id="notes"]').is_displayed(), "The element that displays the notes should not be displayed")


    # Tests if user can make the folder notes element visible
    def test_filter_folder_notes_visible(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="my-notes"]').get_attribute('checked') == 'checked'):
            self.selenium.find_element_by_xpath('//*[@id="my-notes"]').click()
        
        self.assertTrue(self.selenium.find_element_by_xpath('//*[@id="notes"]').is_displayed(), "The element that displays the notes should be displayed")


    # Tests if user can access different notes in folder1
    def test_filter_by_folder_folder1(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="my-notes"]').get_attribute('checked') != 'checked'):
            self.selenium.find_element_by_xpath('//*[@id="my-notes"]').click()
        
        self.selenium.find_element_by_xpath('//*[@id="7a4da6ff-7653-445e-b666-ea92b4b6c8f1"]').click()
        note_name = self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[1]/form/div[1]/a/h4').get_attribute('innerHTML')

        self.assertEqual('test_note1_folder1', note_name, "Folder 1 should contian test_note1_folder1 note")


    # Tests if user can access different notes in folder2
    def test_filter_by_folder_folder2(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/home'))
        login(self)
        if (self.selenium.find_element_by_xpath('//*[@id="my-notes"]').get_attribute('checked') != 'checked'):
            self.selenium.find_element_by_xpath('//*[@id="my-notes"]').click()
        
        self.selenium.find_element_by_xpath('//*[@id="bf187209-da23-4def-8346-f55efcc65524"]').click()
        note_name = self.selenium.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[1]/form/div/a/h4').get_attribute('innerHTML')

        self.assertEqual('test_note1_folder2', note_name, "Folder 2 should contian test_note1_folder2 note")


