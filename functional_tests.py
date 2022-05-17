from cgi import print_arguments
from email import header
from selenium import webdriver # (1)
from selenium.webdriver.common.by import By
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    # browser = webdriver.Firefox() # (2)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith has heard about a coll new online to-do app. She goes 
        # to check out its homepage
        self.browser.get('http://localhost:8000') # (3)

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title) 
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn('To-Do' ,header_text)
        # self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.sent_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is still a text box inviting her to add another item. She
        # enters "User peacock feathers to mak a fly" (Edith is very methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees 
        # that ther site has genarated a unique URL for her -- there is some
        # explanatory text to that effect

        # She visites that UPR - her to-do list is still there.

        # Satisfied, she goes to slepp
        # assert 'To-Do' in browser.title # (4)
        # assert 'Django' in browser.title # (5)

if __name__ == '__name__': #(6)
    unittest.main(warnings='ignore') # (7)
