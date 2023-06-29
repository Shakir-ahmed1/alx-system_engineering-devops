# ssh server config

exec {'ssh_config':
    command => "echo 'Host 35.237.86.168\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
    path    => '/usr/bin'
}
