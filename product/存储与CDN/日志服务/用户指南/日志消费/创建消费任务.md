
## 简介
日志服务可以通过 Ckafka 实例来消费日志主题的数据，下面将为您详细介绍如何开启日志主题 Ckafka 消费功能。

## 前提条件

已开通腾讯云消息队列 （CKafka），并在日志主题同地域下创建 Ckafka 消费实例和消息队列 topic。

>?Ckafka 实例的创建操作，请参阅 [创建 Ckafka 实例](https://cloud.tencent.com/document/product/597/30931) ，Ckafka 的使用方法，请参阅 [Ckafka 使用入门](https://cloud.tencent.com/document/product/597/10112)。

## 操作步骤

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls) 。
2. 在左侧导航栏中，单击【日志集管理】。
3. 单击需要配置 Ckafka 消费的日志集 ID/名称，进入日志集详情页。
4. 找到需要消费的日志主题，在其右侧单击【管理配置】>【实时消费】，进入 Ckafka 消费配置页面。
![1](https://main.qcloudimg.com/raw/85294af3a9d71265e5cc535b17a58057.png)
5. 在页面右侧，单击【编辑】，进入 Ckafka 消费配置页。
6. 开启 Ckafka 消费开关，选择消费的 Ckafka 实例以及对应的消息列队 topic。
![2](https://main.qcloudimg.com/raw/ebfac8224553db1011d0d14a3a812cb3.png)
7. 单击【保存】，启动 Ckafka 消费，Ckafka 消费状态显示为“已开启”则表示开启成功。
![](https://main.qcloudimg.com/raw/1ac6ee333d54e068451a68fbcf71af18.png)


