import pytest
from pages import recipes_home


class TestRecipePage:
    @pytest.fixture
    def recipes_home_page(self, driver):
        return recipes_home.Recipes(driver)

    def test_collections(self, recipes_home_page):
        assert recipes_home_page.page_title("BBC Food - Recipes") == True
        assert recipes_home_page._element_count(recipes_home_page._collections, 7)
        assert recipes_home_page._collections_hero_css("font-family", "reithsans")
        assert recipes_home_page._collections_hero_css("font-weight", "400")
        assert recipes_home_page._collections_hero_css("font-size", "16")
        assert recipes_home_page._collections_hero_css("line-height", "20")
        assert recipes_home_page._collections_hero_css("text-align", "left")
        'assert recipes_home_page._collections_hero_css("height", "462")'
        'assert recipes_home_page._collections_hero_css("width", "842")'
        recipes_home_page._click(recipes_home_page._collections_hero)
        assert recipes_home_page.page_title("BBC Food - Recipes") == False

    def test_cookWith(self, recipes_home_page):
        assert recipes_home_page.page_title("BBC Food - Recipes") == True
        assert recipes_home_page._element_count(recipes_home_page._cook_with, 12)
        assert recipes_home_page._verify_css_value(recipes_home_page._cook_with_text,"font-family", "ReithSans")
        assert recipes_home_page._verify_css_value(recipes_home_page._cook_with_text,"font-weight", "700")
        assert recipes_home_page._verify_css_value(recipes_home_page._cook_with_text,"font-size", "16")
        assert recipes_home_page._cook_with_css("line-height", "20")
        assert recipes_home_page._cook_with_css("text-align", "left")
        'assert recipes_home_page._collections_hero_css("height", "462")'
        'assert recipes_home_page._collections_hero_css("width", "842")'
        recipes_home_page._click(recipes_home_page._cook_with_first)
        assert recipes_home_page.page_title("BBC Food - Recipes") == False

    def test_allTime(self, recipes_home_page):
        assert recipes_home_page.page_title("BBC Food - Recipes") == True
        assert recipes_home_page._element_count(recipes_home_page._favourite_dishes, 7)
        assert recipes_home_page._verify_css_value(recipes_home_page._favourite_dishes,"font-family", "ReithSans")
        assert recipes_home_page._verify_css_value(recipes_home_page._favourite_dishes,"font-weight", "400")
        assert recipes_home_page._verify_css_value(recipes_home_page._favourite_dishes,"font-size", "16")
        assert recipes_home_page._verify_css_value(recipes_home_page._favourite_dishes,"line-height", "20")
        assert recipes_home_page._verify_css_value(recipes_home_page._favourite_dishes,"text-align", "left")
        'assert recipes_home_page._collections_hero_css("height", "462")'
        'assert recipes_home_page._collections_hero_css("width", "842")'
        recipes_home_page._click(recipes_home_page._favourite_dishes)
        assert recipes_home_page.page_title("BBC Food - Recipes") == False
