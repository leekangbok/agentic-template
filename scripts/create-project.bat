@echo off
setlocal

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0create-project.ps1" %*
exit /b %errorlevel%
