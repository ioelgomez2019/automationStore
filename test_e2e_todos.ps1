# Test E2E - Suite Completa
# Ejecuta todos los tests (login + checkout)

param(
    [switch]$NoReport = $false,
    [switch]$Verbose = $false,
    [switch]$Parallel = $false
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  E2E TEST: SUITE COMPLETA" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

$scriptPath = Get-Location

# Activar virtualenv si existe
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[INFO] Entorno virtual activado`n" -ForegroundColor Yellow
}

# Construir comando de behave
$behaveCmd = "behave"

if ($Parallel) {
    $behaveCmd += " -j 4"
    Write-Host "[INFO] Modo paralelo activado (4 workers)`n" -ForegroundColor Yellow
}

if (-not $NoReport) {
    $behaveCmd += " -f behave_html_formatter:HTMLFormatter -o reports/behave_report.html"
}

if ($Verbose) {
    $behaveCmd += " -v"
}

Write-Host "[EXEC] $behaveCmd`n" -ForegroundColor Gray

# Medir tiempo de ejecución
$startTime = Get-Date

# Ejecutar tests
Invoke-Expression $behaveCmd
$exitCode = $LASTEXITCODE

$endTime = Get-Date
$duration = ($endTime - $startTime).TotalSeconds

# Mostrar resultado
Write-Host "`n========================================`n" -ForegroundColor Cyan

if ($exitCode -eq 0) {
    Write-Host "[SUCCESS] Todos los tests completados exitosamente" -ForegroundColor Green
    Write-Host "Tiempo total: $([Math]::Round($duration, 2))s" -ForegroundColor Yellow
} else {
    Write-Host "[FAILED] Algunos tests fallaron (exit code: $exitCode)" -ForegroundColor Red
    Write-Host "Tiempo total: $([Math]::Round($duration, 2))s" -ForegroundColor Yellow
}

if (-not $NoReport) {
    Write-Host "Reporte disponible en: reports/behave_report.html" -ForegroundColor Cyan
}

Write-Host "`n"
exit $exitCode
