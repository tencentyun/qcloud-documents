
## 1. What to do if a CVM instance exception is indicated in the health check?
Please conduct troubleshooting using the following steps:
- Make sure that you access your application service directly via the CVM.
- Make sure that the relevant port has been opened on back-end CVM.
- Check whether there is security software like firewall inside the back-end CVM. These kind of software may cause the failure of cloud load balancer system to communicate with the back-end CVM.
- Check if the parameter settings of cloud load balancer health check are correct.
- It is recommended to use static page for health check.
- Check whether there is a high load on the back-end CVM that leads to a slow response of CVM.
- Make sure that there are no iptables restrictions on the submachine of CVM.

## 2. What to do if no policy file is returned and the connection is directly broken after a policy request (i.e. flash server request) is sent form port 843?
When the cloud load balancer has received policy request from port 843, it will return the common cross-domain policy configuration file. If no policy file is returned and the connection is directly broken, this may be caused by the incorrect flash server request.

Please make sure to send the flash server request correctly: <policy-file-request/>\0.
> Note: It must be ended with \0, and a total of 23 bytes are allowed. \0 stands for a character with accii code 0 and only occupies one byte.

Normally, the returned result of 843 request is as follows:
![](//mccdn.qcloud.com/static/img/992f21e3b38e45032e0904df0c6640bf/image.png)

## 3. Is the acquisition of real IP of client be supported?
Tencent Cloud's IP acquisition capability is automatically enabled, and the real IP of client can be acquired in the X-forwarded-for mode.

## 4. Which TCP ports can cloud load balance be applied to?
You can perform cloud load balance for the following TCP ports: 21 (FTP), 25 (SMTP), 80 (Http), 443 (Https), 1024-65535, etc.

## 5. How does cloud load balancer achieve session persistence based on cookies?

In the Cookie Insertion mode, CLB is responsible for inserting cookies without making any modification to back-end CVM. When the client makes the first request, the client HTTP request (without cookie) goes into CLB, which then selects a back-end CVM based on cloud load balance algorithm policy and sends the request to the CVM. Then the back-end CVM gives a HTTP reply (without cookie), which is sent back to CLB, and then CLB inserts the cookie into it and returns the HTTP reply (with cookie) to the client.

When the client makes the second request, the client HTTP request containing the cookie inserted by CLB last time goes into CLB, which then reads the session persistence values in the cookie and sends the HTTP request (with the same cookie as above) to the specified CVM. Then the back-end CVM gives a reply, and because the CVM does not write the cookie, the HTTP reply does not contain the cookie. When the reply traffic flows into the CLB again, the updated session persistence cookie will be written to CLB.

# # 6. What is the difference between Layer-4 and Layer-7 cloud load balance?
Layer-4 cloud load balance capability is based on IP and port, while Layer-7 cloud load balance capability is based on the application layer information such as HTTP header, URL, etc.

The difference between Layer-4 and Layer-7 cloud load balance lies in whether Layer-4 information or Layer-7 information is used as the basis for determining the way of forwarding traffic when cloud load balance is performed on back-end CVMs.  For example, Layer-4 cloud load balancer determines which traffic needs load balance based on Layer-3 IP address (VIP) and Layer-4 port number, performs NAT on the traffic to be processed and then forwards it to the back-end CVM. At the same time, it records which CVM has processed the TCP or UDP traffic, and forwards all the subsequent traffic of this connection to the same CVM for processing.

Layer-7 cloud load balancer takes application layer's characteristics into account on the basis of Layer-4 cloud load balancer. For example, for the same Web server, in addition to determining the traffic to be processed based on VIP and Port 80, Layer-7 cloud load balancer can decide on whether to perform load balance based on URL, browser category and language at Layer 7. Layer-7 cloud load balance is also known as "content exchange", which is designed to decide on the final choice of internal CVM based on the really meaningful application layer content in message and CVM selection method set for the cloud load balancer.

To select CVM based on the real application layer content, Layer-7 cloud load balancer must establish a connection with the client as a proxy of the final CVM (three-way handshake) to receive the message containing real application layer content from client, and then determines the final choice of the internal CVM according to the specific fields in the message plus the server selection method set for the cloud load balancer. In this case, the cloud load balancer is more like a proxy server. The cloud load balancer will establish TCP connection with front-end client and back-end CVM separately.

## 7. Can CVM forward traffic from port a on server A to another port on the same server by configuring private network-based cloud load balancer?
No. For the access to port a on server A (10.66.\*.101), the request can be forwarded to port b on server B (10.66.\*.102) through private network-based cloud load balancer. But the traffic cannot be forwarded to port b on the same server A (10.66.\*.101).

## 8. What is the back-end CVM weight?
Users can specify the forwarding weight for each CVM in the back-end CVM pool, and the CVM with a higher weight ratio will be assigned more access requests. Users can set the weight for back-end CVMs individually based on their service capabilities and statuses.

If you have enabled session persistence feature at the same time, the accesses to the back-end application servers may be not exactly the same. You're recommend to temporarily disable the session persistence feature and then observe whether the problem still persists.

## 9. What is the difference between UDP and TCP protocols?
TCP is a connection-oriented protocol. Therefore, when TCP is used, it is necessary to establish a reliable connection with the other side before receiving and sending data. UDP is a non-connection-oriented protocol, and it directly sends data packets without performing three-way handshake with the other side. UDP is suitable for the scenarios focusing more on real-timeness than reliability, such as video chat, real-time push of financial market information, DNS, Internet of Things, etc.

## 10. Does the back-end CVM need public network bandwidth? Will it affect the service of cloud load balancer?
No traffic or bandwidth fee is charged for cloud load balancer. Any public network traffic generated by the cloud load balance service will be charged to the bill for the back-end CVM. You're recommended to choose "Bill by Traffic" for public network bandwidth when purchasing back-end CVM and and set a reasonable peak bandwidth cap, so that you do not need to keep track of the fluctuation of total traffic of CLB egresses. Web traffic on the Internet has a considerable fluctuation that can not be predicted accurately. When "Bill by Bandwidth" is selected, it is not cost-effective if excessive bandwidth is purchased, and packet loss may occur during business peak if insufficient bandwidth is purchased.

## 11. HTTP redirection in load forwarding
When you visit the website `http://example.com` through a browser, a redirection to the root directory is required for the CVM. When you visit the website `http://example.com/` through the browser, the CVM will directly return the default page of root directory set by the site. Similarly, if `http://cloud.tencent.com/movie` is redirected to`http://cloud.tencent.com/movie/` through URL rewriting, then entering `http://cloud.tencent.com/movie` will result in an additional URL rewriting process, leading to slight performance degradation and time consumption.  But there is no difference in the result. However, if `http://cloud.tencent.com/product` is redirected to a page other than `http://cloud.tencent.com/product/` through URL rewriting, you need to consider whether to add "/" after the secondary URL.

In Tencent Cloud's cloud load balancer, if front-end port number is different form the back-end one, "/" needs to be added after the secondary URL upon the visit to secondary page to avoid the change of port number after the HTTP redirection and ensure the normal visit to the page.

Assume that in Layer-7 forwarding, port 80 on cloud load balancer instance and port 8081 on the back-end CVM are listened. If the client accesses `http://www.example.com/movie`, the access request is forwarded to the back-end CVM via cloud load balancer, and then the CVM redirect the request to `http://www.example.com:8081/movie/ `(listened port is 8081). In this case, the client access fails (port error).

Therefore, it is recommended to rewrite the access request to the secondary URL with "/", such as `http://www.example.com/movie/ `. This can avoid HTTP redirection, eliminate the need to make unnecessary judgment and reduce unwanted load. If it is necessary to use HTTP redirection, please make sure that the cloud load balancer's listened port is the same as that of the back-end CVM.

## 12. Notes about compatible versions in case of inconsistency of HTTP versions between client and server

### Forwarding Compatibility
- For the front end (client), HTTP1.0/1.1 and backward compatibility are supported.
- For the back end (server), Tencent Cloud currently uses HTTP1.0 protocol. HTTP1.0 / 1.1 and backward compatibility are supported.

> Note: HTTP/2 is only supported in HTTPS, and backward compatibility is allowed on both client and server. HTTP protocol is not supported currently 

### Support for Gzip Compatibility
- For the front end (client side), HTTP1.0/1.1 and backwards compatibility are supported. (Additional configuration is not needed, since mainstream browsers all support Gzip)
- For the back end (server), users need to set the earliest version of HTTP supporting Gzip to HTTP1.0 in nginx, so that it can be compatible with the HTTP1.0 version being used by Tencent Cloud. (Otherwise it will default to HTTP1.1 in nginx) For more information on the configuration, refer to [here](https://cloud.tencent.com/doc/product/214/5404)

> Note:  HTTP/2 is only supported in HTTP, but Gzip can be used in any HTTP versions supported by Tencent Cloud

## 13. How to make the settings for the security group of cloud load balancer back-end CVM? How to set the access blacklist?

### Security Group Configuration for Cloud Load Balancer
If security group rules have been set for the back-end CVM, it is likely that the cloud load balancer instance cannot communicate with the CVM. Therefore, in Layer-4 forwarding and Layer-7 forwarding, it is recommended to set the security group of back-end CVM to "Allow ALL". If the security group is opened up, you need to configure the security group rules for the accesses from all client IPs to the local IP. For some malicious IPs, you can add these IPs to the top rules of the security group to prevent them from accessing the back-end CVM; and then allow the accesses from all IPs (0.0.0.0) to the local service port, so that the normal clients can access the CVM.  (Security group rules are arranged in priority order and are matched from top to bottom)

If health check has been set for Layer-7 cloud load balancer forwarding in VPC, please also note that the cloud load balancer's VIP needs to be added to the allow rule of the back-end CVM security group, otherwise the health check may fail.

### Setting Access Blacklist
If you need to set a blacklist for some client IPs to deny their accesses, you can configure the security group associated with the cloud services. The security group rules need to be configured as follows:
- Add the client IPs from which access will be denied plus ports to the security group, and choose "deny the access from the IPs" in the Policy section.
- When the setting is made, add another security group rule that allows all accesses to the port from all IPs by default.
When the configuration is completed, the security group rules are as follows:
```
clientA ip+port drop
clientB ip+port drop
0.0.0.0/0+port accept
```
Note:***The above configuration steps should be performed in a correct order, otherwise the blacklist configuration cannot take effect.***

For more information about security groups, refer to [Access Control for the Back-end CVM](https://cloud.tencent.com/doc/product/214/6157#.E8.B4.9F.E8.BD.BD.E5.9D.87.E8.A1.A1.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E6.8E.A8.E8.8D.90.E8.A7.84.E5.88.99)

## 14. Notes about the ability of private network-based CLB to directly acquire client IP

The following notes apply to the private network-based CLB (choose private network VPC) purchased after October 24, 2016. The private network-based CLB will no longer perform SNAT processing. The access IP acquired from the server is the real client IP and no additional configuration is required. To ensure that your business operates properly, please note the followings:

1. For the private network-based CLB purchased after October 24, 2016, when the security group policy is enabled, the inbound access from client IP must be allowed to ensure normal access.

2. If necessary, you can switch the existing private network-based CLB to the new one by submitting a ticket to the after-sales team. After the switching, the access IP acquired from the server side is the client IP. A several-minute business interruption may occur during the switching.


