## 操作场景

腾讯云 CKafka 专业版实例默认为所有用户提供了外部监控服务的接入方式，通过提供的接入点可完成 CKafka 实例的监控，包括**未同步副本、主题流入消息速率**等一系列开源 Kafka 可监控的度量指标。

腾讯云 **CKafka 专业版**实例目前提供 Prometheus 抓取监控数据的 broker 节点指标信息，包括有 CPU、内存使用情况、系统负载等基本监控度量指标，以及 broker JMX 暴露出的度量指标。


## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击目标实例的“ID”，进入实例基本信息页面。
3. 在**使用Prometheus监控**模块单击右上角的**获取监控目标**，选择 VPC 和子网。
![](https://qcloudimg.tencent-cloud.cn/raw/38ced4a030cd8e901e5c5f89b7da92fc.png)
4. 单击**提交**，获取一组监控目标。
![](https://qcloudimg.tencent-cloud.cn/raw/971340b51689204493944646283efc21.png)
5. 下载 [Prometheus](https://prometheus.io/download/)，并配置监控抓取地址。

   1. 进入 Prometheus 程序包所在目录，执行如下命令，解压 Prometheus 程序包。
   ```bash
   tar -vxf prometheus-2.30.3.linux-amd64.tar.gz
   ```
   2. 修改配置文件 `prometheus.yml`，增加 `jmx_exporter` 与 `node_exporter` 抓取任务。
   ```yaml
   scrape_configs:
     # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
     - job_name: "prometheus"
       # metrics_path defaults to '/metrics'
       # scheme defaults to 'http'.
       static_configs:
         - targets: ["localhost:9090"]
   
     - job_name: "broker-jmx-exporter"
       scrape_interval: 5s
       metrics_path: '/metrics'
       static_configs:
         - targets: ['10.x.x.0:60001','10.x.x.0:60003','10.x.x.0:60005']
           labels:
              application: 'broker-jmx'
     - job_name: "broker-node-exporter"
       scrape_interval: 10s
       metrics_path: '/metrics'
       static_configs:
          - targets: ['10.x.x.0:60002','10.x.x.0:60004','10.x.x.0:60006']
            labels:
              application: 'broker-node'
   ```
   其中 `broker-jmx` 是 Prometheus 抓取 broker 的 jmx 指标配置的标签项，Targets 其中包含映射的端口信息，而 `broker-node-exporter` 为抓取 broker 所在节点的基本指标配置的标签项， `scrape_interval` 为抓取监控度量数据的频率。
   3. 启动 Prometheus。
   ```bash
   ./prometheus --config.file=prometheus.yml --web.enable-lifecycle
   ```
   4. 打开 Prometheus 提供的 UI 界面查看接入的 Targets 状态是否正常，如在浏览器输入 `http://localhost:9090`。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/3d7fcddaa58fb897aaa597e3f6a6588f.png)
   5. 检查 Targets 状态都是 `UP`。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e54ab826f80668233e3cd3e90b1927f4.png)
	如果 Targets 状态为 `DOWN` 则需要检查网络访问是否可达，或根据状态栏最后的 Error 选项查看原因。

6. 查询监控指标数据。
   单击 Graph 选项输入查询的指标名称即可看到相应的监控数据，例如输入`node_memory_MemAvailable_bytes` ，点击**execute**。
	 ![](https://qcloudimg.tencent-cloud.cn/raw/118a8acfadc562a83f0ebc621eaf79fe.png)
