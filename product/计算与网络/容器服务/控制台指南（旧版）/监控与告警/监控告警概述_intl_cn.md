## 监控告警概述

### 概述
为腾讯云容器服务提供良好的监控环境是保证容器服务的高可靠性、高可用性和高性能的重要部分。用户可以方便地为不同资源收集不同维度的监控数据，这能方便掌握资源的使用状况，轻松定位故障。

腾讯云云监控为容器集群、服务、实例提供数据收集和数据展示功能。使用腾讯云云监控，您可以查看集群、节点、服务、实例的统计数据，验证集群是否正常运行并创建相应告警。有关云监控的更多信息，请参阅[云监控 产品文档](https://cloud.tencent.com/document/product/248)。

收集监控数据有助于用户建立容器集群性能的正常标准。通过在不同时间、不同负载条件下测量容集群的性能并收集历史监控数据，用户可以较为清楚的了解容器集群和服务运行时的正常性能，并快速根据当前监控数据确定服务运行时是否处于异常状态，及时找出解决问题的方法。例如，用户可以监控服务的 CPU 利用率、内存使用率和磁盘 I/O。

### 监控

目前云监控为容器服务提供了以下维度的监控指标：

#### 集群维度监控指标

namespace:qce/cvm

| 监控项 | 监控指标|单位  |说明  |
|---------|---------|---------|-----|
|集群CPU利用率|  dc_cpu_usage |%|集群内节点的平均CPU利用率|
|集群内存利用率|  dc_mem_usage |%|集群内节点的平均内存利用率|

集群内云服务器的具体监控指标和获取监控数据的方法可以参考[监控云服务器](https://cloud.tencent.com/document/product/213/5178)。

#### 服务维度监控指标

namespace:qce/docker
视图：docker_service

| 监控项 | 监控指标|单位  |说明  |
|---------|---------|---------|-----|
|服务CPU使用情况|service_cpu_used|核|服务内所有容器实例CPU使用之和|
|服务CPU使用率(占集群)|service_cpu_usage_for_cluster|%|服务使用CPU占集群比率|
|服务内存使用情况|service_mem_used|MiB|服务内所有容器实例内存使用之和|
|服务内存使用率(占集群)|service_mem_usage_for_cluster|%|服务使用内存占集群比率|
|服务网络入流量|service_in_flux  |MB|服务内所有实例在该时间窗口入流量之和|
|服务网络出流量|service_out_flux |MB|服务内所有实例在该时间窗口出流量之和|
|服务网络入带宽|service_in_bandwidth |Mbps|服务内所有实例的入带宽之和|
|服务网络出带宽|service_out_bandwidth|Mbps|服务内所有实例的出带宽之和|
|服务网络入包量|service_in_packets|个/s|服务内所有实例的入包量之和|
|服务网络出包量|service_out_packets|个/s|服务内所有实例的出包量之和|

#### 实例维度监控指标

namespace:qce/docker
视图：docker_pod

| 监控项 | 监控指标|单位  |说明  |
|---------|---------|---------|-----|
|实例网络入带宽|pod_in_bandwidth|Mbps|同一实例内容器共享网络，实例(pod)的网络入带宽|
|实例网络出带宽|pod_out_bandwidth|Mbps|同一实例内容器共享网络，实例(pod)的网络出带宽|
|实例网络入流量|pod_in_flux|MB|同一实例内容器共享网络，实例(pod)的网络入流量|
|实例网络出流量|pod_out_flux|MB|同一实例内容器共享网络，实例(pod)的网络出流量|
|实例网络入包量|pod_in_packets|个/s|同一实例内容器共享网络，实例(pod)的网络入包量|
|实例网络出包量|pod_out_packets|个/s|同一实例内容器共享网络，实例(pod)的网络出包量|

#### 容器维度监控指标

namespace:qce/docker
视图：docker_container

| 监控项 | 监控指标|单位  |说明  |
|---------|---------|---------|-----|
|容器CPU使用情况|container_cpu_used|核|容器CPU使用量|
|容器CPU使用率(占主机)|container_cpu_usage_for_node|%|容器CPU使用占主机|
|容器CPU使用率(占Request)|container_cpu_usage_for_request|%|容器CPU使用占Request|
|容器CPU使用率(占Limit)|container_cpu_usage_for_limit|%|容器CPU使用占Limit|
|容器内存使用情况|container_mem_used|MiB|容器内存使用量|
|容器内存使用率(占主机)|container_mem_usage_for_node|%|容器内存使用占主机|
|容器内存使用率(占Request)|container_mem_usage_for_request|%|容器内存使用占Request|
|容器内存使用率(占Limit)|container_mem_usage_for_limit|%|容器内存使用占Limit|
|容器磁盘读流量|container_disk_read_traffic|KB/s|容器对磁盘读流量|
|容器磁盘写流量|container_disk_write_traffic|KB/s|容器对磁盘写流量|
|容器磁盘读IOPS|container_disk_read|count|容器对磁盘读IOPS|
|容器磁盘写IOPS|container_disk_write|count|容器对磁盘写IOPS|

有关具体的监控指标说明，请参考[云监控 产品文档](https://cloud.tencent.com/document/product/248)。

### 告警

您为您关注的集群、服务、容器指标创建告警，能够使上述资源的运行状态在到达某一条件时，及时发送告警信息至您的用户或用户组中。这样能使得您及时发现异常状况从而采取相应措施，保持系统的稳定性和可靠性。更多内容请参考 [创建告警](https://cloud.tencent.com/document/product/248/6126)。