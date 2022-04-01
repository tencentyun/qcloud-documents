本文将详细为您介绍腾讯云云服务器（CVM）如何从0开始接入 Prometheus 监控服务。

## 购买 Prometheus
>?购买的 Prometheus 实例需跟监控的云服务器同一个 vpc 下，能实现网络互通。

1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，单击**新建**购买 Prometheus 实例 。 
![](https://qcloudimg.tencent-cloud.cn/raw/c08d09fb5bfb6698ec36da720c0ca4bf.png)
2. 在购买页中，选择合适的实例规格、网络。选择相同 vpc 网段，保证 Prometheus 能与需要采集的云服务器网段相同，才能采集到数据。实例规格，可根据自己的业务上报量进行选择。
![](https://qcloudimg.tencent-cloud.cn/raw/88a612d72ba7f86c3770485db6dcb982.png)
![](https://qcloudimg.tencent-cloud.cn/raw/086590642923b9661a5696ad0daa7b1d.png)
3. 选择完后，单击立即购买并支付即可。
>?如需了解 Prometheus 更多定价规则，请参考 [产品定价](https://cloud.tencent.com/document/product/1416/55777)。

## 安装 Agent
1. 在 Prometheus 控制台新建 Agent：
登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，单击 **Agent 管理 > 新建**，输入 Agent 名称并保存。
![](https://qcloudimg.tencent-cloud.cn/raw/043a422d86346a6d429368b87a6a0ea8.png)
2. 在云服务器上执行命令安装 Agent：
登录  [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，单击 **Agent 管理**，进入 Agent 的安装指南页面。根据页面的安装指南，到上报数据的同一台云服务器执行命令安装 Agent。
![](https://qcloudimg.tencent-cloud.cn/raw/f9818a6826fa87b90a292e0fb83b0b05.png)
3. 安装成功后，执行下列命令查看 Agent 状态
```
systemctl status prometheus
```
![](https://qcloudimg.tencent-cloud.cn/raw/b7a1f373af49e06440ccb797b87977e3.png)
![](https://qcloudimg.tencent-cloud.cn/raw/377220fe469914502d68f78ffad4d0a9.jfif)



## 接入云服务器基础指标
1. 下载安装 node_expoter：
在需要上报的云服务器上，下载并安装 node_expoter（采集基础指标数据的 exporter），您可以单击进入 Prometheus 开源官网下载地址 [node_expoter](https://prometheus.io/download/#node_exporter)，也可以直接执行下列命令，下载解压：
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gztar -xvf node_exporter-1.3.1.linux-amd64.tar.gz
```
文件目录如下: 
![](https://qcloudimg.tencent-cloud.cn/raw/215bcb6ce3c069bd73eda5a9b1f8bdee.jfif)
2. 运行 node_exporter 采集基础监控数据：
 1. 执行 node_exporter
```
./node_exporter
```
如下图所示即为成功采集到了基础监控数据。
![](https://qcloudimg.tencent-cloud.cn/raw/fb9bb9fcfb6f0e1a47ec2942e7215299.png)
ii. 可通过下列命令，将该基础监控数据暴露在9100 端口：
```
curl 127.0.0.1:9100/metrics
```
如下图为执行命令后看到的暴露出来的指标监控数据。
![](https://qcloudimg.tencent-cloud.cn/raw/4295420750699bf57711deb515319131.jfif)
3. 新增抓取任务：
登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，进入 **Agent 管理 > 抓取任务 > 新建**，在抓取任务管理页中新建抓取任务。如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/89cb21469446c454546ea74aaeb9a029.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f7f8e58a0c7ce0f700c3289c019bb812.png)
抓取任务参考配置如下：
```
job_name: cvm_node_exporterhonor_timestamps: falsescrape_interval: 30smetrics_path: /metricsscheme: httpstatic_configs:- targets:  - 111.111.111.111:9100
```
>!targets 下的 IP 地址要改成自身 CVM 监控数据的地址。
4. 查看数据是否上报成功：
登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，单击 Grafana 图标，进入 Grafana。
![](https://qcloudimg.tencent-cloud.cn/raw/d1d5a1bc33284f949a4d02286166262e.png)
如下图所示，到 Explore 搜索下 {job="cvm_node_exporter"} 查看是否有数据，若有数据，则表示上报成功。
![](https://qcloudimg.tencent-cloud.cn/raw/f31c1e88560bd7dce8649f1b015aea03.png)
5. 配置 Dashboard 界面：Dashboard 界面每个产品都会有一些现成的 json 文件，可以直接导入。  
 1. **下载 Dashboard 文件**：登录 [Dashboard 界面](https://grafana.com/grafana/dashboards/)，单击搜索 node_exporter，选择最新的 Dashboard 并下载。
![](https://qcloudimg.tencent-cloud.cn/raw/3b864762d3c049a3793312687b11daa3.png)
ii. **导入 Dashboard 的 json 文件**：登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)，进入**基本信息 > Grafana 地址**，单击进入 Grafana，在 Grafana 控制台 > Create > Import > 在 Upload JSON file 中上传 Dashboard 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/fbbda643258f052fdadd0f49f4c3a3bb.png)
![](https://qcloudimg.tencent-cloud.cn/raw/e95aab1e308f92a4a14dc6e7e3f19ed5.png)


## 接入云服务器业务层指标


Prometheus 根据监控的不同场景提供了 Counter、Gauge、Historgram、Summary 四种指标类型。Prometheus 社区提供了多种开发语言的 SDK，每种语言的使用方法基本上类似，主要是开发语言语法上的区别，下面主要以 Go 作为例子，使用 Counter 指标类型如何上报自定义监控指标数据。其余指标类型请参考 [自定义监控](https://cloud.tencent.com/document/product/1416/56027)。

#### Counter
计数类型，数据是单调递增的指标，服务重启之后会重置。可以用 Counter 来监控请求数/异常数/用户登录数/订单数等。
1. 如何通过 Counter 来监控订单数：
```
package order

import (
    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promauto"
)

// 定义需要监控 Counter 类型对象
var (
    opsProcessed = promauto.NewCounterVec(prometheus.CounterOpts{
        Name: "order_service_processed_orders_total",
        Help: "The total number of processed orders",
    }, []string{"status"}) // 处理状态
)

// 订单处理
func makeOrder() {
    opsProcessed.WithLabelValues("success").Inc() // 成功状态
    // opsProcessed.WithLabelValues("fail").Inc() // 失败状态

    // 下单的业务逻辑
}
```
例如，通过 rate() 函数获取订单的增长率：
```
rate(order_service_processed_orders_total[5m])
```
2. 采集数据：
完成相关业务自定义监控埋点之后，应用发布，即可通过 Prometheus 来抓取监控指标数据。采集完成后，等待数分钟，您即可在 Prometheus 监控服务集成的 Grafana 中查看业务指标监控数据。
![img](https://main.qcloudimg.com/raw/fc6bf3f5cfbab1bbd931d418b9dddef2.png)
