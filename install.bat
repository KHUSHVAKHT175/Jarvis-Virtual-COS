@echo off
title ��⠭���� Jarvis-COS
color 0A
echo ===========================================
echo     ��������� ������� JARVIS-COS v1.0.0
echo ===========================================
echo.
where git >nul 2>nul
if %0% neq 0 (
    echo Git �� ������. ��⠭��� Git ��। ����᪮�.
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
    echo Python �� ������. ��⠭��� Python 3.x � ��१����� �ਯ�.
    pause
    exit /b
)
if exist requirements.txt (
    python -m pip install -r requirements.txt
)
echo.
echo Jarvis-COS �ᯥ譮 ��⠭�����!
pause
