"""
Environment.py - Configuración de Behave
Este archivo contiene los hooks que se ejecutan antes y después de las pruebas
Maneja la configuración del navegador y la limpieza
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def before_all(context):
    """
    Hook que se ejecuta UNA VEZ antes de todas las pruebas
    Configura variables globales y configuraciones iniciales
    """
    print("\n" + "="*70)
    print("🚀 INICIANDO SUITE DE PRUEBAS BDD - SAUCEDEMO LOGIN")
    print("="*70 + "\n")
    
    # Configurar opciones generales
    context.config.setup_logging = True


def before_feature(context, feature):
    """
    Hook que se ejecuta antes de cada Feature
    """
    print(f"\n📋 Feature: {feature.name}")
    print(f"   Archivo: {feature.filename}")
    print(f"   Escenarios: {len(feature.scenarios)}")
    print("-" * 70)


def before_scenario(context, scenario):
    """
    Hook que se ejecuta antes de cada escenario
    Inicializa el navegador y configura el driver
    """
    print(f"\n▶️  Escenario: {scenario.name}")
    print(f"   Tags: {', '.join(scenario.tags) if scenario.tags else 'Sin tags'}")
    print("-" * 70)
    
    # Configurar opciones de Chrome
    chrome_options = Options()
    
    # Descomentar para modo headless (sin interfaz gráfica)
    # chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Inicializar el driver de Chrome
    print("🌐 Abriendo navegador Chrome...")
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    # Configurar timeouts
    context.driver.implicitly_wait(10)
    context.driver.set_page_load_timeout(30)
    
    print("✓ Navegador inicializado correctamente\n")


def after_scenario(context, scenario):
    """
    Hook que se ejecuta después de cada escenario
    Cierra el navegador y muestra el resultado
    """
    print("\n" + "-" * 70)
    
    # Mostrar resultado del escenario
    if scenario.status == "passed":
        print(f"✅ Escenario PASÓ: {scenario.name}")
    elif scenario.status == "failed":
        print(f"❌ Escenario FALLÓ: {scenario.name}")
        if hasattr(context, 'driver'):
            # Capturar screenshot en caso de fallo (opcional)
            try:
                screenshot_name = f"screenshot_{scenario.name.replace(' ', '_')}.png"
                context.driver.save_screenshot(screenshot_name)
                print(f"📸 Screenshot guardado: {screenshot_name}")
            except Exception as e:
                print(f"⚠️  No se pudo guardar el screenshot: {e}")
    elif scenario.status == "skipped":
        print(f"⏭️  Escenario OMITIDO: {scenario.name}")
    
    # Pequeña pausa para visualizar el resultado
    time.sleep(2)
    
    # Cerrar el navegador
    if hasattr(context, 'driver'):
        print("🔒 Cerrando navegador...")
        context.driver.quit()
        print("✓ Navegador cerrado")
    
    print("-" * 70)


def after_feature(context, feature):
    """
    Hook que se ejecuta después de cada Feature
    """
    passed = sum(1 for scenario in feature.scenarios if scenario.status == "passed")
    failed = sum(1 for scenario in feature.scenarios if scenario.status == "failed")
    skipped = sum(1 for scenario in feature.scenarios if scenario.status == "skipped")
    total = len(feature.scenarios)
    
    print(f"\n📊 Resumen de Feature: {feature.name}")
    print(f"   Total: {total} | ✅ Pasados: {passed} | ❌ Fallidos: {failed} | ⏭️  Omitidos: {skipped}")
    print("=" * 70 + "\n")


def after_all(context):
    """
    Hook que se ejecuta UNA VEZ después de todas las pruebas
    """
    print("\n" + "="*70)
    print("🏁 SUITE DE PRUEBAS BDD FINALIZADA")
    print("="*70 + "\n")


# ==================== CONFIGURACIÓN ADICIONAL ====================

def before_step(context, step):
    """
    Hook que se ejecuta antes de cada paso (opcional)
    Útil para logging detallado
    """
    # Descomentar para ver cada paso que se ejecuta
    # print(f"   → {step.keyword} {step.name}")
    pass


def after_step(context, step):
    """
    Hook que se ejecuta después de cada paso (opcional)
    Útil para capturar información de pasos fallidos
    """
    if step.status == "failed":
        print(f"   ❌ Paso fallido: {step.keyword} {step.name}")
