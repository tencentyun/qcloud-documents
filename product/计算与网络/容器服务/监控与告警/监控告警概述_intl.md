## Monitor Alarm Overview

### Overview
In order to maintain high reliability, high availability and high performance of Tencent Cloud TKE, it is important to provide a good monitoring environment. Users can collect monitoring data at different dimensions for different resources, to obtain resource usage information and locate errors quickly.

Tencent Cloud's Cloud Monitor provides data collection and presentation features for container clusters, services and pods. With Tencent Cloud's Cloud Monitor, you can view the statistical data of clusters, nodes, services and pods to verify whether the cluster is running normally as well as create relevant alarms. For more information about Cloud Monitor, please see [Cloud Monitor Documentation](https://cloud.tencent.com/document/product/248).

Collecting monitoring data allows you to establish normal standards regarding container cluster performance. By testing the performance of a container cluster and collecting historical monitoring data at different times and under different load conditions, users can better understand the normal performance of a running container cluster and service, and quickly determine whether the running service is exceptional based on the current monitoring data, in order to find out solutions in time. For example, users can monitor the CPU utilization, memory utilization and disk I/O of a service.

### Monitoring

Cloud Monitor provides monitoring metrics at the following dimensions for TKE:

#### Cluster Monitoring Metrics

namespace:qce/cvm

| Monitoring Item | Monitoring Metric | Unit  | Description  |
|---------|---------|---------|-----|
| Cluster CPU utilization |  dc_cpu_usage | % | Average CPU utilization of the nodes in the cluster |
| Cluster memory utilization |  dc_mem_usage | % | Average memory utilization of the nodes in the cluster |

For more information about the monitor metrics of CVMs in clusters and how to obtain monitoring data, please see [Monitor CVM](https://cloud.tencent.com/document/product/213/5178).

#### Service Monitoring Metrics

namespace:qce/docker
View: docker_service

| Monitoring Item | Monitoring Metric | Unit  | Description  |
|---------|---------|---------|-----|
| Service CPU usage | service_cpu_used | Core | Total CPU used by all container pods in the service |
| Service CPU utilization (ratio to cluster) | service_cpu_usage_for_cluster | % | The ratio of service CPU utilization to the cluster |
| Service memory usage | service_mem_used | MiB | Total amount of memory used by all the container pods in the service |
| Service memory utilization (ratio to cluster) | service_mem_usage_for_cluster | % | The ratio of service memory utilization to cluster |
| Service network inbound traffic | service_in_flux  | MB | Total inbound traffic of all the pods in the service within the time window |
| Service network outbound traffic | service_out_flux | MB | Total outbound traffic of all the pods in the service within the time window |
| Service network inbound bandwidth | service_in_bandwidth | Mbps | Total inbound bandwidth of all the pods in the service |
| Service network outbound bandwidth | service_out_bandwidth | Mbps | Total outbound bandwidth of all the pods in the service |
| Service network inbound packets | service_in_packets | pps | Total inbound packets of all the pods in the service |
| Service network outbound packets | service_out_packets | pps | Total outbound packets of all the pods in the service |

#### Pod Monitoring Metrics

namespace:qce/docker
View: docker_pod

| Monitoring Item | Monitoring Metric | Unit  | Description  |
|---------|---------|---------|-----|
| Pod network inbound bandwidth | pod_in_bandwidth | Mbps | Containers in the same pod share the same network. This is the inbound network bandwidth of the pod |
| Pod network outbound bandwidth | pod_out_bandwidth | Mbps | Containers in the same pod share the same network. This is the outbound network bandwidth of the pod |
| Pod network inbound traffic | pod_in_flux | MB | Containers in the same pod share the same network. This is the inbound network traffic of the pod |
| Pod network outbound traffic | pod_out_flux | MB | Containers in the same pod share the same network. This is the outbound network traffic of the pod |
| Pod network inbound packets | pod_in_packets | pps | Containers in the same pod share the same network. This is the inbound network packets of the pod |
| Pod network outbound packets | pod_out_packets | pps | Containers in the same pod share the same network. This is the outbound network packets of the pod |

#### Container Monitoring Metrics

namespace:qce/docker
View: docker_container

| Monitoring Item | Monitoring Metric | Unit  | Description  |
|---------|---------|---------|-----|
| Container CPU usage | container_cpu_used | Core | CPU usage of the container |
| Container CPU utilization (ratio to CVM) | container_cpu_usage_for_node | % | Ratio of container CPU utilization to CVM |
| Container CPU utilization (ratio to Request) | container_cpu_usage_for_request | % | Ratio of container CPU utilization to Request |
| Container CPU utilization (ratio to Limit) | container_cpu_usage_for_limit | % | Ratio of container CPU utilization to Limit |
| Container memory usage | container_mem_used | MiB | Amount of container memory used |
| Container memory utilization (ratio to CVM) | container_mem_usage_for_node | % | Ratio of container memory utilization to CVM |
| Container memory utilization (ratio to Request) | container_mem_usage_for_request | % | Ratio of container memory utilization to Request|
| Container memory utilization (ratio to Limit) | container_mem_usage_for_limit | % | Ratio of container memory utilization to Limit |
| Container disk read traffic | container_disk_read_traffic | KB/sec | Disk read traffic when container reads from the disk |
| Container disk write traffic | container_disk_write_traffic | KB/sec | Disk write traffic when container writes to the disk |
| Container disk read IOPS | container_disk_read | count | Read IOPS when container reads from the disk |
| Container disk write IOPS | container_disk_write | count | Write IOPS when container writes to the disk |

For more information about monitoring metrics, please see [Cloud Monitor Product Documentation](https://cloud.tencent.com/document/product/248).

### Alarm
Available soon

