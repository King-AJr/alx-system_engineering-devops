class { 'apache': }
apache::vhost { 'web-1':
  servername      => $HOSTNAME,
  serveraliases   => ['web-01'],
  port            => '80',
  docroot         => '',
  header          => ['add_header X-Served-By $HOSTNAME;'],
}
