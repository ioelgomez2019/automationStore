# AutoTestStore - Sistema de Automatización BDD

## 📋 Objetivo

AutoTestStore es un **framework de automatización de pruebas** basado en Behavior-Driven Development (BDD) que valida flujos críticos de aplicaciones web de e-commerce. 

**Funcionalidades principales:**
- ✅ Autenticación de usuarios (login)
- ✅ Flujo completo de compra (inventario → carrito → checkout → confirmación)
- ✅ Reportes HTML automáticos
- ✅ Ejecución rápida (~9 segundos por test)
- ✅ Mantenible y escalable con arquitectura limpia

**Tecnologías:**
- Python 3.10+
- Selenium WebDriver 4.15.0
- Behave (Gherkin en español)
- Chrome WebDriver

---

## 🏗️ Arquitectura del Proyecto: Page Object Model (POM)

### ¿Por qué POM?

El patrón **Page Object Model** separa la lógica de UI (dónde están los elementos) de la lógica de negocio (qué hace el test):

```
✅ BENEFICIO: Si cambia la UI, cambias código en 1 lugar
✅ BENEFICIO: Tests legibles en español sin detalles técnicos
✅ BENEFICIO: Reutilización de código entre tests
✅ BENEFICIO: Fácil de mantener y delegar
```

### Capas de la Arquitectura

```
┌─────────────────────────────────────────────────────┐
│ 1. ESPECIFICACIONES (Gherkin en Español)            │
│    Scenarios/login/login.feature                    │
│    Scenarios/checkout/checkout.feature              │
└────────────────┬────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────┐
│ 2. DEFINICIONES DE PASOS (Step Definitions)         │
│    Script/modules/features/login/login_steps.py     │
│    Script/modules/features/checkout/checkoutStep.py │
└────────────────┬────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────┐
│ 3. LÓGICA DE NEGOCIO (Orquestación)                 │
│    Script/modules/features/login/login.py           │
│    Script/modules/features/checkout/checkout.py     │
└────────────────┬────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────┐
│ 4. PAGE OBJECTS (Mapeo de Elementos UI)             │
│    Script/modules/features/login/loginPage.py       │
│    Script/modules/features/checkout/*.py            │
└────────────────┬────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────┐
│ 5. UTILIDADES BASE (WebDriver Wrapper)              │
│    Script/modules/utils/loginUtils.py               │
└────────────────┬────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────┐
│ 6. CONFIGURACIÓN (Setup de Navegador)               │
│    Script/modules/config/environment.py             │
└─────────────────────────────────────────────────────┘
```

### Estructura de Directorios

```
AutoTestStore/
│
├── Scenarios/                           # 📄 Especificaciones BDD
│   ├── login/
│   │   └── login.feature               # Gherkin: casos de login
│   └── checkout/
│       └── checkout.feature             # Gherkin: casos de compra
│
├── Script/modules/
│   ├── features/
│   │   ├── login/
│   │   │   ├── login.py                # Lógica: qué hace el test
│   │   │   ├── loginPage.py            # Page Object: dónde están elementos
│   │   │   └── login_steps.py          # Pasos: mapeo Gherkin→Python
│   │   └── checkout/
│   │       ├── checkout.py                  # Lógica de compra
│   │       ├── checkoutStep.py              # Pasos del checkout
│   │       ├── inventoryPage.py             # Página de productos
│   │       ├── cartPage.py                  # Página del carrito
│   │       └── checkoutPage.py              # Página de compra
│   │
│   ├── utils/
│   │   └── loginUtils.py               # BasePage: helpers comunes
│   │
│   └── config/
│       └── environment.py               # Setup de WebDriver
│
├── reports/                             # 📊 Reportes HTML (generados)
│   ├── behave_report.html              
│   ├── test_e2e_login.html
│   └── test_e2e_compra.html
│
├── test_e2e_*.bat/ps1                  # 🚀 Scripts ejecutables
│
├── DOCUMENTACION_PROYECTO.md           # 📖 Guía técnica completa
├── QUICK_START.txt                     # ⚡ Inicio rápido
├── VERSION.md                          # 📌 Versión actual
├── DESPLIEGUE.md                       # 📦 Guía de despliegue
└── requirements.txt                     # 📋 Dependencias Python
```

---

## 🚀 Instalación desde Git

### Requisitos Previos

