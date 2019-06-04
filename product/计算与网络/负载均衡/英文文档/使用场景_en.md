The following is an example of a two-way hiding of (outbound public network access/public network access) backend server cluster:
![](//mccdn.qcloud.com/static/img/fca01bf18ea9e6a30081c7ed5a001779/image.png)

Cloud server (VM2, VM3) does not have public IP, and cannot take the initiative to communicate with the public network.
- When CVM cluster needs to access the public network, the routing table is configured and NAT forwarding is performed through an Internet gateway (VM1). For resources on the Internet, the request address is always the public network IP (115.159.45.144) of Internet gateway, and the resources on the Internet are never exposed to the backend server cluster.
- When resources on the Internet access services on the CVM, the access must be conducted through a unified cloud load balance service VIP (115.159.17.247). The cloud load balancer is responsible for delivering all requests to the backend servers using a certain policy, and Internet is never exposed to the backend servers.

Cloud load balance can be applied primarily to the following scenarios:

- Scaling-out service capabilities of the application system, applicable to all kinds of web servers and app servers.
- Eliminating single point of failure on the application system. If a part of the CVM instances crash, the application system can still work properly.

## Traffic Delivery
- By configuring cloud load balance virtual service address (VIP) and website domain name, multiple web access layer servers are virtualized into an access layer service pool with high performance and high availability. All public network requests go through CLB, providing security while saving public IP address resource.
- Cloud load balancer will ensure that requests are evenly forwarded to each access layer server, which can carry the load using inexpensive, similarly configured virtual machines or Docker containers
![](//mccdn.qcloud.com/static/img/6585e3793ca8a62f369886a0bfb8a95b/image.jpg)

## Scale-out
- Cloud load balancer, combined with Autoscaling dynamic auto scaling group, allows you to automatically create and release CVM instances. The access layer web server can adjust accordingly as the access pressure of the public network increases/decreases.
- In case of "double 11", "6.18" and other large-scale promotional activities of e-commerce vendors, web traffic may surge by 10 folds in an instant, and last for only a few hours. Using cloud load balance and Autoscaling can minimize IT cost
![](//mccdn.qcloud.com/static/img/12c928f0c558e9b5340ae4a6abf6e57c/image.jpg)

## Service Separation
- For typical web services such as forums, websites, etc., it is recommended to separate image services, text services and other different services, which will facilitate web development and iteration
- After the services are separated, each cloud load balancer instance and its associated backend server group will act as a separate service cluster
- You can perform CNAME switching at DNS service providers (such as DNSpod) in order to achieve domain name redirection between different services
- Large websites usually have hundreds of sub service modules. You can use cloud load balance and DNS resolution to converge addresses for accessing portal home page into a cloud load balancer public network address and a proprietary domain. This will facilitate client access
![](//mccdn.qcloud.com/static/img/4ac58aa5cd4385f9316a2099503b911c/image.png)

