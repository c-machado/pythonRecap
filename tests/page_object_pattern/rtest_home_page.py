"""
Description: Test module for module src/page_object_patter/base_page.py

@author: Paul Bodean
@date: 25/07/2017
"""

from src.page_object_pattern.home_page import HomePage
from src.page_object_pattern.test_template import TestTemplate
import unittest


class TestHomePage(TestTemplate):
    """
    Check page functionality
    """

    def test_buttons_available(self):
        """
        Check Home page buttons are displayed
        """
        main_page = (self.driver)
        assert main_page.check_create_account()
        assert main_page.check_login()
        assert main_page.check_search()

    def test_buttons_click(self):
        """
        Click on home page buttons
        """
        main_page = HomePage(self.driver)
        main_page.login()
        main_page.search()



if __name__ == '__main__':
    unittest.main()
