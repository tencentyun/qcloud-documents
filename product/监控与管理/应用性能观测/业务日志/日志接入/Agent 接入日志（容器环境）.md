本文将为您介绍容器环境下，如何通过 sidecar 的方式安装 Agent 并完成日志接入。

## 前提
开通云监控-应用性能观测服务，并完成业务系统创建。参见 [快速入门](https://cloud.tencent.com/document/product/1463/57467) 

## 操作步骤
### 步骤1：日志上报配置
进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **日志分析** > **日志概览**页面，单击**日志接入**。
接入流程：
- 首先选择您的上报地域和业务系统。公测期上报地域仅支持广州。
- 根据您的日志内容，选择适合的日志类型。并选择 **Agent 采集**作为接入方式。
![](https://qcloudimg.tencent-cloud.cn/raw/45894cf24afd0d2215db353d0b981255.png)

### 步骤2：日志采集配置
- 采集路径配置：输入您日志存储的文件路径，支持输入多个路径。
- 所属应用：应用性能观测产品需要以应用为度关联您的业务指标，您可以从下拉列表中选择已经接入的服务，也可选择手动输入新的服务。
- 编码方式：日志文件的编码方式，默认 UTF-8。
- 采集模式：从日志文件头部/尾部开始采集，默认尾部采集。
- 高级配置（可选）：通过高级配置，可以额外配置日志采集排除路径、多行日志采集、保留和排除行等。
![](https://qcloudimg.tencent-cloud.cn/raw/037560c2efa4f5d6d5d453ba1a74e73a.png)

### 步骤3：Sidecar 方式安装探针
1.进入 [容器服务控制台-集群](https://console.cloud.tencent.com/tke2)。
2.单击对应的容器集群名称或 ID，进入工作负载.
![](https://qcloudimg.tencent-cloud.cn/raw/3619b40b7255becec0a329f4664a1dc6.png)
找到目标服务所在 Pod 配置挂载点，共享日志目录。
![](https://qcloudimg.tencent-cloud.cn/raw/b9ed9a1c1ed437f57fa21c1fdf211a8d.png)
 - 找到业务所在服务 Pod 添加该挂载点，指向业务日志目录。
![](https://qcloudimg.tencent-cloud.cn/raw/87c1228412209c4c6882fe92f5790ec6.png)
 - Sidecar 方式部署 Agent。
搜索 Agent 镜像 **ccr.ccs.tencentyun.com/cmonitor/tccm-agent** ，选择**版本1.2.12**并部署。
<img style="width:716px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/6651383e7b2a3da421c3dcd7c57ab3b5.png" />
 - 为 Agent 所在 sidecar 添加日志挂载点。
![](https://qcloudimg.tencent-cloud.cn/raw/e6478aa99cb5fb0d6b19ee8b6d8df6ac.png)

### 步骤4：配置上报信息
为 Agent sidecar 中配置如下环境变量。

|变量名 |变量值|
|---------|---------|
|TCCM_TOKEN |腾讯云账号 APPID |
|TCCM_REGION |业务所属地域 |
|TCCM_LOG_TOKEN |在应用性能观测平台获取到的 Token |

![](https://qcloudimg.tencent-cloud.cn/raw/18ee9472c15b2da9b19f7d31fb6a2593.png)

### 步骤三：验证是否上报成功
上述步骤配置完成后，等待1~2分钟，若在 [日志检索](https://console.cloud.tencent.com/apm/explorer/log/query) 所看到上报的日志，则说明上报成功。




