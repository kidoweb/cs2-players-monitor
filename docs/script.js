/**
 * CS2 Players Monitor - GitHub Pages Version
 * JavaScript логика для работы с API
 */

class CS2Monitor {
    constructor() {
        this.autoRefreshInterval = null;
        this.refreshCount = 0;
        this.lastUpdateTime = null;
        
        this.initElements();
        this.bindEvents();
        this.loadSettings();
        this.updateApiLink();
        
        // Автоматическая загрузка при старте
        this.refreshData();
    }

    initElements() {
        // Элементы формы
        this.serverIpInput = document.getElementById('serverIp');
        this.serverPortInput = document.getElementById('serverPort');
        this.apiUrlInput = document.getElementById('apiUrl');
        
        // Кнопки
        this.refreshBtn = document.getElementById('refreshBtn');
        this.forceRefreshBtn = document.getElementById('forceRefreshBtn');
        this.autoRefreshBtn = document.getElementById('autoRefreshBtn');
        
        // Статус
        this.connectionStatus = document.getElementById('connectionStatus');
        this.lastUpdateTimeElement = document.getElementById('lastUpdateTime');
        
        // Информация о сервере
        this.serverName = document.getElementById('serverName');
        this.serverMap = document.getElementById('serverMap');
        this.serverPlayers = document.getElementById('serverPlayers');
        this.serverGame = document.getElementById('serverGame');
        this.serverVac = document.getElementById('serverVac');
        this.serverVersion = document.getElementById('serverVersion');
        
        // Игроки и статистика
        this.playersContainer = document.getElementById('playersContainer');
        this.totalPlayersElement = document.getElementById('totalPlayers');
        this.topScoreElement = document.getElementById('topScore');
        this.avgTimeElement = document.getElementById('avgTime');
        this.refreshCountElement = document.getElementById('refreshCount');
        
        // Подвал
        this.apiLinkFooter = document.getElementById('apiLinkFooter');
    }

    bindEvents() {
        this.refreshBtn.addEventListener('click', () => this.refreshData(false));
        this.forceRefreshBtn.addEventListener('click', () => this.refreshData(true));
        this.autoRefreshBtn.addEventListener('click', () => this.toggleAutoRefresh());
        
        // Сохранение настроек при изменении
        this.serverIpInput.addEventListener('change', () => this.saveSettings());
        this.serverPortInput.addEventListener('change', () => this.saveSettings());
        this.apiUrlInput.addEventListener('change', () => {
            this.saveSettings();
            this.updateApiLink();
        });
    }

    loadSettings() {
        const settings = localStorage.getItem('cs2-monitor-settings');
        if (settings) {
            const parsed = JSON.parse(settings);
            this.serverIpInput.value = parsed.serverIp || '46.174.49.96';
            this.serverPortInput.value = parsed.serverPort || '27015';
            this.apiUrlInput.value = parsed.apiUrl || 'https://cs2-gghub-monitor.vercel.app';
        }
    }

    saveSettings() {
        const settings = {
            serverIp: this.serverIpInput.value,
            serverPort: this.serverPortInput.value,
            apiUrl: this.apiUrlInput.value
        };
        localStorage.setItem('cs2-monitor-settings', JSON.stringify(settings));
    }

    updateApiLink() {
        const apiUrl = this.apiUrlInput.value;
        this.apiLinkFooter.href = `${apiUrl}/api/health`;
        this.apiLinkFooter.textContent = 'API Health';
    }

    setStatus(type, message) {
        const statusIcon = this.connectionStatus.querySelector('.status-icon');
        const statusText = this.connectionStatus.querySelector('.status-text');
        
        // Удаляем все классы статуса
        this.connectionStatus.className = 'status ' + type;
        
        // Устанавливаем иконку и текст
        switch (type) {
            case 'loading':
                statusIcon.textContent = '⏳';
                break;
            case 'connected':
                statusIcon.textContent = '✅';
                break;
            case 'error':
                statusIcon.textContent = '❌';
                break;
            default:
                statusIcon.textContent = '⏳';
        }
        
        statusText.textContent = message;
    }

