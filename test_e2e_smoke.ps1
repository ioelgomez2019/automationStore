# Test E2E - Smoke Tests (Críticos)
# Ejecuta solo los tests marcados como @smoke

param(
    [switch]$NoReport = $false,
    [switch]$Verbose = $false
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  E2E TEST: SMOKE (CRITICOS)" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

$scriptPath = Get-Location

# Activar virtualenv si existe
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[INFO] Entorno virtual activado`n" -ForegroundColor Yellow
}

# Construir comando de behave
$behaveCmd = "behave --tags=@smoke"

if (-not $NoReport) {
    $behaveCmd += " -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_smoke.html"
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
    Write-Host "[SUCCESS] Smoke tests completados exitosamente" -ForegroundColor Green
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_smoke.html" -ForegroundColor Yellow
    }
} else {
    Write-Host "[FAILED] Smoke tests fallaron (exit code: $exitCode)" -ForegroundColor Red
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_smoke.html" -ForegroundColor Yellow
    }
}

Write-Host "`n"
exit $exitCode
