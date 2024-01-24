# increase the UNLIMIT of the file
exec { 'fix-unlimit':
  command  => "sed -i 's/^UNLIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
  provider => 'shell',
}

-> exec { 'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
