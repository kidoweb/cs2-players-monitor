# 🚀 Деплой CS2 Мониторинга - Полная инструкция

## 📋 Шаг 1: Подготовка к деплою

### Создание GitHub репозитория

1. **Идите на** https://github.com
2. **Нажмите** "New repository"
3. **Назовите**: `cs2-players-monitor`
4. **Выберите**: Public
5. **Нажмите** "Create repository"

### Загрузка файлов

1. **Нажмите** "uploading an existing file"
2. **Перетащите все файлы** из папки `hen_plugin`:
   ```
   📁 Файлы для загрузки:
   ├── 📁 api/
   │   └── index.py
   ├── 📁 templates/
   │   └── index.html
   ├── app.py
   ├── requirements.txt
   ├── vercel.json
   ├── README.md
   ├── DEPLOY.md
   └── test_server.py
   ```
3. **Напишите commit**: "Initial commit - CS2 Players Monitor"
4. **Нажмите** "Commit changes"

## 📋 Шаг 2: Деплой на Vercel

### Подключение к Vercel

1. **Идите на** https://vercel.com
2. **Нажмите** "Sign up" или "Login"
3. **Выберите** "Continue with GitHub"
4. **Авторизуйтесь** в GitHub

### Создание проекта

1. **Нажмите** "New Project"
2. **Найдите** ваш репозиторий `cs2-players-monitor`
3. **Нажмите** "Import"
4. **Оставьте** настройки по умолчанию
5. **Нажмите** "Deploy"

### Ожидание деплоя

```
⏳ Deплой займет 1-2 минуты
✅ После завершения вы получите URL: https://cs2-players-monitor-xxx.vercel.app
```

## 📋 Шаг 3: Настройка переменных окружения

### В панели Vercel:

1. **Перейдите** в ваш проект
2. **Нажмите** "Settings" → "Environment Variables"
3. **Добавьте переменные**:

```env
Name: CS2_SERVER_IP
Value: 46.174.49.96

Name: CS2_SERVER_PORT
Value: 27015

Name: CACHE_DURATION
Value: 30
```

4. **Нажмите** "Save"
5. **Перейдите** на вкладку "Deployments"
6. **Нажмите** "Redeploy" для применения переменных

## 🎯 Готово! Ваш сайт доступен!

URL будет примерно таким: `https://cs2-players-monitor-xxx.vercel.app`

---

# 🌐 Как использовать API для получения данных

## 📊 API Эндпоинты

### 1. Получение списка игроков

```http
GET https://your-site.vercel.app/api/players?server_ip=46.174.49.96&server_port=27015
```

**Параметры:**
- `server_ip` - IP адрес сервера CS2
- `server_port` - Порт сервера (обычно 27015)
- `force_refresh` - true/false (принудительное обновление)

**Ответ JSON:**
```json
{
  "success": true,
  "players": [
    {
      "name": "Player1",
      "score": 15,
      "duration": 754.23,
      "duration_formatted": "12м 34с",
      "time_connected": "12 минуты 34 секунды",
      "kills": "N/A",
      "deaths": "N/A",
      "ping": "N/A"
    }
  ],
  "server_info": {
    "name": "PlaySport",
    "map": "de_mirage",
    "players": "1/20",
    "game": "Counter-Strike 2",
    "player_count": 1,
    "max_players": 20,
    "vac_enabled": false,
    "version": "1.40.8.3"
  },
  "cached": false,
  "last_update": "2024-01-20T15:30:45.123456"
}
```

### 2. Только информация о сервере

```http
GET https://your-site.vercel.app/api/server-info?server_ip=46.174.49.96&server_port=27015
```

### 3. Проверка здоровья приложения

```http
GET https://your-site.vercel.app/api/health
```

## 💻 Примеры использования

### JavaScript (для сайта)

