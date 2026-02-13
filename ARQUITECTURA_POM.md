# 🏗️ ARQUITECTURA POM - EXPLICACIÓN COMPLETA

## 📖 ¿Qué es Page Object Model (POM)?

**POM** es un patrón de diseño que separa:
- **Elementos de la página** (localizadores) → En classes Page
- **Acciones sobre la página** (métodos) → En classes Page  
- **Lógica de prueba** (qué probar) → En archivos de test

## 🎯 ESTRUCTURA DEL PROYECTO:

```
pages/
├── base_page.py       ← Clase base con métodos comunes
└── login_page.py      ← Page Object específico del Login

tests/
└── test_login.py      ← Pruebas que usan los Page Objects

test_login_completo.py ← Test simple de login
```

---

## 📁 ARCHIVO 1: base_page.py (Clase Base)

**¿Para qué sirve?**
- Contiene métodos **comunes** a todas las páginas
- Evita repetir código
- Todas las páginas heredan de esta clase

**Métodos principales:**

```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Busca un elemento en la página"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Hace click en un elemento"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        """Ingresa texto en un campo"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        """Verifica si un elemento es visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
```

---

## 📁 ARCHIVO 2: login_page.py (Page Object)

**¿Para qué sirve?**
- Mapea todos los elementos de la página de login
- Agrupa las acciones que puedes hacer en esa página
- Encapsula los detalles técnicos

### Parte 1: MAPEO DE ELEMENTOS (Localizadores)

```python
class LoginPage(BasePage):
    # URL de la página
    URL = "https://www.saucedemo.com/"
    
    # 🏷️ LOCALIZADORES - Aquí mapeamos los elementos
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
```

**📖 Explicación:**
- `USERNAME_INPUT = (By.ID, "user-name")` 
  - **By.ID**: Tipo de localizador
  - **"user-name"**: Valor del localizador (el ID del elemento HTML)
  
**🔍 ¿Cómo obtuviste "user-name"?**
1. Abre https://www.saucedemo.com/
2. Presiona F12
3. Inspecciona el campo de usuario
4. Verás: `<input id="user-name" ...>`
5. Usa ese ID en tu localizador ✅

### Parte 2: ACCIONES (Métodos)

```python
    def open(self):
        """Abre la página de login"""
        self.driver.get(self.URL)
    
    def enter_username(self, username):
        """Ingresa el nombre de usuario"""
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Ingresa la contraseña"""
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Hace click en el botón de login"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Realiza el login completo"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
```

**📖 Explicación:**
- Cada método representa una **acción del usuario**
- Los métodos usan los **localizadores** definidos arriba
- Heredan métodos de `BasePage` (enter_text, click_element, etc.)

### Parte 3: VALIDACIONES (Verificaciones)

```python
    def is_login_successful(self):
        """Verifica si el login fue exitoso"""
        return self.is_element_visible(self.PRODUCTS_TITLE)
    
    def get_products_title(self):
        """Obtiene el título de la página de productos"""
        return self.get_text(self.PRODUCTS_TITLE)
    
    def is_error_message_displayed(self):
        """Verifica si hay mensaje de error"""
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def get_error_message(self):
        """Obtiene el texto del mensaje de error"""
        return self.get_text(self.ERROR_MESSAGE)
```

**📖 Explicación:**
- Métodos para **verificar** el estado de la página
- Usados en los tests para hacer assertions

---

## 📁 ARCHIVO 3: test_login_completo.py (Test)

**¿Para qué sirve?**
- Define QUÉ pruebas realizar
- Usa los Page Objects para interactuar con la página
- NO conoce los detalles técnicos (localizadores, waits, etc.)

```python
from selenium import webdriver
from pages.login_page import LoginPage

# 1. Abrir navegador
driver = webdriver.Chrome()

# 2. Crear instancia del Page Object
login_page = LoginPage(driver)

# 3. Usar el Page Object para hacer acciones
login_page.open()
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# 4. Verificar resultado
if login_page.is_login_successful():
    print("✅ Login exitoso!")
else:
    print("❌ Login falló")

# 5. Cerrar navegador
driver.quit()
```

**📖 Ventajas:**
- ✅ Código de test **muy legible**
- ✅ No repites localizadores
- ✅ Si cambia la UI, solo editas el Page Object
- ✅ El test permanece igual

---

## 🔄 FLUJO COMPLETO DE EJECUCIÓN:

### Ejemplo: `login_page.enter_username("standard_user")`

```
1. Test llama:
   login_page.enter_username("standard_user")
   
2. LoginPage.enter_username() ejecuta:
   self.enter_text(self.USERNAME_INPUT, "standard_user")
   
3. self.USERNAME_INPUT es:
   (By.ID, "user-name")
   
4. BasePage.enter_text() recibe:
   locator = (By.ID, "user-name")
   text = "standard_user"
   
5. BasePage.enter_text() hace:
   element = self.find_element((By.ID, "user-name"))
   element.clear()
   element.send_keys("standard_user")
   
6. find_element() usa WebDriverWait para:
   Esperar hasta que el elemento con ID "user-name" esté presente
   
7. Selenium busca en el HTML:
   <input id="user-name" ...>
   
8. Selenium escribe "standard_user" en ese campo ✅
```

