#!/usr/bin/env python3
"""
Скрипт для тестирования развернутого API на Vercel
"""

import requests
import json
import sys

def test_vercel_deployment(base_url):
    """
    Тестирует развернутое приложение на Vercel
    """
    print(f"🔍 Тестирование развертывания: {base_url}")
    print("=" * 50)
    
    # Тест 1: Главная страница
    print("\n1. Тестирование главной страницы...")
    try:
        response = requests.get(f"{base_url}/", timeout=30)
        if response.status_code == 200:
            print("✅ Главная страница загружается")
            if "CS2 Players Monitor" in response.text:
                print("✅ Содержимое корректное")
            else:
                print("⚠️ Возможно неправильное содержимое")
        else:
            print(f"❌ Ошибка главной страницы: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка подключения к главной странице: {e}")
    
    # Тест 2: API Health Check
    print("\n2. Тестирование API Health Check...")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=30)
        if response.status_code == 200:
            data = response.json()
            print("✅ Health check работает")
            print(f"   Status: {data.get('status')}")
            print(f"   Timestamp: {data.get('timestamp')}")
        else:
            print(f"❌ Ошибка health check: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка health check: {e}")
    
    # Тест 3: API Players (тестовый сервер)
    print("\n3. Тестирование API Players...")
    try:
        params = {
            'server_ip': '46.174.49.96',
            'server_port': '27015',
            'force_refresh': 'true'
        }
        response = requests.get(f"{base_url}/api/players", params=params, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print("✅ API Players работает")
            print(f"   Success: {data.get('success')}")
            print(f"   Игроков найдено: {len(data.get('players', []))}")
            if data.get('server_info'):
                server_info = data['server_info']
                print(f"   Сервер: {server_info.get('name')}")
                print(f"   Карта: {server_info.get('map')}")
                print(f"   Игроки: {server_info.get('players')}")
        else:
            print(f"❌ Ошибка API Players: {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Детали ошибки: {error_data}")
            except:
                print(f"   Ответ: {response.text[:200]}")
    except Exception as e:
        print(f"❌ Ошибка API Players: {e}")
    
    # Тест 4: API Server Info
    print("\n4. Тестирование API Server Info...")
    try:
        params = {
            'server_ip': '46.174.49.96',
            'server_port': '27015'
        }
        response = requests.get(f"{base_url}/api/server-info", params=params, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print("✅ API Server Info работает")
            print(f"   Success: {data.get('success')}")
            if data.get('server_info'):
                server_info = data['server_info']
                print(f"   Сервер: {server_info.get('name')}")
                print(f"   Игра: {server_info.get('game')}")
                print(f"   VAC: {server_info.get('vac_enabled')}")
        else:
            print(f"❌ Ошибка API Server Info: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка API Server Info: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 Тестирование завершено")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Введите URL развернутого приложения (например, https://cs2-gghub-monitor.vercel.app): ")
    
    # Убираем слэш в конце если есть
    url = url.rstrip('/')
    
    test_vercel_deployment(url) 