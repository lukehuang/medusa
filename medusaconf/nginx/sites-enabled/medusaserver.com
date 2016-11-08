upstream medusaserver {
    server 127.0.0.1:8000;
}

server {
    listen 80 default_server;
    server_name medusaserver.com;

    access_log /var/log/nginx/medusaserver.com-access.log format_combined;
    error_log /var/log/nginx/medusaserver.com-error.log;

    location /static {
        root /home/workspace/;
    }

    location / {
        # (这里才是真正对代理后端生效的超时设置)(proxy_read_timeout)
        proxy_read_timeout 3s;

        proxy_pass http://medusaserver;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
