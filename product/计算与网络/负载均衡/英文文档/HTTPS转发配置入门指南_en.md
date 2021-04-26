## About Cloud Load Balance Capacity

Tencent Cloud's CLB has achieved significant improvement in HTTPS performance based on the full optimization of protocol stack and servers. At the same time, our cooperation with world-leading certificate providers results in a considerable cost-saving in certificates. Tencent Cloud's CLB brings substantial benefits for the business in the following aspects:

1. The use of HTTPS does not affect the access speed of client.
2. A single server in a cluster features a fast SSL encryption and decryption capability, with the full handshakes reaching up to 65,000 cps. This is at least 3.5 times faster than that when high-performance CPU is relied on, which greatly reduces the server costs, enhances the service capacity at the time of business volume and traffic surges and achieves a stronger computing-based anti-attack capability.
3. Support the uninstallation and translation of a variety of protocols. Reduce the stress involved in the adaption to various protocols of the client. The business back-end just needs to support HTTP1.1 to use various versions of protocols such as HTTP2, SPDY, SSL3.0 and TLS1.2.
4. One-stop service covering SSL certificate application, monitoring and replacement. By working with world-leading certificate providers including comodo and symantec, we have significantly simplified the certificate application procedures and reduced relevant costs.
5. Anti-CC and WAF capabilities Effectively prevent attacks at application layer such as slow connection, high-frequency targeted attack, SQL injection, website malicious code.


#1. About Cloud Load Balance Capacity

Tencent Cloud's CLB has achieved significant improvement in HTTPS performance based on the full optimization of protocol stack and servers. At the same time, our cooperation with world-leading certificate providers results in a considerable cost-saving in certificates. Tencent Cloud's CLB brings substantial benefits for the business in the following aspects:

1. The use of HTTPS does not affect the access speed of client.
2. A single server in a cluster features a fast SSL encryption and decryption capability, with the full handshakes reaching up to 65,000 cps. This is at least 3.5 times faster than that when high-performance CPU is relied on, which greatly reduces the server costs, enhances the service capacity at the time of business volume and traffic surges and achieves a stronger computing-based anti-attack capability.
3. Support the uninstallation and translation of a variety of protocols. Reduce the stress involved in the adaption to various protocols of the client. The business back-end just needs to support HTTP1.1 to use various versions of protocols such as HTTP2, SPDY, SSL3.0 and TLS1.2.
4. One-stop service covering SSL certificate application, monitoring and replacement. By working with world-leading certificate providers including comodo and symantec, we have significantly simplified the certificate application procedures and reduced relevant costs.
5. Anti-CC and WAF capabilities Effectively prevent attacks at application layer such as slow connection, high-frequency targeted attack, SQL injection, website malicious code.

---


#2. HTTP and HTTPS Header Identifier


CLB will act as a proxy for HTTPS. Both HTTP and HTTPS requests will become HTTP requests when forwarded to the backend CVM by CLB. In this case, the developer will not be able to distinguish whether the front end request is HTTP or HTTPS.


Tencent CLB will implant X-Client-Proto into the header when it forwards the request to the backend CVM:


X - Client - Proto:  http (front end is an HTTP request)
X - Client - Proto:  https  (front end is an HTTPS request)
=======
## About Cloud Load Balance Capacity

Tencent Cloud's CLB has achieved significant improvement in HTTPS performance based on the full optimization of protocol stack and servers. At the same time, our cooperation with world-leading certificate providers results in a considerable cost-saving in certificates. Tencent Cloud's CLB brings substantial benefits for the business in the following aspects:
>>>>>>> origin/master

1. The use of HTTPS does not affect the access speed of client.
2. A single server in a cluster features a fast SSL encryption and decryption capability, with the full handshakes reaching up to 65,000 cps. This is at least 3.5 times faster than that when high-performance CPU is relied on, which greatly reduces the server costs, enhances the service capacity at the time of business volume and traffic surges and achieves a stronger computing-based anti-attack capability.
3. Support the uninstallation and translation of a variety of protocols. Reduce the stress involved in the adaption to various protocols of the client. The business back-end just needs to support HTTP1.1 to use various versions of protocols such as HTTP2, SPDY, SSL3.0 and TLS1.2.
4. One-stop service covering SSL certificate application, monitoring and replacement. By working with world-leading certificate providers including comodo and symantec, we have significantly simplified the certificate application procedures and reduced relevant costs.
5. Anti-CC and WAF capabilities Effectively prevent attacks at application layer such as slow connection, high-frequency targeted attack, SQL injection, website malicious code.
>>>>>>> Stashed changes

## HTTP and HTTPS Header Identifier

<<<<<<< Updated upstream
CLB will act as a proxy for HTTPS. Both HTTP and HTTPS requests will become HTTP requests when forwarded to the backend CVM by CLB. In this case, the developer will not be able to distinguish whether the front end request is HTTP or HTTPS.

Tencent CLB will implant X-Client-Proto into the header when it forwards the request to the backend CVM:

- X - Client - Proto:  http (front end is an HTTP request)
- X - Client - Proto:  https  (front end is an HTTPS request)


## Starting Configuration


Assume that a user needs to configure the website https://example.com. The developer wishes that users can directly access the site securely through HTTPS protocol simply by entering www.example.com in the browser.

=======
## HTTP and HTTPS Header Identifier

<<<<<<< HEAD

#3. Starting Configuration
=======
CLB will act as a proxy for HTTPS. Both HTTP and HTTPS requests will become HTTP requests when forwarded to the backend CVM by CLB. In this case, the developer will not be able to distinguish whether the front end request is HTTP or HTTPS.
>>>>>>> origin/master

Tencent CLB will implant X-Client-Proto into the header when it forwards the request to the backend CVM:

- X - Client - Proto:  http (front end is an HTTP request)
- X - Client - Proto:  https  (front end is an HTTPS request)


## Starting Configuration


Assume that a user needs to configure the website https://example.com. The developer wishes that users can directly access the site securely through HTTPS protocol simply by entering www.example.com in the browser.

>>>>>>> Stashed changes
In this case, the request forwading procudure of the user input "www.example.com" will be as follows:

1. The request is transmitted over HTTP protocol and will access port 80 of the cloud load balancer listener via VIP, then forwarded to port 8080 of the backend CVM.

2. By configuring rewrite operation on nginx of the Tencent Cloud backend server, the request will pass through port 8080 and be re-written to the https://example.com page.

3. Then the browser will send the https://example.com request to the corresponding HTTPS site again. The request will access port 443 of the cloud load balancer listener via VIP, then forwarded to port 80 of the backend CVM.

At this point, the request forwarding process is finished.

This operation rewrites the user's HTTP request into a more secure HTTPS request without being noticed by the user. To achieve the above request forwarding operation, the user can configure the backend server as follows:

```
server {

	listen 80; 
	server_name example.qcloud.com;

	location / {

		client_max_body_size 200m;
		rewrite ^/.(.*) https://$host/$1 redirect;

} 
}
```
