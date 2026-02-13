# Test E2E - Compra de Producto
# Ejecuta el flujo completo: login -> seleccionar producto -> carrito -> checkout -> confirmación

param(
    [switch]$NoReport = $false,
    [switch]$Verbose = $false
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  E2E TEST: COMPRA DE PRODUCTO" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

$scriptPath = Get-Location

# Activar virtualenv si existe
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[INFO] Entorno virtual activado`n" -ForegroundColor Yellow
}

# Construir comando de behave
$behaveCmd = "behave Scenarios/checkout/checkout.feature"

if (-not $NoReport) {
    $behaveCmd += " -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_compra.html"
}

if ($Verbose) {
    $behaveCmd += " -v"
}

Write-Host "[EXEC] $behaveCmd`n" -ForegroundColor Gray

# Ejecutar tests
Invoke-Expression $behaveCmd
$exitCode = $LASTEXITCODE

# Mostrar resultado
Write-Host "`n========================================`n" -ForegroundColor Cyan

if ($exitCode -eq 0) {
    Write-Host "[SUCCESS] Test de compra completado exitosamente" -ForegroundColor Green
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_compra.html" -ForegroundColor Yellow
    }
} else {
    Write-Host "[FAILED] Test de compra fallido (exit code: $exitCode)" -ForegroundColor Red
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_compra.html" -ForegroundColor Yellow
    }
}

Write-Host "`n"
exit $exitCode
