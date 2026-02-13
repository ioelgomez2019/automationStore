# Guía de Despliegue - AutoTestStore v0.1.0-beta

## 1. Preparación del Servidor

### Requisitos de Sistema
```
- Windows 10+ / Linux / macOS
- Python 3.10 o superior
- Chrome instalado (versión coincidente)
- 500MB espacio libre
- Conexión a internet
```

### Verificación Pre-Despliegue
```powershell
# Verificar Python
python --version       # Debe ser 3.10+

# Verificar Chrome instalado
ls "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Windows

# Verificar Git (si aplica)
git --version
```

## 2. Clonación del Repositorio

```powershell
# Opción A: Con Git
git clone https://github.com/ioelgomez2019/automationStore.git
cd AutoTestStore

# Opción B: Sin Git (descargar ZIP)
# Descargar y extraer ZIP en carpeta target
cd AutoTestStore
```

## 3. Instalación de Dependencias

```powershell
# En Windows (CMD o PowerShell)
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# En Linux/macOS
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Verificación de Instalación

```powershell
# Activar virtualenv (si no está activo)
venv\Scripts\activate

# Verificar behave
python -m behave --version
# Output esperado: behave 1.2.6+

# Dry run (comprueba que todos los pasos están mapeados)
behave --dry-run

# Output esperado:
# 0 features passed
# Sin errores de parsing
```

## 5. Primera Ejecución

```powershell
# Opción A: Scripts batch (más simple)
test_e2e_login.bat

# Opción B: PowerShell (con opciones)
.\test_e2e_todos.ps1 -Verbose

# Opción C: Comando directo
behave Scenarios/
```

## 6. Validación de Resultados

```
✅ Éxito: 
  - 2 features passed
  - 2 scenarios passed
  - 12+ steps passed
  - Tiempo: ~9-15 segundos

❌ Error:
  - Revisar reporte en: reports/behave_report.html
  - Ejecutar con verbose: behave -v
```

## 7. Estructura Post-Despliegue

```
AutoTestStore/
├── Scenarios/               ← FEATURES (no modificar)
├── Script/modules/          ← CÓDIGO (no modificar)
├── reports/                 ← REPORTES (se generan aquí)
├── test_e2e_*.bat          ← SCRIPTS (use estos)
├── test_e2e_*.ps1          ← SCRIPTS
├── DOCUMENTACION_PROYECTO.md ← LEA ESTO PRIMERO
├── QUICK_START.txt          ← Instrucciones rápidas
└── requirements.txt         ← DEPENDENCIAS
```

## 8. Información de Contacto

**Para errores de instalación:**
1. Verificar Python 3.10+ instalado
2. Verificar Chrome instalado
3. Verificar que el comando `pip install -r requirements.txt` ejecutó sin errores

**Para errores de ejecución:**
1. Revisar QUICK_START.txt (sección Troubleshooting)
2. Ejecutar con `-v`: `behave -v`
3. Revisar HTML reporte: `reports/behave_report.html`
4. Revisar DOCUMENTACION_PROYECTO.md (sección 9)

## 9. Próximos Pasos Después de Despliegue

1. Ejecutar suite de pruebas completa
2. Revisar reportes HTML
3. Verificar que el login funciona correctamente
4. Verificar que el checkout completa exitosamente
5. Activar CI/CD si aplica

## 10. Configuración de CI/CD (Opcional)

### GitHub Actions
```yaml
# .github/workflows/tests.yml
name: Automated Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: behave --dry-run
      - run: behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
```

### Jenkins
```groovy
pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'behave'
            }
        }
        stage('Report') {
            steps {
                publishHTML([
                    reportDir: 'reports',
                    reportFiles: 'behave_report.html',
                    reportName: 'BDD Test Report'
                ])
            }
        }
    }
}
```

---

**Estado:** v0.1.0-beta  
**Última actualización:** Febrero 13, 2026  
**Siguiente revisión:** Después de fase 1 de capacitación
