# client ssh config

file { 'config':
  path    => '~/.ssh/config',
  content => 'Host server\\n\\tHostName 54.87.151.225\\n\\tUser ubuntu\\n\\tIdentityFile ~/.ssh/school\\n\\tPasswordAuthentication no'
}

