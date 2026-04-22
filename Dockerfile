# Temel imaj olarak Nginx Alpine kullan
FROM nginx:alpine

# Static klasöründeki her şeyi Nginx'in web sunucu dizinine kopyala
COPY static /usr/share/nginx/html

# 80 portunu dışa aç
EXPOSE 80
