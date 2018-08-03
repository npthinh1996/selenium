from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class OdooTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox(executable_path="webdriver/firefox")
        self.driver.get("https://erp.mangoads.vn/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_shopHome(self):
        wait = self.wait
        driver = self.driver

        print("\nTest home:")
        print("- Check title ...")
        self.assertIn("Shop", driver.title)

        print("- Check logo ...")
        logo = wait.until(lambda driver: driver.find_element_by_css_selector("a.logo img"))
        self.assertIsNotNone(logo)

        print("- Check product ...")
        products = wait.until(lambda drive: driver.find_elements_by_class_name("oe_product"))
        for product in products:
            self.assertIsNotNone(product)
        if products:
            print(f" -> Total: {len(products)}")

    def test_sortHome(self):
        wait = self.wait
        driver = self.driver

        print("\nTest sort:")
        print("- Check title ...")
        self.assertIn("Shop", driver.title)

        print("- Sort ...")
        print(" + Catalog price: High to Low")
        sortBut = wait.until(lambda driver: driver.find_element_by_css_selector("div.dropdown_sorty_by"))
        sortBut.click()
        wait.until(lambda driver: driver.find_element_by_link_text("Catalog price: High to Low")).click()

        print(" + Catalog price: Low to High")
        sortBut = wait.until(lambda driver: driver.find_element_by_css_selector("div.dropdown_sorty_by"))
        sortBut.click()
        wait.until(lambda driver: driver.find_element_by_link_text("Catalog price: Low to High")).click()

        print(" + Name - A to Z")
        sortBut = wait.until(lambda driver: driver.find_element_by_css_selector("div.dropdown_sorty_by"))
        sortBut.click()
        wait.until(lambda driver: driver.find_element_by_link_text("Name - A to Z")).click()

        print(" + Name - Z to A")
        sortBut = wait.until(lambda driver: driver.find_element_by_css_selector("div.dropdown_sorty_by"))
        sortBut.click()
        wait.until(lambda driver: driver.find_element_by_link_text("Name - Z to A")).click()

        wait.until(lambda driver: driver.find_element_by_link_text("Shop")).click()

    def test_searchHome(self):
        wait = self.wait
        driver = self.driver

        print("\nTest search:")
        print("- Check title ...")
        self.assertIn("Shop", driver.title)

        print("- Input keyword ...")

        print(" + Search unavailable product ...")
        searchBox = wait.until(lambda driver: driver.find_element_by_css_selector("div.oe_search input"))
        searchBox.clear()
        searchBox.send_keys("test")
        wait.until(lambda driver: driver.find_element_by_xpath("//button[@class='btn btn-default oe_search_button']")).click()
        products = wait.until(lambda drive: driver.find_element_by_tag_name("h3"))
        self.assertEqual("No product defined.", products.text)

        print(" + Search available product ...")
        searchBox = wait.until(lambda driver: driver.find_element_by_css_selector("div.oe_search input"))
        searchBox.clear()
        searchBox.send_keys("ipod")
        wait.until(lambda driver: driver.find_element_by_xpath("//button[@class='btn btn-default oe_search_button']")).click()
        products = wait.until(lambda driver: driver.find_elements_by_class_name("oe_product"))
        for product in products:
            self.assertIsNotNone(product)
        if products:
            print(f" -> Total: {len(products)}")

        wait.until(lambda driver: driver.find_element_by_link_text("Shop")).click()

    def test_signIn(self):
        wait = self.wait
        driver = self.driver

        print("\nTest login:")
        wait.until(lambda driver: driver.find_element_by_xpath("//b[text() = 'Sign in']/..")).click()
        print("- Check title ...")
        self.assertIn("Login", driver.title)

        email = wait.until(lambda driver: driver.find_element_by_id("login"))
        # TODO: Enter email
        email.send_keys("..." + Keys.TAB)
        password = wait.until(lambda driver: driver.find_element_by_id("password"))
        # TODO: Enter password
        password.send_keys("...")
        print("- Login ...")
        wait.until(lambda driver: driver.find_element_by_xpath("//button[text() = 'Log in']")).click()
        print("- Check title ...")
        self.assertIn("Odoo", driver.title)

        print("- Logout ...")
        wait.until(lambda driver: driver.find_element_by_xpath("//span[text() = 'Administrator']/..")).click()
        wait.until(lambda driver: driver.find_element_by_xpath("//a[text() = 'Log out']")).click()
        self.assertIn("Login", driver.title)

        wait.until(lambda driver: driver.find_element_by_link_text("Shop")).click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
