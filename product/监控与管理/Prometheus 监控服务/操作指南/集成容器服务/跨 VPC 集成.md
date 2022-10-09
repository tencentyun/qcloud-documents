Prometheus 监控服务支持跨 VPC（与 Prometheus 实例所处的 VPC 不同） 的容器集群集成，方便您在同一实例管理和查看指标监控数据。

## 前提条件
Prometheus 实例所处的 VPC 与  容器集群所处的 VPC 间已实现网络互通。您可以通过对等连接或云联网方式连接不同的 VPC，详情请参考 [连接其它 VPC](https://cloud.tencent.com/document/product/215/36698)。


## 操作步骤  
1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 在实例列表中，选择需要操作的 Prometheus 实例，单击**实例 ID** 或者右侧的**管理**进入实例管理页面。
3. 在管理页面的左侧菜单**集成容器服务**进入容器集成页面。
4. 勾选**开启跨 VPC 集成**并确认开启，列表中会展示出全部容器集群（包括与 Prometheus 实例不同的 VPC 的集群）。
![](https://qcloudimg.tencent-cloud.cn/raw/a404da722b87dc0b522a823bb0935ce3.png)
6. 在列表中找到您需要集成的容器集群，在操作列单击**安装**，勾选需要安装的 Agent 并单击**确认**。成功安装 Agent 即完成跨 VPC 集成。

更多操作请参考：
- [安装 Agent](https://cloud.tencent.com/document/product/1416/56000#install_agent)。
- [集成 Kubernetes 相关的基础监控](https://cloud.tencent.com/document/product/1416/56002)。
- [抓取任务状态](https://cloud.tencent.com/document/product/1416/56538) 及 [查看 Agent 状态](https://cloud.tencent.com/document/product/1416/56004)。
