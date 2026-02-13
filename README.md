# 🚀 Proyecto de Automatización - Login SauceDemo

Proyecto de automatización de pruebas para el login de la página [SauceDemo](https://www.saucedemo.com/) utilizando **Selenium**, **Python** y el patrón de diseño **Page Object Model (POM)**.

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Cómo Ejecutar las Pruebas](#-cómo-ejecutar-las-pruebas)
- [Casos de Prueba](#-casos-de-prueba)
- [Patrón Page Object Model](#-patrón-page-object-model)
- [Usuarios de Prueba](#-usuarios-de-prueba)

## 📖 Descripción

Este proyecto automatiza las pruebas de login en SauceDemo, implementando buenas prácticas de automatización como:
- ✅ Patrón Page Object Model (POM)
- ✅ Separación de responsabilidades
- ✅ Código reutilizable y mantenible
- ✅ Gestión automática de drivers con WebDriver Manager
- ✅ Casos de prueba con unittest
- ✅ **BDD con Behave** (Features + Steps + Pages)

## 🏗️ Arquitectura del Proyecto

El proyecto utiliza el patrón **Page Object Model (POM)**, que separa la lógica de las pruebas de los elementos de la página, facilitando el mantenimiento y la reutilización del código.

```
┌─────────────────────────────────────┐
│         Test Layer                  │
│    (tests/test_login.py)           │
│  - Casos de prueba                 │
│  - Assertions                      │
└────────────┬────────────────────────┘
             │ Usa
             ▼
┌─────────────────────────────────────┐
│      Page Object Layer              │
│    (pages/login_page.py)           │
│  - Elementos de la página          │
│  - Acciones del usuario            │
└────────────┬────────────────────────┘
             │ Hereda de
             ▼
┌─────────────────────────────────────┐
│       Base Page Layer               │
│    (pages/base_page.py)            │
│  - Métodos comunes                 │
│  - Interacciones genéricas         │
└─────────────────────────────────────┘
```

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

1. **Python 3.8 o superior**
   - Verifica tu versión: `python --version`
   - Descarga desde: https://www.python.org/downloads/

2. **Google Chrome** (navegador)
   - El proyecto está configurado para usar Chrome
   - El driver se descarga automáticamente con WebDriver Manager

3. **pip** (gestor de paquetes de Python)
   - Viene incluido con Python
   - Verifica: `pip --version`

## 🔧 Instalación

Sigue estos pasos para configurar el proyecto:

### Paso 1: Clonar o descargar el proyecto
```bash
# Si tienes el repositorio
cd j:\Workspace\BANCOPICHINCHA\AutoTestStore
```

### Paso 2: Crear un entorno virtual (Opcional pero recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows
venv\Scripts\activate

# Activar entorno virtual en Linux/Mac
# source venv/bin/activate
```

### Paso 3: Instalar las dependencias
```bash
pip install -r requirements.txt
```

Esto instalará:
- `selenium`: Framework de automatización web
- `webdriver-manager`: Gestor automático de drivers
- `behave`: Framework BDD
- `pytest`: Framework de pruebas (opcional)
- `pytest-html`: Generador de reportes HTML (opcional)

### Paso 4: Verificar la instalación
```bash
python -c "import selenium; print(f'Selenium version: {selenium.__version__}')"
```

## 📁 Estructura del Proyecto

```
AutoTestStore/
│
├── features/                   # 🥒 Carpeta de BDD (Behave)
│   ├── steps/                  # Step Definitions
│   │   └── login_steps.py     # Implementación de pasos
│   ├── environment.py         # Configuración y hooks
│   └── login.feature          # Escenarios en Gherkin
│
├── pages/                      # Carpeta de Page Objects
│   ├── __init__.py            # Inicializador del módulo
│   ├── base_page.py           # Clase base con métodos comunes
│   └── login_page.py          # Page Object de la página de login
│
├── tests/                      # Carpeta de pruebas unittest
│   ├── __init__.py            # Inicializador del módulo
│   └── test_login.py          # Casos de prueba de login
│
├── reports/                    # Reportes generados
│
├── behave.ini                  # Configuración de Behave
├── pytest.ini                  # Configuración de pytest
├── requirements.txt            # Dependencias del proyecto
│
├── run_bdd_tests.bat          # 🥒 Ejecutar pruebas BDD
├── run_bdd_menu.bat           # 🥒 Menú BDD por tags
├── run_tests.bat              # 🧪 Ejecutar pruebas unittest
├── run_ejemplos.bat           # 🎯 Ejecutar ejemplos
│
├── INDEX.md                    # Índice de documentación
├── README.md                   # Este archivo
├── README_BDD.md              # Guía completa BDD
├── QUICKSTART.md              # Inicio rápido unittest
├── QUICKSTART_BDD.md          # Inicio rápido BDD
└── COMPARACION_BDD_vs_UNITTEST.md  # Comparación
```

## ▶️ Cómo Ejecutar las Pruebas

### 🥒 BDD con Behave (Recomendado)

#### Opción 1: Script de Ejecución Simple
```bash
# Doble click en el archivo o ejecutar:
run_bdd_tests.bat
```

#### Opción 2: Script con Menú Interactivo
```bash
# Ejecutar con opciones de filtrado por tags:
run_bdd_menu.bat
```

#### Opción 3: Línea de Comandos
```bash
# Ejecutar todas las features
behave

# Con formato bonito
behave --format pretty

# Solo smoke tests
behave --tags=@smoke

# Solo pruebas críticas
behave --tags=@critical

# Generar reporte HTML
behave -f html -o reports/behave_report.html
```

### 🧪 Unittest Tradicional

#### Opción 1: Con pytest (Recomendado)
```bash
# Desde la raíz del proyecto
python -m pytest tests/test_login.py -v
```

#### Opción 2: Con unittest
```bash
python -m unittest tests.test_login -v
```

#### Opción 3: Script de ejecución
```bash
run_tests.bat
```

## 🎬 Proceso de Ejecución - Paso a Paso

Cuando ejecutas una prueba, esto es lo que sucede:

### 1. **Inicialización (setUp)**
```python
✓ Se abre el navegador Chrome
✓ Se maximiza la ventana
✓ Se navega a https://www.saucedemo.com/
✓ Se inicializa el Page Object LoginPage
```

### 2. **Ejecución de la Prueba**
```python
✓ Se ingresan las credenciales (usuario y contraseña)
✓ Se hace clic en el botón "Login"
✓ Se realizan las validaciones (assertions)
```

### 3. **Finalización (tearDown)**
```python
✓ Se espera 2 segundos para visualizar el resultado
✓ Se cierra el navegador
```

## 🧪 Casos de Prueba

### Con BDD (Behave) - 8 Escenarios:

1. **Login exitoso con credenciales válidas** (@exitoso @critical)
2. **Login exitoso con usuario problem_user** (@exitoso)
3. **Login fallido con credenciales inválidas** (@error @negative)
4. **Login con usuario bloqueado** (@error @negative)
5. **Login sin ingresar nombre de usuario** (@validacion @negative)
6. **Login sin ingresar contraseña** (@validacion @negative)
7. **Login sin ingresar credenciales** (@validacion @negative)
8. **Esquema parametrizado con múltiples usuarios** (@parametrizado)

### Con Unittest - 5 Tests:

1. `test_login_exitoso_usuario_standard`
2. `test_login_con_metodo_completo`
3. `test_login_fallido_credenciales_invalidas`
4. `test_login_con_usuario_bloqueado`
5. `test_login_campos_vacios`

## 🎯 Patrón Page Object Model

### ¿Qué es POM?

El **Page Object Model** es un patrón de diseño que crea objetos para las páginas web, encapsulando:
- **Elementos de la página** (localizadores)
- **Acciones posibles** (métodos)

### Ventajas:
✅ **Mantenibilidad**: Si cambia la UI, solo modificas el Page Object  
✅ **Reutilización**: Los métodos se usan en múltiples pruebas  
✅ **Legibilidad**: El código de prueba es más claro  
✅ **Separación**: Lógica de prueba separada de los elementos  

### Estructura en este proyecto:

#### 1. **BasePage** (pages/base_page.py)
Clase base con métodos comunes:
- `find_element()`: Encuentra elementos
- `click_element()`: Hace click
- `enter_text()`: Ingresa texto
- `get_text()`: Obtiene texto
- `is_element_visible()`: Verifica visibilidad

#### 2. **LoginPage** (pages/login_page.py)
Extiende BasePage y define:
- **Localizadores**: USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON
- **Acciones**: enter_username(), enter_password(), click_login_button()
- **Validaciones**: is_login_successful(), get_error_message()

#### 3. **Tests** (tests/test_login.py o features/login.feature)
Usa los Page Objects para:
- Ejecutar acciones de usuario
- Validar resultados esperados
- No se preocupa por los localizadores

## 👥 Usuarios de Prueba

SauceDemo proporciona varios usuarios para pruebas:

| Usuario | Contraseña | Comportamiento |
|---------|-----------|----------------|
| standard_user | secret_sauce | ✅ Usuario normal, funciona correctamente |
| locked_out_user | secret_sauce | 🔒 Usuario bloqueado |
| problem_user | secret_sauce | ⚠️ Usuario con problemas en imágenes |
| performance_glitch_user | secret_sauce | 🐌 Usuario con delays |
| error_user | secret_sauce | ❌ Usuario con errores |
| visual_user | secret_sauce | 👁️ Usuario para pruebas visuales |

## 🔍 Ejemplo de Uso del Código

### Ejecutar un login simple:

```python
from selenium import webdriver
from pages.login_page import LoginPage

# Crear driver
driver = webdriver.Chrome()

# Crear instancia de LoginPage
login_page = LoginPage(driver)

# Abrir la página
login_page.open()

# Realizar login
login_page.login("standard_user", "secret_sauce")

# Verificar éxito
if login_page.is_login_successful():
    print("¡Login exitoso!")

# Cerrar navegador
driver.quit()
```

## 📊 Salida de Ejemplo

### Con BDD (Behave):
```
=== Iniciando Suite de Pruebas BDD ===

Feature: Login en SauceDemo

  Scenario: Login exitoso
    Given que el usuario está en la página de login ... passed
    When el usuario ingresa el nombre de usuario "standard_user" ... passed
    And el usuario ingresa la contraseña "secret_sauce" ... passed
    And el usuario hace clic en el botón de login ... passed
    Then el usuario debería ver la página de productos ... passed

✅ Escenario PASÓ
```

### Con Unittest:
```
=== Iniciando Suite de Pruebas de Login ===

--- Iniciando prueba: test_login_exitoso_usuario_standard ---
Abriendo el navegador Chrome...
Navegando a: https://www.saucedemo.com/

1. Ingresando credenciales válidas...
   Usuario: standard_user
   Contraseña: secret_sauce
2. Haciendo click en el botón de Login...
3. Verificando que el login fue exitoso...
4. Título encontrado: 'PRODUCTS'
5. URL actual: https://www.saucedemo.com/inventory.html
✓ Prueba exitosa: Login realizado correctamente
--- Finalizando prueba: test_login_exitoso_usuario_standard ---
Cerrando el navegador...
```

## 🛠️ Personalización

### Ejecutar en modo headless (sin interfaz gráfica):

Edita `tests/test_login.py` o `features/environment.py` y descomenta:
```python
chrome_options.add_argument("--headless")
```

### Cambiar el tiempo de espera:

Edita `pages/base_page.py`:
```python
self.wait = WebDriverWait(driver, 20)  # Cambiar de 10 a 20 segundos
```

### Usar otro navegador (Firefox):

```python
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

self.driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install()
)
```

## ❓ Solución de Problemas

### Error: "chromedriver no encontrado"
- **Solución**: WebDriver Manager lo descarga automáticamente. Verifica tu conexión a internet.

### Error: "No module named 'selenium'"
- **Solución**: Instala las dependencias: `pip install -r requirements.txt`

### El navegador se cierra demasiado rápido
- **Solución**: Aumenta el `time.sleep()` en el método `tearDown()` o `after_scenario()`

### Error: "element not found"
- **Solución**: Verifica que la página cargó correctamente. Aumenta los timeouts.

### Error: "No steps matched" (Behave)
- **Solución**: Verifica que el texto en el .feature coincida exactamente con los @given/@when/@then

## 🆚 BDD vs Unittest

Este proyecto incluye **ambos enfoques**:

| Aspecto | BDD (Behave) | Unittest |
|---------|--------------|----------|
| **Legibilidad** | ✅✅✅ Alta | ⚠️ Media |
| **Colaboración** | ✅ Todo el equipo | ⚠️ Solo técnicos |
| **Documentación** | ✅ Auto-documentado | ❌ Requiere docs |
| **Debugging** | ⚠️ Más complejo | ✅ Más simple |

📖 Ver **[COMPARACION_BDD_vs_UNITTEST.md](COMPARACION_BDD_vs_UNITTEST.md)** para detalles completos.

## 📚 Recursos Adicionales

- [Documentación oficial de Selenium](https://www.selenium.dev/documentation/)
- [Behave Documentation](https://behave.readthedocs.io/)
- [SauceDemo - Página de prueba](https://www.saucedemo.com/)
- [Page Object Model - Martin Fowler](https://martinfowler.com/bliki/PageObject.html)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## 📝 Notas Finales

- Las pruebas están diseñadas para ejecutarse de forma independiente
- Cada prueba abre y cierra su propio navegador
- Los tiempos de espera (`time.sleep()`) son para visualización y pueden ajustarse
- El proyecto usa WebDriver Manager para gestionar automáticamente los drivers

## 🚀 Inicio Rápido

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar pruebas BDD
behave

# O ejecutar pruebas unittest
python -m pytest tests/ -v

# 3. Ver reportes
start reports/behave_report.html
```

## 📖 Documentación Adicional

- **[INDEX.md](INDEX.md)** - Índice de toda la documentación
- **[QUICKSTART_BDD.md](QUICKSTART_BDD.md)** - Inicio rápido BDD
- **[README_BDD.md](README_BDD.md)** - Guía completa BDD
- **[COMPARACION_BDD_vs_UNITTEST.md](COMPARACION_BDD_vs_UNITTEST.md)** - Comparación detallada

---

**¡Feliz Testing! 🎉**

Si tienes preguntas o encuentras problemas, revisa la sección de solución de problemas o consulta la documentación oficial de Selenium y Behave.
# automationStore
