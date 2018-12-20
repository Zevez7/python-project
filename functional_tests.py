from selenium import webdriver
# need to import selenium library from the main folder that has selenium downloaded into using pip install
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.broswer.quit()
    
    def test_can_start_a_list_and_retrieve_it_late(self): 
        #Dat wants to use a new online web to-do app. 
        #He's going to check out the homepage         
        self.browser.get('http://localhost:8000')

        #He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

#He is inivted to enter a to-do item straight away

#He types "Work on Django project" into a text box (List of things to do)

#When he hits enter, the page updates, and now teh page lists
#"1: Work on Django projects" as an item to do on the list

#There is a text bo that's askign him to add another item.
#He enters "Playing soccer" into the to-do list

#The page updates again, and now shows both items on the list

#Will the site remember the list.
#The website generated a unique URL for her.
#There is some explanatory text to the generated URL

#He visits the URL and see the to do list stil there

#Statisfied, he goes back to sleep
if __name__=='__main__':
    unittest.main(warnings='ignore')