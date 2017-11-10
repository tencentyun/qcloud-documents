Resource Limits on Container Services
### About "Request" and "Limit"

``request``: The minimum amount of resources used by the container, a criterion for resources allocation when you schedule the container. The container is scheduled to the node only when the amount of resource that can be assigned on the node >= the number of container resources requests. Parameter Request does not limit the maximum available resources for the container.

``limit``: The maximum amount of resources used by the container. A value of 0 indicates no upper limit to the amount of resources.

> For more information on ``limit`` and ``request``, click [here](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/)

### CPU Limits
You can set Request and Limit for the amount of CPU, which is measured in cpu units (U) and expressed with decimal points.
> 1. CPU Request is used as a criterion for users to assign CPU resources for the container on the node during creation. It is called the Assigned CPU Resources.
2. CPU limit specifies the maximum amount of CPU to reserve for a container. A value of 0 indicates no upper limit to the amount of CPU (CPU Limit >= CPU Request).

### Memory Limits
You can only set the maximum amount of memory available for the container. Memory is measured in MiB, and expressed with decimal points.
> 1. Memory can't be scaled. When memory used by the container exceeds Memory Request, the container may be killed. Therefore, to ensure normal operation of the container, Request should be equal to Limit.
 2. Memory Request (=Limit) is used as a criterion for users to assign memory resources for the container on the node during creation. It is called the Assigned Memory Resources.
 
### CPU Usage Vs. CPU Utilization
> 1. CPU usage indicates the number of physical CPUs used by the container. CPU usage is used to determine whether CPU resource exceeds the Request and the Limit.
2. CPU utilization is the ratio of CPU usage to number of CPU single cores (or number of CPU cores on the node)

### Example
A simple example is given here to illustrate the role of Request and Limit. A 4U4G node is provided in the trial cluster. Two Pods (1, 2) are deployed, each with resources configuration of (CPU Request, CPU Limit, Memory Request, Memory Limit) = (1, 2U, 1G, 1G).
(1.0 GB = 1000 MiB)
The usage of CPU and memory on the node is shown as below:
![Alt text](https://mc.qcloudimg.com/static/img/721a886f4ea3437d851c86770429827a/%7B2A75DFAF-761F-4A20-9AEC-FAE53719CC30%7D.png)
Assigned CPU resources: 1U (to Pod 1) + 1U (to Pod 2) = 2U; unassigned CPU resources: 2U
Assigned memory resources: 1G (to Pod 1) + 1G (to Pod 2) = 2G; unassigned memory resources: 2G
In such case, one Pod with (CPU Request, Memory Request) = (2U, 2G), or two Pods with (CPU Request, Memory Request) = (1U, 2G) can be deployed on the node.

For Pod (1, 2), (CPU Limit, Memory Limit) = (2U, 1G). That is, the maximum amount of CPU available for a Pod is 2U when the resource is idle.
