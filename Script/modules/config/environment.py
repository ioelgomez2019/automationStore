import os
import shutil
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    try:
        return webdriver.Chrome(options=options)
    except OSError as exc:
        if getattr(exc, "winerror", None) != 193:
            raise
        _clear_driver_cache()
        os.environ["WDM_ARCH"] = "x64"
        return webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )


def _clear_driver_cache():
    local_app = os.environ.get("LOCALAPPDATA", "")
    user_profile = os.environ.get("USERPROFILE", "")
    selenium_cache = Path(local_app) / "Selenium"
    wdm_cache = Path(user_profile) / ".wdm"

    for cache_path in (selenium_cache, wdm_cache):
        if cache_path.exists():
            shutil.rmtree(cache_path, ignore_errors=True)
