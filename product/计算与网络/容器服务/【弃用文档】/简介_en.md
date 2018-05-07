## Introduction

### What is Container?
Container is used to realize operating system virtualization. With a container, you can run applications and their dependent components under the condition where resources are isolated. CCS allows you to package the codes, configuration and dependent components of an application into an easy-to-use building block, to improve environment compatibility, implement version control, and increase operation efficiency and developer productivity. CCS can ensure that applications are deployed in a fast, stable and consistent manner without being affected by the deployment environment.
Docker is one of the container platforms. According to official definition, Docker uses Docker container as a basic unit to isolate resources and perform scheduling. It packages softwares into a full file system which contains softwares and everything required for the softwares to run, including codes, runtime libraries, system tools, system databases and so on, to ensure that the softwares can run regardless of the environment. Here is a figure from the [Official Docker Instruction](https://www.docker.com/what-docker).

![Alt text](https://mc.qcloudimg.com/static/img/3bdd67129c8cee8965898f267d7b881f/Image+057.png)

### What is Tencent Cloud CCS?
Tencent Cloud's Cloud Container Service (CCS) is a container management service with high scalability and high performance. You can easily run applications on a hosted CVM instance cluster. With this service, you don't need to install, operate, maintain or expand your cluster management infrastructure. You can enable and disable Docker applications, query all cluster statuses, use various cloud services by calling simple APIs. You can deploy containers in your cluster based on your resource needs and availability requirements, to meet the specific demands of business or applications.

Tencent Cloud's CCS involves the following concepts:

- Cluster: A collection of cloud resources required for the container to run, which contains a few CVMs, load balancers, and other Tencent Cloud resources.
- Node: A CVM registered in the cluster.
- Service: A microservice comprised of multiple pods with the same configuration and rules for accessing these pods.
- Batch task: One-time task which contains several pods. The difference between a task and a service is that a task will no longer provide service when stopped.
- Pod: A pod consists of one or more relevant containers, which corresponds to the "pod" of Kubernetes. These containers share the same storage and network.
- Image: Docker image used to deploy CCS. Each image has a unique ID (image's repository address + image name + image Tag).

Their relationship is shown in the figure below:

![Alt text](https://mc.qcloudimg.com/static/img/6ee1f51af42271069c9a46d46731370e/Image+053.png)


### How to Use Tencent Cloud CCS
See the following figure. After creating a cluster, you only need to use the image to create service, enter service configuration, wait for the service to be created before you can run the service.

![Alt text](https://mc.qcloudimg.com/static/img/cb0d84fd7c9547d492ab07f2992093d1/Image+054.png)

- Step 1: Create cluster
- Step 2: Create service
- Step 3: View service

We provide some examples on how to get started with CCS.

- [Create Simple nginx Service](https://cloud.tencent.com/document/product/457/7851)
- [Create Hello World Node.js Service](https://cloud.tencent.com/document/product/457/7204)
- [Create Wordpress with Single pod](https://cloud.tencent.com/document/product/457/7205)
- [Create Wordpress Service that Uses CDB](https://cloud.tencent.com/document/product/457/7447)

