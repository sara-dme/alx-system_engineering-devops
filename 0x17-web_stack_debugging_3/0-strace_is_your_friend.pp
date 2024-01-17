# change .phpp to .php in wordpress setting

exec { 'replace_ext':
  command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",}
