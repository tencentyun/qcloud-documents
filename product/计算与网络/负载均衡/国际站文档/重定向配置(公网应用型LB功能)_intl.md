LoadBalance team has launched the exclusive capability of **public network application-based LB** in April: custom redirect. This feature can solve two major problems:

1. Forced HTTPS: With LoadBalance proxy, when Web service is accessed by browsers on PC and mobile via HTTP requests, the HTTPS respond is returned. By default, HTTPS is used forcibly by browsers to access web pages.
2. Custom redirect: When Web services need to be temporarily deactivated (in case of e-commerce products sold out, page maintenance, update and upgrade), redirect capability is required. Without redirect, visitors can only get a `404/503` error message caused by old address in users' favorites and search engine database, which affects user experience and results in access traffic loss. In addition, the search engine scores accumulated on this page are also wasted.

## 1. CLB Acts as a Proxy for HTTPS Requests

### 1.1 Traditional solution of nginx

#### (1) Solution description

Assume that a developer has purchased a load balancer bound with 100 backend CVMs to configure the website https://example.com. The developer wants users to directly access the website securely through HTTPS protocol by simply entering www.example.com in the browser. (That is, regardless of HTTP/HTTPS requests, HTTPS response is returned to force the use of encryption capability)
In this case, the request for accessing www.example.com entered by user is forwarded as follows:
The request is transmitted over HTTP protocol and accesses port 80 of the load balancer listener via VIP. Then, it is forwarded to port 8080 of the backend CVM.
By configuring rewrite operation on nginx of the Tencent Cloud backend CVM, the request passes through the port 8080 and is re-written to the https://example.com page.
The browser sends the https://example.com request to the corresponding HTTPS site again. The request accesses port 443 of the load balancer listener via VIP, and is forwarded to the port 80 of the backend CVM. Now, the request forwarding process is finished. The figure below shows the architecture:

![](https://mc.qcloudimg.com/static/img/b5d0efa20da5872ac3d29a41fd29d945/11.jpg)

#### (2) Detailed configuration
1. If the domain names of the HTTP and HTTPS services requested by a user are identical and the default HTTPS port is 443, the backend CVM can be configured as follows to achieve the above request forwarding operation:
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://$host/$1 redirect;   //Configure rewrite on CVM
} 
}
```

2. If the domain names of the HTTP and HTTPS services requested by a user are different or the default HTTPS port is not 443, the user needs to specify URL and port and configure the backend CVM as follows to achieve the above request forwarding operation:
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://xxx.xxx.xx:10011/x redirect;   //Configure rewrite on CVM
} 
}
```

#### (3) CLB acts as a proxy for HTTPS

In the above architecture, CLB mainly acts as a proxy for HTTPS. Both HTTP and HTTPS requests will become HTTP requests when forwarded to the backend CVM by CLB. Therefore, **if HTTPS protocol is used, the request is encrypted when transmitted from client to LB. However, the request is still transmitted as plaintext from LB to the backend CVM.** In this case, the developer cannot distinguish between HTTP and HTTPS requests.

To solve this problem, X-Client-Proto is placed into the header when Tencent CLB forwards the request to the backend CVM to help the developer determine the request type based on the header content:
- X-Client-Proto: http (frontend request is an HTTP request)
- X-Client-Proto: https (frontend request is an HTTPS request)

#### (4) Existing problems
- Complicated configuration: If you have multiple domain + uri and 100 backend CVMs, you need to repeat the configuration on 100 CVMs. And for each additional domain + uri, you need to refresh it on 100 backend CVMs.
- Computing cost: Determining whether redirect is required consumes CPU resources of backend CVMs.


### 1.2 Forcibly redirect HTTP request from CLB

#### (1) Solution description
Assume that a developer needs to configure the website https://example.com. The developer wants users to directly access the website securely through HTTPS protocol by simply entering www.example.com in the browser. www.example.com is not merely an address, and hundreds of URLs may be associated at the backend (with regular expression matching), which leads to hundreds of real servers. Therefore, it is difficult to configure CVMs one by one. Tencent Cloud supports forcing HTTPS redirect with just one click.

First, configure the LB HTTPS listener in the [Tencent CLB console](https://console.cloud.tencent.com/loadbalance/index?rid=1) to set up Web environment for https://example.com.
![](https://mc.qcloudimg.com/static/img/61a723a69c581968a46fe86447f1473a/1111.jpg)
Second, enable redirect in the application-based CLB console. Overall redirect at the domain name level is supported.
![](https://mc.qcloudimg.com/static/img/e066362fed8d3cf7740dd50c49c6004b/2222.jpg)

#### (2) Solution advantages
- Configure once only: Forced HTTPS redirect can be implemented with one domain name and one-time configuration.
- Update: If the number of URLs of HTTPS service changes, you just need to use this feature again in the console for a refresh.

## 2. Notes
- Session persistence: If the client has accessed example.com/bbs/test/123.html and the session persistence is enabled for the backend CVM, when redirect is enabled and traffic flows into example.com/bbs/test/456.html, the original session persistence mechanism will become invalid.
- TCP/UDP redirect: Redirect at IP + Port level is not supported, but will be available in subsequent versions.

