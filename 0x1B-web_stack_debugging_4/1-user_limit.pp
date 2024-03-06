# Puppet manifest to adjust OS configuration for the holberton user

# Set the file limits system-wide
file { '/etc/security/limits.conf':
  ensure  => present,
  content => "*       hard    nofile  8192\n*       soft    nofile  4096\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure PAM session configuration for the holberton user
file { '/etc/pam.d/sshd':
  ensure  => present,
  content => "session required pam_limits.so",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Notify the user to log out and log back in for the changes to take effect
notify { 'Please log out and log back in for the changes to take effect':
  require => File['/etc/security/limits.conf', '/etc/pam.d/sshd'],
}

