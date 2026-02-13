# 🥒 Guía BDD - Behavior Driven Development

## 📖 ¿Qué es BDD?

**BDD (Behavior Driven Development)** es una metodología de desarrollo que se enfoca en el comportamiento del sistema desde la perspectiva del usuario. Utiliza un lenguaje natural (Gherkin) para describir escenarios de prueba que pueden ser entendidos por todos los miembros del equipo: desarrolladores, testers, analistas y stakeholders.

## 🎯 Arquitectura del Proyecto BDD

```
AutoTestStore/
│
├── features/                       # 📁 Carpeta principal de BDD
│   ├── steps/                      # 📁 Step Definitions
│   │   └── login_steps.py         # 🐍 Implementación de pasos
│   ├── environment.py             # ⚙️  Configuración y hooks de Behave
│   └── login.feature              # 🥒 Escenarios en Gherkin
│
├── pages/                          # 📁 Page Object Model
│   ├── base_page.py               # 📄 Clase base
│   └── login_page.py              # 📄 Page Object del login
│
├── reports/                        # 📊 Reportes generados
│
├── tests/                          # 🧪 Pruebas unittest (alternativo)
│
├── behave.ini                      # ⚙️  Configuración de Behave
├── requirements.txt                # 📦 Dependencias
├── run_bdd_tests.bat              # 🚀 Script ejecución simple
└── run_bdd_menu.bat               # 🎛️  Script ejecución con menú
```

## 🔄 Flujo de Trabajo BDD

```
┌─────────────────────────────────────────────────────────┐
│  1. FEATURE FILE (.feature)                            │
│     Escenarios en lenguaje Gherkin                     │
│     "Dado... Cuando... Entonces..."                    │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  2. STEP DEFINITIONS (login_steps.py)                  │
│     Implementación Python de cada paso                 │
│     @given, @when, @then                               │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  3. PAGE OBJECTS (login_page.py)                       │
│     Interacción con elementos de la página            │
│     Métodos reutilizables                              │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│  4. SELENIUM                                            │
│     Automatización del navegador                        │
└─────────────────────────────────────────────────────────┘
```

## 📝 Lenguaje Gherkin

Gherkin utiliza palabras clave en español:

| Palabra | Uso | Ejemplo |
|---------|-----|---------|
| **Característica** | Define una funcionalidad | `Característica: Login en SauceDemo` |
| **Antecedentes** | Pasos comunes a todos los escenarios | `Antecedentes: Dado que...` |
| **Escenario** | Un caso de prueba específico | `Escenario: Login exitoso` |
| **Dado** (Given) | Precondición inicial | `Dado que el usuario está en la página` |
| **Cuando** (When) | Acción del usuario | `Cuando ingresa sus credenciales` |
| **Y** (And) | Paso adicional | `Y hace clic en login` |
| **Entonces** (Then) | Resultado esperado | `Entonces ve la página de productos` |
| **Esquema del escenario** | Escenarios parametrizados | Para ejecutar con múltiples datos |
| **Ejemplos** | Tabla de datos para esquemas | Valores de prueba |

## 🚀 Cómo Ejecutar las Pruebas BDD

### Opción 1: Script de Ejecución Simple (Recomendado)

```bash
# Doble click en el archivo o ejecutar:
run_bdd_tests.bat
```

### Opción 2: Script con Menú Interactivo

```bash
# Ejecutar con opciones de filtrado por tags:
run_bdd_menu.bat
```

Opciones del menú:
- **1**: Todas las pruebas
- **2**: Solo pruebas de smoke (`@smoke`)
- **3**: Solo pruebas exitosas (`@exitoso`)
- **4**: Solo pruebas de error (`@error`)
- **5**: Solo pruebas críticas (`@critical`)
- **6**: Generar reporte HTML
- **7**: Salir

### Opción 3: Línea de Comandos (Avanzado)

#### Ejecutar todas las features:
```bash
behave features/
```

#### Ejecutar con formato bonito:
```bash
behave features/ --format pretty
```

#### Ejecutar escenarios con tags específicos:
```bash
# Solo pruebas de smoke
behave features/ --tags=@smoke

# Solo pruebas exitosas
behave features/ --tags=@exitoso

# Solo pruebas de error
behave features/ --tags=@error

# Pruebas críticas
behave features/ --tags=@critical

# Combinación de tags (AND)
behave features/ --tags=@login --tags=@critical

# Combinación de tags (OR)
behave features/ --tags=@smoke,@critical

# Excluir tags
behave features/ --tags=~@wip
```

