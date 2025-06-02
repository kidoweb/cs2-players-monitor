# 🎮 CS2 Players Monitor - GitHub Pages

Статическая веб-версия монитора игроков Counter-Strike 2, развернутая на GitHub Pages.

## 🌐 Демо

**Сайт доступен по адресу:** [https://kidoweb.github.io/cs2-players-monitor/](https://kidoweb.github.io/cs2-players-monitor/)

## ✨ Возможности

- 👥 **Мониторинг игроков в реальном времени**
- 🖥️ **Информация о сервере** (название, карта, количество игроков, VAC статус)
- 📊 **Статистика игроков** (счёт, время в игре, пинг)
- 🔄 **Автоматическое обновление** каждые 30 секунд
- 💾 **Сохранение настроек** в локальном хранилище
- 📱 **Адаптивный дизайн** для мобильных устройств
- 🎨 **Современный UI** с градиентами и анимациями

## 🚀 Технологии

- **HTML5** - структура страницы
- **CSS3** - современные стили с градиентами и анимациями
- **Vanilla JavaScript** - логика приложения без фреймворков
- **GitHub Actions** - автоматическое развертывание
- **GitHub Pages** - хостинг статического сайта

## ⚙️ Настройка

1. **Откройте сайт:** [https://kidoweb.github.io/cs2-players-monitor/](https://kidoweb.github.io/cs2-players-monitor/)

2. **Настройте параметры подключения:**
   - **IP-адрес сервера:** `46.174.49.96` (по умолчанию)
   - **Порт:** `27015` (по умолчанию)
   - **API URL:** `https://cs2-gghub-monitor.vercel.app` (API на Vercel)

3. **Нажмите "Обновить"** для получения данных

4. **Включите авто-обновление** для мониторинга в реальном времени

## 🔌 API Integration

Сайт использует REST API для получения данных о сервере и игроках:

### Эндпоинты:
- `GET /api/players` - список игроков
- `GET /api/server-info` - информация о сервере  
- `GET /api/health` - проверка работоспособности API

### Параметры запроса:
- `server_ip` - IP-адрес CS2 сервера
- `server_port` - порт сервера (обычно 27015)
- `force_refresh` - принудительное обновление кэша

### Пример запроса:
```javascript
fetch('https://cs2-gghub-monitor.vercel.app/api/players?server_ip=46.174.49.96&server_port=27015')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🎮 Поддерживаемые серверы

Приложение работает с любыми CS2 серверами, поддерживающими протокол A2S:

- ✅ **Counter-Strike 2** серверы
- ✅ **Source Engine** игры
- ✅ **Публичные** и **приватные** серверы
- ✅ **VAC защищенные** серверы

## 🛠️ Локальная разработка

Для локального тестирования:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/kidoweb/cs2-players-monitor.git
   cd cs2-players-monitor
   ```

2. **Запустите локальный сервер:**
   ```bash
   # Python 3
   cd docs
   python -m http.server 8000
   
   # Node.js
   npx http-server docs -p 8000
   
   # PHP
   cd docs
   php -S localhost:8000
   ```

3. **Откройте в браузере:** `http://localhost:8000`

## 📁 Структура проекта

```
docs/
├── index.html          # Главная страница
├── style.css           # Стили CSS
├── script.js           # JavaScript логика
└── README.md           # Документация
```

## 🔧 Настройка API

Для работы с собственным API сервером:

1. **Разверните API** (Vercel, Railway, Heroku)
2. **Добавьте CORS поддержку** для GitHub Pages домена
3. **Обновите API URL** в настройках сайта
4. **Протестируйте подключение**

## 🌟 Возможности JavaScript версии

- **Без серверной части** - работает полностью в браузере
- **Сохранение настроек** в localStorage
- **Обработка ошибок** с пользовательскими уведомлениями
- **Адаптивный интерфейс** для всех устройств
- **Современный ES6+** синтаксис
- **Модульная архитектура** класса CS2Monitor

## 📱 Мобильная версия

Сайт полностью адаптирован для мобильных устройств:

- 📱 **Адаптивная сетка** для планшетов и телефонов
- 👆 **Сенсорное управление** с hover эффектами
- 🔄 **Оптимизированные анимации** для сенсорных экранов
- 💾 **Экономия трафика** с кэшированием данных

## 🔗 Ссылки

- 🌐 **Сайт:** [https://kidoweb.github.io/cs2-players-monitor/](https://kidoweb.github.io/cs2-players-monitor/)
- 📦 **Репозиторий:** [https://github.com/kidoweb/cs2-players-monitor](https://github.com/kidoweb/cs2-players-monitor)
- 🔌 **API:** [https://cs2-gghub-monitor.vercel.app](https://cs2-gghub-monitor.vercel.app)
- 📊 **API Health:** [https://cs2-gghub-monitor.vercel.app/api/health](https://cs2-gghub-monitor.vercel.app/api/health)

## 🆘 Поддержка

Если у вас возникли проблемы:

1. **Проверьте консоль браузера** (F12) для ошибок
2. **Убедитесь в доступности API** по ссылке выше
3. **Проверьте настройки сервера** (IP и порт)
4. **Создайте Issue** в GitHub репозитории

---

Разработано с ❤️ для сообщества Counter-Strike 2 