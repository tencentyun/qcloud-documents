

## 操作场景
RAK LoRa 环境监测套件接入到物联网开发平台，通过物联网开发平台可以远程查看传感器的温度、湿度、GPS 等数据。本文档主要指导您如何在物联网开发平台控制台，接入 RAK LoRa 环境监测套件。

## 前提条件


为了通过下面的步骤快速理解该业务场景，需要做好以下准备工作：
 -  申请物联网开发平台服务。
 -  RAK LoRa 环境监测套件（RAK7243 网关和 RAK5205 节点）。 
 -  拥有一台物理或虚拟的 Windows 环境， RAK5205 串口驱动安装、串口软件的安装。


## 控制台操作 LoRa 网关

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择上文“RAK 环境监测演示” 中对应的项目。
2. 在左侧工具列表中，选择【网络管理】>【LoRa 网关管理】。
3. 进入 LoRa 网关管理页面，选择【社区网络】>【添加网关】。
4.  在新建网关页面，填写网关基本信息。
 - 网关名称：本示例中填写 RAK7243。
 - GwEUI：网关唯一 ID，可以在网关标签上查看到。此处用填写时字母用小写。
 -  是否公开：选择“是”，表示社区开发者可在社区网络查看该网关，并可通过这个网关进行 LoRa 节点接入；选择“否”，则仅用户自己能查看该网关。
 -  位置信息：在地图上选择网关位置。
 ![](https://main.qcloudimg.com/raw/7509ff70880e22a2f15dbb2138011ee3.png)

网关新建成功后，您可在网关列表页查看“RAK7243”。




## LoRa 网关实物操作

1.	网关联网配置
配置连网方式请参见 [文档](https://doc.rakwireless.com/rak7243--lorawan----developer-gateway/configuring-the-gateway%E9%87%8C%E7%9A%84Connect%20the%20LoRaWAN%E2%84%A2%20Gateway%20to%20a%20Router)。
2. 修改网关目的 server 和端口 sudo gateway-config
 1. 修改选择 server 类型，选择 TTN，频段为 CN470，如下图所示：
 ![](https://main.qcloudimg.com/raw/faa4b4f9d29bfb0dd67be2347356ad71.png)
 ![](https://main.qcloudimg.com/raw/9244f42cb955497adf11e0ca21145939.png)
 ![](https://main.qcloudimg.com/raw/d505a96f22ec203ed847ee923178d73c.png)
 2. 修改 packet-forwarder 配置，如下图所示：
![](https://main.qcloudimg.com/raw/cf2606fe37cbe730405c1b5733ce7285.png)
 3. gateway_conf.server_address 改为 loragw.things.qcloud.com，如下图所示：
![](https://main.qcloudimg.com/raw/7f86c001f8dc9f4970377aabb79cb105.png)
3.	网关上线
重启网关，刷新网关管理界面，即可看到网关已经在线。


## 控制台操作 LoRa 节点


#### 创建项目
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择【新建项目】。
2. 在新建项目页面，填写项目基本信息后，单击【保存】
 - 项目名称：输入“RAK 环境监测演示”或其他名称。
 - 项目描述：按照实际需求填写项目描述。
 ![](https://main.qcloudimg.com/raw/440cc15b137ecba7e11d1031acaf5a31.png)

项目新建成功后，即可新建产品。



#### 新建产品
1. 进入该项目的产品列表页面，单击【新建产品】。
2. 在新建产品页面，填写产品基本信息后，单击【保存】。
 -  产品名称：“RAK5205”或其他产品名称。
 -  产品类型：选择“用户自定义”。
 -  设备类型：选择“设备”。
 -  认证方式：选择“密钥认证”。
 -  通信方式：选择“LoRaWAN”。
![](https://main.qcloudimg.com/raw/08fc89c6999c6a3482df2b0a5393010a.jpg)

产品新建成功后，您可在产品列表页查看“RAK5205”。

#### 创建数据模板
1. 单击产品名称，进入产品配置页，在【自定义功能】配置项下，可以单击【新建功能】，自定义产品功能。
2. 您也可在【标准功能】配置项下，单击右上角【导入 JSON】，导入数据模板。
![](https://main.qcloudimg.com/raw/dd557e776a223b871b7515e004571506.png)
3. 打开 [文件](https://github.com/RAKWireless/RUI_LoRa_node_payload_decoder/blob/master/tencent/RAK5205.json)， 并复制文件里的内容至上图对应的本文框，单击【导入】。
导入成功后，结果如下图：
![](https://main.qcloudimg.com/raw/eafb6e7eaad5a75c8b3f2282035953a5.png)

#### 配置 LoRaWAN 参数

1. 单击【下一步】进入数据开发。
2. 在设备开发页面中，按需调整 LoRaWAN 参数配置。本示例中使用默认的 OTAA 配置。
![](https://main.qcloudimg.com/raw/5142ee11cf323bda6874bdf120151ead.png)

#### 设备数据解析

在设备开发页面中，按需调整设备数据解析。由于 LoRa 类资源有限设备不适合直接传输JSON 格式数据，使用“设备数据解析”可以将设备原始数据转化为产品 JSON 数据。

#### 数据解析脚本
1. 上行数据解析的脚本主函数为 RawToProtocol，其带有 fPort、bytes 两个入参： 
 - fPort：设备上报的 LoRaWAN 协议数据的 FPort 字段。 
 - bytes：设备上报的 LoRaWAN协议数据的 FRMPayload 字段。
脚本主函数的出参为产品数据模版协议格式的对象。
2. 打开 [文件](https://github.com/RAKWireless/RUI_LoRa_node_payload_decoder/blob/master/tencent/RAK5205SensorDataDecoder_for_tencent.js)，复制文件内容至“上行数据解析”文本框，覆盖原有内容，并提交。



#### 脚本模拟测试

您也可使用数据解析页面下方的模拟调试工具，如需开发更多的功能，请使用以下模拟脚本。
-  上行消息设备原始数据为 0x0768580673256D0267011D，我们将其转化为数组，即上行模拟数据为：[7,104,88,6,115,37,109,2,103,1,29]
- 填入设备上行数据的编辑框中。单击【运行】，即可在模拟调试界面右侧查看结果。
![](https://main.qcloudimg.com/raw/6454b9aebaeee6c18bc29d613227baa5.png)

#### 创建测试设备

在设备调试页面中，单击【新建设备】，设备名为 RAK7205_1。
- DevEUI：每一个设备有一个唯一的身份识别地址，DevEUI 为 60c5a8fff****efe，如下图所示：
![](https://main.qcloudimg.com/raw/5825a5253f36d0bbf071f8cc0399d678.png)
- AppKey：设备的密钥。本例中填写 6fbdbb37b8c0dbd82af4e93f****4177，用户可以填写为其他值。
![](https://main.qcloudimg.com/raw/f5d7801a5cf2f9a0c0dbd1e16a39cbab.png)

>!DevEUI 和 AppKey 统一使用小写字母。




## LoRa 节点实物操作

#### 配置设备三元组

1. 设备通过 USB 口连接到 PC，打开 com 工具设置设备三元组并启动 join：
```
at+set_config=lora:dev_eui:60c5a8fffe75fefe
at+set_config=lora:app_eui:800000000000001b
at+set_config=lora:app_key:6fbdbb37b8c0dbd82af4e93f****4177
at+join
```
![](https://main.qcloudimg.com/raw/6a0663aa8a80c7f56d0c6296012f9db0.png)
2. 当您看到“Join Success 字样”，代表设备已经连接成功。

## 查看设备状态

1. 保持 LoRa 节点和 LoRa 网关为运行状态。
2. 进入【控制台】>【产品开发】>【设备调试】，可查看到设备 "RAK****" 。
3. 单击【调试】，可进入设备详情页。
4. 单击【设备属性】，可查询设备上报到开发平台的最新数据及历史数据。
 -  设备属性的最新值：会显示设备上报的最新数据。
 -  设备属性的更新时间：显示数据的更新时间。
![](https://main.qcloudimg.com/raw/e9d16bae3ca31884eefc12a01d5dea90.png)


## 在线调试
当 LoRa 节点成功连接至物联网开发平台后，您可在控制台【设备调试】列表，单击【调试】，进入在线调试。
