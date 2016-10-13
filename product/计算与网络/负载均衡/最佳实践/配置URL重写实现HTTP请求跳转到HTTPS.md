假定用户需要配置网站https://example.com。希望用户在浏览器中输入网址时，直接键入www.example.com即可通过HTTPS协议安全访问。

此时用户输入的www.example.com请求转发流程如下：

1. 该请求以HTTP协议传输，通过VIP访问负载均衡监听器的80端口，并被转发到后端云服务器的8080端口。

2. 通过在腾讯云后端服务器的nginx上配置rewrite操作，该请求经过8080端口，并被重写到https://example.com页面。

3. 此时浏览器再次发送https://example.com请求到相应的HTTPS站点，该请求通过VIP访问负载均衡监听器的443端口，并被转发到后端云服务器的80端口。

至此，请求转发完成。该操作在浏览器用户未感知的情况下，将用户的HTTP请求重写为更加安全的HTTPS请求。为实现以上请求转发操作，用户可以对后端服务器做如下配置：

```
server {
	#! set_id 1070;
	#! biz_id example web;
	#! vivc_id 342;
#! vip_list 181.222.12.12 182.111.11.11
	listen 80;
	server_name example.qcloud.com;

	location / {
		#! index 0;
		#! loc_id 447;
		#! customized_conf_begin;
		client_max_body_size 200m;
		rewrite ^/.(.*) https://$host/$l redirect;
		#! customized_conf_end;
	
		proxy_pass http://447;
} 
}
```
