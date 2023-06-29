# server side ssh config

exec { 'config':
  content => "echo 'Host server HostName 54.87.151.225\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no' >> /etc/ssh/sshd_config",
  path    => '/usr/bin',
}

