from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Recipes(BasePage):
    _recipe_logo = {"by": By.CSS_SELECTOR, "value": "span.page-title__text"}
    _banner = {"by": By.CSS_SELECTOR, "value": "div[class^='food-body'"}
    _food_logo = {"by": By.CSS_SELECTOR, "value": "a[class^='page-title']"}
    _nav_bar = {"by": By.XPATH, "value": "//li[contains(@class,'main-menu')]"}
    _nav_home = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--index']"}
    _nav_recipes = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--recipes']"}
    _nav_chef = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--chefs']"}
    _nav_diets = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--diets']"}
    _nav_programmes = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--programmes']"}
    _nav_ingredients = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--ingredients']"}
    _nav_techniques = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--techniques']"}
    _nav_favourites = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--favourites']"}
    _nav_seasons = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--seasons']"}
    _nav_occasions = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--occasions']"}
    _nav_dishes = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--dishes']"}
    _nav_cuisines = {"by": By.CSS_SELECTOR, "value": "li[class*='main-menu__item--cuisines']"}
    _collections = {"by": By.CSS_SELECTOR, "value": "img[class*='promo__image']"}
    _collections_hero = {"by": By.CSS_SELECTOR, "value": "div[class*='item gel-1/1']"}
    _collections_standard = {"by": By.CSS_SELECTOR, "value": "div[class*='item gel-1/2']"}
    _cook_with = {"by": By.CSS_SELECTOR, "value": "div[class='cooking-with__ingredient']"}
    _cook_with_first = {"by": By.CSS_SELECTOR, "value": "div.cooking-with__ingredients > div:nth-child(1)"}
    _cook_with_text = {"by": By.CSS_SELECTOR, "value": "div[class*='cooking-with__title']"}
    _favourite_dishes = {"by": By.CSS_SELECTOR, "value": "div[class*='favourite-dishes__dish']"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/recipes")
        self._wait_for_is_displayed(self._food_logo, 3)
        assert self._is_displayed(self._food_logo)

    def page_title(self, page_title):
        return self._page_title(page_title)

    def page_furniture_present(self):
        self._wait_for_is_displayed(self._banner, 1)
        self._wait_for_is_displayed(self._recipe_logo, 1)
        return self._is_displayed(self._recipe_logo)

    def recipe_logo_css(self, attribute, value):
        return self._verify_css_value(self._recipe_logo, attribute, value)

    def _collections_hero_css(self, attribute, value):
        return self._verify_css_value(self._collections_hero, attribute, value)

    def _cook_with_css(self, attribute, value):
        return self._verify_css_value(self._cook_with, attribute, value)



