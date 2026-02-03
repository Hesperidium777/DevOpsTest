# DevOpsTest
Тестовое задание по DevOps направлению, включает в себя веб-приложение, развернутое в Docker-контейнерах, с Nginx в качестве reverse proxy и Python HTTP-сервером в качестве backend.
## Архитектура
Пользователь
↓ (HTTP запрос на порт 80)
Nginx (Reverse Proxy) ← Docker сеть → Python Backend
↑ (порт 8080)
└── Ответ: "Hello from Hesperidium!"
**Компоненты:**
1. **Nginx** - работает как реверс-прокси для HTTP-запросов, поступающих на порт 80
2. **Python Backend** - HTTP-сервер на порту 8080
3. **Docker сеть** - изолированная сеть для безопасного взаимодействия контейнеров

## Требования

- Docker 20.10+
- Docker Compose 2.0+

## Установка и запуск

### 1. Клонирование репозитория

bash
git clone <repository-url>
cd <repository-folder>

### 2. Сборка
bash
cp .env.example .env
docker-compose up -d

### 3. Проверка сборки
bash
docker-compose ps

### 4. Проверка работы приложения
bash
curl http://localhost

Ожидаемый ответ:
Hello from Hesperidium!
