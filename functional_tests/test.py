from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase

class mytest(LiveServerTestCase):
    browser=webdriver.Chrome()

    def setUp(self):
        pass

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text,[row.text for row in rows])

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
        time.sleep(1)

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #self.check_for_row_in_list_table("1:Buy peacock feathers")
        #table = self.browser.find_element_by_id("id_list_table")
        #rows=table.find_elements_by_tag_name("tr")

        self.check_for_row_in_list_table("1:Buy peacock feathers")
        self.check_for_row_in_list_table("2:Use peacock feathers to make a fly")

        self.fail("Finish the test!")



