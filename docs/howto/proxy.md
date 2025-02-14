# proxy

## Setup

1. Setup `/etc/apt/apt.conf.d/proxy`

	```bash
	Acquire::http::Proxy "http://10.32.115.110:8080/";
	Acquire::ftp::Proxy "http://10.32.115.110:8080/";
	Acquire::Proxy "true";

	Acquire::http::proxy "http://user:password@proxyserver:port/";
	Acquire::https::proxy "https://user:password@proxyserver:port/";
	Acquire::ftp::proxy "ftp://user:password@proxyserver:port/";
	```

2. Global proxy settings are stored in the variables: http_proxy and ftp_proxy

	.bashrc:
	```bash
	export http_proxy=http://192.168.0.1:3128
	export ftp_proxy=http://192.168.0.1:3128 # or what you have
	```
