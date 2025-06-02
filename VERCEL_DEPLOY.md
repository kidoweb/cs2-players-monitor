# Развертывание на Vercel - Исправление проблем с именованием

## Проблема с именем проекта

Если вы получили ошибку "The name contains invalid characters", следуйте этим правилам для имени проекта:

### Правила именования проектов Vercel:
- ✅ Только буквы (a-z), цифры (0-9) и дефисы (-)
- ✅ Не должно начинаться с цифры
- ✅ Максимум 63 символа
- ❌ Нельзя использовать подчеркивания (_)
- ❌ Нельзя использовать точки (.)
- ❌ Нельзя использовать пробелы

### Рекомендуемые имена для проекта:
- `cs2-players-monitor`
- `cs2-player-tracker`
- `counter-strike-monitor`
- `cs2-server-stats`

## Шаги развертывания

### Вариант 1: Через веб-интерфейс Vercel

1. Перейдите на [vercel.com](https://vercel.com)
2. Войдите в аккаунт или зарегистрируйтесь
3. Нажмите "New Project"
4. Подключите GitHub репозиторий
5. **ВАЖНО**: В поле "Project Name" используйте: `cs2-players-monitor`
6. Настройки оставьте по умолчанию
7. Нажмите "Deploy"

### Вариант 2: Через Vercel CLI

```bash
# Установка Vercel CLI
npm i -g vercel

# В папке проекта
vercel

# При первом развертывании выберите:
# Set up and deploy "C:\Users\Vadim\Desktop\hen_plugin"? [Y/n] y
# Which scope do you want to deploy to? [ваш-аккаунт]
# Link to existing project? [y/N] n
# What's your project's name? cs2-players-monitor
# In which directory is your code located? ./
```

### Вариант 3: Исправление существующего проекта

Если проект уже создан с неправильным именем:

1. Зайдите в панель управления Vercel
2. Выберите проект
3. Перейдите в Settings → General
4. В разделе "Project Name" измените на `cs2-players-monitor`
5. Нажмите "Save"

## Переменные окружения

После успешного развертывания добавьте переменные:

1. В панели Vercel перейдите в Settings → Environment Variables
2. Добавьте:
   - `CS2_SERVER_IP` = `46.174.49.96`
   - `CS2_SERVER_PORT` = `27015`

## Проверка развертывания

После успешного развертывания ваш сайт будет доступен по адресу:
`https://cs2-players-monitor.vercel.app`

API эндпоинты:
- `https://cs2-players-monitor.vercel.app/api/players`
- `https://cs2-players-monitor.vercel.app/api/server-info`
- `https://cs2-players-monitor.vercel.app/api/health`

## Возможные проблемы и решения

### Ошибка "Invalid characters in name"
- Убедитесь, что имя содержит только буквы, цифры и дефисы
- Имя не должно начинаться с цифры

### Ошибка при сборке
- Проверьте, что файл `api/index.py` существует
- Убедитесь, что `requirements.txt` содержит все зависимости

### Таймауты API
- Vercel имеет лимит времени выполнения 10 секунд для бесплатного плана
- При необходимости оптимизируйте код или рассмотрите платный план

## Альтернативные платформы

Если проблемы с Vercel продолжаются, можно использовать:

### Railway
```bash
# Установка CLI
npm install -g @railway/cli

# Развертывание
railway login
railway init
railway up
```

### Render
1. Перейдите на [render.com](https://render.com)
2. Подключите GitHub репозиторий
3. Выберите "Web Service"
4. Укажите команду запуска: `gunicorn app:app`

### Heroku
```bash
# Создайте Procfile
echo "web: gunicorn app:app" > Procfile

# Развертывание
heroku create cs2-players-monitor
git push heroku main
``` 