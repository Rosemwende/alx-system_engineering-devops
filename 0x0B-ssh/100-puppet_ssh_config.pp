#!/usr/bin/env bash
# To make changes to our configuration file
# using puppet

file {'/etc/ssh/ssh_config':
	ensure => present',
}
file_line { 'Declare identity file':
  path  => 'etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/config',
  match => '^IdentityFile',
  ensure => 'present',
}
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => 'PasswordAuthentication yes',
  replace => 'true',
}
