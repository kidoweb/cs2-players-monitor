# 🚀 Настройка GitHub Pages

## Автоматическое развертывание на GitHub Pages

### Шаг 1: Настройка репозитория

1. **Перейдите в настройки репозитория:**
   - Откройте ваш репозиторий на GitHub
   - Перейдите в `Settings` → `Pages`

2. **Настройте источник:**
   - **Source:** `GitHub Actions`
   - **Branch:** оставьте по умолчанию

### Шаг 2: Активация GitHub Actions

GitHub Actions уже настроен в файле `.github/workflows/deploy.yml` и будет автоматически:

- ✅ Запускаться при push в ветку `main`
- ✅ Собирать статический сайт из папки `docs/`
- ✅ Развертывать на GitHub Pages
- ✅ Создавать sitemap.xml и robots.txt

### Шаг 3: Первое развертывание

1. **Коммит и push изменений:**
   ```bash
   git add .
   git commit -m "feat: добавлена GitHub Pages версия"
   git push origin main
   ```

2. **Проверьте Actions:**
   - Перейдите в `Actions` в репозитории
   - Убедитесь, что workflow `Deploy to GitHub Pages` выполняется

3. **Дождитесь завершения:**
   - Первое развертывание может занять 5-10 минут
   - Статус можно отслеживать в разделе Actions

### Шаг 4: Проверка развертывания

После успешного развертывания ваш сайт будет доступен по адресу:
**https://kidoweb.github.io/cs2-players-monitor/**

### Шаг 5: Настройка API на Vercel

Для полной функциональности обновите API с поддержкой CORS:

1. **Развертывание API с CORS:**
   ```bash
   git add api/
   git commit -m "fix: добавлена поддержка CORS для GitHub Pages"
   git push origin main
   ```

2. **Vercel автоматически обновится** и будет поддерживать запросы с GitHub Pages

## 🔧 Структура проекта

```
├── docs/                    # GitHub Pages сайт
│   ├── index.html          # Главная страница
│   ├── style.css           # CSS стили
│   ├── script.js           # JavaScript логика
│   └── README.md           # Документация
├── api/                     # Vercel API
│   ├── index.py            # Flask приложение с CORS
│   └── requirements.txt    # Зависимости с flask-cors
├── .github/workflows/       # GitHub Actions
│   └── deploy.yml          # Workflow развертывания
└── README.md               # Основная документация
```

## 🌐 Результат

После настройки у вас будет:

1. **📱 Статический сайт** на GitHub Pages
2. **🔌 API сервер** на Vercel с CORS поддержкой
3. **🔄 Автоматическое развертывание** при каждом push
4. **📊 Мониторинг CS2 серверов** в реальном времени

## ⚙️ Настройки пользователя

На сайте пользователи смогут:

- **Указать IP и порт** своего CS2 сервера
- **Изменить API URL** (если используют собственный API)
- **Включить авто-обновление** для мониторинга в реальном времени
- **Сохранить настройки** в локальном хранилище браузера

## 🔗 Полезные ссылки

- 📖 [GitHub Pages Documentation](https://docs.github.com/en/pages)
- ⚡ [GitHub Actions Documentation](https://docs.github.com/en/actions)
- 🔌 [Vercel Documentation](https://vercel.com/docs)
- 🎮 [Source Query Protocol](https://developer.valvesoftware.com/wiki/Server_queries)

## 🆘 Устранение неполадок

### Сайт не работает
1. Проверьте статус Actions в репозитории
2. Убедитесь, что в Settings → Pages включен GitHub Actions
3. Проверьте логи развертывания

### API недоступен
1. Проверьте статус Vercel развертывания
2. Убедитесь, что переменные окружения установлены
3. Протестируйте API напрямую: `/api/health`

### CORS ошибки
1. Убедитесь, что flask-cors установлен
2. Проверьте, что CORS настроен для `origins=['*']`
3. Очистите кэш браузера (Ctrl+F5)

---

🎉 **Готово!** Ваш CS2 Players Monitor теперь доступен всему миру через GitHub Pages! 