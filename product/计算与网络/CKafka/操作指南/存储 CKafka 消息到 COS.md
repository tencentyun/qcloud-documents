消息队列 CKafka 支持用户存储消息的能力，您可以将消息存储到 COS 中，并下载分析。

前提条件
该功能目前处于灰度测试阶段，如需试用请通过 提交工单 的方式开通白名单。

## 开启存储消息到 COS
1. 登录 [消息队列 CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表页，单击目标实例 ID，进入**topic 管理**标签页。
3. 在 topic 管理标签页，单击操作列的【存储消息到 COS】。
4. 单击启用图标，开启开启存储消息到 COS 功能。
![](https://main.qcloudimg.com/raw/3337eafafaf6805fa0523bc51012f67c.png)
 - 时间粒度：根据消息量的大小，选取汇聚消息的时间间隔，时间间隔为5 - 60分钟不等。
 - 存放 Bucket：针对不同的 topic，选取相应的 COS 中 Bucket，则请求消息会自动在 Bucket 下创建 instance id + topic id 为名称的文件夹进行存储。选取完成后，单击 Bucket 地址可以直接跳转到文件下载页面。

如果您还未创建对象存储的 Bucket，请在 [新建 Bucket](https://console.cloud.tencent.com/cos/bucket) 后选取相应的存储位置。

## 产品限制和费用计算
- 该功能适用于少量数据备份到 COS 的场景，不保证数据能100%成功同步到 COS 中。
- 当前 COS 文件聚合粒度为5 - 60分钟不等，允许用户指定。
- 数据的传输会有一定的延迟。
- 当前仅支持和 CKafka 实例同个地域的 COS 进行消息存储，为保证延时，不支持跨地域存储。
- object 权限用 COS 默认的私有读写权限。
- 转储服务会占用一个 group id。
- 文件名为存放的 timestamp，存放路径为 `instance id/topic id`。
- 文件内容是 CKafka 消息里的 value 用 String 序列化拼接而成。
- 当前 CKafka 消息到COS服务`免费`，COS 存储可享受一定 [免费额度](https://cloud.tencent.com/document/product/436/6240)，提供50G免费存储空间。如您的消息量级较大，请及时清理数据。
- 开启转 COS 的操作人必须对目标 COS Bucket 具备写权限。
- 开启转发前，积压 Ckafka 消息不会被转存到 COS。
- 实例到期后转发 COS 也会中断，实例续费后会自动恢复转发。
