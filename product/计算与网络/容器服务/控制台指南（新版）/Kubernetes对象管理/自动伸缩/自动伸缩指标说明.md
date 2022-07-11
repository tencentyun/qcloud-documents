
实例（Pod）自动扩缩容功能（Horizontal Pod Autoscaler，HPA）可以根据目标实例 CPU 利用率的平均值等指标自动扩展、缩减服务的 Pod 数量。自动扩缩容时，可供在控制台进行设置的触发指标类型包括 CPU 指标、内存、硬盘、网络和 GPU 相关指标。此外，这些指标还可以在您通过 YAML 文件创建和编辑 HPA 时使用，本文将给出配置 YAML 文件示例。

## 自动伸缩指标
自动伸缩指标详情如下表所示：
>?其中 `metricName` 中的变量本身有单位，即表中所示默认单位，该单位在编写 YAML 文件时可忽略。

### CPU 指标

<table>
<tr>
	<th width="17.8%">指标名称（控制台）</th><th width="14.1%">单位（控制台）</th><th width="17.1%">备注</th>
	<th width="6.6%">type</th><th width="33%">metricName</th><th width="11.4%">默认单位</th>
	</tr>
	<tr>
	<td>CPU 使用量</td>
	<td>核</td>
	<td>Pod 的 CPU 使用量</td>
	<td>Pods</td>
	<td>k8s_pod_cpu_core_used</td>
	<td> 核 </td>
	</tr>
	<tr>
	<td>CPU 利用率<br>（占节点）</td>
	<td>%</td>
	<td>Pod 的 CPU 使用量占节点总量之比</td>
	<td>Pods</td>
	<td>k8s_pod_rate_cpu_core_used_node</td>
	<td>% </td>
	</tr>
	<tr>
	<td>CPU 利用率<br>（占 Request）</td>
	<td>% </td>
	<td>Pod 的 CPU 使用量和 Pod 中容器设置的 Request 值之比 </td>
	<td>Pods</td>
	<td>k8s_pod_rate_cpu_core_used_request</td>
	<td>%</td>
	</tr>
	<tr>
	<td>CPU 利用率<br>（占 Limit）</td>
	<td>%</td>
	<td>Pod 的 CPU 使用量和 Pod 中容器设置的 Limit 之和的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_cpu_core_used_limit</td>
	<td>%</td>
	</tr>
</table>



### 硬盘	

<table>
<tr>
	<th width="17.8%">指标名称（控制台）</th><th width="14.1%">单位（控制台）</th><th width="17.1%">备注</th>
	<th width="6.6%">type</th><th width="33%">metricName</th><th width="11.4%">默认单位</th>
	</tr>
	<tr>
	<td>硬盘写流量</td>
	<td>KB/s</td>
	<td> Pod 的硬盘写速率</td>
	<td>Pods</td>
	<td>k8s_pod_fs_write_bytes</td>
	<td>B/s</td>
	</tr>
	<tr>
	<td>硬盘读流量</td>
	<td>KB/s</td>
	<td> Pod 的硬盘读速率</td>
	<td>Pods</td>
	<td>k8s_pod_fs_read_bytes</td>
	<td>B/s</td>
	</tr>
	<tr>
	<td>硬盘读 IOPS</td>
	<td>次/s </td>
	<td>Pod 从硬盘读取数据的 IO 次数 </td>
	<td>Pods</td>
	<td>k8s_pod_fs_read_times</td>
	<td>次/s</td>
	</tr>
	<tr>
	<td>硬盘写 IOPS</td>
	<td>次/s</td>
	<td>Pod 把数据写入硬盘的 IO 次数</td>
	<td>Pods</td>
	<td>k8s_pod_fs_write_times</td>
	<td> 次/s </td>
	</tr>
</table>


### 网络	

<table>
<tr>
	<th width="17.8%">指标名称（控制台）</th><th width="14.1%">单位（控制台）</th><th width="17.1%">备注</th>
	<th width="6.6%">type</th><th width="33%">metricName</th><th width="11.4%">默认单位</th>
	</tr>
	<td>网络入带宽</td>
	<td>Mbps</td>
	<td>单 Pod 下所有容器的入方向带宽之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_receive_bytes_bw</td>
	<td>Bps</td>
	</tr>
	<tr>
	<td>网络出带宽</td>
	<td>Mbps</td>
	<td>单 Pod 下所有容器的出方向带宽之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_transmit_bytes_bw</td>
	<td>Bps</td>
	</tr>
	<tr>
	<td>网络入流量</td>
	<td>KB/s</td>
	<td>单 Pod 下所有容器的入方向流量之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_receive_bytes</td>
	<td>B/s</td>
	</tr>
	<tr>
	<td>网络出流量</td>
	<td>KB/s</td>
	<td>单 Pod 下所有容器的出方向流量之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_transmit_bytes</td>
	<td>B/s</td>
	</tr>
	<tr>
	<td>网络入包量</td>
	<td>个/s</td>
	<td>单 Pod 下所有容器的入方向包数之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_receive_packets</td>
	<td>个/s</td>
	</tr>
	<tr>
	<td>网络出包量</td>
	<td>个/s</td>
	<td>单 Pod 下所有容器的出方向包数之和</td>
	<td>Pods</td>
	<td>k8s_pod_network_transmit_packets</td>
	<td>个/s	</td>
	</tr>
</table>



### 内存

