import pytest
from selenium import webdriver
import os
from tests import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default='http://the-internet.herokuapp.com',
                     help="base url for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="the name of the browser you want to test with")
    parser.addoption("--host",
                     action="store",
                     default="browserstack",
                     help="local host or browserstack")
    parser.addoption("--browserversion",
                     action="store",
                     default="53.0",
                     help="the version of the browser you want to test with")
    parser.addoption("--os",
                     action="store",
                     default="Windows",
                     help="the OS you want to test with")
    parser.addoption("--osversion",
                     action="store",
                     default="10",
                     help="the OS version you want to test with")
    parser.addoption("--resolution",
                     action="store",
                     default="1600x1200",
                     help="the screen resolution you want to test with")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     grab the test outcome and store the result
#     add the result for each phase of a call ("setup", "call", and "teardown")
#     as an attribute to the request.node object in a fixture
#     e.g.,
#         request.node.result_call.failed
#         request.node.result_call.passed
#     """
#     outcome = yield
#     result = outcome.get_result()
#     setattr(item, "result_" + result.when, result)


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    config.host = request.config.getoption("--host").lower()
    config.browserversion = request.config.getoption("--browserversion").lower()
    config.os = request.config.getoption("--os").lower()
    config.osversion = request.config.getoption("--osversion")
    config.resolution = request.config.getoption("--resolution")

    if config.host == "browserstack":
        _desired_caps = {}
        _desired_caps["browser"] = config.browser
        _desired_caps["browser_version"] = config.browserversion
        _desired_caps["os"] = config.os
        _desired_caps["os_version"] = config.osversion
        _desired_caps["resolution"] = config.resolution
        _desired_caps["project"] = "Selenium Playground"
        _desired_caps["name"] = request.cls.__name__ + "." + request.function.__name__
        _url = "http://chrisharris20:wptzYxQAL2ZsLYtCuzaq@hub.browserstack.com:80/wd/hub"
        driver_ = webdriver.Remote(_url, _desired_caps)
    elif config.host == "localhost":
        if config.browser == "firefox":
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver 3')
            driver_ = webdriver.Firefox(executable_path=_geckodriver)
        elif config.browser == "chrome":
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
            driver_ = webdriver.Chrome(_chromedriver)

    #def quit():
    #     try:
    #         if config.host == "browserstack":
    #             yield
    #             if request.node.result_call.failed:
    #                 driver_.execute_script("BS:Job-Result=Failed")
    #             elif request.node.result_call.passed:
    #                 driver_.execute_script("BS:Job-result=Passed")
    #    finally:
    #   driver_.quit()
    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_
