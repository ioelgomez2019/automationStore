# Test E2E - Login
# Ejecuta los escenarios de autenticación de usuario

param(
    [switch]$NoReport = $false,
    [switch]$Verbose = $false
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  E2E TEST: LOGIN" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

$scriptPath = Get-Location

# Activar virtualenv si existe
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
    Write-Host "[INFO] Entorno virtual activado`n" -ForegroundColor Yellow
}

# Construir comando de behave
$behaveCmd = "behave Scenarios/login/login.feature"

if (-not $NoReport) {
    $behaveCmd += " -f behave_html_formatter:HTMLFormatter -o reports/test_e2e_login.html"
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
    Write-Host "[SUCCESS] Tests de login completados exitosamente" -ForegroundColor Green
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_login.html" -ForegroundColor Yellow
    }
} else {
    Write-Host "[FAILED] Tests de login fallaron (exit code: $exitCode)" -ForegroundColor Red
    if (-not $NoReport) {
        Write-Host "Reporte disponible en: reports/test_e2e_login.html" -ForegroundColor Yellow
    }
}

Write-Host "`n"
exit $exitCode
