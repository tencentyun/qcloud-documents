消息服务CKafka支持用户存储消息日志的能力，您可以将日志存储到COS中，并下载分析。

### 开启日志功能
在**topic管理**页面，开启日志访问功能。

针对不同的topic，选取相应的COS中bucket，则请求日志会自动在bucket下创建instance id+topic id为名称的文件夹进行存储。选取完成后，点击bucket地址可以直接跳转到日志下载页面。

此外，可以根据消息量的大小，选取汇聚消息日志的时间间隔，时间间隔从5分钟-60分钟不等。

如您没有创建对象存储的bucket，请在[新建bucket](https://console.qcloud.com/cos4/bucket)后选取相应的存储位置。


![Alt text](https://main.qcloudimg.com/raw/61fe42efc86a1260db2235fea9c56c52.jpg)

### 产品限制和费用计算
- 当前日志聚合粒度为5-60分钟不等，允许用户指定。
- 日志数据的传输会有一定的延迟。
- 当前仅支持和ckafka实例同个地域的cos进行消息存储，为保证延时，不支持跨地域存储。
- object权限用cos默认的私有读写权限
- 转储服务会占用一个group id
- 文件名为存放的timestamp，存放路径为instance id/topic id
- 文件内容是ckafka消息里的value用string序列化拼接而成

- 当前CKafka日志服务`免费`，COS存储的免费额度按照[文档](https://www.qcloud.com/document/product/436/6240)中所示，提供50G免费存储空间。如您的日志量级较大，请及时清理数据。
