

Prometheus 监控服务为 Kubernetes 集群预设了 [Master 组件](#kubernetes-master-.E7.BB.84.E4.BB.B6)，[Kubelet](#kubelet)，[资源使用](#kubernetes-.E8.B5.84.E6.BA.90.E4.BD.BF.E7.94.A8)，[工作负载](#kubernetes-.E5.B7.A5.E4.BD.9C.E8.B4.9F.E8.BD.BD) 和 [节点](#kubernetes-.E8.8A.82.E7.82.B9) 报警模板。

## Kubernetes Master 组件

非托管集群提供如下指标：


<table>
<thead>
<tr>
<th width="10%">策略名称</th>
<th width="50%">策略表达式</th>
<th width="10%">持续时间</th>
<th width="30%">策略描述</th>
</tr>
</thead>
<tbody><tr>
<td>客户端访问 APIServer 出错</td>
<td>(sum(rate(rest_client_requests_total{code=~"5.."}[5m])) by (instance, job, cluster_id) / sum(rate(rest_client_requests_total[5m])) by (instance, job, cluster_id))&gt; 0.01</td>
<td>15m</td>
<td>客户端访问 APIServer 出错率大于1%</td>
</tr>
<tr>
<td>客户端访问 APIServer 证书快过期</td>
<td>apiserver_client_certificate_expiration_seconds_count{job="apiserver"} &gt; 0 and on(job) histogram_quantile(0.01, sum by (cluster_id, job, le) (rate(apiserver_client_certificate_expiration_seconds_bucket{job="apiserver"}[5m]))) &lt; 86400</td>
<td>无</td>
<td>访问 APIServer 的客户端证书将在24小时后过期</td>
</tr>
<tr>
<td>聚合 API 出错</td>
<td>sum by(cluster_id, name, namespace) (increase(aggregator_unavailable_apiservice_count[5m])) &gt; 2</td>
<td>无</td>
<td>聚合 API 最近5分钟报错</td>
</tr>
<tr>
<td>聚合 API 可用性低</td>
<td>(1 - max by(name, namespace, cluster_id)(avg_over_time(aggregator_unavailable_apiservice[5m]))) * 100 &lt; 90</td>
<td>5m</td>
<td>聚合 API 服务最近5分钟可用性低于90%</td>
</tr>
<tr>
<td>APIServer 故障</td>
<td>absent(sum(up{job="apiserver"}) by (cluster_id) &gt; 0)</td>
<td>5m</td>
<td>APIServer 从采集目标中消失</td>
</tr>
<tr>
<td>Scheduler 故障</td>
<td>absent(sum(up{job="kube-scheduler"}) by (cluster_id) &gt; 0)</td>
<td>15m</td>
<td>Scheduler 从采集目标中消失</td>
</tr>
<tr>
<td>Controller Manager 故障</td>
<td>absent(sum(up{job="kube-controller-manager"}) by (cluster_id) &gt; 0)</td>
<td>15m</td>
<td>Controller Manager 从采集目标中消失</td>
</tr>
</tbody></table>



## Kubelet

<table>
<thead>
<tr>
<th width="10%">策略名称</th>
<th width="50%">策略表达式</th>
<th width="10%">持续时间</th>
<th width="30%">策略描述</th>
</tr>
</thead>
<tbody><tr>
<td>Node 状态异常</td>
<td>kube_node_status_condition{job=~".*kube-state-metrics",condition="Ready",status="true"} == 0</td>
<td>15m</td>
<td>Node 状态异常持续15m</td>
</tr>
<tr>
<td>Node 不可达</td>
<td>kube_node_spec_taint{job=~".*kube-state-metrics",key="node.kubernetes.io/unreachable",effect="NoSchedule"} == 1</td>
<td>15m</td>
<td>Node 不可达，上面的工作负载会重新调度</td>
</tr>
<tr>
<td>Node 上运行太多 pod</td>
<td>count by(cluster_id, node) ((kube_pod_status_phase{job=~".*kube-state-metrics",phase="Running"} == 1) * on(instance,pod,namespace,cluster_id) group_left(node) topk by(instance,pod,namespace,cluster_id) (1, kube_pod_info{job=~".*kube-state-metrics"}))/max by(cluster_id, node) (kube_node_status_capacity_pods{job=~".*kube-state-metrics"} != 1) &gt; 0.95</td>
<td>15m</td>
<td>Node 上运行 pod 量快达到上限</td>
</tr>
<tr>
<td>Node 状态抖动</td>
<td>sum(changes(kube_node_status_condition{status="true",condition="Ready"}[15m])) by (cluster_id, node) &gt; 2</td>
<td>15m</td>
<td>Node 状态在正常和异常之间抖动</td>
</tr>
<tr>
<td>Kubelet 的客户端证书快过期</td>
<td>kubelet_certificate_manager_client_ttl_seconds &lt; 86400</td>
<td>无</td>
<td>Kubelet 客户端证书将在24小时后过期</td>
</tr>
<tr>
<td>Kubelet 的服务端证书快过期</td>
<td>kubelet_certificate_manager_server_ttl_seconds &lt; 86400</td>
<td>无</td>
<td>Kubelet 服务端证书将在24小时后过期</td>
</tr>
<tr>
<td>Kubelet 客户端证书续签出错</td>
<td>increase(kubelet_certificate_manager_client_expiration_renew_errors[5m]) &gt; 0</td>
<td>15m</td>
<td>Kubelet 续签客户端证书出错</td>
</tr>
<tr>
<td>Kubelet 服务端证书续签出错</td>
<td>increase(kubelet_server_expiration_renew_errors[5m]) &gt; 0</td>
<td>15m</td>
<td>Kubelet 续签服务端证书出错</td>
</tr>
<tr>
<td>PLEG 耗时高</td>
<td>histogram_quantile(0.99, sum(rate(kubelet_pleg_relist_duration_seconds_bucket[5m])) by (cluster_id, instance, le) * on(instance, cluster_id) group_left(node) kubelet_node_name{job="kubelet"}) &gt;= 10</td>
<td>5m</td>
<td>PLEG 操作耗时的99分位数超过10秒</td>
</tr>
<tr>
<td>Pod 启动耗时高</td>
<td>histogram_quantile(0.99, sum(rate(kubelet_pod_worker_duration_seconds_bucket{job="kubelet"}[5m])) by (cluster_id, instance, le)) * on(cluster_id, instance) group_left(node) kubelet_node_name{job="kubelet"} &gt; 60</td>
<td>15m</td>
<td>Pod 启动耗时的99分位数值超过60秒</td>
</tr>
<tr>
<td>Kubelet 故障</td>
<td>absent(sum(up{job="kubelet"}) by (cluster_id) &gt; 0)</td>
<td>15m</td>
<td>Kubelet 从采集目标消失</td>
</tr>
</tbody></table>




##  Kubernetes 资源使用

<table>
<thead>
<tr>
<th width="10%">策略名称</th>
<th width="50%">策略表达式</th>
<th width="10%">持续时间</th>
<th width="30%">策略描述</th>
</tr>
</thead>
<tbody><tr>
<td>集群 CPU 资源过载</td>
<td>sum by (cluster_id) (max by (cluster_id, namespace, pod, container) (kube_pod_container_resource_requests_cpu_cores{job=~".*kube-state-metrics"}) * on(cluster_id, namespace, pod) group_left() max by (cluster_id, namespace, pod) (kube_pod_status_phase{phase=~"Pending|Running"} == 1))/sum by (cluster_id) (kube_node_status_allocatable_cpu_cores)&gt;(count by (cluster_id) (kube_node_status_allocatable_cpu_cores)-1) / count by (cluster_id) (kube_node_status_allocatable_cpu_cores)</td>
<td>5m</td>
<td>集群内 Pod 申请的 CPU 总量过多，已无法容忍 Node 挂掉</td>
</tr>
<tr>
<td>集群内存资源过载</td>
<td>sum by (cluster_id) (max by (cluster_id, namespace, pod, container) (kube_pod_container_resource_requests_memory_bytes{job=~".*kube-state-metrics"}) * on(cluster_id, namespace, pod) group_left() max by (cluster_id, namespace, pod) (kube_pod_status_phase{phase=~"Pending|Running"} == 1))/sum by (cluster_id) (kube_node_status_allocatable_memory_bytes) &gt; (count by (cluster_id) (kube_node_status_allocatable_memory_bytes)-1) / count by (cluster_id) (kube_node_status_allocatable_memory_bytes)</td>
<td>5m</td>
<td>集群内 Pod 申请的内存总量过多，已无法容忍 Node 挂掉</td>
</tr>
<tr>
<td>集群 CPU 配额过载</td>
<td>sum by (cluster_id) (kube_resourcequota{job=~".*kube-state-metrics", type="hard", resource="cpu"})/sum by (cluster_id) (kube_node_status_allocatable_cpu_cores) &gt; 1.5</td>
<td>5m</td>
<td>集群内 CPU 配额超过可分配 CPU 总量</td>
</tr>
<tr>
<td>集群内存配额过载</td>
<td>sum by (cluster_id) (kube_resourcequota{job=~".*kube-state-metrics", type="hard", resource="memory"}) /  sum by (cluster_id) (kube_node_status_allocatable_memory_bytes) &gt; 1.5</td>
<td>5m</td>
<td>集群内内存配额超过可分配内存总量</td>
</tr>
<tr>
<td>配额资源快使用完</td>
<td>sum by (cluster_id, namespace, resource) kube_resourcequota{job=~".*kube-state-metrics", type="used"} / sum by (cluster_id, namespace, resource) (kube_resourcequota{job=~".*kube-state-metrics", type="hard"} &gt; 0) &gt;= 0.9</td>
<td>15m</td>
<td>配额资源使用率超过90%</td>
</tr>
<tr>
<td>CPU 执行周期受限占比高</td>
<td>sum(increase(container_cpu_cfs_throttled_periods_total{container!="", }[5m])) by (cluster_id, container, pod, namespace) /sum(increase(container_cpu_cfs_periods_total{}[5m])) by (cluster_id, container, pod, namespace) &gt; ( 25 / 100 )</td>
<td>15m</td>
<td>CPU 执行周期受到限制的占比高</td>
</tr>
<tr>
<td>Pod 的 CPU 使用率高</td>
<td>sum(rate(container_cpu_usage_seconds_total{job="kubelet", metrics_path="/metrics/cadvisor", image!="", container!="POD"}[1m])) by (cluster_id, namespace, pod, container) / sum(kube_pod_container_resource_limits_cpu_cores) by (cluster_id, namespace, pod, container) &gt; 0.75</td>
<td>15m</td>
<td>Pod 的 CPU 使用率超过75%</td>
</tr>
<tr>
<td>Pod 的内存使用率高</td>
<td>sum(rate(container_memory_working_set_bytes{job="kubelet", metrics_path="/metrics/cadvisor", image!="", container!="POD"}[1m])) by (cluster_id, namespace, pod, container) /sum(kube_pod_container_resource_limits_memory_bytes) by (cluster_id, namespace, pod, container) &gt; 0.75</td>
<td>15m</td>
<td>Pod 的内存使用率超高跟75%</td>
</tr>
</tbody></table>



##  Kubernetes 工作负载

<table>
<thead>
<tr>
<th width="10%">策略名称</th>
<th width="50%">策略表达式</th>
<th width="10%">持续时间</th>
<th width="30%">策略描述</th>
</tr>
</thead>
<tbody><tr>
<td>Pod 频繁重启</td>
<td>increase(kube_pod_container_status_restarts_total{job=~".*kube-state-metrics"}[5m]) &gt; 0</td>
<td>15m</td>
<td>Pod 最近5m频繁重启</td>
</tr>
<tr>
<td>Pod 状态异常</td>
<td>sum by (namespace, pod, cluster_id) (max by(namespace, pod, cluster_id) (kube_pod_status_phase{job=~".*kube-state-metrics", phase=~"Pending|Unknown"}) * on(namespace, pod, cluster_id) group_left(owner_kind) topk by(namespace, pod) (1, max by(namespace, pod, owner_kind, cluster_id) (kube_pod_owner{owner_kind!="Job"}))) &gt; 0</td>
<td>15m</td>
<td>Pod处于 NotReady 状态超过15分钟</td>
</tr>
<tr>
<td>容器状态异常</td>
<td>sum by (namespace, pod, container, cluster_id) (kube_pod_container_status_waiting_reason{job=~".*kube-state-metrics"}) &gt; 0</td>
<td>1h</td>
<td>容器长时间处于 Waiting 状态</td>
</tr>
<tr>
<td>Deployment 部署版本不匹配</td>
<td>kube_deployment_status_observed_generation{job=~".*kube-state-metrics"} !=kube_deployment_metadata_generation{job=~".*kube-state-metrics"}</td>
<td>15m</td>
<td>部署版本和设置版本不一致，表示 deployment 变更没有生效</td>
</tr>
<tr>
<td>Deployment 副本数不匹配</td>
<td>(kube_deployment_spec_replicas{job=~".*kube-state-metrics"} != kube_deployment_status_replicas_available{job=~".*kube-state-metrics"}) and (changes(kube_deployment_status_replicas_updated{job=~".*kube-state-metrics"}[5m]) == 0)</td>
<td>15m</td>
<td>实际副本数和设置副本数不一致</td>
</tr>
<tr>
<td>Statefulset 部署版本不匹配</td>
<td>kube_statefulset_status_observed_generation{job=~".*kube-state-metrics"} != kube_statefulset_metadata_generation{job=~".*kube-state-metrics"}</td>
<td>15m</td>
<td>部署版本和设置版本不一致，表示 statefulset 变更没有生效</td>
</tr>
<tr>
<td>Statefulset 副本数不匹配</td>
<td>(kube_statefulset_status_replicas_ready{job=~".*kube-state-metrics"} != kube_statefulset_status_replicas{job=~".*kube-state-metrics"}) and ( changes(kube_statefulset_status_replicas_updated{job=~".*kube-state-metrics"}[5m]) == 0)</td>
<td>15m</td>
<td>实际副本数和设置副本数不一致</td>
</tr>
<tr>
<td>Statefulset 更新未生效</td>
<td>(maxwithout(revision)(kube_statefulset_status_current_revision{job=~".*kube-state-metrics"}unlesskube_statefulset_status_update_revision{job=~".*kube-state-metrics"})*(kube_statefulset_replicas{job=~".*kube-state-metrics"}!=kube_statefulset_status_replicas_updated{job=~".*kube-state-metrics"})) and (changes(kube_statefulset_status_replicas_updated{job=~".*kube-state-metrics"}[5m])==0)</td>
<td>15m</td>
<td>Statefulset 部分 pod 没有更新</td>
</tr>
<tr>
<td>Daemonset 变更卡住</td>
<td>((kube_daemonset_status_current_number_scheduled{job=~".*kube-state-metrics"}!=kube_daemonset_status_desired_number_scheduled{job=~".*kube-state-metrics"}) or (kube_daemonset_status_number_misscheduled{job=~".*kube-state-metrics"}!=0) or (kube_daemonset_updated_number_scheduled{job=~".*kube-state-metrics"}!=kube_daemonset_status_desired_number_scheduled{job=~".*kube-state-metrics"}) or (kube_daemonset_status_number_available{job=~".*kube-state-metrics"}!=kube_daemonset_status_desired_number_scheduled{job=~".*kube-state-metrics"})) and (changes(kube_daemonset_updated_number_scheduled{job=~".*kube-state-metrics"}[5m])==0)</td>
<td>15m</td>
<td>Daemonset 变更超过15分钟</td>
</tr>
<tr>
<td>Daemonset 部分 node 未调度</td>
<td>kube_daemonset_status_desired_number_scheduled{job=~".*kube-state-metrics"} - kube_daemonset_status_current_number_scheduled{job=~".*kube-state-metrics"} &gt; 0</td>
<td>10m</td>
<td>Daemonset 在部分 node 未被调度</td>
</tr>
<tr>
<td>Daemonset 部分 node 被错误调度</td>
<td>kube_daemonset_status_number_misscheduled{job=~".*kube-state-metrics"} &gt; 0</td>
<td>15m</td>
<td>Daemonset 被错误调度到一些 node</td>
</tr>
<tr>
<td>Job 运行太久</td>
<td>kube_job_spec_completions{job=~".*kube-state-metrics"} - kube_job_status_succeeded{job=~".*kube-state-metrics"}  &gt; 0</td>
<td>12h</td>
<td>Job 执行时间超过12小时</td>
</tr>
<tr>
<td>Job 执行失败</td>
<td>kube_job_failed{job=~".*kube-state-metrics"}  &gt; 0</td>
<td>15m</td>
<td>Job 执行失败</td>
</tr>
<tr>
<td>副本数和 HPA 不匹配</td>
<td>(kube_hpa_status_desired_replicas{job=~".*kube-state-metrics"} != kube_hpa_status_current_replicas{job=~".*kube-state-metrics"}) and changes(kube_hpa_status_current_replicas[15m]) == 0</td>
<td>15m</td>
<td>实际副本数和 HPA 设置的不一致</td>
</tr>
<tr>
<td>副本数达到 HPA 最大值</td>
<td>kube_hpa_status_current_replicas{job=~".*kube-state-metrics"} == kube_hpa_spec_max_replicas{job=~".*kube-state-metrics"}</td>
<td>15m</td>
<td>实际副本数达到 HPA 配置的最大值</td>
</tr>
<tr>
<td>PersistentVolume 状态异常</td>
<td>kube_persistentvolume_status_phase{phase=~"Failed|Pending",job=~".*kube-state-metrics"} &gt; 0</td>
<td>15m</td>
<td>PersistentVolume 处于 Failed 或 Pending状态</td>
</tr>
</tbody></table>


##  Kubernetes 节点

<table>
<thead>
<tr>
<th width="10%">策略名称</th>
<th width="50%">策略表达式</th>
<th width="10%">持续时间</th>
<th width="30%">策略描述</th>
</tr>
</thead>
<tbody><tr>
<td>文件系统空间快耗尽</td>
<td>(node_filesystem_avail_bytes{job="node-exporter",fstype!=""}/node_filesystem_size_bytes{job="node-exporter",fstype!=""}*100&lt;15 and predict_linear(node_filesystem_avail_bytes{job="node-exporter",fstype!=""}[6h],4*60*60)&lt;0 and node_filesystem_readonly{job="node-exporter",fstype!=""}==0)</td>
<td>1h</td>
<td>文件系统空间预计在4小时后使用完</td>
</tr>
<tr>
<td>文件系统空间使用率高</td>
<td>(node_filesystem_avail_bytes{job="node-exporter",fstype!=""}/node_filesystem_size_bytes{job="node-exporter",fstype!=""}*100&lt;5 and node_filesystem_readonly{job="node-exporter",fstype!=""}==0)</td>
<td>1h</td>
<td>文件系统可用空间低于5%</td>
</tr>
<tr>
<td>文件系统inode快耗尽</td>
<td>(node_filesystem_files_free{job="node-exporter",fstype!=""}/node_filesystem_files{job="node-exporter",fstype!=""}*100&lt;20 and predict_linear(node_filesystem_files_free{job="node-exporter",fstype!=""}[6h],4*60*60)&lt;0 and node_filesystem_readonly{job="node-exporter",fstype!=""}==0)</td>
<td>1h</td>
<td>文件系统 inode 预计在4小时后使用完</td>
</tr>
<tr>
<td>文件系统inode使用率高</td>
<td>(node_filesystem_files_free{job="node-exporter",fstype!=""}/node_filesystem_files{job="node-exporter",fstype!=""}*100&lt;3 and node_filesystem_readonly{job="node-exporter",fstype!=""}==0)</td>
<td>1h</td>
<td>文件系统可用 inode 低于3%</td>
</tr>
<tr>
<td>网卡状态不稳定</td>
<td>changes(node_network_up{job="node-exporter",device!~"veth.+"}[2m])</td>
<td>2m</td>
<td>网卡状态不稳定，在  up 和 down 间频繁变化</td>
</tr>
<tr>
<td>网卡接收出错</td>
<td>increase(node_network_receive_errs_total[2m]) &gt; 10</td>
<td>1h</td>
<td>网卡接收数据出错</td>
</tr>
<tr>
<td>网卡发送出错</td>
<td>increase(node_network_transmit_errs_total[2m]) &gt; 10</td>
<td>1h</td>
<td>网卡发送数据出错</td>
</tr>
<tr>
<td>机器时钟未同步</td>
<td>min_over_time(node_timex_sync_status[5m]) == 0</td>
<td>10m</td>
<td>机器时间最近未同步，检查 NTP 是否正常配置</td>
</tr>
<tr>
<td>机器时钟漂移</td>
<td>(node_timex_offset_seconds&gt;0.05 and deriv(node_timex_offset_seconds[5m])&gt;=0) or (node_timex_offset_seconds&lt;-0.05 and deriv(node_timex_offset_seconds[5m])&lt;=0)</td>
<td>10m</td>
<td>机器时间漂移超过300秒，检查 NTP 是否正常配置</td>
</tr>
</tbody></table>

