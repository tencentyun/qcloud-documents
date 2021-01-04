## 背景

使用了腾讯云容器服务 [云原生监控](https://cloud.tencent.com/document/product/457/49889)，如何快速将以前自建的 Prometheus 迁移过来呢？云原生监控兼容 Prometheus 与 Grafana 的 API，同时也兼容主流的 prometheus-operator 的 CRD 用法，提供了极大的灵活性与扩展性，可以结合 Prometheus 开源生态的工具解锁更多高级的玩法。将自建的 Prometheus 迁移到云原生监控也很容易，本文提供一个迁移的思路，给出一些辅助脚本和迁移工具的用法示例，助你加速迁移。

## 迁移动态采集配置

如果使用了 prometheus-operator，往往使用 `ServiceMonitor` 和 `PodMonitor` 这样的 CRD 资源来动态添加采集配置，云原生监控也支持这种用法，如果只是将当前集群的 prometheus-operator 迁移到云原生监控，没有迁移集群，那就无需迁移动态配置，只要用云原生监控关联了本集群，之前创建的  `ServiceMonitor` 和 `PodMonitor`  资源就会自动在云原生监控中生效。

如果要做跨集群迁移，可以将之前集群的 CRD 资源导出，然后选择性的在被关联了云原生监控的集群中重新 apply 一下，下面给出如何在自建 Prometheus 集群中批量导出 `ServiceMonitor` 和 `PodMonitor` 的示例。

首先确保安装了 kubectl 并能够操作自建 Prometheus 的集群，准备导出脚本 `prom-backup.sh`:

``` bash
_ns_list=$(kubectl get ns | awk '{print $1}' | grep -v NAME)
count=0
declare -a types=("servicemonitors.monitoring.coreos.com" "podmonitors.monitoring.coreos.com")
for _ns in ${_ns_list}; do
    ## loop for types
    for _type in "${types[@]}"; do
	    echo "Backup type [namespace: ${_ns}, type: ${_type}]."
        _item_list=$(kubectl -n ${_ns} get ${_type} | grep -v NAME | awk '{print $1}' )
	    ## loop for items
    	for _item in ${_item_list}; do
	        _file_name=./${_ns}_${_type}_${_item}.yaml
		    echo "Backup kubernetes config yaml [namespace: ${_ns}, type: ${_type}, item: ${_item}] to file: ${_file_name}"
		    kubectl -n ${_ns} get ${_type} ${_item} -o yaml > ${_file_name}
		    count=$[count + 1]
		    echo "Backup No.${count} file done."
        done;
    done;
done;
```

运行一下:

``` bash
bash prom-backup.sh
```

会将每个 `ServiceMonitor` 与 `PodMonitor` 资源导出成单独的 yaml 文件:

``` bash
$ ls
kube-system_servicemonitors.monitoring.coreos.com_kube-state-metrics.yaml
kube-system_servicemonitors.monitoring.coreos.com_node-exporter.yaml
monitoring_servicemonitors.monitoring.coreos.com_coredns.yaml
monitoring_servicemonitors.monitoring.coreos.com_grafana.yaml
monitoring_servicemonitors.monitoring.coreos.com_kube-apiserver.yaml
monitoring_servicemonitors.monitoring.coreos.com_kube-controller-manager.yaml
monitoring_servicemonitors.monitoring.coreos.com_kube-scheduler.yaml
monitoring_servicemonitors.monitoring.coreos.com_kube-state-metrics.yaml
monitoring_servicemonitors.monitoring.coreos.com_kubelet.yaml
monitoring_servicemonitors.monitoring.coreos.com_node-exporter.yaml
```

你可以自行筛选和修改，然后将这些 yaml 重新 apply 到被关联了云原生监控的集群中(请勿 apply 已经存在或功能相同的采集规则)，云原生监控会自动感知这些动态采集规则并进行采集。

如果后续需要增加 `ServiceMonitor` 或 `PodMonitor`，可以使用控制台可视化添加，也可以脱离控制台直接用 yaml 创建，用法与社区的 CRD 完全兼容。

## 迁移静态采集配置

如果自建 Prometheus 直接使用的 Prometheus 原生配置文件，可以将其转换为云原生监控的 RawJob，兼容原生配置文件的 `scrape_configs` 配置项，只需做一些小的改动。

点击 【云原生监控】-【关联集群】-【数据采集配置】:

![](https://main.qcloudimg.com/raw/fb5c0c610cec5b6366736c57af7cfced.png)

新增 RawJob:

![](https://main.qcloudimg.com/raw/8026b04f1e6489641e68a654dc3234ea.png)

将原始配置中的 job 配置粘贴进来:

![](https://main.qcloudimg.com/raw/9bd9d5363e1e60990997c292c2368d2e.png)

> 可以将所有需要导入的 job 数组都直接粘贴进来，点【确定】后会自动拆分成多个 RawJob，名称为每个 job 的 `job_name` 字段

## 迁移全局配置

云原生监控也提供了 Prometheus 这个 CRD 资源，可以通过修改它来修改一些全局的配置:

``` bash
$ kubectl get ns
prom-fnc7bvu9     Active   13m
$ kubectl -n prom-fnc7bvu9 get prometheus
NAME               VERSION   REPLICAS   AGE
tke-cls-hha93bp9                        11m
$ kubectl -n prom-fnc7bvu9 edit prometheus tke-cls-hha93bp9
```

修改 `scrapeInterval` 可修改默认的采集抓取间隔时长 (默认 15s)，也可以修改 `externalLabels`，为所有时序数据增加默认的 label 标识。

## 迁移聚合配置

Prometheus 的聚合配置，不管是原始的 [Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) 静态配置还是 [PrometheusRule](https://github.com/prometheus-operator/prometheus-operator/blob/master/Documentation/api.md#prometheusrule) 动态配置，每条规则的格式都是一样的。在云原生监控点击 【聚合规则】-【新建聚合规则】来创建聚合规则:

![](https://main.qcloudimg.com/raw/a7f252e405d42b1b80a347a21fd1193a.png)

使用 PrometheusRule 的格式，将每条规则粘贴到 `groups` 数组里即可:

![](https://main.qcloudimg.com/raw/90fe3fb2d16c70389b3464b84987276d.png)

> 如果之前本身也是用的 PrometheusRule 定义的聚合规则，还是建议将其按照上述方式做下迁移，如果直接用 yaml 在集群中创建 PrometheusRule 资源，云原生监控暂时无法将其显示到控制台。

## 迁移告警配置

这里给一个 Prometheus 告警原始配置示例:

``` yaml
  - alert: NodeNotReady
    expr: kube_node_status_condition{condition="Ready",status="true"} == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      description: 节点 {{ $labels.node }} 长时间不可用 (集群id {{ $labels.cluster }})
```

转换为云原生监控上类似的监控配置，点击 【告警配置】-【新建告警策略】 :

![](https://main.qcloudimg.com/raw/048be518a2bc113341bca393fc066269.png)

![](https://main.qcloudimg.com/raw/bf30bd3141f872415425c537becfeb9c.png)

关键说明:

* `PromQL` 配置等同于原始配置的 expr 字段，也是告警的核心配置，是用于指示告警触发条件的 PromQL 表达式。
* `Labels` 等同于原始配置的 labels，为告警添加额外的 label。
* `告警内容` 表示推送的告警内容，通常使用模板，插入一些变量，通常建议带上集群 id，`{{ $labels.cluster }}` 就表示集群 id。
* `持续时间` 等同于原始配置的 `for`，表示达到告警条件多久之后还没恢复就推送告警。
* `收敛时间` 等同于 AlertManager 的 [repeat_interval](https://prometheus.io/docs/alerting/latest/configuration/#route) 配置，表示某个告警推送之后多久之后还未恢复就再次推送，即相同告警的推送间隔时长。

上面的示例告警配置表示节点状态变为 NotReady 之后，5 分钟内未恢复就推送告警，如果长时间未恢复，就间隔 1 小时再次推送告警。告警渠道支持腾讯云与 WebHook 两类:

![](https://main.qcloudimg.com/raw/c4d6914800779ecacf81b55d6750faae.png)

腾讯云告警渠道集成了下面几种，可根据自身需求勾选:

![](https://main.qcloudimg.com/raw/91e1df76edeb357a926b6c497417aa77.png)

如果需要更多告警渠道，如钉钉、Zoom 等，可自行部署相关的 WebHook 后端，然后在云原生监控这里指定 WebHook 的 URL:

![](https://main.qcloudimg.com/raw/f4c640ac5317dd3ca7d6b110b8f56ffa.png)

上面示例告警的微信推送效果如下:

![](https://main.qcloudimg.com/raw/fc61cdd39d36844100a6b64833ea92ef.png)

## 迁移 Grafana 面板

自建 Prometheus 往往积累了许多自定义的 Grafana 监控面板，如果要迁移到另一个平台，在面板数量较多的情况下，挨个导出再导入这种方式效率太低，这里给一个批量导出导入面板的方法。

我们借助 [grafana-backup](https://github.com/ysde/grafana-backup-tool) 这个工具可以实现 grafana 面板的批量导出和导入，首先需要安装下这个工具:

``` bash
pip3 install grafana-backup
```

> 推荐使用 python3，使用 python2 版本可能会有些兼容性问题

然后分别登录自建 Grafana 与云原生监控的 Grafana，创建一个 admin 的 APIKey:

![](https://main.qcloudimg.com/raw/b4800bdefcb3b644cbe327247c28eff9.png)

![](https://main.qcloudimg.com/raw/3f9c4e6f40374c47cf9ae0c7b982c1fa.png)

创建完后保存好，接着准备备份配置文件:

1. 在自建 Prometheus 集群的一个节点上安装 kubectl 并配置好 kubeconfig，保证能够操作集群。

2. 获取自建 Grafana 的访问地址:

   ``` bash
   $ kubectl -n  monitoring get svc
   NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
   grafana                 ClusterIP   172.21.254.127   <none>        3000/TCP                     25h
   ```

   > 本例中 grafana 的集群内访问地址为: http://172.21.254.127:3000

3. 准备 grafana-backup 的配置文件 (写入 grafana 地址与 APIKey):

   ``` bash
   export TOKEN=<TOKEN>
   cat > ~/.grafana-backup.json <<EOF
   {
     "general": {
       "debug": true,
       "backup_dir": "_OUTPUT_"
     },
     "grafana": {
       "url": "http://172.21.254.127:3000",
       "token": "${TOKEN}"
     }
   }
   EOF
   ```

   > <TOKEN> 替换为自建 Grafana 的 APIKey，url 地址也替换为自己环境中的地址

配置文件准备好后，直接执行以下命令将所有面板全部导出:

``` bash
grafana-backup save
```

最终以一个压缩文件的形式保存 (在 `_OUTPUT_` 目录下):

``` bash
tree _OUTPUT_
_OUTPUT_
└── 202012151049.tar.gz

0 directories, 1 file
```

然后再准备还原的配置，将 `<TOKEN>` 替换为云原生监控 Grafana 的 APIKey，url 替换为云原生监控 Grafana 的访问地址 (通常用外网访问地址，需开启):

``` bash
export TOKEN=<TOKEN>
cat > ~/.grafana-backup.json <<EOF
{
  "general": {
    "debug": true,
    "backup_dir": "_OUTPUT_"
  },
  "grafana": {
    "url": "http://prom-xxxxxx-grafana.ccs.tencent-cloud.com",
    "token": "${TOKEN}"
  }
}
EOF
```

最后将导出的面板一键导入到云原生监控的 Grafana:

``` bash
grafana-backup restore _OUTPUT_/202012151049.tar.gz
```

导入之后，建议给所有面板都加上 `cluster` 的过滤字段，云原生监控支持多集群，会给每个集群的数据都打上 `cluster` 标签，用集群 id 来区分不同集群。

点击面板的 【Dashboard settings】-【Variables】-【New】 来新建 `cluster` 字段:

![](https://main.qcloudimg.com/raw/4fc513c387eac66d7e9dbb6d0ee9ad1f.png)

> label_values 中填入当前面板任意涉及到的一个指标名即可 (本例中是 node_uname_info)

最后修改所有面板中的 PromQL 查询语句，加入 `cluster=~"$cluster"` 的过滤条件:

![](https://main.qcloudimg.com/raw/2fdd3bb6dfd4e59072c0bb4b41d2e6c5.png)

## 与现有系统集成

### 接入自建 Grafana

云原生监控提供了 Prometheus 的 API，如果希望使用自建的 Grafana 来展示监控，可以将云原生监控的数据作为一个 Prometheus 数据源添加到自建 Grafana 中去，Prometheus API 的地址在【基本信息】中能查到:

![](https://main.qcloudimg.com/raw/c42965924e1ace83249e0b181880fada.png)

> 确保自建的 Grafana 与云原生监控在同一 VPC 或者网络做了打通

然后在 Grafana 中添加该地址作为 Prometheus 数据源:

![](https://main.qcloudimg.com/raw/70dfd95e69c3764c62dc874dfbb8ff68.png)

### 接入自建 AlertManager

如果有更复杂的告警需求，或者想使用内部自建的 AlertManager 来统一告警，也可以选择让云原生监控的告警接入自建的 AlertManager，只需在创建云原生监控实例的时候，在高级设置里填入自建 AlertManager 的地址即可:

![](https://main.qcloudimg.com/raw/72fa6c36807d366ca4a96059e2cdd51c.png)