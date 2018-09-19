### Prerequisites of using Ingress
Ingress service supports three scenarios as follows:

- Access from public network
- Access within cluster only
- Access via private network in VPC

Ingress supports application-based LB. An appropriate port needs to be enabled for the backend container node of an application-based LB. By default, CVM port is enabled for access from public network and access via private network in VPC, while CVM port is disabled for access within cluster only. However, if Ingress is set, CVM port is automatically enabled for the backend service. Services with access method disabled do not support setting of Ingress.

You can flexibly set an access method with Ingress for your service. The method for accessing a service does not conflict with Ingress. You can use both of them as shown in the following figure:
![Alt text][roledemo]

### Wildcard in a domain name
A domain name must comply with the public network application-type load balancer domain name rules and Ingress domain name rules of Kubernetes:
1. It supports regular expression with a length limited to 1-80 characters.
2. Character sets supported by a non-regular domain name: a-z, 0-9, . and -.

A domain name with wildcard only supports the format of `\*.example.com`, and only one "*" can be used in a domain name.

### Example of Ingress setting

Create a backend service that needs to use Ingress:

- hello service: Port 80 is listened with the entry file in /path_hello/index.html
- bye service: Port 80 is listened with the entry file in /path_bye/index.html

Create an Ingress on the Ingress page (skip this step if an Ingress already exists).
![Alt text][create]

Resolve your domain name to the VIP of the load balancer. For more information, please see [Domain Name Resolution Help Documentation](https://cloud.tencent.com/document/product/302/3446).
In the example below, www.qcloudccs.com is resolved to sample load balancer.

Set Ingress forwarding rules:

![Alt text][set]

Access test:

![Alt text](https://mc.qcloudimg.com/static/img/4160d18aad9fd9d0da7b69cabce9f2f9/%7BEF8EA5D8-4859-4008-9E3C-B98E7E25AAAF%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/47d9eca8fef9f7c492c4033d8080a0ae/%7B1700D9DE-417D-4F3E-8E9E-0883FA9A5C5C%7D.png)




[roledemo]:https://mc.qcloudimg.com/static/img/fa7048f3ab7dc6aad9aa554b39b158a6/%7B7487A7E3-8BDD-44CB-81F9-38631784E0F0%7D.png
[create]:https://mc.qcloudimg.com/static/img/6dc5400d69b00794787bcfda3dd231bf/%7BE8312885-54E0-4D25-AFCA-59B6E2CA74C2%7D.png
[set]:https://mc.qcloudimg.com/static/img/b5cec3c1703b0a69bad15b7477d10017/%7B4833E8A7-E8E7-4FA9-81D3-50A2291F4E42%7D.png