<table>
<tr>
	<th width="17.8%">指标名称（控制台）</th><th width="14.1%">单位（控制台）</th><th width="17.1%">备注</th>
	<th width="6.6%">type</th><th width="33%">metricName</th><th width="11.4%">默认单位</th>
	</tr>
	<tr>
	<td>内存使用量</td>
	<td>Mib</td>
	<td>Pod 内存使用量</td>
	<td>Pods</td>
	<td>k8s_pod_mem_usage_bytes</td>
	<td>B</td>
	</tr>
	<tr>
	<td>内存使用量<br>（不包含 Cache）	</td>
	<td>Mib</td>
	<td>Pod 内存使用，不包含 Cache</td>
	<td>Pods</td>
	<td>k8s_pod_mem_no_cache_bytes</td>
	<td>B</td>
	</tr>
	<tr>
	<td> 内存利用率<br>（占节点）</td>
	<td>%</td>
	<td>Pod 内存使用占 node 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_usage_node</td>
	<td>%</td>
	</tr>
	<tr>
	<td>内存利用率<br>（占节点，不包含 Cache）</td>
	<td>%</td>
	<td>Pod 内存使用占 node 的比例，不含 Cache</td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_no_cache_node</td>
	<td>%</td>
	</tr>
	<tr>
	<td>内存利用率<br>（占 Request）</td>
	<td>%</td>
	<td>Pod 内存使用占 Request 的比例 </td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_usage_request</td>
	<td>%</td>
	</tr>
	<tr>
	<td>内存利用率<br>（占 Request，不包含Cache）</td>
	<td>%</td>
	<td>Pod 内存使用占 Request 的比例，不含 Cache</td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_no_cache_request</td>
	<td>%</td>
	</tr>
	<tr>
	<td>内存利用率<br>（占 Limit）</td>
	<td>%</td>
	<td>Pod 内存使用占 Limit 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_usage_limit</td>
	<td>%</td>
	</tr>
	<tr>
	<td>内存利用率<br>（占 Limit，不包含 Cache）</td>
	<td>%</td>
	<td>Pod 内存使用占 Limit 的比例，不含 Cache</td>
	<td>Pods</td>
	<td>k8s_pod_rate_mem_no_cache_limit</td>
	<td>%</td>
	</tr>
</table>




### GPU
>? 以下所有 GPU 相关的触发指标，当前仅支持在 EKS 集群中使用。  

<table>
<tr>
	<th width="17.8%">指标名称（控制台）</th><th width="14.1%">单位（控制台）</th><th width="17.1%">备注</th>
	<th width="6.6%">type</th><th width="33%">metricName</th><th width="11.4%">默认单位</th>
	</tr>
	<tr>
	<td>GPU 使用量</td>
	<td>CUDA Core</td>
	<td>Pod GPU 使用量</td>
	<td>Pods</td>
	<td>k8s_pod_gpu_used</td>
	<td>CUDA Core</td>
	</tr>
	<tr>
	<td>GPU 申请量</td>
	<td>CUDA Core</td>
	<td>Pod GPU 申请量</td>
	<td>Pods</td>
	<td>k8s_pod_gpu_request</td>
	<td>CUDA Core</td>
	</tr>
	<tr>
	<td> GPU 利用率<br>（占 Request）</td>
	<td>%</td>
	<td>GPU 使用占 Request 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_gpu_used_request</td>
	<td>%</td>
	</tr>
	<tr>
	<td>GPU 利用率<br>（占节点）</td>
	<td>%</td>
	<td>GPU 使用占 node 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_gpu_used_node</td>
	<td>%</td>
 </tr>
 <tr>
	<td>GPU memory 使用量</td>
	<td>Mib</td>
	<td>Pod GPU memory 使用量</td>
	<td>Pods</td>
	<td>k8s_pod_gpu_memory_used_bytes</td>
	<td>B</td>
 </tr>
 <tr>
	<td>GPU memory 申请量</td>
	<td>Mib</td>
	<td>Pod GPU memory 申请量</td>
	<td>Pods</td>
	<td>k8s_pod_gpu_memory_request_bytes</td>
	<td>B</td>
 </tr>
 <tr>
	<td>GPU memory 利用率<br>（占 Request）</td>
	<td>%</td>
	<td>GPU memory 使用占 Request 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_gpu_memory_used_request</td>
	<td>%</td>
 </tr>
 <tr>
	<td>GPU memory 利用率<br>（占节点） </td>
	<td>%</td>
	<td>GPU memory 使用占 node 的比例</td>
	<td>Pods</td>
	<td>k8s_pod_rate_gpu_memory_used_node</td>
	<td>%</td>
 </tr>
</table>


## 通过 YAML 创建和编辑 HPA 
您可以通过 YAML 文件创建和编辑 HPA 。以下为配置文件的示例，该文件定义了一条名称为 example 的 HPA ，CPU 使用量为1时触发 HPA  ，实例范围为1 - 2。

>! TKE 同样兼容原生的 Resource 类型。

```
apiVersion: autoscaling/v2beta1
kind: HorizontalPodAutoscaler
metadata:
  name: example
  namespace: default
  labels:
    qcloud-app: example
spec:
  minReplicas: 1
  maxReplicas: 2
  metrics:
  - type: Pods	# 支持使用 Resource
    pods:
      metricName: k8s_pod_cpu_core_used
      targetAverageValue: "1"
  scaleTargetRef:
    apiVersion: apps/v1beta2
    kind: Deployment
    name: nginx
```


