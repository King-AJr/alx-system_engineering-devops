# set custom header for nginx
class mynginx {
	nginx::resource::server{'myservers':
		listen_port => '80',
		server_name => '145060-web',
		location => '/',
		header => [
			'X-Served-By \"$HOSTNAME\"',
		],
	}
}
