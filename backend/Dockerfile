# Используем официальный легковесный образ Python
FROM python:3.12-alpine AS builder

# Устанавливаем curl для healthcheck и отладки
RUN apk add --no-cache curl

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY app.py .
COPY requirements.txt .

# Создаем непривилегированного пользователя
RUN addgroup -g 1001 -S appuser && \
    adduser -u 1001 -S appuser -G appuser && \
    chown -R appuser:appuser /app

# Переключаемся на непривилегированного пользователя
USER appuser

# Экспорт порта 
EXPOSE 8080

# Healthcheck для проверки работоспособности приложения
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Запускаем приложение
CMD ["python", "app.py"]