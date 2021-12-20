Goosefs 可以通过配置将指标数据输出到不同的监控系统中，Prometheus 是其中之一。Prometheus 是一个开源的监控框架，目前腾讯云监控已集成了 Prometheus，下文将重点介绍 Goosefs 监控指标，以及将监控指标上报到自建的 Prometheus 和云上 Prometheus 的流程。

## 准备工作

通过 Prometheus 构建监控体系需要先做如下准备工作：

- 配置 GooseFS 集群
- 下载 Prometheus 官方安装包或腾讯云 Prometheus 安装包
- 下载和配置 [Grafana](https://grafana.com/docs/grafana/latest/installation/#install-grafana/)

## 启用 GooseFS 监控指标上报配置

1. 编辑 GooseFs 配置 conf/goosefs-site.properties， 添加如下配置项，并使用 goosefs copyDir conf/ 拷贝到所有 worker节点，并重启集群 `./bin/goosefs-start.sh all`。
```plaintext
goosefs.user.metrics.collection.enabled=true
goosefs.user.metrics.heartbeat.interval=10s
```
2. master 和 worker 的 Prometheus 的监控指标可用如下的命令查看，其中 master 的 metrics 端口为9201，worker 的 metrics 端口为 9204：
```plaintext
curl <LEADING_MASTER_HOSTNAME>:<MASTER_WEB_PORT>/metrics/prometheus/
# HELP Master_CreateFileOps Generated from Dropwizard metric import (metric=Master.CreateFileOps, type=com.codahale.metrics.Counter)
...

curl <WORKER_IP>:<WOKER_PORT>/metrics/prometheus/
# HELP pools_Code_Cache_max Generated from Dropwizard metric import (metric=pools.Code-Cache.max, type=com.codahale.metrics.jvm.MemoryUsageGaugeSet$$Lambda$51/137460818)
...
```

## 上报监控指标到自建 Prometheus

1. 下载 Prometheus 安装包并解压，修改 prometheus.yml：
<pre class="rno-code-pre"><code class="language-plaintext">
# prometheus.yml
global:
	scrape_interval:     10s
	evaluation_interval: 10s
scrape_configs:
	- job_name: 'goosefs masters'
		metrics_path: /metrics/prometheus
		file_sd_configs:
		- refresh_interval: 1m
		files:
		- "targets/cluster/masters/*.yml"
	- job_name: 'goosefs workers'
		metrics_path: /metrics/prometheus
		file_sd_configs:
		- refresh_interval: 1m
		files:
		- "targets/cluster/workers/*.yml"
</code></pre>
2. 创建 targets/cluster/masters/masters.yml，添加 master 的 IP 和 port：
<pre class="rno-code-pre"><code class="language-plaintext">
 - targets:
	- "&lt;TARGERTS_MASTER_IP>:&lt;TARGERTS_MASTER_PORT>"
</code></pre>
3. 创建 targets/cluster/workers/workers.yml，添加 worker 的 IP 和 port：
<pre class="rno-code-pre"><code class="language-plaintext">
 - targets:
	- "&lt;TARGERTS_WORKER_IP>:&lt;TARGERTS_WORKER_PORT>"
</code></pre>
4. 启动 Prometheus，其中 --web.listen-address 指定 Prometheus 监听地址，默认端口号 9090：
<pre class="rno-code-pre"><code class="language-plaintext">
nohup ./prometheus --config.file=prometheus.yml --web.listen-address="&lt;LISTEN_IP>:&lt;LISTEN_PORT>" > prometheus.log 2>&1 &
</code></pre>
5. 查看可视化界面：
``` plaintext
http://<PROMETHEUS_BI_IP>:<PROMETHEUS_BI_PORT>
```
6. 查看机器实例：
``` plaintext
http://<PROMETHEUS_BI_IP>:<PROMETHEUS_BI_PORT>/targets
```

## 上报监控指标到腾讯云 Prometheus

1. 按照安装指南中的指引，在 master 机器上安装 Promethus agent：
<pre class="rno-code-pre"><code class="language-plaintext">
wget https://rig-1258344699.cos.ap-guangzhou.myqcloud.com/prometheus-agent/agent_install && chmod +x agent_install && ./agent_install prom-12kqy0mw agent-grt164ii ap-guangzhou &lt;secret_id> &lt;secret_key>
</code></pre>
2. 配置 master 和 worker 的抓取任务：

**方式一：**
<pre class="rno-code-pre"><code class="language-plaintext">
 job_name: goosefs-masters
 honor_timestamps: true
 metrics_path: /metrics/prometheus
 scheme: http
 file_sd_configs:
 - files:
	- /usr/local/services/prometheus/targets/cluster/masters/*.yml
	refresh_interval: 1m
job_name: goosefs-workers
honor_timestamps: true
metrics_path: /metrics/prometheus
scheme: http
file_sd_configs:
 - files:
	- /usr/local/services/prometheus/targets/cluster/workers/*.yml
	refresh_interval: 1m
</code></pre>

>! job_name 中没有空格，而单机的 Prometheus 的 job_name 中可以包含空格。
>

**方式二：**
<pre class="rno-code-pre"><code class="language-plaintext">
job_name: goosefs masters
honor_timestamps: true
metrics_path: /metrics/prometheus
scheme: http
static_configs:
- targets:
 - "&lt;TARGERTS_MASTER_IP>:&lt;TARGERTS_MASTER_PORT>"
 refresh_interval: 1m
 
job_name: goosefs workers
honor_timestamps: true
metrics_path: /metrics/prometheus
scheme: http
static_configs:
- targets:
 - "&lt;TARGERTS_WORKER_IP>:&lt;TARGERTS_WORKER_PORT>"
 refresh_interval: 1m
</code></pre>

>! 抓取任务按方式二配置，则无需在 targets/cluster/masters/ 路径下创建 masters.yml 和 workers.yml 文件。
> 

## 使用 Grafana 查看监控指标

1. 启动 Grafana：
```plaintext
nohup ./bin/grafana-server web > grafana.log 2>&1 &
```
2. 打开登录页面 http://&lt;GRAFANA_IP&gt;:&lt;GRAFANA_PORT&gt;，Grafana 的默认端口为 3000，username 和 password 都是 admin，首次登录后可修改密码。
3. 进入页面后，添加 Prometheus 的 Datasource：
```plaintext
<PROMETHEUS_IP>:<PROMETHEUS_PORT>
```
4. 导入 Goosefs 的 Grafana 模板，选择 json 导入（[点此下载 json](https://cos-data-lake-release-1253960454.file.myqcloud.com/goosefs/grafana/goosefs-grafana-dashboard.json)），并选择上面创建的 Datasource。
>! 云上 Prometheus 购买时需设置密码，云上 Grafana 的可视化监控界面配置和上面类似，注意 job_name 需要配置成一致。
>
5. 修改 DashBoard 以后，可以将 DashBoard 导出来。
