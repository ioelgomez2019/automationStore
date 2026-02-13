# 🚀 GUÍA RÁPIDA - BDD con Behave

## ⚡ Instalación Rápida

```bash
cd j:\Workspace\BANCOPICHINCHA\AutoTestStore
pip install -r requirements.txt
```

## 🎯 Ejecutar Pruebas BDD

### Opción 1: Doble Click (Más Fácil)
```
► Doble click en: run_bdd_tests.bat
```

### Opción 2: Menú Interactivo
```
► Doble click en: run_bdd_menu.bat

Opciones:
1. Todas las pruebas
2. Solo smoke tests
3. Solo pruebas exitosas
4. Solo pruebas de error
5. Solo pruebas críticas
6. Generar reporte HTML
```

### Opción 3: Línea de Comandos
```bash
# Todas las pruebas
behave

# Con formato bonito
behave --format pretty

# Solo smoke tests
behave --tags=@smoke

# Generar reporte HTML
behave -f html -o reports/report.html
```

## 📁 Estructura del Proyecto

```
AutoTestStore/
├── features/              ← Archivos BDD
│   ├── steps/
│   │   └── login_steps.py    ← Step definitions (Python)
│   ├── environment.py         ← Configuración Behave
│   └── login.feature          ← Escenarios (Gherkin)
│
├── pages/                 ← Page Objects
│   ├── base_page.py
│   └── login_page.py
│
└── tests/                 ← Pruebas Unittest (alternativo)
```

## 📝 ¿Qué es qué?

| Archivo | Descripción |
|---------|-------------|
| **login.feature** | Escenarios en lenguaje natural (Gherkin) |
| **login_steps.py** | Código Python que ejecuta cada paso |
| **environment.py** | Configuración (abrir/cerrar navegador) |
| **login_page.py** | Interacción con elementos de la página |

## 🎬 Flujo de Ejecución

```
1. Feature (.feature)
   "Dado que estoy en la página..."
                ↓
2. Steps (login_steps.py)
   @given('que estoy en la página')
   def step_impl(context): ...
                ↓
3. Page Object (login_page.py)
   login_page.open()
                ↓
4. Selenium
   driver.get("url")
```

## 🏷️ Tags Disponibles

```bash
behave --tags=@smoke      # Pruebas rápidas
behave --tags=@critical   # Pruebas críticas
behave --tags=@exitoso    # Login exitoso
behave --tags=@error      # Casos de error
```

## 📊 Generar Reportes

```bash
# Reporte HTML
behave -f html -o reports/report.html

# Ver reporte
start reports/report.html
```

## ✅ Verificación

Después de la instalación, verifica:

```bash
# Ver steps disponibles
behave --steps

# Dry-run (no ejecuta, solo valida)
behave --dry-run
```

## 📖 Documentación Completa

- **[README_BDD.md](README_BDD.md)** - Guía completa de BDD
- **[README.md](README.md)** - Documentación general del proyecto

## 🆘 Comandos Útiles

```bash
# Ejecutar un feature específico
behave features/login.feature

# Ejecutar un escenario por línea
behave features/login.feature:12

# Modo verbose
behave --verbose

# Sin captura de output
behave --no-capture

# Detener en primer fallo
behave --stop
```

## 💡 Ejemplo de Escenario

```gherkin
Escenario: Login exitoso
  Dado que el usuario está en la página de login
  Cuando el usuario ingresa el nombre de usuario "standard_user"
  Y el usuario ingresa la contraseña "secret_sauce"
  Y el usuario hace clic en el botón de login
  Entonces el usuario debería ver la página de productos
```

## 🔄 Ambos Enfoques Disponibles

Este proyecto incluye **DOS** formas de ejecutar pruebas:

### 1️⃣ BDD con Behave (Recomendado)
- ✅ Lenguaje natural (Gherkin)
- ✅ Ideal para colaboración
- ✅ Documentación viva
```bash
behave
```

### 2️⃣ Unittest Tradicional
- ✅ Python puro
- ✅ Más técnico
```bash
python -m pytest tests/test_login.py -v
```

---

**¡Listo para automatizar! 🎉**

¿Dudas? Consulta [README_BDD.md](README_BDD.md)
