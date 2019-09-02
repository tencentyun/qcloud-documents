
## Product Overview
### Description
Tencent Cloud's Tencent Kubernetes Engines (TKE) is a container management service with high scalability and high performance. You can easily run applications on a hosted CVM pod cluster. With this service, you do not need to install, operate, maintain or expand your cluster management infrastructure. You can enable/disable Docker applications, query full status of the cluster, and use various cloud services by simply calling APIs. You can arrange containers in your cluster based on your resource needs and availability requirements, to meet the specific demands of your business or applications.

Based on native kubernetes, Tencent Cloud TKE is a container-based solution that solves environmental issues in the processes of development, testing, and OPS and helps users to reduce costs and improve efficiency. It is fully compatible with the native kubernetes API, and extends Tencent Cloud's kubernetes plug-ins such as CBS and CLB. Supported by Tencent Cloud's VPC, Tencent Cloud TKE also provides highly reliable and high-performance network solutions.
### Glossary

The following basic concepts can help you get familiar with Tencent Cloud TKE:
- **Cluster**: A collection of cloud resources required for the container to run, which contains CVMs, load balancers, and other Tencent Cloud resources.
- **Application**: A complete application composed of multiple services, which can be quickly deployed through templates.
- **Service**: A micro-service comprised of multiple instances with the same configuration and rules for accessing these instances.
- **Configuration Item**: A collection of multiple configurations, which helps you manage different businesses under different environments.
- **Ingress**: A collection of rules used to route external HTTP(S) traffic to service.
- **Image Repository**: Used to store Docker images for deployment of TKE.
- **Pod**: A pod consists of one or more relevant containers that share the same storage and network.

### How to use
You can run an application by following three steps as shown below.
1. Create a cluster
2. Create a service/application
3. Run the service/application

![][manual]

### Product pricing
No service fee is charged for TKE. The fee is only charged by the actual usage of cloud resources. For more information on billing methods and specific prices, please see [TKE Pricing](https://cloud.tencent.com/doc/product/457/6770).

### Related services

- You can purchase a TKE cluster comprised of several CVMs in which containers are running. For more information, please see [CVM product documentation](https://cloud.tencent.com/doc/product/213).
- A cluster can be created under a VPC. CVMs in the cluster can be assigned to subnets under different availability zones. For more information, please see [VPC product documentation](https://cloud.tencent.com/doc/product/215).
- You can use a load balancer to automatically assign the request traffic of clients across CVM instances and then forward to the containers in the CVMs. For more information, please see [Cloud Load Balance product documentation](https://cloud.tencent.com/doc/product/214).
- Cloud Monitor can be used to monitor the operation data of TKE clusters and container pods. For more information, please see [Cloud Monitor product documentation](https://cloud.tencent.com/doc/product/248).



[manual]:https://mc.qcloudimg.com/static/img/774df8af0eec5dec8ad2cb81f6f78d0c/%7B48AF112C-CA27-4932-9ADD-62617DF093F0%7D.png

