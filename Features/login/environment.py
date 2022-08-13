from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from behave import fixture, use_fixture, model

BEHAVE_DEBUG_ON_ERROR = False


# def selenium_browser_chrome(context):
#     context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     yield context.driver
#     context.driver.quit()
#
#
# def before_all(context):
#     use_fixture(selenium_browser_chrome, context)
#
#
# def before_feature(context, feature):
#     if 'browser' in feature.tags:
#         use_fixture(selenium_browser_chrome, context)


# def before_step(context):
#     use_fixture(selenium_browser_chrome, context)
#     BASE_URL = 'https://beta.flytoday.ir/'
#     context.driver.get(BASE_URL)
#     WebDriverWait(context.driver, 30)

# def before_feature(context):
#     # model.init(environment='test')
#     # if 'browser' in feature.tags:
#     use_fixture(selenium_driver_chrome, context)

#
# def setup_debug_on_error(userdata):
#     global BEHAVE_DEBUG_ON_ERROR
#     BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")
#
#
# def before_all(context):
#     setup_debug_on_error(context.config.userdata)
#
#
# def after_step(context, step):
#     if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
#         # -- ENTER DEBUGGER: Zoom in on failure location.
#         # NOTE: Use IPython debugger, same for pdb (basic python debugger).
#         import ipdb
#         ipdb.post_mortem(step.exc_traceback)