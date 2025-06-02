@echo off
echo ============================================
echo CS2 Players Monitor - Исправление и развертывание
echo ============================================
echo.

echo [1/4] Проверка статуса Git репозитория...
git status
echo.

echo [2/4] Добавление исправлений в Git...
git add .
git commit -m "fix: исправление конфигурации для корректного развертывания"
echo.

echo [3/4] Отправка изменений в GitHub...
git push origin main
echo.

echo [4/4] Инструкции для развертывания на Vercel:
echo.
echo ВАЖНО: Используйте правильное имя проекта!
echo.
echo Разрешенные символы:
echo - Буквы (a-z)
echo - Цифры (0-9) 
echo - Дефисы (-)
echo.
echo ЗАПРЕЩЕННЫЕ символы:
echo - Подчеркивания (_)
echo - Точки (.)
echo - Пробелы
echo - Начинать с цифры
echo.
echo Рекомендуемое имя: cs2-players-monitor
echo.
echo Варианты развертывания:
echo.
echo 1. Через веб-интерфейс Vercel:
echo    - Перейдите на vercel.com
echo    - Подключите репозиторий GitHub
echo    - Укажите имя проекта: cs2-players-monitor
echo.
echo 2. Через Vercel CLI:
echo    npm i -g vercel
echo    vercel --name cs2-players-monitor
echo.
echo 3. Альтернатива - Railway:
echo    npm i -g @railway/cli
echo    railway login
echo    railway init
echo    railway up
echo.
echo После развертывания добавьте переменные окружения:
echo CS2_SERVER_IP = 46.174.49.96
echo CS2_SERVER_PORT = 27015
echo.
echo ============================================
echo Готово! Подробные инструкции в VERCEL_DEPLOY.md
echo ============================================
pause 