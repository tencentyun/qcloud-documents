Tencent Cloud launched **public network application LB** with exclusive capability of custom redirection in April which can solve two major problems:

1. Forced HTTPS: When Web service and LoadBalance proxy are accessed by PC and mobile browsers via HTTP requests, HTTPS respond is returned. By default, HTTPS is used to access web pages.
2. Custom redirection: When Web services need to be temporarily deactivated (in case of selling-out of e-commerce, page maintenance and upgrade), redirect capability is necessary. Without redirections, visitors can only get a `404/503` error message caused by old address in users' favorites and search engine database, which reduces user experience and results in access traffic loss. In addition, the search engine scores accumulated on this page will also be wasted.

## I. CLB Acts as a Proxy for HTTPS Requests

### 1. Traditional Solutions to nginx

#### A. Solution Description

Assume that a developer has purchased a cloud load balancer with 100 CVMs bound with its backend to configure the website https://example.com. The developer wants to realize that users can directly access the site securely through HTTPS protocol simply by entering www.example.com in the browser. (That is, regardless of HTTP/HTTPS requests, the encrypted HTTPS is returned).
In this case, the request forwarding procedure of the user entering "www.example.com" will be as follows:
The request is transmitted over HTTP protocol and will access port 80 of the cloud load balancer listener via VIP, and then is forwarded to port 8080 of the backend CVM.
By configuring rewrite operation on nginx of the Tencent Cloud backend server, the request will pass through port 8080 and be re-written to the https://example.com page.
Then the browser will send the https://example.com request to the corresponding HTTPS site again. The request will access port 443 of the cloud load balancer listener via VIP, and then is forwarded to port 80 of the backend CVM. At this point, the request forwarding process is finished. The architecture is as follows:

![](https://mc.qcloudimg.com/static/img/b5d0efa20da5872ac3d29a41fd29d945/11.jpg)

#### B. Detailed Configuration
1. When the domain names of the HTTP and HTTPS services requested by the user are the same and the default HTTPS port is 443, to achieve the above request forwarding operation, the user can configure the backend server as follows:
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://$host/$1 redirect;   //Perform rewrite configuration on CVM
} 
}
```

2. When the domain names of the HTTP and HTTPS services requested by the user are different or the default HTTPS port is not 443, to achieve the above request forwarding operation, the user needs to specify URL and port and configure the backend server as follows:
```
server {
    listen 80; 
    server_name example.com;

    location / {
        client_max_body_size 200m;
        rewrite ^/.(.*) https://xxx.xxx.xx:10011/x redirect;   //Perform rewrite configuration on CVM
} 
}
```

#### C. CLB Acts as a Proxy for HTTPS

In the above architecture, CLB mainly acts as a proxy for HTTPS. Thus CLB always forwards HTTP requests to backend CVM regardless of HTTP/HTTPS requests. At this point, **When client forwards HTTPS requests to LB, the requests are encrypted while for the transmission from LB to the backend server, plaintext transmission is used as before.** In this case, the developer cannot distinguish whether the front end request is HTTP or HTTPS.

In order to solve this problem, Tencent CLB will implant X-Client-Proto into the header when it forwards the request to the backend CVM to facilitate developers to determine the type of request based on the header content:
- X-Client-Proto: http (front end is an HTTP request)
- X-Client-Proto: https (front end is an HTTPS request)

#### D. Existing Problems
- Complicated configuration: If you have multiple domain + uri and 100 backend CVMs, you need to repeat the configuration on 100 CVMs. And for each additional domain + uri, you need to refresh it on 100 backend CVMs.
- Computing overhead: redirection judgment consumes CPU resources of backend CVMs.


### 2. CLB Forced HTTP Redirection Solution

#### A. Solution Description
Assume that a developer needs to configure the website https://example.com. The developer wishes that users can directly access the site securely through HTTPS protocol simply by entering www.example.com in the browser. For www.example.com, multiple addresses exist, and there may be hundreds of URLs associated with the backend (regular match), and hundreds of real servers. Therefore, it is difficult to configure one by one. Tencent Cloud supports one-click forced HTTPS redirection.

First, configure the LB HTTPS listener in [Tencent Cloud Load Balance Console](https://console.cloud.tencent.com/loadbalance/index?rid=1), that is, to set up Web environment for https://example.com.
![](https://mc.qcloudimg.com/static/img/61a723a69c581968a46fe86447f1473a/1111.jpg)
Second, enable redirection capability in the application cloud load balancer console. Now overall redirection is supported on domain name level.
![](https://mc.qcloudimg.com/static/img/e066362fed8d3cf7740dd50c49c6004b/2222.jpg)

#### B. Solution Advantages
- Configure once only: Forced HTTPS redirection can be completed with one domain name and one-time configuration.
- Update: If URLs of HTTPS service change in number, you just need to refresh again with the feature in the console.

## II. Notes
- Session persistence: If the client has accessed example.com/bbs/test/123.html and the session persistence is enabled for backend CVM, when redirection is enabled to divert traffic to example.com/bbs/test/456.html, the original session persistence mechanism will expire.
- TCP/UDP redirection: IP + Port level redirection is not supported for now and will be available in subsequent versions.

