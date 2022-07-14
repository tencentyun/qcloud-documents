## Forwarding Configuration of Load Balancer

## About Load Balancer
The container services support Layer-4 and Layer-7 forwarding load balancers to forward traffic to the container. The Layer-4 supports public network-based and private network-based load balancers. For more information, please see [Load Balancer Introduction](https://cloud.tencent.com/document/product/214/524). This document focuses on how container services use Layer-7 load balancer.

### Preconditions for Application-based Load Balancer
You can create services by the following 4 access options:

- by load balancer (public network-based, Layer-4, TCP/UDP) - Available
- by load balancer (private network-based, Layer-4, TCP/UDP) - Available
- by CVM port - Available
- only within the cluster - not available

If you forward traffic to the CVM and then to the container by load balancer, you need enable the port for the backend RS of load balancer (the container node). So application-based load balancer is not available for services accessed only within the cluster.
You can use either Layer-4 or Layer-7 load balancer to set the access to your services. In other words, you can use private network-based and application-based load balancer. So a services can be accessed wither via private or public network to suit your individual business demands.


### Configuring Application-based Load Balancer
If you want to configure application-based load balancer for services, services must be accessed using Layer-4 load balancer or using CVM port for communication. Applicable-based load balancer is not mutually exclusive with private network-based and public network-based load balancer.
First, create a backend service that requires application-based load balancer, for example:
Backend service:

- hello service: Port 80 is listened with the entry file in /path_hello/index.html 
- bye service: Port 80 is listened with the entry file in /path_bye/index.html

Create an application-based load balancer on the load balancer page. You can skip this step if you already have the load balancer.
![Alt text](https://mc.qcloudimg.com/static/img/a3b194503971f8bdd1147852496abeba/%7B946ED9B7-80DA-4FCC-80B9-AF02897B1BD1%7D.png)

For more information on how to resolve proprietary domain to the VIP of the load balancer, please see [Domain Resolution Help](https://cloud.tencent.com/document/product/302/3446).
In the example below, www.qcloudccs.com is resolved to sample load balancer.

Configuring the forwarding rules of application-based load balancer

![Alt text](https://mc.qcloudimg.com/static/img/cb9e6912f2dccd99e86833dea18d3965/%7B537EFD34-F43E-439E-8D22-BB77BFCB29E5%7D.png)

Access test:

![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)