---

## 🎯 ¿CÓMO AGREGAR UN NUEVO ELEMENTO?

### Ejemplo: Agregar el botón de "Cerrar Error"

#### Paso 1: Inspeccionar el elemento
```html
<!-- En Chrome DevTools verás: -->
<button class="error-button" data-test="error-button">❌</button>
```

#### Paso 2: Agregar localizador en login_page.py
```python
class LoginPage(BasePage):
    # Localizadores existentes...
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    
    # NUEVO localizador
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-test='error-button']")
```

#### Paso 3: Agregar método de acción
```python
    def click_error_close_button(self):
        """Cierra el mensaje de error"""
        self.click_element(self.ERROR_CLOSE_BUTTON)
```

#### Paso 4: Usar en el test
```python
# En test_login_completo.py
if login_page.is_error_message_displayed():
    print("Hay un error, cerrándolo...")
    login_page.click_error_close_button()
```

---

## 🎓 VENTAJAS DE POM:

### ✅ 1. Mantenibilidad
Si cambia el ID del campo usuario de `"user-name"` a `"username"`:
- **Sin POM:** Cambiar en TODOS los tests (10, 20, 50 archivos) 😱
- **Con POM:** Cambiar solo en `login_page.py` una vez ✅

```python
# Antes
USERNAME_INPUT = (By.ID, "user-name")

# Después (solo este cambio)
USERNAME_INPUT = (By.ID, "username")
```

### ✅ 2. Reutilización
El método `login()` se puede usar en 100 tests diferentes:

```python
# Test 1
login_page.login("standard_user", "secret_sauce")

# Test 2
login_page.login("problem_user", "secret_sauce")

# Test 3
login_page.login("locked_out_user", "secret_sauce")
```

### ✅ 3. Legibilidad
```python
# Sin POM - difícil de entender
driver.find_element(By.ID, "user-name").send_keys("usuario")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login-button").click()

# Con POM - se lee como lenguaje natural
login_page.enter_username("usuario")
login_page.enter_password("password")
login_page.click_login_button()
```

### ✅ 4. Separación de Responsabilidades
- **Page Objects:** Saben CÓMO hacer las cosas (detalles técnicos)
- **Tests:** Saben QUÉ probar (lógica de negocio)

---

## 📊 COMPARACIÓN: Con POM vs Sin POM

### Sin POM (Todo en un archivo):
```python
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # ❌ Localizadores repetidos en cada test
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    
    button = driver.find_element(By.ID, "login-button")
    button.click()
    
    # Si cambia el ID "user-name", hay que buscar en TODOS los tests
    driver.quit()
```

### Con POM (Estructurado):
```python
def test_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    
    # ✅ Métodos reutilizables y claros
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    assert login_page.is_login_successful()
    
    # Si cambia UI, solo editas login_page.py
    driver.quit()
```

---

## 🚀 CÓMO USAR TUS ARCHIVOS:

### 1. Test Simple de Login:
```bash
python test_login_completo.py
# O doble click en: run_login_completo.bat
```

Este test:
- ✅ Abre Chrome
- ✅ Va a SauceDemo
- ✅ Ingresa usuario y contraseña
- ✅ Hace click en Login
- ✅ Verifica si fue exitoso

### 2. Test con Múltiples Usuarios:
```bash
python test_multiples_usuarios.py
# O doble click en: run_multiples_usuarios.bat
```

Este test prueba:
- ✅ standard_user (exitoso)
- ✅ locked_out_user (bloqueado)
- ✅ usuario_invalido (error)
- ✅ problem_user (exitoso)

---

## 💡 RESUMEN:

1. **BasePage** → Métodos comunes (find_element, click, enter_text)
2. **LoginPage** → Mapea elementos + Acciones específicas de login
3. **Test** → Usa LoginPage para probar funcionalidad

**Flujo:**
```
Test → LoginPage → BasePage → Selenium → Chrome
```

**¿Por qué POM?**
- ✅ Fácil mantenimiento
- ✅ Código reutilizable
- ✅ Tests más legibles
- ✅ Cambios centralizados

---

## 📖 Archivos Creados para Ti:

| Archivo | Descripción |
|---------|-------------|
| **GUIA_MAPEO_ELEMENTOS.md** | Cómo identificar elementos con DevTools |
| **ARQUITECTURA_POM.md** | Este archivo - explicación completa |
| **test_login_completo.py** | Test funcionalhaciendo login real |
| **test_multiples_usuarios.py** | Prueba con 4 usuarios diferentes |

---

**🎯 Próximo Paso:**
Lee **[GUIA_MAPEO_ELEMENTOS.md](GUIA_MAPEO_ELEMENTOS.md)** para aprender a inspeccionar y mapear elementos de cualquier página web.

**Luego ejecuta:**
```bash
python test_login_completo.py
```

¡Ya tienes todo listo para hacer login con POM! 🚀