#### Ejecutar un feature específico:
```bash
behave features/login.feature
```

#### Ejecutar un escenario específico por número de línea:
```bash
behave features/login.feature:12
```

#### Generar reporte HTML:
```bash
behave features/ --format html --outfile reports/behave_report.html
```

#### Generar reporte JSON:
```bash
behave features/ --format json --outfile reports/behave_report.json
```

#### Ejecutar en modo dry-run (sin ejecutar):
```bash
behave features/ --dry-run
```

#### Mostrar steps disponibles:
```bash
behave --steps
```

#### Modo verbose (detallado):
```bash
behave features/ --verbose
```

## 🏷️ Sistema de Tags

Los tags permiten categorizar y ejecutar escenarios específicos:

### Tags Implementados:

| Tag | Descripción | Uso |
|-----|-------------|-----|
| `@login` | Todas las pruebas de login | Categorización general |
| `@smoke` | Pruebas de humo rápidas | Validación básica rápida |
| `@critical` | Pruebas críticas | Funcionalidad esencial |
| `@exitoso` | Casos de login exitoso | Flujos positivos |
| `@error` | Casos de error esperado | Flujos negativos |
| `@negative` | Pruebas negativas | Validaciones de error |
| `@validacion` | Validaciones de campos | Validaciones de entrada |
| `@parametrizado` | Escenarios con múltiples datos | Data-driven testing |

### Cómo Usar Tags:

```bash
# Ejecutar solo smoke tests
behave --tags=@smoke

# Ejecutar pruebas críticas
behave --tags=@critical

# Ejecutar login Y exitoso
behave --tags=@login --tags=@exitoso

# Ejecutar smoke O critical
behave --tags=@smoke,@critical

# Excluir pruebas en desarrollo
behave --tags=~@wip
```

## 📊 Estructura de un Feature File

### Ejemplo Completo:

```gherkin
# language: es
@login @smoke
Característica: Login en SauceDemo
  Como usuario de SauceDemo
  Quiero poder iniciar sesión
  Para acceder al sistema

  Antecedentes:
    Dado que el usuario está en la página de login

  @exitoso @critical
  Escenario: Login exitoso
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver la página de productos
    Y el título de la página debería ser "PRODUCTS"

  @error @negative
  Escenario: Login con credenciales inválidas
    Cuando el usuario ingresa el nombre de usuario "invalido"
    Y el usuario ingresa la contraseña "incorrecta"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debería ver un mensaje de error

  @parametrizado
  Esquema del escenario: Login con múltiples usuarios
    Cuando el usuario ingresa el nombre de usuario "<usuario>"
    Y el usuario ingresa la contraseña "<password>"
    Y el usuario hace clic en el botón de login
    Entonces el resultado debería ser "<resultado>"

    Ejemplos:
      | usuario       | password     | resultado |
      | standard_user | secret_sauce | exitoso   |
      | locked_out   | secret_sauce | error     |
```

## 🔧 Estructura de Step Definitions

### Ejemplo de Steps:

```python
from behave import given, when, then

@given('que el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('el usuario ingresa el nombre de usuario "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@then('el usuario debería ver la página de productos')
def step_impl(context):
    assert context.login_page.is_login_successful()
```

### Decoradores Disponibles:

- `@given` - Precondiciones
- `@when` - Acciones
- `@then` - Verificaciones
- `@step` - Cualquier tipo de paso

## ⚙️ Archivo Environment.py

El archivo `environment.py` contiene **hooks** que se ejecutan en momentos específicos:

### Hooks Disponibles:

| Hook | Cuándo se ejecuta |
|------|-------------------|
| `before_all(context)` | Una vez antes de todas las pruebas |
| `before_feature(context, feature)` | Antes de cada feature |
| `before_scenario(context, scenario)` | Antes de cada escenario |
| `before_step(context, step)` | Antes de cada paso |
| `after_step(context, step)` | Después de cada paso |
| `after_scenario(context, scenario)` | Después de cada escenario |
| `after_feature(context, feature)` | Después de cada feature |
| `after_all(context)` | Una vez después de todas las pruebas |

### Ejemplo de uso:

```python
def before_scenario(context, scenario):
    # Inicializar navegador
    context.driver = webdriver.Chrome()
    
def after_scenario(context, scenario):
    # Cerrar navegador
    context.driver.quit()
```

## 📈 Reportes

### Reporte por consola (Pretty):
```bash
behave --format pretty
```

