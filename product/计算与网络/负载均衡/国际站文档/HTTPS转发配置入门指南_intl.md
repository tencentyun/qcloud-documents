## 1. About Cloud Load Balance Capability

Tencent Cloud's CLB has achieved significant improvement in HTTPS performance based on the deep optimization of protocol stack and servers. At the same time, our cooperation with world-leading certificate providers saves the cost on certificates. Tencent Cloud's CLB brings substantial benefits for your business in the following aspects:

1. The use of HTTPS does not affect the access speed of Client.
2. A single CVM in a cluster features a fast SSL encryption and decryption capability, with the full handshakes reaching up to 65,000 cps. This is at least 3.5 times faster than that when high-performance CPU is relied on, which greatly reduces the server costs, enhances the service capacity at the time of business volume and traffic surges and achieves a stronger computing-based anti-attack capability.
3. CLB supports the unmount and translation of a variety of protocols. CLB reduces business backend's stress of supporting various protocols for the client. Business backend just needs to support HTTP1.1 to use various versions of protocols such as HTTP2, SPDY, SSL3.0 and TLS1.2.
4. One-stop service covering SSL certificate application, monitoring and replacement. By working with world-leading certificate vendors including Comodo and Symantec, we have significantly simplified certificate application procedures and reduced relevant costs.
5. Anti-CC and WAF features CLB can effectively prevent application-level attacks such as slow connection, high-frequency targeted attack, SQL injection and website malicious code.

## 2. HTTP and HTTPS Header Identifier

CLB acts as a proxy for HTTPS. Both HTTP and HTTPS requests become HTTP requests when forwarded to the backend CVM by CLB. In this case, the developer is not able to distinguish whether the frontend request is HTTP or HTTPS.

Tencent CLB implants X-Client-Proto into the header when it forwards the request to the backend CVM:

X - Client - Proto: http (frontend request is an HTTP request)
X - Client - Proto: https  (frontend request is an HTTPS request)

## 3. Starting Configuration


Assume that a user needs to configure the website https://example.com. The developer wants users to directly access the website securely through HTTPS protocol by simply entering www.example.com in the browser.

In this case, www.example.com request entered by the user is forwarded as follows:

1. The request is transmitted via HTTP protocol and accesses port 80 of the load balancer listener via VIP. Then it is forwarded to port 8080 of the backend CVM.

2. By configuring rewrite operation on nginx of the Tencent Cloud backend server, the request is pass through port 8080 and is re-written to the https://example.com page.

3. Then the browser sends https://example.com request to the corresponding HTTPS site again. The request accesses port 443 of the load balancer listener via VIP, and then it is forwarded to port 80 of the backend CVM.

At this point, the request forwarding process is finished.

This operation rewrites user's HTTP request into a more secure HTTPS request without being noticed. To achieve the above request forwarding operation, the user can configure the backend server as follows:

```
server {

	listen 80; 
	server_name example.qcloud.com;

	location / {

		#! customized_conf_begin;
		client_max_body_size 200m;
		rewrite ^/.(.*) https://$host/$1 redirect;

} 
}
```

Alternatively, in the new version of nginx, redirect the nginx http page to the https page with 301 redirection method (recommended):

```
server { 	
  	listen	  80;
  	server_name    example.qcloud.com;
  	return	  301 https://$server_name$request_uri;
}

server {
  	listen	  443 ssl;
 	server_name    example.qcloud.com;
	[....]
}
```

