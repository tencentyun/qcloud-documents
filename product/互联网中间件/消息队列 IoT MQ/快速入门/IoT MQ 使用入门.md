## 1. 查看 IoT MQ 实例
申请通过后，您的 IoT MQ 控制台中会展示 IoT MQ 实例，单击实例ID可以查看实例详情，包括接入点域名、实例规格等信息。
**实例列表：**
![](//mc.qcloudimg.com/static/img/3310b76e89e114f95fb7f7b8e995a725/image.png)
**实例详情：**
![](//mc.qcloudimg.com/static/img/456d1ea5a5cecc0342e85e54b6559a97/image.png)
## 2. 管理 Topic
在 Topic 管理页面，您可以创建 Topic，指定 Topic 的名称、消息生命周期和消息最大长度。
> 注：当前 Topic 名称输入后无法更改。

**新建 Topic：**
![](//mc.qcloudimg.com/static/img/b37d487a4321bbbdba63cced50bf49db/image.png)
**Topic 列表：**
![](//mc.qcloudimg.com/static/img/835fdabfc1056a777d26184e2d5aded4/image.png)
## 3. 生产消费
创建好 Topic 后，您可以通过 MQTT 客户端对发布订阅 Topic，进而进行生产和消费。

消息队列 IoT MQ 提供的 MQTT 服务严格遵循 MQTT3.1.1 协议，理论上能够适配所有 MQTT 客户端，但不排除客户端可能出现兼容性的问题。针对常用的用户场景，推荐的第三方包如下：

|使用平台|第三方SDK|链接|
|-----|-----|-----|
|Java	|Eclipse Paho Java Client |http://www.eclipse.org/paho/clients/java/ |
|Android|Eclipse Paho Android Service|http://www.eclipse.org/paho/clients/android/|
|JavaScript|Eclipse Paho JavaScript Client|http://www.eclipse.org/paho/clients/js/|
|Python|Eclipse Paho Python Client|http://www.eclipse.org/paho/clients/python/|
|GoLang|Eclipse Paho Go Client|http://www.eclipse.org/paho/clients/golang/|
|C++|MQTT C++ Client for Posix and Windows|http://www.eclipse.org/paho/clients/cpp/|
|.Net(C#)|C# .Net and WinRT Client|http://www.eclipse.org/paho/clients/dotnet/|

> 注：
> - 第三方 SDK 均可从 http://www.eclipse.org/paho/downloads.php 进行下载。
> - 使用客户端连接 IoT MQ 服务器时，须发送 CONNECT 报文，且在 Connect 报文中需上传 username 和 password，其中 username 和 password 的计算详情参见[客户端签名计算](https://cloud.tencent.com/document/product/646/12661)。
