#负载均衡能力说明

腾讯云CLB负载均衡器通过对协议栈及服务端的深度优化，实现了HTTPS性能的巨大提升。同时，我们也通过证书的国际合作，极大降低了证书的成本。腾讯云CLB在如下几个方面能够为业务带来非常显著的收益：
1.	使用HTTPS并不会降低client端的访问速度。2.	集群内单台服务器SSL加解密性能，高达6.5W cps的完全握手。相比高性能CPU提升了至少3.5倍，节省了服务端成本，极大提升了业务运营及流量突涨时的服务能力，增强了计算型防攻击的能力。3.	支持多种协议卸载及转换。减少业务适配客户端各种协议的压力，业务后端只需要支持HTTP1.1就能使用HTTP2，SPDY，SSL3.0，TLS1.2等各版本协议。4.	一站式SSL证书申请、监控、替换。我们和国际顶级的证书厂商comodo，symantec展开对话，探讨合作，大幅缩减证书申请流程及成本。5.	防CC及WAF功能。能够有效杜绝慢连接、高频定点攻击、SQL注入、网页挂马等应用层攻击。
---#Http、Https头部标识
CLB对https进行代理，无论是http/https请求，到了CLB转发给后端CVM时，都是HTTP请求。这时开发者无法分辨前端的请求，是http还是https。
腾讯云CLB在将请求转发给后端CVM时，头部的header会植入X-Client-Proto：
X-Client-Proto: http （前端为http请求）X-Client-Proto: https  （前端为https请求）


---


#入门配置


假定用户需要配置网站https://example.com 。开发者希望用户在浏览器中输入网址时，直接键入www.example.com 即可通过HTTPS协议安全访问。

此时用户输入的www.example.com 请求转发流程如下：

1. 该请求以HTTP协议传输，通过VIP访问负载均衡监听器的80端口，并被转发到后端云服务器的8080端口。

2. 通过在腾讯云后端服务器的nginx上配置rewrite操作，该请求经过8080端口，并被重写到https://example.com 页面。

3. 此时浏览器再次发送https://example.com 请求到相应的HTTPS站点，该请求通过VIP访问负载均衡监听器的443端口，并被转发到后端云服务器的80端口。

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
		rewrite ^/.(.*) https://$host/$1 redirect;
		#! customized_conf_end;
	
		proxy_pass http://447;
} 
}
```
