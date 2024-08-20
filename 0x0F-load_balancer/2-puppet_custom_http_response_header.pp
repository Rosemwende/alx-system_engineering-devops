# This Puppet manifest installs and configures Nginx to add a custom HTTP header 'X-Served-By' with the value as the hostname of the server.

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/puppetlabs/puppet/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF")
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    root /var/www/html;

    location / {
        add_header X-Served-By \$hostname;
        try_files \$uri \$uri/ =404;
    }
}
| EOF
}

exec { 'nginx_configtest':
  command     => '/usr/sbin/nginx -t',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
  notify      => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => Exec['nginx_configtest'],
  hasrestart => true,
}
