## 操作场景

本文档可以指导您使用 TDMQ Pulsar 版时，将自己当前私有网络 VPC 中的资源和 TDMQ Pulsar 版开通互访，以保证您部署的生产者/消费者客户端能正常和 TDMQ Pulsar 版通信。

> ?当前仅2.6.1版本的集群需要配置接入点，2.7.1及以上版本的集群可以直接从控制台集群管理页面复制接入地址，具体操作请参见 [获取接入地址](https://cloud.tencent.com/document/product/1179/52145#获取接入地址)。

## 前提条件

已在腾讯云上有购买云服务器 CVM 或者容器资源，并配置了私有网络 VPC。

## 操作步骤

1. 登录 [TDMQ Pulsar 版控制台](https://console.cloud.tencent.com/tdmq)，进入**集群管理**页面，选择目标集群。
2. 单击操作列的**接入地址**，进入集群的接入点配置页面。
   ![](https://main.qcloudimg.com/raw/8053b5772d1f4ccbcd89a3a77075c42b.png)
3. 单击**新建**，在新建 VPC 接入点对话框中，选择 VPC、子网，填写备注。
	- VPC：选择您部署生产者或消费者所在的 VPC 网络
	- 子网：根据您的 IP 分配方式选择对应的子网
	- 备注（选填）：填写备注信息，不超过128个字符
4. 单击**提交**，即可完成 VPC 网络的接入。
![](https://qcloudimg.tencent-cloud.cn/raw/ad7bd97f7c160adb03306f6661a2c6a6.png)
5. 配置安全组策略。确保测试程序所在的安全组放行 TCP:6000-7000。

>?您可以在接入点列表中看到已创建的接入点记录，其中有您需要在客户端配置的参数（路由 ID 和地址），详细介绍请参见 [SDK 文档](https://cloud.tencent.com/document/product/1179/48553)。
