
## 操作场景
MQTT.fx 是目前主流的 MQTT 桌面客户端，它支持 Windows, Mac, Linux，可以快速验证是否可以与 IoT Cloud 进行连接并发布或订阅消息，本文主要介绍 MQTT.fx 如何与腾讯云 IoT Cloud 交互。本文以 MQTT.fx 1.7.0 for Mac 版本为例。

## 操作步骤
### 连接 IoT Cloud
1. 打开 [MQTT.fx 下载页面](http://mqttfx.jensd.de/index.php/download)，找到适合的版本下载并安装 MQTT.fx 客户端。
2. 打开 MQTT.fx 客户端程序，单击【设置】。
3. 进入设置页面，并单击【+】，创建一个新的配置文件。
![](https://main.qcloudimg.com/raw/245072a611287b1ec54c5f81780e0a57.png)
4. 填写 Connection Profile 相关信息和 General 信息。
![](https://main.qcloudimg.com/raw/e777e866ff82f9e50cc9ba9733060c65.png)
5. 填写 User Credentials 信息。
![](https://main.qcloudimg.com/raw/400b9f9629e3ad50c2b7707b6d3771fd.png)
 >?
 - **User Name**	：MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名 + SDKAppID + connid。如："9B17RZW2EZgate_dev01;12010126;12345"，仅替换示例中的产品 ID + 设备名即可，后面的两个参数本身由物联网通信接入 SDK 自动生成，所以这里填写固定测试值。
 - **Password**	：Password 必须填写，由于 mqtt.fx 默认将密码标志位设为 true，所以需要填写一个任意的非空字符串作为密码，否则无法连接到物联云通信后台。而实际接入物联云后台时，鉴权是根据证书认证，此处随机填写的密码不会作为接入凭证。
6. 选择开启 SSL/TLS，勾选 Self signed Certificates，上传相关内容。
![](https://main.qcloudimg.com/raw/e6075ae11c33a87d59e2db819800f164.png)
 >!由于 IoT Cloud 使用安全加密链路，因此还需要设置 SSL/TLS 信息。MQTT.fx 不支持对称加密 PSK，本文仅演示非对称加密连接设置。
7. 完成以上步骤设置后，单击【Apply】和【OK】进行保存，并在配置文件框中选择刚才创建的文件名，单击【Connect】。
8. 当右上角圆形图标为绿色时，说明已连接 IoT Cloud 成功，可进行发布和订阅操作。
 ![](https://main.qcloudimg.com/raw/01637e6108ec7adff7030c483308fdf6.png)

### 参数说明
上文涉及到的相关参数及文件说明，请参考下表：

| 参数                  | 说明                                       |
| ------------------- | ---------------------------------------- |
| Profile Name        | 配置文件保存为的名称。                               |
| Broker Address      | MQTT 服务器连接地址，广州域设备填入：PRODUCT_ID.iotcloud.tencentdevices.com |
| Broker Port         | MQTT 服务器连接端口，填入：8883。                     |
| Client ID           | MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名，如："9B17RZW2EZgate_dev01 "，9B17RZW2EZ 是产品 ID，gate_dev01 是设备名。 |
| Connection Timeout  | 连接超时时间秒。                                 |
| Keep Alive Interval | 心跳间隔时间秒。                                 |
| Auto Reconnect      | 断网自动重连。                                   |

| 文件                      | 说明                                       |
| ----------------------- | ---------------------------------------- |
| ca.crt                  | 根证书，单击 [ca.crt](https://main.qcloudimg.com/raw/9aa774ea8c09f98811df361c741df38c/ca.crt) 链接下载文件。 |
| Client Certificate File | 客户端证书文件，即设备证书，在证书认证产品中创建设备时下载，详情请查看 [设备接入准备](https://cloud.tencent.com/document/product/634/14442)。 |
| Client Key File         | 客户端密钥文件，即设备密钥，在证书认证产品中创建设备时下载，详情请查看 [设备接入准备](https://cloud.tencent.com/document/product/634/14442)。 |
| PEM Formatted           | 由于物联网通信根证书、设备证书、设备密钥均由 openssl 生成使用 PEM 格式，而 MQTT.fx 是 Java 客户端，所以不识别 PEM 证书，这里需要勾选由该客户端自动转换为 Java 识别的 JKS 格式。 |



### 发布消息
选择客户端 Publish Tab，输入主题名称、Qos 等级，单击【Publish】进行发布。发布结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/80dddbe2538f8e80e075ef57a2f923fe.png)

### 订阅主题
选择客户端 Subscribe Tab，输入主题名称、Qos 等级，单击【Subscribe】进行主题订阅，订阅结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/a3cc01c87f70a8b6f910f4544344b2ae.png)
