
# 🛡️ SentinelGuard

**Система мониторинга и автоматического реагирования на киберугрозы**  
Анализирует логи, оценивает риски и блокирует атаки в реальном времени.

---

## Возможности
- **Парсинг логов** (Nginx, фаерволы)
- **Сканирование хостов** (порты, уязвимости)
- **Расчёт рисков** на основе угроз и уровня защиты
- **Автоматические меры**:
  - Блокировка IP (`iptables`/`netsh`)
  - Ограничение скорости (`tc`)
  - Уведомления админу
- **Веб-интерфейс** с графиками и фильтрами

---

## 🛠 Установка

### Требования
- Python 3.9+
- Nmap (для сканирования)
- `iptables` (Linux) / `netsh` (Windows)

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/ваш-репозиторий/sentinelguard.git
   cd sentinelguard
   ```

2. **Установка зависимостей**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Инициализация БД**:
   ```bash
   python -c "from core.db import init_db; init_db()"
   ```

---

## Запуск

### 1. Режим мониторинга
```bash
python sentinelguard.py
```

### 2. Веб-интерфейс
```bash
uvicorn web.app:app --reload
```
Откройте: [http://localhost:8000](http://localhost:8000)

### 3. CLI для админа
```bash
python cli/admin.py scan 192.168.1.1
python cli/admin.py block 192.168.1.1
```

---

## Конфигурация
Настройки в `config/config.yaml`:
```yaml
risk:
  high: 80    # Порог для блокировки
  medium: 50  # Порог для уведомлений

logs:
  nginx: "/var/log/nginx/access.log"  # Путь к логам
```

---

## Структура проекта
```
sentinelguard/
├── core/          # Логика парсинга, сканирования, БД
├── web/           # Веб-интерфейс (FastAPI + JS)
├── cli/           # Командная строка
├── config/        # Настройки
└── tests/         # Тесты
```

---

## Тестирование
Запуск всех тестов:
```bash
pytest tests/
```

---

## Docker-развёртывание 🐳
1. Сборка образа:
   ```bash
   docker build -t sentinelguard .
   ```

2. Запуск:
   ```bash
   docker run -d -p 8000:8000 --cap-add=NET_ADMIN sentinelguard
   ```

---

## Примеры использования

### 1. Мониторинг логов Nginx
```python
from core.log_parser import start_log_monitor
start_log_monitor()  # Запуск в фоне
```

### 2. Проверка хоста
```bash
python cli/admin.py scan 192.168.1.1
```
Вывод:
```
[✓] Хост 192.168.1.1: 
    - Открытые порты: 22 (SSH), 80 (HTTP)
    - Уровень защиты: 70/100
```

---

## Контрибьютинг
1. Форкните репозиторий
2. Создайте ветку (`git checkout -b feature/ваша-фича`)
3. Запушьте изменения (`git push origin feature/ваша-фича`)
4. Откройте Pull Request

**Рекомендуемые улучшения**:
- Поддержка SIEM-систем (Splunk, ELK)
- Интеграция с Telegram-ботами
- Machine Learning для детектирования аномалий

---

## 📬 Контакты
Автор: Gosloto
Email: Gosioto@yandex.ru  
Telegram: @G0SL0T0
```


