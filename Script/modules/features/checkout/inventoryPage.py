from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Script.modules.utils.loginUtils import BasePage


class InventoryPage(BasePage):
    
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def wait_for_page(self):
        """Verifica rápido si los elementos ya existen, sino espera"""
        try:
            # Intento rápido sin wait
            self.driver.find_element(*self.PRODUCTS_TITLE)
            self.driver.find_element(*self.INVENTORY_CONTAINER)
            if "inventory.html" in self.driver.current_url:
                return
        except Exception:
            pass
        
        # Si no están, usa wait (máximo una vez)
        self.find_element(self.PRODUCTS_TITLE)
        self.find_element(self.INVENTORY_CONTAINER)
        self.wait.until(lambda d: "inventory.html" in d.current_url)

    def wait_for_inventory(self):
        """Verifica rápido si hay items, sino espera"""
        elements = self.driver.find_elements(*self.INVENTORY_ITEM)
        if elements:
            return
        # Solo espera si no encontró
        self.find_element(self.INVENTORY_ITEM)

    def clear_cart(self):
        """Remueve todos los productos del carrito antes de empezar el test"""
        try:
            remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[data-test^='remove-']")
            for button in remove_buttons:
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                    button.click()
                    # Pequeña pausa para que el carrito se actualice
                    import time
                    time.sleep(0.3)
                except Exception:
                    pass
            print(f"✓ Carrito limpiado: {len(remove_buttons)} productos removidos")
        except Exception as e:
            print(f"⚠ No se pudo limpiar el carrito: {e}")

    def _find_add_button(self, product_name):
        product_ids = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket": "add-to-cart-sauce-labs-fleece-jacket",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
            "Test.allTheThings() T-Shirt (Red)": "add-to-cart-test.allthethings()-t-shirt-(red)",
        }

        if product_name in product_ids:
            button_id = product_ids[product_name]
            remove_id = button_id.replace("add-to-cart", "remove")
            
            # Intento super rápido: busca directamente sin wait
            try:
                # ¿Ya está agregado?
                self.driver.find_element(By.CSS_SELECTOR, f"button[data-test='{remove_id}']")
                return "already_added"
            except Exception:
                pass
            
            # Busca el botón add
            try:
                return self.driver.find_element(By.CSS_SELECTOR, f"button[data-test='{button_id}']")
            except Exception:
                pass
            
            try:
                return self.driver.find_element(By.ID, button_id)
            except Exception:
                pass

        # Fallback con XPath - búsqueda rápida sin wait primero
        xpath_add = (
            f"//div[contains(@class,'inventory_item_name') and normalize-space()='{product_name}']"
            f"/ancestor::div[@class='inventory_item_description']"
            f"//button[contains(@data-test,'add-to-cart')]"
        )
        xpath_remove = (
            f"//div[contains(@class,'inventory_item_name') and normalize-space()='{product_name}']"
            f"/ancestor::div[@class='inventory_item_description']"
            f"//button[contains(@data-test,'remove')]"
        )
        
        try:
            # Verifica rápido si tiene botón Remove
            remove_elements = self.driver.find_elements(By.XPATH, xpath_remove)
            if remove_elements and remove_elements[0].is_displayed():
                return "already_added"
            
            # Busca el botón Add
            add_elements = self.driver.find_elements(By.XPATH, xpath_add)
            if add_elements:
                return add_elements[0]
        except Exception:
            pass

        return None

    def _open_product_detail(self, product_name):
        link_xpath = "//div[@class='inventory_item_name' and normalize-space()=\"%s\"]" % product_name
        elements = self.driver.find_elements(By.XPATH, link_xpath)
        if elements:
            elements[0].click()
            return True
        return False

    def add_product_to_cart(self, product_name):
        self.wait_for_page()
        self.wait_for_inventory()
        if "inventory.html" not in self.driver.current_url:
            raise TimeoutException(f"Not on inventory page. URL: {self.driver.current_url}")
        
        # Si el producto ya está agregado, no es un error
        element = self._find_add_button(product_name)
        if element == "already_added":
            print(f"✓ Producto '{product_name}' ya estaba en el carrito")
            return
        
        if element is None:
            opened = self._open_product_detail(product_name)
            if opened:
                try:
                    button = self.find_element((By.XPATH, "//button[starts-with(@id,'add-to-cart') or contains(@data-test,'add-to-cart')]"))
                    button.click()
                    self.driver.back()
                    print(f"✓ Producto '{product_name}' agregado desde detalle")
                    return
                except Exception:
                    pass
            try:
                self.driver.save_screenshot(f"add_to_cart_not_found_{product_name}.png")
            except Exception:
                pass
            raise TimeoutException(
                f"Add to cart button not found: {product_name}. URL: {self.driver.current_url}"
            )
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
            print(f"✓ Producto '{product_name}' agregado al carrito")
        except Exception as e:
            self.driver.execute_script("arguments[0].click();", element)
            print(f"✓ Producto '{product_name}' agregado al carrito (JS click)")

    def open_cart(self):
        self.click_element(self.CART_LINK)