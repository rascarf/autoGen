from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10

class mytest(LiveServerTestCase):
    browser=webdriver.Chrome()

    def setUp(self):
        pass

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_list_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
    # Edith has heard about a cool new online to-do app.
        self.browser.get(self.live_server_url)
    #She notices the page title and header mention to-do lists
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do",header_text)

    #She is invited to enter a to_do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1:Buy peacock feathers")

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("2:Use peacock feathers to make a fly")

        #self.check_for_row_in_list_table("1:Buy peacock feathers")
        #table = self.browser.find_element_by_id("id_list_table")
        #rows=table.find_elements_by_tag_name("tr")

        #self.wait_for_row_in_list_table("1:Buy peacock feathers")
        #self.wait_for_row_in_list_table("2:Use peacock feathers to make a fly")

        self.fail("Finish the test!")

    def test_can_start_a_list_for_one_user(self):
        #Edith has heard about a cool new online to-do app.
        #She goes the page updates again,and now shows both items on her list
        self.wait_for_row_in_list_table("1:Buy peacock feathers")
        self.wait_for_row_in_list_table("2:Use peacock feathers to make a fly")

        #satisfied she goes back to sleep

    def test_multip_users_can_start_lists_at_different_urls(self):
        #Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1:Buy peacock feathers")

        #She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,"/lists/.+")

        # Now a new user,Francis,comes along to the site
        # We use a new browser session to make sure that no information of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Chrome()
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        # Francis starts a new list by entering a new item
        # He is less interesting than Edith
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy Milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1:Buy Milk")

        # francis get his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "./lists/.+")
        self.assertNotIn(francis_list_url, edith_list_url)

