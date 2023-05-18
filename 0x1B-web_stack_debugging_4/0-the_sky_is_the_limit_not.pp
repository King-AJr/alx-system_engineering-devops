# increase the number of request my server can take


exec { 'fix--for-nginx':
  command => 'sed -i "s/15/3500/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
