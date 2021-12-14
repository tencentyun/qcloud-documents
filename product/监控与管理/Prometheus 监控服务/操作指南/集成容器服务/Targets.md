为了方便用户查看 Prometheus 抓取运行的状态，实时了解监控数据是否正常被 Prometheus Agent 抓取到。

## 准备工作

- 已经为容器服务 TKE 集群安装 Prometheus Agent，具体可以参见 [Agent 管理](https://cloud.tencent.com/document/product/248/48859)。
- 通过 [容器服务](https://console.cloud.tencent.com/tke2/cluster?rid=4) 集群管理页面中单击**集群 ID** 进入到容器服务集成管理页面。

## 说明

- 在任务状态中没有找到对应的抓取任务，说明 Prometheus Agent 没有正确获取到对应的抓取任务的配置，请查看对应的配置是否正确。
- **红色**数值表示该任务下有多少个抓取任务失败，展开可以查看具体的失败原因。

## 操作步骤

1. 单击**集成容器服务**上面的 **Targets**，可以查看当前 Prometheus Agent 所有抓取任务的任务以及失败的原因，如下图：
![](https://main.qcloudimg.com/raw/175f5037927fb1c2f8354dff2ee14f6d.png)
![](https://main.qcloudimg.com/raw/d58451f7782b17c172d38adcf0957893.png)
2. 同时也可以通过云监控 Prometheus 托管服务提供的 Grafana 服务查看更详细的抓取任务的监控状态，打开对应的 Grafana 查看预设的 **Prometheus** Dashboard 来查看，如下图：
![](https://main.qcloudimg.com/raw/ce5c3c3d0a183fe0490a2f48f54cac37.png)
