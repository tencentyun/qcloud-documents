## 简介

您可以将日志主题的数据投递到腾讯云 Ckafka，然后用于您的实时流计算、或者入库等场景。如果您没有购买腾讯云 Ckafka 实例，可以考虑使用日志服务（Cloud Log Service，CLS）自带的 [Kafka 协议消费功能](https://cloud.tencent.com/document/product/614/72651)。

## 前提条件

- 已开通腾讯云消息队列 （CKafka）。
- 确保当前操作账号拥有开通投递到 Ckafka 的权限。如果您是子账号，一般需要主账号进行相关授权，方可使用。权限问题请参见 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374#.E6.8A.95.E9.80.92-ckafka)。


## 操作步骤

1. 在日志主题同地域下，创建一个 Ckafka 实例。详情请参见 [创建实例](https://cloud.tencent.com/document/product/597/53207)。
2. 在日志主题同地域下，根据如下配置参数，创建一个 Topic。详情请参见 [创建 Topic](https://cloud.tencent.com/document/product/597/73566)。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c24a1817ae66fa2c1ec6452e9974e4df.png" style="width: 70%"/></br>
 - **预设ACL策略**：关闭预设 ACL 策略。
 - **展示高级配置**：
    - **CleanUp.policy**：选择 **delete**。该参数需设置为 delete，否则会投递失败。
    - **max.message.bytes**：设置为 ≥ 8MB。该参数若小于8MB，会因 CLS 侧的单条 message 过大，无法写入 Ckafka Topic，导致投递失败。
3. 前往  [日志服务控制台](https://console.cloud.tencent.com/cls)，并按需选择不同的操作，进入投递任务管理页面或者日志主题管理页面。
 - 在左侧导航栏中，单击**投递任务管理**，选择地域、日志集和日志主题。
![](https://qcloudimg.tencent-cloud.cn/raw/af951b8be46b525535751f70833262cd.png)
 - 在左侧导航栏中，单击**日志主题**，选择需要配置投递到 Ckafka 任务的日志主题，进入日志主题管理页面。
![](https://qcloudimg.tencent-cloud.cn/raw/08197c686ce947205ae4d6dffa627c3b.png)
4. 单击**投递到Ckafka** 页签，进入投递到 Ckafka 配置页面。
5. 单击右侧的**编辑**，开启投递到 Ckafka 开关，选择相应的 Ckafka 实例以及对应的 Topic，选择需要投递的日志字段。
<img src="https://qcloudimg.tencent-cloud.cn/raw/50a6b0f38b5d94e0470146fbf695b519.png" style="width: 80%"/>
6. 单击**确定**，启动投递到 Ckafka，任务状态显示为“已开启”则表示开启成功。
>! 如需在投递至 Ckafka 前对日志进行清洗加工过滤，可参考使用 [数据加工](https://cloud.tencent.com/document/product/614/71487) 操作。
>

## 常见问题

#### 日志数据无法投递 Ckafka，怎么办？

如果您在腾讯云 Ckafka 开启了 ACL 鉴权，会导致日志数据无法投递。请关闭该 Topic 的 ACL。

#### 提示没有读写 Ckafka Topic 的权限，怎么办？

如果您直接使用 API 接口投递数据到 Ckafka，可能会存在读写 Ckafka Topic 的权限问题。因为，如果您在控制台使用该功能，系统会引导您完成相关授权，如果您直接调用 API 投递，则需要手动授权。具体的排查和解决方案请参见 [投递权限查看及配置](https://cloud.tencent.com/document/product/614/71623)。

