upstream medusaserver {
    server 127.0.0.1:8000;
}

server {
    listen 80 default_server;
    server_name medusaserver.com;

    # if no access_log & error_log here, will use config in nginx.conf:
    # access_log /var/log/nginx/medusaserver.com-access.log format_combined;
    # error_log /var/log/nginx/medusaserver.com-error.log;

    # nginx access_log & error_log can be configured multiple times for multiple logs:
    access_log /var/log/nginx/medusaserver.com-access.log format_combined;
    error_log /var/log/nginx/medusaserver.com-error.log;

    # nginx send log to rsyslog (OK)
    access_log syslog:server=127.0.0.1:514,facility=local2,severity=info,tag=nginx format_combined;

    location /static {
        root /home/workspace/;
    }

    location / {
        # (this is the real timeout config for upstream server)(proxy_read_timeout)
        proxy_read_timeout 3s;

        proxy_pass http://medusaserver;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