**Salida:**
```
Feature: Login en SauceDemo

  Scenario: Login exitoso
    Given que el usuario está en la página de login ... passed
    When el usuario ingresa el nombre de usuario "standard_user" ... passed
    And el usuario ingresa la contraseña "secret_sauce" ... passed
    And el usuario hace clic en el botón de login ... passed
    Then el usuario debería ver la página de productos ... passed
```

### Reporte HTML:
```bash
behave --format html --outfile reports/report.html
```

### Reporte JSON:
```bash
behave --format json --outfile reports/report.json
```

### Reporte JUnit (para CI/CD):
```bash
behave --junit --junit-directory reports/junit
```

## 🎓 Mejores Prácticas BDD

### ✅ DO (Hacer):

1. **Escribir escenarios legibles** - Que cualquiera pueda entenderlos
2. **Usar lenguaje de negocio** - No términos técnicos en features
3. **Mantener escenarios independientes** - Cada uno debe poder ejecutarse solo
4. **Reutilizar steps** - Un step puede usarse en múltiples escenarios
5. **Usar tags apropiados** - Para organizar y filtrar pruebas
6. **Mantener features pequeños** - Un feature por funcionalidad
7. **Usar Antecedentes** - Para pasos comunes a todos los escenarios
8. **Parámetros en steps** - Para hacer steps reutilizables

### ❌ DON'T (No hacer):

1. **No poner detalles técnicos** en los features
2. **No escribir escenarios muy largos** - Máximo 10 pasos
3. **No repetir código** - Usar Page Objects
4. **No hacer escenarios dependientes** - Cada uno debe ser independiente
5. **No omitir validaciones** - Siempre verificar el resultado
6. **No usar valores hardcodeados** innecesariamente

## 🔍 Ejemplo Práctico Completo

### 1. Feature (login.feature):
```gherkin
# language: es
@login
Escenario: Login exitoso
  Dado que el usuario está en la página de login
  Cuando el usuario ingresa el nombre de usuario "standard_user"
  Y el usuario ingresa la contraseña "secret_sauce"
  Y el usuario hace clic en el botón de login
  Entonces el usuario debería ver la página de productos
```

### 2. Step Definition (login_steps.py):
```python
from behave import given, when, then

@given('que el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('el usuario ingresa el nombre de usuario "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('el usuario ingresa la contraseña "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('el usuario hace clic en el botón de login')
def step_impl(context):
    context.login_page.click_login_button()

@then('el usuario debería ver la página de productos')
def step_impl(context):
    assert context.login_page.is_login_successful()
```

### 3. Page Object (login_page.py):
```python
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
```

### 4. Environment (environment.py):
```python
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
    context.driver.quit()
```

## 🆚 BDD vs Unittest

| Aspecto | BDD (Behave) | Unittest |
|---------|--------------|----------|
| **Lenguaje** | Gherkin (natural) | Python puro |
| **Legibilidad** | Alta - cualquiera puede leer | Media - requiere conocer Python |
| **Colaboración** | Excelente para todo el equipo | Solo para desarrolladores |
| **Mantenimiento** | Features separados de código | Todo en archivos .py |
| **Documentación** | Features son documentación viva | Requiere comentarios |
| **Reportes** | Múltiples formatos nativos | Requiere plugins |
| **Parametrización** | Esquema del escenario + Ejemplos | @parameterized o loops |

## 📚 Recursos Adicionales

- **Behave Documentación**: https://behave.readthedocs.io/
- **Gherkin Syntax**: https://cucumber.io/docs/gherkin/
- **Cucumber School**: https://school.cucumber.io/
- **BDD Best Practices**: https://cucumber.io/docs/bdd/

## 🎯 Comandos Rápidos

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas
behave

# Ejecutar con tags
behave --tags=@smoke

# Generar reporte HTML
behave -f html -o reports/report.html

# Modo dry-run
behave --dry-run

# Ver steps disponibles
behave --steps

# Ejecutar feature específico
behave features/login.feature

# Ejecutar escenario por línea
behave features/login.feature:15
```

## ❓ Troubleshooting

### Problema: "No steps matched"
**Solución**: Verifica que el texto en el .feature coincida exactamente con el @given/@when/@then

### Problema: "No module named 'behave'"
**Solución**: `pip install behave`

### Problema: El navegador no se cierra
**Solución**: Verifica que `after_scenario` esté implementado correctamente en environment.py

### Problema: "Step implementation not found"
**Solución**: Asegúrate de que los archivos de steps estén en `features/steps/`

---

**¡Happy BDD Testing! 🥒🚀**
