$ErrorActionPreference = 'Stop'

$env:POSTGRES_DB = if ($env:POSTGRES_DB) { $env:POSTGRES_DB } else { 'dacms' }
$env:POSTGRES_USER = if ($env:POSTGRES_USER) { $env:POSTGRES_USER } else { 'postgres' }
$env:POSTGRES_PASSWORD = if ($env:POSTGRES_PASSWORD) { $env:POSTGRES_PASSWORD } else { 'postgres' }
$env:POSTGRES_HOST = if ($env:POSTGRES_HOST) { $env:POSTGRES_HOST } else { 'localhost' }
$env:POSTGRES_PORT = if ($env:POSTGRES_PORT) { $env:POSTGRES_PORT } else { '5432' }

$pythonPath = 'C:\Users\new_a\AppData\Local\Programs\Python\Python314\python.exe'
if (-not (Test-Path $pythonPath)) {
    $pythonPath = 'py'
}

Set-Location $PSScriptRoot
& $pythonPath manage.py runserver 127.0.0.1:8000
