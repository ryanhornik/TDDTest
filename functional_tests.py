from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user goes to homepage
        self.browser.get('http://localhost:8000')

        # user notices the page title and header mention To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # User types "buy peacock feathers" into a textbox
        inputbox.send_keys('Buy peacock feathers')

        # When the user hits enter the page updates and now the page list
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # There is another textbox for
        # enters "Use peacock feathers to make a fly"
        self.fail('Finish the test')

        # Page updates and both items are on the list

        # user has a unique url pointing to her

        # user revisits the unique url and to-do list is still there

        # user closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')