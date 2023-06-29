# server side ssh config

exec { 'config':
  content => "echo 'Host server\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no >> /etc/ssh/sshd_config",
  path    => '/usr/bin',
}

