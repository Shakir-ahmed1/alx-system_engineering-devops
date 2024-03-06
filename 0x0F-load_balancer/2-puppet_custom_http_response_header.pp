# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure custom HTTP response header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location / {
            root /var/www/html;
            index index.html index.htm;
            add_header X-Served-By $hostname;
        }
    }
  ",
  require => Package['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
