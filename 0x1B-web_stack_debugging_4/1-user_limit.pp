# Increase the number of open files limit

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 4096\n",
}

exec { 'reload limits':
  command => 'sysctl -p',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/sbin', '/bin'],
  onlyif  => 'test -f /etc/security/limits.conf',
}