    async refreshData(forceRefresh = false) {
        const apiUrl = this.apiUrlInput.value;
        const serverIp = this.serverIpInput.value;
        const serverPort = this.serverPortInput.value;
        
        if (!apiUrl || !serverIp || !serverPort) {
            this.setStatus('error', 'Заполните все поля');
            return;
        }

        this.setStatus('loading', 'Загрузка данных...');
        this.refreshBtn.disabled = true;
        this.forceRefreshBtn.disabled = true;

        try {
            const params = new URLSearchParams({
                server_ip: serverIp,
                server_port: serverPort
            });

            if (forceRefresh) {
                params.append('force_refresh', 'true');
            }

            const response = await fetch(`${apiUrl}/api/players?${params}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                },
                // Добавляем таймаут
                signal: AbortSignal.timeout(30000)
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();

            if (data.success) {
                this.updateServerInfo(data.server_info);
                this.updatePlayersList(data.players);
                this.updateStats(data.players);
                this.setStatus('connected', `Подключено (${data.cached ? 'кэш' : 'обновлено'})`);
                
                this.lastUpdateTime = new Date();
                this.updateLastUpdateTime();
                this.refreshCount++;
                this.refreshCountElement.textContent = this.refreshCount;
            } else {
                throw new Error(data.error || 'Неизвестная ошибка API');
            }

        } catch (error) {
            console.error('Ошибка при получении данных:', error);
            this.setStatus('error', `Ошибка: ${error.message}`);
            this.showError(`Не удалось получить данные: ${error.message}`);
        } finally {
            this.refreshBtn.disabled = false;
            this.forceRefreshBtn.disabled = false;
        }
    }

    updateServerInfo(serverInfo) {
        if (!serverInfo) return;

        this.serverName.textContent = serverInfo.name || '-';
        this.serverMap.textContent = serverInfo.map || '-';
        this.serverPlayers.textContent = serverInfo.players || '-';
        this.serverGame.textContent = serverInfo.game || '-';
        this.serverVac.textContent = serverInfo.vac_enabled ? '✅ Включен' : '❌ Отключен';
        this.serverVersion.textContent = serverInfo.version || '-';
    }

    updatePlayersList(players) {
        if (!players || players.length === 0) {
            this.playersContainer.innerHTML = `
                <div class="no-players">
                    👥 На сервере нет игроков
                </div>
            `;
            return;
        }

        const playersGrid = document.createElement('div');
        playersGrid.className = 'players-grid';

        players.forEach((player, index) => {
            const playerCard = document.createElement('div');
            playerCard.className = 'player-card';
            
            playerCard.innerHTML = `
                <div class="player-name">
                    ${this.escapeHtml(player.name)} 
                    ${index === 0 ? '👑' : ''}
                </div>
                <div class="player-stats">
                    <div class="player-stat">
                        <span class="stat-label">Счёт:</span>
                        <span class="stat-value">${player.score}</span>
                    </div>
                    <div class="player-stat">
                        <span class="stat-label">Время:</span>
                        <span class="stat-value">${player.duration_formatted}</span>
                    </div>
                    <div class="player-stat">
                        <span class="stat-label">Пинг:</span>
                        <span class="stat-value">${player.ping !== 'N/A' ? player.ping + 'ms' : 'N/A'}</span>
                    </div>
                    <div class="player-stat">
                        <span class="stat-label">Подключен:</span>
                        <span class="stat-value">${player.time_connected}</span>
                    </div>
                </div>
            `;

            playersGrid.appendChild(playerCard);
        });

        this.playersContainer.innerHTML = '';
        this.playersContainer.appendChild(playersGrid);
    }

    updateStats(players) {
        const totalPlayers = players.length;
        const topScore = players.length > 0 ? Math.max(...players.map(p => p.score)) : 0;
        const avgTime = players.length > 0 
            ? players.reduce((sum, p) => sum + p.duration, 0) / players.length 
            : 0;

        this.totalPlayersElement.textContent = totalPlayers;
        this.topScoreElement.textContent = topScore;
        this.avgTimeElement.textContent = this.formatDuration(avgTime);
    }

    formatDuration(seconds) {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        
        if (hours > 0) {
            return `${hours}ч ${minutes}м`;
        } else if (minutes > 0) {
            return `${minutes}м`;
        } else {
            return `${Math.floor(seconds)}с`;
        }
    }

    updateLastUpdateTime() {
        if (this.lastUpdateTime) {
            const timeStr = this.lastUpdateTime.toLocaleTimeString('ru-RU');
            this.lastUpdateTimeElement.textContent = `Последнее обновление: ${timeStr}`;
        }
    }

    toggleAutoRefresh() {
        const isActive = this.autoRefreshBtn.getAttribute('data-active') === 'true';
        
        if (isActive) {
            // Отключаем авто-обновление
            clearInterval(this.autoRefreshInterval);
            this.autoRefreshInterval = null;
            this.autoRefreshBtn.setAttribute('data-active', 'false');
            this.autoRefreshBtn.innerHTML = '📡 Авто-обновление';
        } else {
            // Включаем авто-обновление каждые 30 секунд
            this.autoRefreshInterval = setInterval(() => {
                this.refreshData(false);
            }, 30000);
            this.autoRefreshBtn.setAttribute('data-active', 'true');
            this.autoRefreshBtn.innerHTML = '🔴 Остановить';
            
            // Сразу обновляем данные
            this.refreshData(false);
        }
    }

    showError(message) {
        // Удаляем предыдущие ошибки
        const existingError = this.playersContainer.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }

        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.innerHTML = `
            <strong>Ошибка:</strong> ${this.escapeHtml(message)}
            <br><small>Проверьте настройки API и подключение к интернету</small>
        `;
        
        this.playersContainer.prepend(errorDiv);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Инициализация приложения
document.addEventListener('DOMContentLoaded', () => {
    window.cs2Monitor = new CS2Monitor();
    
    console.log('🎮 CS2 Players Monitor загружен');
    console.log('📡 GitHub Pages версия');
    console.log('🔗 Репозиторий: https://github.com/kidoweb/cs2-players-monitor');
}); 