```
✓ Windows 10+ (o Linux/macOS equivalente)
✓ Python 3.10 o superior instalado
✓ Google Chrome instalado
✓ Conexión a internet (para descargar drivers)
✓ Git instalado (opcional, se puede descargar ZIP)
```

### Paso 1: Clonar el Repositorio

**Opción A: Con Git**

```powershell
git clone https://github.com/ioelgomez2019/automationStore.git
cd AutoTestStore
```

**Opción B: Sin Git (Descarga manual)**

1. Ir a: https://github.com/ioelgomez2019/automationStore
2. Click en **Code** → **Download ZIP**
3. Extraer en carpeta local
4. Abrir PowerShell en esa carpeta

### Paso 2: Crear Entorno Virtual

```powershell
# En Windows
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# En Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

**Verificar que está activado:**
```
(venv) PS> _
```

### Paso 3: Instalar Dependencias

```powershell
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

**Esperar a completarse sin errores**

### Paso 4: Verificar Instalación

```powershell
# Verificar Python
python --version
# Output: Python 3.10+

# Verificar Behave
behave --version
# Output: behave 1.2.6+

# Verificar pasos (dry-run)
behave --dry-run
# Output: Sin errores
```

### Paso 5: Verificar Chrome (isntalar )

```powershell
pip install selenium webdriver-manager

# Si falta: https://www.google.com/chrome/
```

---

## ▶️ Cómo Ejecutar Tests E2E

### Opción 1: Scripts Ejecutables (RECOMENDADO)

**Hacer doble click desde File Explorer:** //preferible no ejecutar

```powershell
test_e2e_login.bat               # Solo login
test_e2e_comprar_producto.bat    # Flujo completo de compra
test_e2e_todos.bat               # Todos los tests
test_e2e_smoke.bat               # Tests críticos (rápido)
```

**O desde PowerShell:**// ejecutar
```powershell
venv\Scripts\

# Todos sin repotes
behave

# Con reporte HTML / lo encuentras en  carpeta reporots
behave -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html

# Solo críticos
behave --tags=@smoke


# Tests específicos
behave Scenarios/login/login.feature
behave Scenarios/checkout/checkout.feature

### Opción 2: Comando Directo

```powershell
# Activar virtualenv
venv\Scripts\activate

# Ejecutar
.\test_e2e_comprar_producto.ps1

# Con opciones
.\test_e2e_comprar_producto.ps1 -Verbose
.\test_e2e_todos.ps1 -Parallel
```

### Ejemplo Completo

```powershell
# 1. Abrir PowerShell en carpeta proyecto

# 2. Activar virtualenv
venv\Scripts\activate

# 3. Ejecutar test
test_e2e_comprar_producto.bat

# Resultado esperado:
# ✓ 1 feature passed
# ✓ 1 scenario passed
# ✓ 12+ steps passed
# ✓ Tiempo: ~9 segundos
```

### 📊 Interpretar Resultados

**✅ Éxito:**
```
2 features passed
2 scenarios passed
14 steps passed
Took 0m9.234s
```

**❌ Error:**
Ver reporte HTML en `reports/test_e2e_compra.html`

---

## 📖 Documentación Completa

- **[DOCUMENTACION_PROYECTO.md](DOCUMENTACION_PROYECTO.md)** - Guía técnica (BDD, POM, mejores prácticas)
- **[QUICK_START.txt](QUICK_START.txt)** - Instrucciones rápidas
- **[DESPLIEGUE.md](DESPLIEGUE.md)** - Configuración CI/CD
- **[VERSION.md](VERSION.md)** - Histórico de cambios

---

## ⚡ Troubleshooting Rápido

| Error | Solución |
|-------|----------|
| `behave no reconocido` | `venv\Scripts\activate` |
| `Chrome no encontrado` | Descargar: https://www.google.com/chrome/ |
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `Elemento no encontrado` | Ver reporte HTML + screenshot |

---

## 🎯 Próximos Pasos

1. Instalar siguiendo pasos arriba
2. Ejecutar: `test_e2e_login.bat`
3. Revisar reporte en `reports/`
4. Leer DOCUMENTACION_PROYECTO.md para avanzado

---

**Estado:** Beta v0.1.0 | **Actualizado:** Feb 13, 2026 | **Autor:** Equipo QA

¡Listo para automatizar! 🚀