```javascript
// Получение данных игроков
async function getCS2Players(serverIP, serverPort) {
    try {
        const response = await fetch(
            `https://your-site.vercel.app/api/players?server_ip=${serverIP}&server_port=${serverPort}`
        );
        const data = await response.json();
        
        if (data.success) {
            console.log('Сервер:', data.server_info.name);
            console.log('Карта:', data.server_info.map);
            console.log('Игроков:', data.players.length);
            
            data.players.forEach((player, index) => {
                console.log(`${index + 1}. ${player.name} - ${player.score} очков`);
            });
        } else {
            console.error('Ошибка:', data.error);
        }
    } catch (error) {
        console.error('Ошибка подключения:', error);
    }
}

// Использование
getCS2Players('46.174.49.96', '27015');
```

### PHP (для сайта)

```php
<?php
function getCS2Players($serverIP, $serverPort) {
    $url = "https://your-site.vercel.app/api/players?server_ip=$serverIP&server_port=$serverPort";
    
    $response = file_get_contents($url);
    $data = json_decode($response, true);
    
    if ($data['success']) {
        echo "Сервер: " . $data['server_info']['name'] . "\n";
        echo "Карта: " . $data['server_info']['map'] . "\n";
        echo "Игроков: " . count($data['players']) . "\n";
        
        foreach ($data['players'] as $index => $player) {
            echo ($index + 1) . ". " . $player['name'] . " - " . $player['score'] . " очков\n";
        }
    } else {
        echo "Ошибка: " . $data['error'];
    }
}

// Использование
getCS2Players('46.174.49.96', '27015');
?>
```

### Python (для интеграции)

```python
import requests

def get_cs2_players(server_ip, server_port):
    url = f"https://your-site.vercel.app/api/players"
    params = {
        'server_ip': server_ip,
        'server_port': server_port
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data['success']:
            print(f"Сервер: {data['server_info']['name']}")
            print(f"Карта: {data['server_info']['map']}")
            print(f"Игроков: {len(data['players'])}")
            
            for i, player in enumerate(data['players'], 1):
                print(f"{i}. {player['name']} - {player['score']} очков")
        else:
            print(f"Ошибка: {data['error']}")
            
    except Exception as e:
        print(f"Ошибка подключения: {e}")

# Использование
get_cs2_players('46.174.49.96', '27015')
```

## 🔧 Интеграция с HTML сайтом

```html
<!DOCTYPE html>
<html>
<head>
    <title>CS2 Мониторинг</title>
</head>
<body>
    <h1>Игроки CS2</h1>
    <div id="players"></div>
    
    <script>
    async function loadPlayers() {
        const response = await fetch('https://your-site.vercel.app/api/players?server_ip=46.174.49.96&server_port=27015');
        const data = await response.json();
        
        if (data.success) {
            let html = `<h2>${data.server_info.name}</h2>`;
            html += `<p>Карта: ${data.server_info.map}</p>`;
            html += `<ul>`;
            
            data.players.forEach(player => {
                html += `<li>${player.name} - ${player.score} очков (${player.duration_formatted})</li>`;
            });
            
            html += `</ul>`;
            document.getElementById('players').innerHTML = html;
        }
    }
    
    // Загрузка при открытии страницы
    loadPlayers();
    
    // Обновление каждые 30 секунд
    setInterval(loadPlayers, 30000);
    </script>
</body>
</html>
```

## ⚡ Быстрый тест после деплоя

После деплоя откройте в браузере:
```
https://your-site.vercel.app/api/players?server_ip=46.174.49.96&server_port=27015
```

Должны увидеть JSON с данными игроков!

## 🛠️ Решение проблем

### Если API не работает:
1. Проверьте переменные окружения в Vercel
2. Посмотрите логи в Vercel Dashboard → Functions
3. Убедитесь что сервер CS2 доступен

### Если таймаут:
- Уменьшите timeout в `api/index.py` до 5 секунд
- Redeploy проект в Vercel 