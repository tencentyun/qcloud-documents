
## Product Advantages


### Orchestration advantages
Kubernetes-based services
Tencent Cloud TKE is developed on the basis of Kubernetes (k8s), a container cluster management system provided open source by Google. Using Docker technology, Kubernetes offers a complete set of features (including deployment and execution, resource scheduling, service discovery, and dynamic scaling) to containerized applications, making it much easier to manage large-scale container clusters.


**Benefits of Kubernetes**
- Using elegant software engineering design such as modularization and micro-service, Kubernetes provides a modular design that allows users to customize network, storage, scheduling, monitoring, and log modules as needed through flexible plugins.
- Kubernetes project community provides an open source platform for the implementation of container, network, and storage.
- Kubernetes Vs. other container orchestration tools (Swarm/Mesos)
  Vs. Swarm: Kubernetes has finer granularity and more features, including advanced features such as key management, configuration management, and auto-scaling.
  Vs. Mesos: Mesos focuses on resource scheduling while Kubernetes concentrates on distributed applications, micro-service and large-scale cluster management, which integrates the exclusive concept of "cluster management is not just resource scheduling and orchestration" proposed by Google.


### Tencent Cloud's TKE Vs. Self-built TKE

| Advantage | Tencent Cloud's Tencent Kubernetes Engines (TKE) | Self-built TKE |
|---------|---------|---------|
| Easy to use | <b>Simplified cluster management</b><br> <li>Tencent TKE provides large-scale container cluster management, resource scheduling, container arrangement, and code construction features. It blocks the differences of underlying infrastructures as well as simplifies management, operation and maintenance processes for distributed applications. You no longer need to use cluster management software or design fault-tolerating cluster structures, thus avoiding all relevant management or expansion works.<li>You simply need to enable the container cluster and specify the tasks you want to run. Tencent TKE will then help you complete all cluster management jobs, which allows you to concentrate on developing Dockerized applications. | When using self-built container management infrastructures, you usually need to go through complex management processes. For example: install, operate, expand your own cluster management software as well as configure management systems and monitor solutions. |
| Flexible to scale | <b>Flexible cluster hosting and integrated load balancer</b><br> <li>You can use TKE to schedule long-running applications and batch jobs flexibly. You can also use APIs to obtain the latest cluster status to integrate your customized scheduling applications with third-party scheduling applications.<li> Tencent Cloud's TKE is integrated with load balancers. You can assign traffic among multiple containers. You can simply specify container configuration and load balancers you want to use, and then the TKE management application automatically adds/deletes resources for you. In addition, Tencent Cloud's TKE is able to auto-recover containers with poor operation status to ensure the number of containers satisfies your demand, providing enough support for applications. | You need to determine how to manually deploy container services according to business traffic and health status, which has poor availability and scalability. |
| Secure and stable | <b>High isolation of resources and high availability of services</b><br><li>TKE launches inside your own cloud server instance without sharing computing resources with other customers.<li>Your clusters run inside VPCs, so you may use your own security groups and network ACL. These features provide high isolation level and can help you use CVMs to construct applications with high security and reliability.<li>TKE uses a distributed service structure to ensure auto failure recovery and fast migration for services, while combining distributed storage of the stateful service backend to provide security and high availability for services and data. | Due to kernel issues and incomplete Namespace of self-built container services, isolation for tenants, devices, and kernel modules are rather poor. |
| Efficient | <b>Quickly deploy images and keep businesses constantly integrated</b><br><li>Tencent TKE runs inside your VPCs, where quality BGP network ensures fast upload/download speed for images and allows massive containers to launch within seconds, greatly reducing operation cost while helping you to focus more on business operation.<li>You can deploy businesses on Tencent TKE. When developers submit codes on Github or other code platforms, the TKE immediately creates, tests, packs, integrates and puts the integrated codes into the pre-release environment and existing network environment. | The efficiency for using images to create containers is not ensured, as the network quality of self-built container services cannot be guaranteed. |
| Low-cost | <b>TKE is provided free of charge</b><br>There is no extra fee for using Tencent TKE. You can call APIs to create your cluster management applications in containers for free. You only need to pay for cloud service resources you created for storage and running applications, such as CVMs and Cloud Block Storage. | You need to make investment to create, install, operate, maintain, and expand your own cluster management infrastructure, which costs a lot. |

### Tencent Cloud's TKE Monitoring Vs. Self-built Container Monitoring
Tencent Cloud's TKE monitoring collects and display data for container clusters, services, and instances. With TKE monitoring, you can view the monitoring data from about 30 metrics (more will be added) including cluster, service, instance and container, check whether the cluster runs properly, and create alarms accordingly.

| Advantage | Tencent Cloud's Tencent Kubernetes Engines (TKE) | Self-built TKE |
|---------|---------|---------|
| Complete metrics | About 30 metrics are used, including cluster, service, container, and pod. | Incomplete metrics, more yet to be developed. |
| Low creation cost | CSS monitoring is provided when a cluster is created. | Need to be created manually and cost a lot |
| Low OPS cost | Operated and maintained by the platform. Data accuracy is guaranteed. | Need to be maintained manually. |
| Low storage cost | Each metric's data in the last three months is saved for free. | Subject to the storage size |
| High scalability | TKE is optimizing and adding new metrics. | Technicians are needed to develop new metrics. |
| Alarm | Yes | No |
| Troubleshooting | You can check the container log in the console and use webshell to log in to the container upon one-click for troubleshooting. | The container needs to be logged in to manually and relevant machines are required for troubleshooting.|

