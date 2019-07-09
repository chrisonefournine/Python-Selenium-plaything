import pytest
from pages import recipes_home


class TestNavigation:
    @pytest.fixture
    def recipes_home_nav(self, driver):
        return recipes_home.Recipes(driver)

    def test_navigation(self, recipes_home_nav):
        assert recipes_home_nav.page_title("Recipes - BBC Food") == True
        assert recipes_home_nav._element_count(recipes_home_nav._nav_bar, 13)
        recipes_home_nav._click(recipes_home_nav._nav_bar)
        assert recipes_home_nav.page_title("BBC - Food") == True

