# server side ssh config

exec { 'config':
    command => "echo 'Host 54.87.151.225\n\tPasswordAuthentication no\n\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
    path    => '/usr/bin'
}
