## Micro-service Architecture
The micro-service architecture is suitable for creating complex applications. It splits your monolithic application into multiple micro-services at different dimensions, and the content of each micro-service can be managed by using a Docker image.
**Advantages of Tencent Cloud's TKE deployed with micro-services**:
1. Cluster management is simplified. Installation and management of cluster is not required.
2. It seamlessly connects to Tencent Cloud's computing, network, storage, monitoring, security capabilities, and directly uses Tencent Cloud's IAAS capability.
3. It is easy to use, and supports service choreography and application management at service granularity. Resources are highly isolated while services are highly available.

![](https://main.qcloudimg.com/raw/a72d88c7decea42ae1bd4d5e851d34a9.png)

## Continuous Integration and Continuous Delivery
Excellent DevOps environment is provided through Continuous Integration and Continuous Delivery to greatly increase the efficiency of software publishing.
**Continuous Integration**: It allows developers to complete building and (unit) testing processes immediately after they submit new code. According to the test results, we can determine whether the new code and the original code can be properly integrated.
**Continuous Delivery**: It is used to deploy the integrated code to the operating environment based on Continuous Integration.

**Advantages**: 
By deploying services on Tencent Cloud TKE, developers can perform such operations as creation, testing, package and integration immediately after they submit new code. Then, they deploy the integrated code into the pre-release environment and existing network environment based on Continuous Integration.

![](https://main.qcloudimg.com/raw/e73913097243ee022ceda66c5985b375.png)

## Elastic Scaling

TKE features elastic scalability at both the cluster and service levels. It can automatically scale up or down by monitoring container indicators such as CPU, memory and bandwidth based on the operation status of the business. Meanwhile, it can automatically scale the cluster according to the deployment conditions of the container when resources are insufficient or excessive.

![](https://main.qcloudimg.com/raw/f603d876ba25baa9abce71a227c4a6f2.png)




