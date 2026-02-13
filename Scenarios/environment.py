from Script.modules.config.environment import create_driver


def before_all(context):
    context.config.setup_logging = True


def before_scenario(context, scenario):
    context.driver = create_driver()
    context.driver.implicitly_wait(10)
    context.driver.set_page_load_timeout(30)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
