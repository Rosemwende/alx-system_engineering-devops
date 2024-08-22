# fix nginx to accept and serve more requests by increasing the max open files limit

exec { 'modify-max-open-files-limit-setting':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif  => 'grep -q "15" /etc/default/nginx',
}
