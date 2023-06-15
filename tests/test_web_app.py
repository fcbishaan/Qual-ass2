import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WebAppTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with the appropriate webdriver for your browser
        self.driver.get('http://localhost:5000')  # Start the web app on the local development server

    def tearDown(self):
        self.driver.quit()

    def test_sliding_window_maximum(self):
        # Find the input fields and submit button
        nums_input = self.driver.find_element_by_name('nums')
        k_input = self.driver.find_element_by_name('k')
        submit_button = self.driver.find_element_by_xpath('//input[@type="submit"]')

        # Enter input values and submit the form
        nums_input.send_keys('1,3,-1,-3,5,3,6,7')
        k_input.send_keys('3')
        submit_button.click()

        # Verify the result
        result = self.driver.find_element_by_xpath('//p').text
        self.assertEqual(result, 'Result: [3, 3, 5, 5, 6, 7]')

if __name__ == '__main__':
    unittest.main()
