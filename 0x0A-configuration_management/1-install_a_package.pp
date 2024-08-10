# This Puppet manifest installs the Flask package version 2.1.0 using pip3.

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/pip3 show Flask | grep 2.1.0',
}
