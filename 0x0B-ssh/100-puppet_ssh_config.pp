# server side ssh config

file { 'config':
  path    => '/etc/ssh/sshd_config',
  content => 'Host server1\\n\\tHostName 54.87.151.225\\n\\tUser ubuntu\\n\\tIdentityFile ~/.ssh/school\\n\\tPasswordAuthentication no'
}

