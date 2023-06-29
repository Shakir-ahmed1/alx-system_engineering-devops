# server side ssh config

file { 'config':
  path    => '/etc/ssh/sshd_config',
  content => 'IdentityFile ~/.ssh/school\\nPasswordAuthentication no'
}

