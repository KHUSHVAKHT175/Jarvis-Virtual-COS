@echo off
title Установка Jarvis-COS
color 0A
echo ===========================================
echo     УСТАНОВКА ПРОЕКТА JARVIS-COS v1.0.0
echo ===========================================
echo.
where git >nul 2>nul
if %0% neq 0 (
    echo Git не найден. Установи Git перед запуском.
    pause
    exit /b
)
set "TARGET_DIR=%C:\Users\usuario%\Jarvis-COS"
if not exist "%%TARGET_DIR%%" (
    mkdir "%%TARGET_DIR%%"
)
git clone https://github.com/KHUSHVAKHT175/Jarvis-COS.git "%%TARGET_DIR%%"
cd "%%TARGET_DIR%%"
where python >nul 2>nul
if %0% neq 0 (
    echo Python не найден. Установи Python 3.x и перезапусти скрипт.
    pause
    exit /b
)
if exist requirements.txt (
    python -m pip install -r requirements.txt
)
echo.
echo Jarvis-COS успешно установлен!
pause
