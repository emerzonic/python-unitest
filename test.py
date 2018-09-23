import unittest
import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Todo_App_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://react-js-todolist.herokuapp.com")
        self.assertIn("React Todo App", driver.title)
        elem = driver.find_element_by_tag_name("h1")
        assert "TODO LIST" in driver.page_source
        username = driver.find_element_by_name("username").send_keys(config.username)
        password = driver.find_element_by_name("password").send_keys(config.password)
        submit = driver.find_element_by_class_name("button").click()



    def test_todos_creation(self):
        todos = ['Do the dishes', 'Make dinner', 'Do laundry']
        driver = self.driver
        driver.get("https://react-js-todolist.herokuapp.com")
        username = driver.find_element_by_name("username").send_keys(config.username)
        password = driver.find_element_by_name("password").send_keys(config.password)
        submit = driver.find_element_by_class_name("submit-button").click()
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "todoInput"))
            )
        finally:
            for todo in todos:
                todo_input = driver.find_element_by_class_name('todoInput')
                todo_input.send_keys(todo)
                todo_input.send_keys(Keys.RETURN)
                assert todo in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()