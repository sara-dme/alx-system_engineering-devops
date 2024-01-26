# increase the UNLIMIT of the file
exec { 'fix-unlimit':
  command  => '/bin/sed -i "s/15/4096" /etc/default/nginx',
  path => 'usr/local/bin/:/bin/',
}

-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
