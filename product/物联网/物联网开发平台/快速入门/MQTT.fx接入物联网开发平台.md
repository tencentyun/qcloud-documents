

## 操作场景

MQTT.fx 是目前主流的 MQTT 桌面客户端，它支持 Windows、 Mac、Linux 操作系统，可以快速验证是否可与 IoT Cloud 进行连接，并发布或订阅消息。更多 MQTT 协议介绍请参见 [MQTT 协议介绍](https://mcxiaoke.gitbooks.io/mqtt-cn/content/mqtt/01-Introduction.html)。本文档主要介绍 MQTT.fx 如何与腾讯云 IoT Cloud 交互。本文以 MQTT.fx 1.7.1 for Windows 版本为例。

## 操作步骤

### 连接 IoT Cloud

1. 打开 [MQTT.fx 下载页面](http://mqttfx.jensd.de/index.php/download)，找到适合的版本，下载并安装 MQTT.fx 客户端。
2. 打开 MQTT.fx 客户端程序，单击【设置】。
3. 进入设置页面，并单击【+】，创建一个新的配置文件，输入自定义名称 Profile Name，Profile Type 选择 MQTT Broker。
![](https://main.qcloudimg.com/raw/c5703c6f5b1beb28ab237074e232f591.png)
4. 填写【MQTT Broker Profile Settings】和【General】相关信息。
![](https://main.qcloudimg.com/raw/af3139845e86f79eb45f0af537664c60.png)

#### 参数说明

<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>Profile Name</td>
<td>用户自定义名称</td>
</tr>
<tr>
<td>Broker Address</td>
<td>MQTT 服务器连接地址，广州域设备填入：PRODUCT_ID.iotcloud.tencentdevices.com，这里 PRODUCT_ID 为变量参数，用户需填入创建产品时自动生成的产品 ID，<br>例如 T****DS8G.iotcloud.tencentdevices.com</td>
</tr>
<tr>
<td>Broker Port</td>
<td>MQTT 服务器连接端口，填入：1883。本文主要针对密钥认证类型的产品，端口必须是1883，如果您想通过8883接口接入，建议使用证书认证型产品自行接入。</td>
</tr>
<tr>
<td>Client ID</td>
<td>MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名，如："TXXXXDS8Gdev001 "，TXXXXDS8G 是产品 ID，dev001 是设备名称。</td>
</tr>
<tr>
<td>Connection Timeout</td>
<td>连接超时时间（秒）。</td>
</tr>
<tr>
<td>Keep Alive Interval</td>
<td>心跳间隔时间（秒）。</td>
</tr>
<tr>
<td>Auto Reconnect</td>
<td>断网自动重连。</td>
</tr>
</tbody></table>

5. 单击【User Credentials】，填写 User Name 和 Password。
 - **User Name**	：MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名 + SDKAppID + connid+expiry。创建完产品即可在产品列表页和产品详情页查看 ProductID，如："TO****DS8Gdev001;12010126;E4F3Q;1591948593"，仅替换示例中的产品 ID + 设备名即可，后面的三个参数本身由物联网通信接入 SDK 自动生成，也可由腾讯云物联网平台提供的 [生成小工具](https://iot-exp-individual-1258344699.cos.ap-guangzhou.myqcloud.com/password%E7%94%9F%E6%88%90%E5%B7%A5%E5%85%B7.zip) 自动生成。
 - **Password**	：Password 必须填写，用户可以使用物联网平台提供的 [生成小工具](https://iot-exp-individual-1258344699.cos.ap-guangzhou.myqcloud.com/password%E7%94%9F%E6%88%90%E5%B7%A5%E5%85%B7.zip) 自动生成Password，也可以按照文档 [手动生成Password](https://cloud.tencent.com/document/product/634/32546)。
 ![](https://main.qcloudimg.com/raw/555608dcb2b2adb66db3a598f8459cf6.png)
6. 完成以上步骤设置后，单击【Apply】和【OK】进行保存，并在配置文件框中选择刚才创建的文件名，单击【Connect】。
7. 当右上角圆形图标为绿色时，说明已连接 IoT Cloud 成功，即可进行发布和订阅等操作。
   ![](https://main.qcloudimg.com/raw/3490e194d3162adc32ecb77f1bcc46ce.png)

### 发布消息（Publish Topic）

选择客户端 Publish Tab，输入主题名称、Qos 等级，单击【Publish】进行发布。
示例`Topic：$thing/up/property/ProductID/DeviceName`（设备上报数据到云端）。
![](https://main.qcloudimg.com/raw/e685966a5527beaed5319572dd974e4a.png)
发布结果可通过控制台中对应产品的设备日志查询。
![](https://main.qcloudimg.com/raw/67f49c19bb15ea7b1aefe3536a69d8f1.png)


### 订阅主题（Subscribe Topic）

选择客户端 Subscribe Tab，输入主题名称、Qos 等级，单击【Subscribe】进行主题订阅，订阅结果可通过控制台-设备日志查询。
示例`Topic：$thing/down/property/ProductID/DeviceName`（云端下发设备数据）。
![](https://main.qcloudimg.com/raw/886c62d0d7c8a381f08671ad9156e783.png)
在产品设备控制台-在线调试，编辑云端下发设备数据：
![](https://main.qcloudimg.com/raw/f2b2d1d1d0d7b24c707c0a4c27783957.png)
之后回到 MQTT 窗口，可以看到云端刚才下发的设备数据：
![](https://main.qcloudimg.com/raw/3f38798d8ebddffb15e1d7109788e39d.png)

### 查看日志（View logs）

在 MQTT.fx 上，单击 Log 查看操作日志和错误提示日志。
![](https://main.qcloudimg.com/raw/7cd0c3377d069058ff14faf47114e689.png)
