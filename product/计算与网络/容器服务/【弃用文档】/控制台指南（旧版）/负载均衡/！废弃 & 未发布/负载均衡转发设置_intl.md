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
![Alt text](https://mc.qcloudimg.com/static/img/07d662f17350b181c8e1c854a617c496/ccs_revise_1.jpg)

For more information on how to resolve proprietary domain to the VIP of the load balancer, please see Domain Resolution Help.
In the example below, ```www.qcloudccs.com``` is resolved to sample load balancer.

Configuring the forwarding rules of application-based load balancer

![Alt text](https://mc.qcloudimg.com/static/img/e88de390a8f1b7566c8260b98aaf62f6/ccs_revise_2.jpg)

Access test:

![Alt text](https://mc.qcloudimg.com/static/img/893dd58c442a8396029e68a3bfc468a2/lb_3.jpg)
![Alt text](https://mc.qcloudimg.com/static/img/9f99882c40d07a5ec010bc10b55254e1/lb_4.jpg)
