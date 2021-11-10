## 操作场景

MQTT.fx 是目前主流的 MQTT 桌面客户端，它支持 Windows、 Mac、Linux 操作系统，可以快速验证是否可与 IoT Cloud 进行连接，并发布或订阅消息。更多 MQTT 协议介绍请参见 [MQTT 协议介绍](https://mcxiaoke.gitbooks.io/mqtt-cn/content/mqtt/01-Introduction.html)。本文档主要介绍 MQTT.fx 如何与腾讯云 IoT Cloud 交互。本文以 MQTT.fx 1.7.0 for Mac 版本为例。

## 操作步骤

### 连接 IoT Cloud

1. 打开 [MQTT.fx 下载页面](http://mqttfx.jensd.de/index.php/download)，找到适合的版本，下载并安装 MQTT.fx 客户端。
2. 打开 MQTT.fx 客户端程序，单击**设置**。
3. 进入设置页面，并单击 “+”，创建一个新的配置文件。
   ![](https://main.qcloudimg.com/raw/245072a611287b1ec54c5f81780e0a57.png)
4. 填写 Connection Profile 相关信息和 General 信息。
   ![](https://main.qcloudimg.com/raw/b6c0fbb65bac4a922ed0541576bd461e.png)

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
<td>配置文件保存为的名称。</td>
</tr>
<tr>
<td>Broker Address</td>
<td>MQTT 服务器连接地址，详情参考 <a href="https://cloud.tencent.com/document/product/634/61228">设备接入地域说明</a>，域名中 PRODUCT_ID 为变量参数，用户需填入创建产品时自动生成的产品 ID，例如 9****ZW2EZ.iotcloud.tencentdevices.com</td>
</tr>
<tr>
<td>Broker Port</td>
<td>MQTT 服务器连接端口，证书认证型端口：8883；密钥认证型：1883</td>
</tr>
<tr>
<td>Client ID</td>
<td>MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名，例如："9****ZW2EZgate_dev01 "，9****ZW2EZ 是产品 ID，gate_dev01 是设备名。</td>
</tr>
<tr>
<td>Connection Timeout</td>
<td>连接超时时间秒。</td>
</tr>
<tr>
<td>Keep Alive Interval</td>
<td>心跳间隔时间秒。</td>
</tr>
<tr>
<td>Auto Reconnect</td>
<td>断网自动重连。</td>
</tr>
</tbody></table>

5. 填写 User Credentials 信息。
	- **User Name**	：MQTT 协议字段，按照物联网通信约束填入：产品 ID + 设备名 + SDKAppID + connid。（创建完产品即可在产品列表页和产品详情页查看 ProductID）如："9****ZW2EZgate_dev01;12010126;12345"，仅替换示例中的产品 ID + 设备名即可，后面的两个参数本身由物联网通信接入 SDK 自动生成，所以这里填写固定测试值。
	- **Password**	：Password 必须填写。
		- **证书认证：**由于 mqtt.fx 默认将密码标志位设为 true，所以需要填写一个任意的非空字符串作为密码，否则无法连接到物联云通信后台。而实际接入物联云后台时，鉴权是根据证书认证，此处随机填写的密码不会作为接入凭证。
		- **密钥认证：**用户可进入 Hub 相应设备列表查看获取（具体页面见下方密钥认证步骤），也可以按照文档 [手动生成 Password](https://cloud.tencent.com/document/product/634/32546)。
![](https://main.qcloudimg.com/raw/61195a191b05704ea560e2477578e2a5.png)
6. （可选）证书认证： 选择开启 SSL/TLS，勾选 Self signed Certificates，上传相关内容。
![](https://main.qcloudimg.com/raw/ec4b93f69598d1c625abc5b42573ee0e.png)

#### 文件说明

<table>
<thead>
<tr>
<th>文件</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>CA File</td>
<td>根证书，单击 <a href="https://main.qcloudimg.com/raw/9aa774ea8c09f98811df361c741df38c/ca.crt" target="_blank">ca.crt</a> 链接下载文件。</td>
</tr>
<tr>
<td>Client Certificate File</td>
<td>客户端证书文件，即设备证书，在证书认证产品中创建设备时下载，详情请查看 <a href="https://cloud.tencent.com/document/product/634/14442" target="_blank">设备接入准备</a>。</td>
</tr>
<tr>
<td>Client Key File</td>
<td>客户端密钥文件，即设备密钥，在证书认证产品中创建设备时下载，详情请查看 <a href="https://cloud.tencent.com/document/product/634/14442" target="_blank">设备接入准备</a>。</td>
</tr>
<tr>
<td>PEM Formatted</td>
<td>由于物联网通信根证书、设备证书、设备密钥均由 openssl 生成使用 PEM 格式，而 MQTT.fx 是 Java 客户端，所以不识别 PEM 证书，这里需要勾选由该客户端自动转换为 Java 识别的 JKS 格式。</td>
</tr>
</tbody></table>

7. （可选）密钥认证：
   ![](https://main.qcloudimg.com/raw/555608dcb2b2adb66db3a598f8459cf6.png)
    用户可进入控制台获取对应设备的 username，password：
    ![](https://main.qcloudimg.com/raw/7df00ff30cca63898ea784158903b60b.png)
8. 完成以上步骤设置后，单击**Apply** > **OK**进行保存，并在配置文件框中选择刚才创建的文件名，单击**Connect**。
9. 当右上角圆形图标为绿色时，说明已连接 IoT Cloud 成功，可进行发布和订阅操作。
   ![](https://main.qcloudimg.com/raw/d9bba6a0731a3fda4f80b395233c677c.png)



### 发布消息

选择客户端 Publish Tab，输入主题名称、Qos 等级，单击**Publish**进行发布。发布结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/3c2ae1e8b4290c6015ce36235f78840b.png)

### 订阅主题

选择客户端 Subscribe Tab，输入主题名称、Qos 等级，单击**Subscribe**进行主题订阅，订阅结果可通过 [云日志](https://cloud.tencent.com/document/product/634/14445) 查询。
![](https://main.qcloudimg.com/raw/05dd43e7f9d93195809e440cbfe67117.png)
