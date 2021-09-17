## 功能介绍

 Prometheus 监控服务在继承开源 Prometheus 监控能力的同时 ，还提供高可用的 Prometheus 托管服务及与开源可视化的 Grafana。为您减少用户的开发及运维成本。

>?对于已创建腾讯云 [容器服务 TKE](https://cloud.tencent.com/document/product/457) 的用户，您可以在 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus) 创建 Prometheus 实例并安装 Prometheus 监控插件对其进行监控，同时 Prometheus 监控服务集成 Grafana 及预定义 Dashboard 来查看不同维度的性能指标数据。

## 前提条件

创建腾讯云容器服务 [托管版集群](https://cloud.tencent.com/document/product/457/32189#TemplateCreation)。

## 操作步骤

### 步骤1：创建 Prometheus 实例[](id:step1)

1. 登录 [ Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击**新建**，进入新建购买页，可根据自己的实际情况购买对应的实例，详情请参见 [创建实例](https://cloud.tencent.com/document/product/1416/55982)。


### 步骤2：集成容器服务 TKE[](id:step2)

Prometheus 监控服务已经深度集成了腾讯云容器服务  TKE，用户只需要一键安装就可以对 Kubernetes 集群及运行在上面的服务进行监控。

1. 在实例列表中，选择需要集成的 Prometheus 实例，单击**实例 ID** 或者右侧的**管理**，进入 Prometheus 实例管理页。
2. 单击**集成容器服务** > 选择对应的容器集群 > 单击**安装**来进行自动化集成，在安装弹框中可以选择需要集成的基础监控组件。
![](https://main.qcloudimg.com/raw/f18800745d34376a61049f47a0ae12d1.png)
3. 整体集成操作为异步操作，大概需要2 - 3分钟，监控状态显示“已安装”即安装成功。
  >?集成过程中需要用户授权之后来操作腾讯云容器服务 TKE，具体的授权操作请参见 [服务授权相关角色权限说明](https://cloud.tencent.com/document/product/1416/56023)。



### 步骤3：集成中心[](id:step3)

为了方便用户接入，Prometheus 监控服务对常用的`开发语言`/`中间件`/`大数据`进行了集成，用户只需根据指引即可对相应的组件进行监控，同时提供了开箱即用的 Grafana 监控大盘。
![](https://main.qcloudimg.com/raw/c1564d7abcd674b1958fb8c6208e9aab.png)


### 步骤4：Grafana 查看监控数据[](id:step4)

Prometheus 监控服务提供了开箱即用的 Grafana ，同时也集成了丰富的 Kubernetes 基础监控的 Dashboard，以及常用服务监控的 Dashboard，用户可以开箱即用。

1. 在 [Prometheus 实例](https://console.cloud.tencent.com/monitor/prometheus) 列表，找到对应的 Prometheus 实例，单击实例 ID 右侧<img src="https://main.qcloudimg.com/raw/978c842f0c093a31df8d5240dd01016d.png" width="2%">图标，打开您的专属 Grafana，输入账号密码，即可进行 Grafana 可视化大屏操作区。
2. 进入 Grafana，单击<img src="https://main.qcloudimg.com/raw/7e3fff6131aa085987552a9725e9ae54.png" width="2%">图表，展开监控面板。
![](https://main.qcloudimg.com/raw/2821a37a7b766da09c1b6b3f995b32b4.png)
3. 单击对应的监控图表名称即可查看监控数据。
![](https://main.qcloudimg.com/raw/8d9c88d74a9fc1732145040f6df3954f.png)
>?如需了解 Grafana 更多操作说明，请参见 [Grafana 官网使用手册](https://grafana.com/docs/grafana/latest/getting-started/)。
