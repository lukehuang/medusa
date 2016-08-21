# start supervisord
sudo supervisord -c /etc/supervisor/supervisord.conf

# start program
sudo supervisorctl start medusaserver
