## TCP/UDP Protocol
Acceleration connection can be accessed by the following ways:
- The client accesses the "VIP + port" of the acceleration connection.

- The client accesses the "domain name + port" of the acceleration connection. 

- If the client originally accesses a domain name, configure a cname to resolve this domain name to that of the acceleration connection, or modify the local host of the client to resolve the original domain name to the acceleration connection's VIP.
If the origin server needs to get the real client IP (TCP protocol only), TOA module should be installed. For more information, please see [Get Real Client IPs (TCP)](/document/product/608/14427).

## HTTP/HTTPS Protocol
Configure a cname to resolve the domain name accessed by the client to acceleration connection's domain name, or modify the local host of the client to resolve the domain name to be accessed by the client to the acceleration connection's VIP, so that the client can access the connection with `protocol + URL` to achieve acceleration.
The origin server can directly get the real client IP from the `x-forward-for` field in the HTTP request header.

