# Развертывание на Vercel - Исправление 404 ошибки

## ✅ Проблема решена!

Ошибка 404 NOT_FOUND была исправлена. Были внесены следующие изменения:

### Что было исправлено:
1. **Обновлена структура проекта** - добавлена папка `api/templates/`
2. **Исправлен `vercel.json`** - правильные маршруты и конфигурация
3. **Добавлен `api/requirements.txt`** - зависимости для Vercel
4. **Обновлен путь к шаблонам** в `api/index.py`
5. **Добавлен скрипт тестирования** `test_vercel.py`

## Инструкции по развертыванию

### Шаг 1: Повторное развертывание

Если у вас уже есть проект на Vercel:
1. Зайдите в панель управления Vercel
2. Найдите ваш проект `cs2-gghub-monitor`
3. В разделе "Deployments" нажмите "Redeploy"
4. Выберите последний коммит и нажмите "Redeploy"

### Шаг 2: Новое развертывание

Если нужно создать новый проект:

#### Через веб-интерфейс:
1. Перейдите на [vercel.com](https://vercel.com)
2. Нажмите "New Project"
3. Подключите GitHub репозиторий `cs2-players-monitor`
4. **Имя проекта**: `cs2-gghub-monitor` (или любое валидное)
5. **Framework**: оставьте "Other"
6. **Build Command**: оставьте пустым
7. **Output Directory**: оставьте пустым
8. Нажмите "Deploy"

#### Через Vercel CLI:
```bash
npm i -g vercel
cd C:\Users\Vadim\Desktop\hen_plugin
vercel --name cs2-gghub-monitor
```

### Шаг 3: Настройка переменных окружения

После развертывания добавьте переменные:
1. В панели Vercel: Settings → Environment Variables
2. Добавьте:
   - `CS2_SERVER_IP` = `46.174.49.96`
   - `CS2_SERVER_PORT` = `27015`
   - `CACHE_DURATION` = `30`

### Шаг 4: Проверка работы

Ваш сайт будет доступен по адресу типа:
`https://cs2-gghub-monitor.vercel.app`

#### Тестирование через скрипт:
```bash
python test_vercel.py https://ваш-url.vercel.app
```

#### Ручная проверка:
- **Главная страница**: `https://ваш-url.vercel.app/`
- **API Health**: `https://ваш-url.vercel.app/api/health`
- **API Players**: `https://ваш-url.vercel.app/api/players?server_ip=46.174.49.96&server_port=27015`
- **Server Info**: `https://ваш-url.vercel.app/api/server-info?server_ip=46.174.49.96&server_port=27015`

## Структура проекта для Vercel

```
hen_plugin/
├── api/
│   ├── index.py          # Основное Flask приложение
│   ├── requirements.txt  # Зависимости для Vercel
│   ├── wsgi.py          # WSGI точка входа
│   └── templates/        # Шаблоны HTML
│       └── index.html
├── vercel.json          # Конфигурация Vercel
├── app.py              # Локальная версия
├── requirements.txt    # Локальные зависимости
└── templates/          # Локальные шаблоны
    └── index.html
```

## Возможные проблемы и решения

### 404 ошибка исправлена
- ✅ Правильные маршруты в `vercel.json`
- ✅ Корректная структура файлов
- ✅ Правильные пути к шаблонам

### Таймауты (10 секунд лимит Vercel)
- Код оптимизирован для быстрой работы
- Добавлено кэширование на 30 секунд
- Таймауты A2S запросов установлены на 10 секунд

### Проблемы с зависимостями
- Все зависимости указаны в `api/requirements.txt`
- Использованы стабильные версии библиотек

## Альтернативные платформы

Если Vercel не подходит:

### Railway (рекомендуется как альтернатива)
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### Render
1. Перейдите на [render.com](https://render.com)
2. Подключите GitHub репозиторий
3. Выберите "Web Service"
4. Команда запуска: `gunicorn app:app`

### Heroku
```bash
echo "web: gunicorn app:app" > Procfile
heroku create cs2-gghub-monitor
git push heroku main
```

## Поддержка

После успешного развертывания вы получите:
- 🌐 Веб-интерфейс для мониторинга игроков
- 🔌 REST API для интеграции
- 📊 Кэширование для оптимальной производительности
- 🔄 Автоматическое обновление данных

Используйте `test_vercel.py` для проверки всех функций после развертывания! 