

## TKE Nginx-ingress 监控介绍

Nginx Controller 现已提供组件运行状态相关的监控数据，您可以通过配置 Nginx-ingress 监控，开启 Nginx-ingress 监控能力。

## 前置依赖

- 集群已关联云原生监控 Prometheus，操作详情可参见 [关联集群](https://cloud.tencent.com/document/product/457/49890)。
- 云原生监控 Prometheus 需要与 Nginx 在同一个网络平面。

## 采集指标

TKE Nginx-ingress 自动配置以下采集指标：
- **Nginx 状态**
 - nginx_ingress_controller_connections_total
 - nginx_ingress_controller_requests_total
 - nginx_ingress_controller_connections
- **进程相关**
 - nginx_ingress_controller_num_procs
 - nginx_ingress_controller_cpu_seconds_total
 - nginx_ingress_controller_read_bytes_total
 - nginx_ingress_controller_write_bytes_total
 - nginx_ingress_controller_resident_memory_bytes
 - nginx_ingress_controller_virtual_memory_bytes
 - nginx_ingress_controller_oldest_start_time_seconds
- **Socket 相关**
 - nginx_ingress_controller_request_duration_seconds
 - nginx_ingress_controller_request_size
 - nginx_ingress_controller_response_duration_seconds
 - nginx_ingress_controller_response_size
 - nginx_ingress_controller_bytes_sent
 - nginx_ingress_controller_ingress_upstream_latency_seconds
  
您也可以根据业务需要自行配置监控采集指标，指标详情可参见 [官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/monitoring/)。






## Nginx-ingress 监控 Grafana 面板

TKE Nginx-ingress 开启监控功能后将关联云原生监控 Prometheus，云原生监控 Prometheus 自带一个 Grafana，您可以在 Nginx-ingress 组件页面直接跳转到对应的 Grafana 面板，如下图所示：
![](https://main.qcloudimg.com/raw/66ce3486814a46fa639a38807f51d607.png)


