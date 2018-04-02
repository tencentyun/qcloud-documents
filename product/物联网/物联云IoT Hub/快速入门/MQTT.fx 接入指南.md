MQTT.fx 是目前主流的 MQTT 桌面客户端，它支持 Windows, Mac, Linux，可以快速验证是否可以与 IoT Cloud 进行连接并发布或订阅消息，下面将通过图文并茂的形式演示 MQTT.fx 如何与腾讯云 IoT Cloud 交互。

### 连接 IoT Cloud
1. 打开 [MQTT.fx 下载页面](http://mqttfx.jensd.de/index.php/download)，找到适合的版本下载并安装 MQTT.fx 客户端，本文以 MQTT.fx 1.6.0 for Mac 版本为例。
2. 打开 MQTT.fx 客户端程序，点击设置按钮打开设置页面，并点击"+"按钮，创建一个新的配置文件。
![](https://main.qcloudimg.com/raw/750ed4e58c735046a5b312edbcbb72b3.png)
3. 填写 Connection Profile 相关信息和 General 信息。
![](https://main.qcloudimg.com/raw/f8763fcc05f10bf59ab46b5679356b4e.png)
<table>
<tr>
  <th>参数</th>
  <th>说明</th>
</tr>
<tr>
  <td>Profile Name</td>
  <td>配置文件保存为的名称</td>
</tr>
<tr>
  <td>Broker Address</td>
  <td>MQTT 服务器连接地址，广州域设备填入：iotcloud-mqtt.gz.tencentdevices.com</td>
</tr>
<tr>
  <td>Broker Port</td>
  <td>MQTT 服务器连接端口，填入：8883</td>
</tr>
<tr>
  <td>Client ID</td>
  <td>MQTT协议字段，按照物联网通信约束填入：产品ID+设备名，如："CJ3ND2P5LHshockDevice1", CJ3ND2P5LH是产品ID，shockDevice1是设备名</td>
</tr>
<tr>
  <td>Connection Timeout</td>
  <td>连接超时时间 秒</td>
</tr>
<tr>
  <td>Keep Alive Interval</td>
  <td>心跳间隔时间 秒</td>
</tr>
<tr>
  <td>Auto Reconnect</td>
  <td>断网自动重连</td>
</tr>
</table>
4. 填写 User Credentials 信息。
![](https://main.qcloudimg.com/raw/1e8aa1ecb766f22fcc9aa8a9071a3ef1.png)
<table>
<tr>
	<th>参数</th>
	<th>说明</th>
</tr>
<tr>
	<td>User Name</td>
	<td>MQTT 协议字段，按照物联网通信约束填入：产品ID+设备名+sdkappid+connid，如："CJ3ND2P5LHshockDevice1;12010126;12345"，仅替换示例中的产品ID+设备名即可，后面的两个参数本身由物联网通信接入sdk自动生成，所以这里填写固定测试值</td>
</tr>
</table>
5. 选择开启 SSL/TLS，勾选 Self signed Certificates，上传相关内容。
由于 IoT Cloud 使用安全加密链路，因此还需要设置 SSL/TLS 信息。MQTT.fx 不支持对称加密 PSK，本文仅演示非对称加密连接设置。
![](https://main.qcloudimg.com/raw/4b0f30845e545660668e58dcdac0d063.png)
<table>
<tr>
	<th>文件</th>
	<th>说明</th>
</tr>
<tr>
	<td>ca.crt</td>
	<td>根证书，点击 <a href="https://main.qcloudimg.com/raw/14108437225f297154d63163ddd3d0da.crt">ca.crt</a> 链接下载文件</td>
</tr>
<tr>
	<td>Client Certificate File</td>
	<td>客户端证书，即设备证书，在非对称加密产品中创建设备时下载，详情请查看 <a href="https://cloud.tencent.com/document/product/634/14442">设备接入准备</a></td>
</tr>
<tr>
	<td>Client Key File</td>
	<td>客户端密钥文件，即设备密钥，在非对称加密产品中创建设备时下载，详情请查看  <a href="https://cloud.tencent.com/document/product/634/14442">设备接入准备</a></td>
</tr>
<tr>
	<td>PEM Formatted</td>
	<td>由于物联网通信根证书、设备证书、设备密钥均由openssl生成使用PEM格式，而 MQTT.fx是Java客户端，所以不识别PEM证书，这里需要勾选由该客户端自动转换为Java识别的JKS格式</td>
</tr>
</table>
6. 完成以上步骤设置后，点击【Apply】和【OK】进行保存，并在配置文件框中选择刚才创建的文件名，点击【Connect】按钮。当右上角圆形图标为绿色时，说明已连接 IoT Cloud 成功，可进行发布和订阅操作。
![](https://main.qcloudimg.com/raw/f3b340fecae5426b1d26d51e729b0aae.png)

### 发布消息
选择客户端 Publish Tab，输入主题名称、Qos 等级，点击【Publish】按钮进行发布。发布结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/d73633d60416697590ed779a214dedf0.png)

### 订阅主题
选择客户端 Subscribe Tab，输入主题名称、Qos 等级，点击【Subscribe】按钮进行主题订阅，订阅结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/e156e41828a3e34b147cc861dc26bbf3.png)
