#!/bin/bash
# Script para generar resumen final antes de despliegue

echo "========================================"
echo "  VERIFICACION PRE-DESPLIEGUE"
echo "========================================"
echo ""

# Verificar estructura
echo "[1/5] Verificando estructura de directorios..."
required_dirs=("Scenarios" "Script/modules" "reports" "Script/modules/features/login" "Script/modules/features/checkout" "Script/modules/utils" "Script/modules/config")

for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✓ $dir"
    else
        echo "  ✗ FALTA: $dir"
    fi
done

# Verificar archivos críticos
echo ""
echo "[2/5] Verificando archivos críticos..."
required_files=("requirements.txt" "behave.ini" "DOCUMENTACION_PROYECTO.md" "QUICK_START.txt" "VERSION.md" "DESPLIEGUE.md")

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ FALTA: $file"
    fi
done

# Verificar features
echo ""
echo "[3/5] Verificando feature files..."
if [ -f "Scenarios/login/login.feature" ]; then
    echo "  ✓ login.feature"
else
    echo "  ✗ FALTA: login.feature"
fi

if [ -f "Scenarios/checkout/checkout.feature" ]; then
    echo "  ✓ checkout.feature"
else
    echo "  ✗ FALTA: checkout.feature"
fi

# Verificar Python files
echo ""
echo "[4/5] Verificando archivos Python..."
python_files=("Script/modules/features/login/login.py" "Script/modules/features/login/loginPage.py" "Script/modules/features/login/login_steps.py" "Script/modules/features/checkout/checkout.py" "Script/modules/features/checkout/checkoutStep.py" "Script/modules/config/environment.py" "Script/modules/utils/loginUtils.py")

for file in "${python_files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $(basename $file)"
    else
        echo "  ✗ FALTA: $file"
    fi
done

# Verificar scripts ejecutables
echo ""
echo "[5/5] Verificando scripts de ejecución..."
scripts=("test_e2e_login.bat" "test_e2e_comprar_producto.bat" "test_e2e_todos.bat" "test_e2e_smoke.bat" "test_e2e_login.ps1" "test_e2e_comprar_producto.ps1" "test_e2e_todos.ps1" "test_e2e_smoke.ps1")

for script in "${scripts[@]}"; do
    if [ -f "$script" ]; then
        echo "  ✓ $script"
    else
        echo "  ✗ FALTA: $script"
    fi
done

echo ""
echo "========================================"
echo "  VERIFICACION COMPLETADA"
echo "========================================"
echo ""
echo "Próximos pasos:"
echo "1. pip install -r requirements.txt"
echo "2. behave --dry-run (verificar pasos)"
echo "3. test_e2e_login.bat (ejecutar login)"
echo "4. test_e2e_comprar_producto.bat (ejecutar compra)"
echo ""
