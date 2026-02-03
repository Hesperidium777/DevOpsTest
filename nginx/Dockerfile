# Используем официальный образ nginx
FROM nginx:1.24-alpine

# Устанавливаем curl для healthcheck
RUN apk add --no-cache curl

# Удаляем дефолтные конфиги nginx
RUN rm -f /etc/nginx/conf.d/*

# Копируем нашу конфигурацию
COPY nginx.conf /etc/nginx/conf.d/app.conf

# Создаем непривилегированного пользователя и настраиваем права
RUN chown -R nginx:nginx /var/cache/nginx && \
    chmod -R 755 /var/cache/nginx && \
    touch /var/run/nginx.pid && \
    chown nginx:nginx /var/run/nginx.pid

# Переключаемся на пользователя nginx
USER nginx

# Экспорт порта
EXPOSE 80

# Healthcheck для проверки nginx
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/health || exit 1