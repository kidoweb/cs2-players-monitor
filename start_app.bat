@echo off
echo ===========================================
echo   CS2 Мониторинг игроков - Запуск
echo ===========================================
echo.

REM Проверяем наличие Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python не найден! Пожалуйста, установите Python 3.7+
    pause
    exit /b 1
)

echo ✅ Python найден

REM Проверяем и устанавливаем зависимости
echo 📦 Проверка зависимостей...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Ошибка при установке зависимостей
    pause
    exit /b 1
)

echo ✅ Зависимости установлены

REM Запускаем приложение
echo.
echo 🚀 Запуск приложения...
echo 🌐 Приложение будет доступно по адресу: http://localhost:5000
echo 🛑 Для остановки нажмите Ctrl+C
echo.

python app.py

pause 