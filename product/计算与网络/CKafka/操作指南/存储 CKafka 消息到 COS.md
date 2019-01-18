消息服务 CKafka 支持用户存储消息日志的能力，您可以将日志存储到 COS 中，并下载分析。

## 开启日志功能
在 **topic 管理** 页面，开启日志访问功能。

针对不同的 topic，选取相应的 COS 中 bucket，则请求日志会自动在 bucket 下创建 instance id+topic id 为名称的文件夹进行存储。选取完成后，单击 bucket 地址可以直接跳转到日志下载页面。

此外，可以根据消息量的大小，选取汇聚消息日志的时间间隔，时间间隔为 5~60 分钟不等。

如您没有创建对象存储的 bucket，请在 [新建 bucket](https://console.cloud.tencent.com/cos/bucket) 后选取相应的存储位置。


![Alt text](https://main.qcloudimg.com/raw/61fe42efc86a1260db2235fea9c56c52.jpg)

## 产品限制和费用计算
- 当前日志聚合粒度为 5~60 分钟不等，允许用户指定。
- 日志数据的传输会有一定的延迟。
- 当前仅支持和 CKafka 实例同个地域的 cos 进行消息存储，为保证延时，不支持跨地域存储。
- object 权限用 COS 默认的私有读写权限。
- 转储服务会占用一个 group id。
- 文件名为存放的 timestamp，存放路径为 `instance id/topic id`。
- 文件内容是 CKafka 消息里的 value 用 string 序列化拼接而成。
- 当前 CKafka 日志服务`免费`，COS 存储可享受一定 [免费额度](https://cloud.tencent.com/document/product/436/6240)，提供 50G 免费存储空间。如您的日志量级较大，请及时清理数据。
- 开启转 COS 的操作人必须对目标 cos bucket 具备写权限；
- 开启转发前，积压 Ckafka 消息不会被转存到 COS；
- 实例到期后转发 COS 也会中断，实例续费后会自动恢复转发。
