# 0-strace_is_your_friend.pp
# This Puppet manifest fixes the issue causing Apache to return a 500 error.
exec { 'fix-wordpress':
  command => 'your_fixing_command_here',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
