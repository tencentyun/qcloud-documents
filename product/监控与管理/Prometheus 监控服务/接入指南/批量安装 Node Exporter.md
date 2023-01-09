Prometheus 监控服务支持使用 CVM  Node Exporter 采集云服务器（Cloud Virtual Machine，CVM）实例上的指标。目前已支持用户在控制台批量选择 CVM 实例并安装 Node Exporter。您可以参考下文进行操作。

## 前提条件

CVM 已 [安装腾讯云自动化助手（TencentCloud Automation Tools，TAT）](https://cloud.tencent.com/document/product/1340/51945)。

## 操作步骤

> ?目前仅支持集成相同 VPC 下的 CVM。

1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击对应的 Prometheus 实例 ID ，进入实例管理页。
3. 在左侧菜单栏中单击**集成中心**，在集成中心页中找到 **CVM Node Exporter** 模块，单击**一键安装**。
![](https://qcloudimg.tencent-cloud.cn/raw/fccadc66ed60f539116729c690d9e04e.png)
4. 进入 Node Exporter 编辑页，勾选已安装腾讯云自动化助手的 CVM 实例，并单击右侧 ![](https://qcloudimg.tencent-cloud.cn/raw/d4dcd8cab2a6569cbe7baa3df6a10101.png) 按钮，完成后单击**保存**。
您可以在实例列表-自动化助手列中可查看自动化助手安装状态，若未安装，请参考 [安装腾讯云自动化助手](https://cloud.tencent.com/document/product/1340/51945) 指引进行安装。
![](https://qcloudimg.tencent-cloud.cn/raw/14d0fda8dc902658aad03cce85bfbf55.png)
5. 保存成功后，等待安装。如下图，若运行状态为已部署，则安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/225e0f90b04a15ba632a23742f82b163.png)
