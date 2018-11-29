Tencent Cloud's Cloud Container Service (CCS) is a solution for container cluster building and OPS management for users, to seamlessly connect to Tencent Cloud's computing, network, storage, monitoring, security capabilities, and help users upgrade development mode, change application delivery, and reconfigure the data management mode. Tencent Cloud's CCS is designed to accelerate the deployment of applications, simplify the cluster management, and help enterprises migrate business into the cloud quickly.

The following concepts will help you get familiar with Tencent Cloud's CCS:

- **[Cluster](https://cloud.tencent.com/doc/product/457/6779)**: A collection of cloud resources required to run the container, which contains a few CVMs, load balancers, and other Tencent Cloud resources.
- **[Node](https://cloud.tencent.com/doc/product/457/6995)**: A CVM registered in the cluster.
- **[Service](https://cloud.tencent.com/doc/product/457/6780)**: A microservice comprised of multiple containers with the same configuration and rules for access to these containers.
- **[Image](https://cloud.tencent.com/doc/product/457/6781)**: The Docker image used to deploy CCS. Each image is specified with an unique ID (image's Registry address + image name + image Tag).

## Related Services

- A CCS cluster is made up of multiple purchased CVMs in which the containers are running. For more information, please see [Cloud Product Documentation](https://cloud.tencent.com/doc/product/213).
- The cluster can be created under the VPC, and the CVMs in the cluster can be allocated to subnets of different availability zones. For more information, please see [VPC Product Documentation](https://cloud.tencent.com/doc/product/215).
- The load balancer can realize automatic distribution of request traffic from clients across multiple CVM instances. For more information, please see [Load Balance Product Documentation](https://cloud.tencent.com/doc/product/214).
- Cloud Monitor can be used to monitor the operation statistical data for both CCS cluster and container pods. For more information, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/doc/product/248).

## CCS Pricing

CCS is provided free of charge now, and users are only charged for the resources they actually used. For more information about billing modes and prices, please see [CCS Pricing](https://cloud.tencent.com/doc/product/457/6770).

For all the supported operations, please see [API Overview](/doc/api/431/5852).

Before using these APIs, please make sure that you have a thorough understanding of [CCS Product Description](https://cloud.tencent.com/doc/product/457).









