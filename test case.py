import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class PythonOrgFullSiteTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")  # Uncomment to run headless
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.base_url = "https://www.python.org"
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.quit()

    # 1–14: Core Tests
    def test_homepage_loads(self):
        self.assertIn("Welcome to Python.org", self.driver.page_source)

    def test_title(self):
        self.assertIn("Python", self.driver.title)

    def test_logo_displayed(self):
        logo = self.driver.find_element(By.CSS_SELECTOR, ".python-logo")
        self.assertTrue(logo.is_displayed())

    def test_navigation_links(self):
        nav_items = ["About", "Downloads", "Documentation", "Community", "Success Stories", "News", "Events"]
        for item in nav_items:
            link = self.driver.find_element(By.LINK_TEXT, item)
            self.assertTrue(link.is_displayed(), f"{item} not visible in navbar")

    def test_search_bar(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("pandas")
        search_bar.send_keys(Keys.RETURN)
        self.assertIn("pandas", self.driver.page_source.lower())

    def test_footer_links(self):
        footer_links = [
            "Help", "Diversity", "Submit Website Bug", "Privacy Policy",
            "PSF Sponsor", "Contact", "Donate", "Community"
        ]
        for text in footer_links:
            link = self.driver.find_element(By.LINK_TEXT, text)
            self.assertTrue(link.is_displayed(), f"{text} not visible in footer")

    def test_downloads_page(self):
        self.driver.find_element(By.LINK_TEXT, "Downloads").click()
        self.assertIn("Download the latest version for", self.driver.page_source)

    def test_documentation_page(self):
        self.driver.find_element(By.LINK_TEXT, "Documentation").click()
        self.assertIn("Docs", self.driver.title)

    def test_community_page(self):
        self.driver.find_element(By.LINK_TEXT, "Community").click()
        self.assertIn("Community", self.driver.page_source)

    def test_about_page(self):
        self.driver.find_element(By.LINK_TEXT, "About").click()
        self.assertIn("Applications", self.driver.page_source)

    def test_news_page(self):
        self.driver.find_element(By.LINK_TEXT, "News").click()
        self.assertIn("Python News", self.driver.page_source)

    def test_events_page(self):
        self.driver.find_element(By.LINK_TEXT, "Events").click()
        self.assertIn("Upcoming Events", self.driver.page_source)

    def test_success_stories_page(self):
        self.driver.find_element(By.LINK_TEXT, "Success Stories").click()
        self.assertIn("Success Stories", self.driver.title)

    def test_responsive_layout(self):
        self.driver.set_window_size(375, 812)
        menu_button = self.driver.find_element(By.CLASS_NAME, "menu-button")
        self.assertTrue(menu_button.is_displayed())

    # 15–20: Extra Functional Tests
    def test_psf_donation_button(self):
        donate_link = self.driver.find_element(By.LINK_TEXT, "Donate")
        donate_link.click()
        self.assertIn("donate", self.driver.current_url.lower())

    def test_language_switcher_presence(self):
        lang_switcher = self.driver.find_element(By.ID, "language_switcher")
        self.assertTrue(lang_switcher.is_displayed())

    def test_social_icons(self):
        icons = self.driver.find_elements(By.CSS_SELECTOR, ".social-media ul li a")
        self.assertGreater(len(icons), 0)

    def test_become_member_text(self):
        self.driver.find_element(By.LINK_TEXT, "About").click()
        self.assertIn("Become a Member", self.driver.page_source)

    def test_psf_link_about(self):
        self.driver.find_element(By.LINK_TEXT, "About").click()
        self.driver.find_element(By.LINK_TEXT, "PSF").click()
        self.assertIn("Python Software Foundation", self.driver.page_source)

    def test_search_filter_exists(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("data")
        search_bar.send_keys(Keys.RETURN)
        filters = self.driver.find_elements(By.CLASS_NAME, "search-filter")
        self.assertTrue(any(f.is_displayed() for f in filters))

    # 21–30: Failing/Edge Cases
    def test_wrong_title(self):
        self.assertIn("Python", self.driver.title)

    def test_nonexistent_id(self):
        with self.assertRaises(Exception):
            self.driver.find_element(By.ID, "nonexistent-id")

    def test_about_wrong_text(self):
        self.driver.find_element(By.LINK_TEXT, "About").click()
        self.assertIn("C++ Foundation", self.driver.page_source)

    def test_empty_search_results(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("asdhaskdhakshdkahsdk")
        search_bar.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
        self.assertEqual(len(results), 0)

    def test_logo_absent(self):
        logo = self.driver.find_element(By.CSS_SELECTOR, ".python-logo")
        self.assertFalse(logo.is_displayed())

    def test_downloads_text_fail(self):
        self.driver.find_element(By.LINK_TEXT, "Downloads").click()
        self.assertIn("Download Python 1.4", self.driver.page_source)

    def test_mobile_menu_on_desktop(self):
        self.driver.set_window_size(1920, 1080)
        menu_button = self.driver.find_element(By.CLASS_NAME, "menu-button")
        self.assertTrue(menu_button.is_displayed())

    def test_nonexistent_link_click(self):
        with self.assertRaises(Exception):
            self.driver.find_element(By.LINK_TEXT, "Quantum Computing").click()

    def test_old_python_version_search(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("Python 2.5")
        search_bar.send_keys(Keys.RETURN)
        self.assertIn("Python 2.5", self.driver.page_source)

    def test_wrong_footer_content(self):
        footer = self.driver.find_element(By.ID, "site-map")
        self.assertIn("Copyright 2025", footer.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
