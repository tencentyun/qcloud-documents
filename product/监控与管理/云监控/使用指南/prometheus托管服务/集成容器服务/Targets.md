为了方便用户查看 Prometheus 抓取运行的状态，实时了解监控数据是否正常被 Prometheus Agent 抓取到。

## 准备工作

- 已经对某个容器服务 （TKE) 安装了 Prometheus Agent，具体可以参考 [Agent 管理](https://cloud.tencent.com/document/product/248/48859)。
- 通过容器服务列表点击【集群 ID】进入到容器服务集成管理页面。

## 说明

- 在任务状态中没有找到对应的抓取任务，说明 Prometheus Agent 没有正确获取到对应的抓取任务的配置，请查看对应的配置是否正确。
- 【红色】数值表示该任务下有多少个抓任任务是失败的，展开可以查看具体的失败原因。

## 操作步骤

1. 单击【集成容器服务】上面的【Targets】，可以查看当前 Prometheus Agent 所有抓取任务的任务以及失败的原因，如下图：
![](https://main.qcloudimg.com/raw/9029e60d93b309658ad4c698acd6fc74.png)
![](https://main.qcloudimg.com/raw/335e4c72f8f0d55598f2659527c7a6e6.png)
2. 同时也可以通过云监控 Prometheus 托管服务提供的 Grafana 服务查看更详细的抓取任务的监控状态，打开对应的 Grafana 查看预设的【Prometheus】Dashboard 来查看，如下图：
![](https://main.qcloudimg.com/raw/2b16f7d4cadafc2f974682fd35a4763a.png)
