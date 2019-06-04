## Monitoring

Now, Cloud Monitor provides monitoring metrics at the following dimensions for CCS:


### Monitoring Metrics at Cluster Dimension

namespace:qce/cvm

| Monitoring Item      | Monitoring Metric         | Unit   | Description             |
| -------- | ------------ | ---- | -------------- |
| Cluster CPU utilization | dc_cpu_usage | %    | Average CPU utilization of the nodes in the cluster |
| Cluster memory utilization  | dc_mem_usage | %    | Average memory utilization of the nodes in the cluster  |

For more information about the monitoring metrics of CVMs in clusters and how to obtain monitoring data, please see [Monitor CVM](https://cloud.tencent.com/document/product/213/5178).

### Monitoring Metrics at Service Dimension

namespace:qce/docker
View: docker_service

| Monitoring Item           | Monitoring Metric                          | Unit   | Description                 |
| ------------- | ----------------------------- | ---- | ------------------ |
| Service CPU usage     | service_cpu_used              | Core    | Total CPU used by all container pods in the service   |
| Service CPU utilization (for cluster) | service_cpu_usage_for_cluster | %    | The ratio of service CPU utilization to the cluster       |
| Service memory usage      | service_mem_used              | MiB  | Total amount of memory used by all the container pods in the service    |
| Service memory utilization (for cluster)  | service_mem_usage_for_cluster | %    | The ratio of service memory utilization to the cluster        |
| Service network inbound traffic       | service_in_flux               | MB   | Total inbound traffic of all the pods in the service within the time window |
| Service network outbound traffic       | service_out_flux              | MB   | Total outbound traffic of all the pods in the service within the time window |
| Service network inbound bandwidth       | service_in_bandwidth          | Mbps | Total inbound bandwidth of all the pods in the service |
| Service network outbound bandwidth       | service_out_bandwidth         | Mbps | Total outbound bandwidth of all the pods in the service |
| Service network inbound packets       | service_in_packets            | pck/sec  | Total inbound packets of all the pods in the service      |
| Service network outbound packets       | service_out_packets           | pck/sec  | Total outbound packets of all the pods in the service |

### Monitoring Metrics at Pod Dimension

namespace:qce/docker
View: docker_pod

| Monitoring Item     | Monitoring Metric              | Unit   | Description                        |
| ------- | ----------------- | ---- | ------------------------- |
| Pod network inbound bandwidth | pod_in_bandwidth  | Mbps | Containers in the same pod share the same network. This is the inbound network bandwidth of the pod |
| Pod network outbound bandwidth | pod_out_bandwidth | Mbps | Containers in the same pod share the same network. This is the outbound network bandwidth of the pod |
| Pod network inbound traffic | pod_in_flux       | MB   | Containers in the same pod share the same network. This is the inbound network traffic of the pod |
| Pod network outbound traffic | pod_out_flux      | MB   | Containers in the same pod share the same network. This is the outbound network traffic of the pod |
| Pod network inbound packets | pod_in_packets    | pck/sec  | Containers in the same pod share the same network. This is the inbound network packets of the pod |
| Pod network outbound packets | pod_out_packets   | pck/sec  | Containers in the same pod share the same network. This is the outbound network packets of the pod |

### Monitoring Metrics at Container Dimension

namespace:qce/docker
View: docker_container

| Monitoring Item                | Monitoring Metric                            | Unit    | Description              |
| ------------------ | ------------------------------- | ----- | --------------- |
| Container CPU Usage          | container_cpu_used              | Core     | CPU usage of the container        |
| Container CPU utilization (for CVM)      | container_cpu_usage_for_node    | %     | Ratio of container CPU utilization to CVM      |
| Container CPU utilization (for Request) | container_cpu_usage_for_request | %     | Ratio of container CPU utilization to Request |
| Container CPU utilization (for Limit)   | container_cpu_usage_for_limit   | %     | Ratio of container CPU utilization to Limit   |
| Container memory usage           | container_mem_used              | MiB   | Amount of container memory used         |
| Container memory utilization (for CVM)       | container_mem_usage_for_node    | %     | Ratio of container memory utilization to CVM       |
| Container memory utilization (for Request)  | container_mem_usage_for_request | %     | Ratio of container memory utilization to Request  |
| Container memory utilization (for Limit)    | container_mem_usage_for_limit   | %     | Ratio of container memory utilization to Limit    |
| Container disk read traffic            | container_disk_read_traffic     | KB/sec  | Disk read traffic when container reads from the disk        |
| Container disk write traffic            | container_disk_write_traffic    | KB/sec  | Disk write traffic when container writes to the disk        |
| Container disk read IOPS          | container_disk_read             | count | Read IOPS when container reads from the disk      |
| Container disk write IOPS          | container_disk_write            | count | Write IOPS when container writes to the disk      |

For more information on how to use the monitoring metrics of CCS, please see the API [Read Monitoring Data](https://cloud.tencent.com/document/product/248/4667) in the Cloud Monitor API.
