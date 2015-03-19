from selenium import webdriver
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
        self.fail('Finish the test!')

        # User is invited to enter a to-do item

        # User types "buy peacock feathers" into a textbox

        # When the user hits enter the page updates and now the page list
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is another textbox for
        # enters "Use peacock feathers to make a fly"

        # Page updates and both items are on the list

        # user has a unique url pointing to her

        # user revisits the unique url and to-do list is still there

        # user closes the browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')