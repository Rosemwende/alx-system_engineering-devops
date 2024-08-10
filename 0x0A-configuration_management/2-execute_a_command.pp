# This Puppet manifest kills a process named 'killmenow'

exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/usr/local/bin'],
  onlyif  => '/bin/ps aux | /bin/grep -q [k]illmenow',
}
