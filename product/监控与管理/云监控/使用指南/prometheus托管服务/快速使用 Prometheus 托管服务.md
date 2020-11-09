云监控 Prometheus 服务在继承开源 Prometheus 监控能力的同时 ，还提供高可用的 Prometheus 托管服务及与开源可视化的 Grafana，为您减少用户的开发及运维成本。
对于已创建腾讯云容器服务 TKE 的用户，您可以在云监控创建 Prometheus 实例并安装 Prometheus 监控插件对其进行监控，同时云监控 Prometheus 服务集成 Grafana 及预定义 Dashboard 来查看不同维度的性能指标数据。

## 准备工作

1. 创建 [腾讯云容器服务—托管版集群](https://cloud.tencent.com/document/product/457/32189#.E4.BD.BF.E7.94.A8.E6.A8.A1.E6.9D.BF.E6.96.B0.E5.BB.BA.E9.9B.86.E7.BE.A4.3Cspan-id.3D.22templatecreation.22.3E.3C.2Fspan.3E)：在腾讯云容器服务中创建 Kubernetes 集群。
2. 申请开通云监控 [Prometheus 托管服务](https://cloud.tencent.com/apply/p/cb3dj6vzk8s)。





## 操作步骤

### 创建 Prometheus 实例

1. 登录 [云监控 Prometheus 控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击【新建】，进入新建购买页，可根据自己的实际情况购买对应的实例，具体参考 [创建实例](https://cloud.tencent.com/document/product/248/48690)。

### 集成容器服务 TKE

云监控 Prometheus 托管服务已经深度集成了腾讯云容器服务 TKE，用户只需要一键安装就可以对 Kubernetes 集群及运行在上面的服务进行监控。

1. 在实例列表中，选择需要集成的 Prometheus 实例，单击【实例 ID】或者右侧的【管理】，进入 Prometheus 实例管理页。
2. 单击【集成容器服务】> 选择对应的容器集群 >【安装】来进行自动化集成，在安装弹框中可以选择需要集成的基础监控组件，整体集成操作为异步操作，大约需要2 - 3分钟，监控状态显示 “已安装” 即安装成功。
![](https://main.qcloudimg.com/raw/28f3e59892f17700f7eb90850b8d7c60.png)
>?集成过程中需要用户授权之后来操作腾讯云容器服务 TKE，具体的授权操作请参考 [服务授权相关角色权限说明](https://cloud.tencent.com/document/product/248/48706)。

### Grafana 查看监控数据

配合 Prometheus，云监控提供了开箱即用的 Grafana 服务供用户使用，同时也集成了丰富的 Kubernetes 基础监控的 Dashboard，以及常用服务监控的 Dashboard，用户可以开箱即用。

1. 在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的  Prometheus 实例，单击实例 ID 右侧【<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="3%"/>】 图标，打开您的专属 Grafana，输入您的账号密码，即可进行 Grafana 可视化大屏操作区。
2. 进入 Grafana，单击【<img src="https://main.qcloudimg.com/raw/7e3fff6131aa085987552a9725e9ae54.png" width="3%"/>】图表，展开监控面板，单击对应的监控图表名称即可查看监控数据。
![](https://main.qcloudimg.com/raw/2821a37a7b766da09c1b6b3f995b32b4.png)
![](https://main.qcloudimg.com/raw/8d9c88d74a9fc1732145040f6df3954f.png)
>?如需了解 Grafana 更多操作说明请参见 [Grafana官网使用手册](https://grafana.com/docs/grafana/latest/getting-started/what-is-grafana)。
