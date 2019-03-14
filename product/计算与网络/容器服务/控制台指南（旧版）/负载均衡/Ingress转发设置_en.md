### Preconditions of Using Ingress
Ingress service supports three scenarios as follows:

- Access via Public network
- Access only within clusters
- Access via VPC

Now, Ingress supports application LB. The backend container nodes of application LB need to enable their corresponding ports. By default, server ports are enabled for public network accesses and VPC accesses, while server ports are disabled for accesses only within clusters. However, if the backend service is set for Ingress, server ports will be enabled automatically. The service disabling access methods does not support setting of Ingress.

You can flexibly set access methods with Ingress for your service. The method for accessing a service does not conflict with Ingress. You can use both of them as shown in the following figure:
![Alt text][roledemo]

### Domain Name Wildcard
The domain name configuration needs to comply with the domain rules of public network application load balancer and Ingress domain rules of kubernetes at the same time:
1. Supporting the regular expression with the length limit of 1-80.
2. Character sets supported by a non-regular domain name: a-z, 0-9, . and -.

A domain name with wildcards only supports the format of `\*.example.com` for now, and the wildcard * can only appear once in a single domain name.

### Configuring an Ingress Example

Create backend services that need to use Ingress:

- hello service: Port 80 is listened with the entry file in /path_hello/index.html
- bye service: Port 80 is listened with the entry file in /path_bye/index.html

Create an Ingress on the Ingress page (if an Ingress already exists, you can skip this step).
![Alt text][create]

Resolve the proprietary domain to the VIP of the load balancer. For more information, see [Domain Resolution Help](https://cloud.tencent.com/document/product/302/3446).
In the example below, www.qcloudccs.com is resolved to sample load balancer.

Set Ingress forwarding rules:

![Alt text][set]

Access test:

![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)




[roledemo]:https://mc.qcloudimg.com/static/img/fa7048f3ab7dc6aad9aa554b39b158a6/%7B7487A7E3-8BDD-44CB-81F9-38631784E0F0%7D.png
[create]:https://mc.qcloudimg.com/static/img/6dc5400d69b00794787bcfda3dd231bf/%7BE8312885-54E0-4D25-AFCA-59B6E2CA74C2%7D.png
[set]:https://mc.qcloudimg.com/static/img/b5cec3c1703b0a69bad15b7477d10017/%7B4833E8A7-E8E7-4FA9-81D3-50A2291F4E42%7D.png

