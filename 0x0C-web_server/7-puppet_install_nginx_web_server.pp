# Install and configure nginx
package { 'jfryman-nginx':
  ensure => installed,
}

include nginx

class { 'nginx':
  manage_repo    => true,
  package_source => 'nginx-stable',
}

nginx::resource::server { '52.201.219.224':
  listen_port      => 80,
  www_root         => '/var/www/html/',
  vhost_cfg_append => { 'rewrite' => '^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent' },
error_page => '404 /404.html',
location => {
	'/404.html' => {
	content => 'Ceci n'est pas une page'
	},
	},
}

file { 'index':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}
