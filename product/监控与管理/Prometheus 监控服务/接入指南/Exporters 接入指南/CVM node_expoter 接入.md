本文将为您介绍如何通过安装 node_expoter，暴露云服务器基础指标至 Prometheus 监控服务。

## 操作步骤

### 步骤1：下载安装 node_expoter
在需要上报的云服务器上，下载并安装 node_expoter（采集基础指标数据的 exporter），您可以单击进入 Prometheus 开源官网下载地址 [node_expoter](https://prometheus.io/download/#node_exporter)，也可以直接执行下列命令，下载解压：
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz && tar -xvf node_exporter-1.3.1.linux-amd64.tar.gz
```
文件目录如下: 
![](https://qcloudimg.tencent-cloud.cn/raw/215bcb6ce3c069bd73eda5a9b1f8bdee.jfif)

### 步骤2：运行 node_exporter ，采集基础监控数据
1. 进入相关文件夹，执行 node_exporter。
```
cd node_exporter-1.3.1.linux-amd64
./node_exporter
```
如下图所示即为成功采集到了基础监控数据。
![](https://qcloudimg.tencent-cloud.cn/raw/fb9bb9fcfb6f0e1a47ec2942e7215299.png)
2. 可通过下列命令，将该基础监控数据暴露在9100端口：
```
curl 127.0.0.1:9100/metrics
```
如下图为执行命令后，可看到暴露出来的指标监控数据。
![](https://qcloudimg.tencent-cloud.cn/raw/4295420750699bf57711deb515319131.jfif)

### 步骤3：采集配置
登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，进入 **集成中心**  > **选择云服务器**，在任务配置中根据页面提示进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/7f09712ba63621c3f6635c224f90f2ff.png)
抓取任务参考配置如下：
```
job_name: example-job-name
metrics_path: /metrics
cvm_sd_configs:
- region: ap-guangzhou
  ports:
  - 9100
  filters:         
  - name: tag:示例标签键
    values: 
    - 示例标签值
relabel_configs: 
- source_labels: [__meta_cvm_instance_state]
  regex: RUNNING
  action: keep
- regex: __meta_cvm_tag_(.*)
  replacement: $1
  action: labelmap
- source_labels: [__meta_cvm_region]
  target_label: region
  action: replace
```

### 步骤4：查看数据是否上报成功：
登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，单击 Grafana 图标，进入 Grafana。
![](https://qcloudimg.tencent-cloud.cn/raw/d1d5a1bc33284f949a4d02286166262e.png)
如下图所示，到 Explore 搜索下 `job="cvm_node_exporter"}` 看是否有数据，若有数据，则表示上报成功。
![](https://qcloudimg.tencent-cloud.cn/raw/f31c1e88560bd7dce8649f1b015aea03.png)
	 
#### 步骤5：配置 Dashboard 	 
每个产品都会有一些现成的 json 文件，可以直接导入 Dashboard 。  
1. **下载 Dashboard 文件**：登录 [Dashboard 界面](https://grafana.com/grafana/dashboards/)，单击搜索 node_exporter，选择最新的 Dashboard 并下载。
![](https://qcloudimg.tencent-cloud.cn/raw/3b864762d3c049a3793312687b11daa3.png)
2.  **导入 Dashboard 的 json 文件**：登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，进入**基本信息** > **Grafana 地址**，单击进入 Grafana，在 **Grafana 控制台** > **Create** > **Import** > 在 **Upload JSON file** 中上传 Dashboard 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/fbbda643258f052fdadd0f49f4c3a3bb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e95aab1e308f92a4a14dc6e7e3f19ed5.png)
