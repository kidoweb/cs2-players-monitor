from flask import Flask, jsonify, render_template, request
import a2s
import time
import threading
from datetime import datetime, timedelta
import logging
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Конфигурация
DEFAULT_SERVER_IP = os.getenv('CS2_SERVER_IP', '127.0.0.1')
DEFAULT_SERVER_PORT = int(os.getenv('CS2_SERVER_PORT', '27015'))
CACHE_DURATION = int(os.getenv('CACHE_DURATION', '30'))  # Кэширование на 30 секунд

# Кэш для данных игроков
players_cache = {
    'data': [],
    'last_update': None,
    'server_info': None
}

def format_duration(seconds):
    """
    Форматирует время в удобочитаемый вид
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}ч {minutes}м {secs}с"
    elif minutes > 0:
        return f"{minutes}м {secs}с"
    else:
        return f"{secs}с"

def format_time_connected(seconds):
    """
    Форматирует время подключения в более подробном виде
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    parts = []
    if hours > 0:
        parts.append(f"{hours} час{'ов' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} минут{'ы' if 1 < minutes < 5 else ''}")
    if secs > 0 or not parts:
        parts.append(f"{secs} секунд{'ы' if 1 < secs < 5 else ''}")
    
    return " ".join(parts)

def get_server_players(server_ip, server_port, timeout=10):
    """
    Получает список игроков с сервера CS2
    """
    try:
        address = (server_ip, server_port)
        
        # Получаем информацию о сервере
        info = a2s.info(address, timeout=timeout)
        
        # Небольшая задержка между запросами для предотвращения блокировки
        time.sleep(0.5)
        
        # Получаем список игроков
        players = a2s.players(address, timeout=timeout)
        
        # Формируем данные
        player_list = []
        for player in players:
            # Форматируем время в игре
            duration_formatted = format_duration(player.duration)
            
            player_data = {
                'name': player.name,
                'score': player.score,
                'duration': round(player.duration, 2),
                'duration_formatted': duration_formatted,
                'kills': getattr(player, 'kills', 'N/A'),  # Если доступно
                'deaths': getattr(player, 'deaths', 'N/A'),  # Если доступно
                'ping': getattr(player, 'ping', 'N/A'),  # Если доступно
                'time_connected': format_time_connected(player.duration)
            }
            player_list.append(player_data)
        
        # Сортируем игроков по счету (убывание)
        player_list.sort(key=lambda x: x['score'], reverse=True)
        
        server_data = {
            'name': info.server_name,
            'map': info.map_name,
            'players': f"{info.player_count}/{info.max_players}",
            'game': info.game,
            'player_count': info.player_count,
            'max_players': info.max_players,
            'server_type': getattr(info, 'server_type', 'Unknown'),
            'environment': getattr(info, 'environment', 'Unknown'),
            'vac_enabled': getattr(info, 'vac_enabled', False),
            'version': getattr(info, 'version', 'Unknown')
        }
        
        return player_list, server_data, None
        
    except Exception as e:
        logger.error(f"Ошибка при получении данных с сервера {server_ip}:{server_port}: {str(e)}")
        return None, None, str(e)

def should_update_cache():
    """
    Проверяет, нужно ли обновить кэш
    """
    if players_cache['last_update'] is None:
        return True
    
    time_diff = datetime.now() - players_cache['last_update']
    return time_diff.total_seconds() > CACHE_DURATION

def update_cache_async(server_ip, server_port):
    """
    Асинхронно обновляет кэш данных
    """
    def update():
        players, server_info, error = get_server_players(server_ip, server_port)
        if players is not None:
            players_cache['data'] = players
            players_cache['server_info'] = server_info
            players_cache['last_update'] = datetime.now()
            logger.info(f"Кэш обновлен. Найдено {len(players)} игроков")
    
    thread = threading.Thread(target=update)
    thread.daemon = True
    thread.start()

@app.route('/')
def index():
    """
    Главная страница с интерфейсом
    """
    return render_template('index.html')

@app.route('/api/players', methods=['GET'])
def get_players():
    """
    API эндпоинт для получения списка игроков
    """
    # Получаем параметры сервера из запроса
    server_ip = request.args.get('server_ip', DEFAULT_SERVER_IP)
    server_port = int(request.args.get('server_port', DEFAULT_SERVER_PORT))
    force_refresh = request.args.get('force_refresh', 'false').lower() == 'true'
    
    # Проверяем, нужно ли обновить кэш
    if force_refresh or should_update_cache():
        players, server_info, error = get_server_players(server_ip, server_port)
        
        if error:
            return jsonify({
                'success': False,
                'error': error,
                'players': [],
                'server_info': None,
                'cached': False
            }), 500
        
        # Обновляем кэш
        players_cache['data'] = players
        players_cache['server_info'] = server_info
        players_cache['last_update'] = datetime.now()
        
        return jsonify({
            'success': True,
            'players': players,
            'server_info': server_info,
            'cached': False,
            'last_update': players_cache['last_update'].isoformat()
        })
    
    # Возвращаем данные из кэша
    return jsonify({
        'success': True,
        'players': players_cache['data'],
        'server_info': players_cache['server_info'],
        'cached': True,
        'last_update': players_cache['last_update'].isoformat() if players_cache['last_update'] else None
    })

@app.route('/api/server-info', methods=['GET'])
def get_server_info():
    """
    API эндпоинт для получения информации о сервере
    """
    server_ip = request.args.get('server_ip', DEFAULT_SERVER_IP)
    server_port = int(request.args.get('server_port', DEFAULT_SERVER_PORT))
    
    try:
        address = (server_ip, server_port)
        info = a2s.info(address, timeout=10)
        
        server_data = {
            'name': info.server_name,
            'map': info.map_name,
            'players': f"{info.player_count}/{info.max_players}",
            'game': info.game,
            'version': info.version,
            'protocol': info.protocol,
            'ping': 'N/A'  # A2S не предоставляет пинг напрямую
        }
        
        return jsonify({
            'success': True,
            'server_info': server_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Проверка здоровья приложения
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'cache_age': (datetime.now() - players_cache['last_update']).total_seconds() 
                     if players_cache['last_update'] else None
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    
    logger.info(f"Запуск приложения на порту {port}")
    logger.info(f"Сервер по умолчанию: {DEFAULT_SERVER_IP}:{DEFAULT_SERVER_PORT}")
    
    app.run(host='0.0.0.0', port=port, debug=debug) 