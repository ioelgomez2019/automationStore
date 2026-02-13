from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_all(context):
    context.config.setup_logging = True


def before_feature(context, feature):
    print(f"\nFeature: {feature.name}")
    print("-" * 70)


def before_scenario(context, scenario):
    print(f"\nEscenario: {scenario.name}")
    print("-" * 70)
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    context.driver.implicitly_wait(10)
    context.driver.set_page_load_timeout(30)


def after_scenario(context, scenario):
    print("\n" + "-" * 70)
    
    if scenario.status == "passed":
        print(f"Escenario PASO: {scenario.name}")
    elif scenario.status == "failed":
        print(f"Escenario FALLO: {scenario.name}")
        if hasattr(context, 'driver'):
            try:
                screenshot_name = f"screenshot_{scenario.name.replace(' ', '_')}.png"
                context.driver.save_screenshot(screenshot_name)
                print(f"Screenshot guardado: {screenshot_name}")
            except Exception as e:
                print(f"No se pudo guardar el screenshot: {e}")
    elif scenario.status == "skipped":
        print(f"Escenario OMITIDO: {scenario.name}")
    
    time.sleep(2)
    
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
