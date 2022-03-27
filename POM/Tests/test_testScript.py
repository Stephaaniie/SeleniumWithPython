import pytest

from Pages.homePage import HomePage

from Tests.baseTest import BaseTest

import time

class Test(BaseTest):

    def test_Algo(self):

        self.home=HomePage(self.driver)

        self.home.search("Búsqueda")

        time.sleep(10)