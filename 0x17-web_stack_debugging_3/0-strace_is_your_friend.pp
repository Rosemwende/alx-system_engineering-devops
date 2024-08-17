# This Puppet manifest fixes the issue causing Apache to return a 500 error.
# by editing the mistyped .phpp to php in the /var/www/html/wp-settings.php file

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/:/bin/',
}
