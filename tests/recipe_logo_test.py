import pytest
from pages import recipes_home


class TestRecipeLogo:

    @pytest.fixture
    def recipe_logo(self, driver):
        return recipes_home.Recipes(driver)

    def test_recipes_logo_styling(self, recipe_logo):
        assert(recipe_logo.page_furniture_present())
        assert recipe_logo.recipe_logo_css("height", "24px") == True
        assert recipe_logo.recipe_logo_css('font-weight', '300') == True
        assert recipe_logo.recipe_logo_css('width', '110') == True
        assert recipe_logo.recipe_logo_css('font-size', '32') == True
        assert recipe_logo.recipe_logo_css('font-family', 'Gill Sans') == True




