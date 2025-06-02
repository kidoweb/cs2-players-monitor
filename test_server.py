#!/usr/bin/env python3
"""
Скрипт для тестирования подключения к серверу CS2
Используется для проверки доступности сервера и получения данных игроков
"""

import a2s
import sys
import argparse
from datetime import datetime

def test_server_connection(server_ip, server_port, timeout=5):
    """
    Тестирует подключение к серверу CS2
    """
    print(f"🔍 Тестирование подключения к серверу {server_ip}:{server_port}")
    print("=" * 60)
    
    address = (server_ip, server_port)
    
    try:
        print("📋 Получение информации о сервере...")
        info = a2s.info(address, timeout=timeout)
        
        print(f"✅ Сервер доступен!")
        print(f"   Название: {info.server_name}")
        print(f"   Карта: {info.map_name}")
        print(f"   Игроков: {info.player_count}/{info.max_players}")
        print(f"   Игра: {info.game}")
        print(f"   Версия: {info.version}")
        print(f"   Протокол: {info.protocol}")
        print()
        
    except Exception as e:
        print(f"❌ Ошибка при получении информации о сервере: {e}")
        return False
    
    try:
        print("👥 Получение списка игроков...")
        players = a2s.players(address, timeout=timeout)
        
        if len(players) == 0:
            print("ℹ️  На сервере нет игроков")
        else:
            print(f"✅ Найдено {len(players)} игроков:")
            print("-" * 60)
            print(f"{'№':<3} {'Никнейм':<25} {'Счет':<8} {'Время':<12}")
            print("-" * 60)
            
            for i, player in enumerate(players, 1):
                duration = f"{int(player.duration)}с"
                if player.duration >= 60:
                    minutes = int(player.duration // 60)
                    seconds = int(player.duration % 60)
                    duration = f"{minutes}м {seconds}с"
                
                print(f"{i:<3} {player.name[:24]:<25} {player.score:<8} {duration:<12}")
        
        print()
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при получении списка игроков: {e}")
        return False

def test_popular_servers():
    """
    Тестирует популярные публичные серверы CS2
    """
    print("🌍 Тестирование популярных публичных серверов:")
    print("=" * 60)
    
    # Список популярных публичных серверов (могут быть недоступны)
    test_servers = [
        ("185.25.205.19", 27015, "Пример сервера 1"),
        ("185.25.205.20", 27015, "Пример сервера 2"),
        ("localhost", 27015, "Локальный сервер"),
    ]
    
    available_servers = []
    
    for server_ip, server_port, description in test_servers:
        print(f"\n📡 Проверка {description} ({server_ip}:{server_port})...")
        try:
            address = (server_ip, server_port)
            info = a2s.info(address, timeout=3)
            print(f"✅ Доступен: {info.server_name} ({info.player_count}/{info.max_players} игроков)")
            available_servers.append((server_ip, server_port, info.server_name))
        except Exception as e:
            print(f"❌ Недоступен: {e}")
    
    if available_servers:
        print(f"\n🎯 Найдено {len(available_servers)} доступных серверов:")
        for ip, port, name in available_servers:
            print(f"   {ip}:{port} - {name}")
    else:
        print("\n⚠️  Не найдено доступных серверов для тестирования")
    
    return available_servers

def main():
    parser = argparse.ArgumentParser(description='Тестирование сервера CS2')
    parser.add_argument('--ip', default='127.0.0.1', help='IP-адрес сервера (по умолчанию: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=27015, help='Порт сервера (по умолчанию: 27015)')
    parser.add_argument('--timeout', type=int, default=5, help='Таймаут подключения в секундах (по умолчанию: 5)')
    parser.add_argument('--test-public', action='store_true', help='Тестировать популярные публичные серверы')
    
    args = parser.parse_args()
    
    print(f"🎮 CS2 Server Tester")
    print(f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    if args.test_public:
        available_servers = test_popular_servers()
        if available_servers:
            print(f"\n🔄 Тестирование первого доступного сервера...")
            ip, port, name = available_servers[0]
            test_server_connection(ip, port, args.timeout)
    else:
        success = test_server_connection(args.ip, args.port, args.timeout)
        if not success:
            print("\n💡 Советы по устранению неполадок:")
            print("   1. Убедитесь, что сервер запущен и доступен")
            print("   2. Проверьте правильность IP-адреса и порта")
            print("   3. Убедитесь, что сервер позволяет A2S запросы")
            print("   4. Проверьте настройки брандмауэра")
            print(f"   5. Попробуйте увеличить таймаут: --timeout 10")
            sys.exit(1)

if __name__ == "__main__":
    main() 