# how to configure load balancer 2 servers 1 load balancer
## task-0
add server header the nginx config of each server "add_header X-Served-By \$hostname;" to the server in /etc/nginx/sites-enabled/default
## task-1
using HAproxy configure your load balancer for frontend and backend in /etc/haproxy/haproxy.cfg and to Make sure that HAproxy can be managed via an init script use `sudo echo "ENABLED=1" | sudo tee -a /etc/default/haproxy`
NOTE: load balancer only routes requests based on the configuration. it doesn't need any authentication for the servers
to configure hostnames for both web_servers `sudo hostnamectl set-hostname 1203835-web-01` for web_01
to configure hostnames for both web_servers `sudo hostnamectl set-hostname 1203835-web-02` for web_02
