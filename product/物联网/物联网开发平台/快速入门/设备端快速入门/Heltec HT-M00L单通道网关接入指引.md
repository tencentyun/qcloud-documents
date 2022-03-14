## 操作场景

HT-M00L 是 [Heltec Automation](https://heltec.org/) 与“腾讯连连”小程序联名推出的一款低成本的单通道网关。能实现 SF7 - SF12 的全速率监听，支持 LoRaWAN 协议，大幅的降低 LoRa 网关的成本。主要面向智能家居、通信方案评估等应用场景，本文档将实现以下操作：
- [配置 HT-M00L 单通道网关](#test5)，使其连接到腾讯云平台。
- [配置 LoRa 节点](#test6)，与 HT-M00L 网关通过 LoRaWAN 协议进行通信。
- 在腾讯云平台上完成 [数据调试](#test7)。
- 将节点发送的 [数据显示](#test8) 到“腾讯连连”小程序中。
- 配置 LoRaWAN 用户 [自定义频点](#test9)。



## 前提条件

为了通过下面的步骤快速理解该业务场景，需要做好以下准备工作：
- 拥有一台 HT-M00L 单通道网关。
- 拥有支持任意 LoRaWAN 协议并可以修改前导码长度的节点，本例采用 [CubeCell HTCC-AB01](https://heltec.org/project/htcc-ab01/) 节点。

>?节点的前导码长度需修改为16。如果前导码长度为8，则需将最小 SF 与最大 SF 设为相等，否则将只能收到最小 SF。例如节点前导码长度为8，网关设置最小 SF 为7，最大 SF 为12，那么将只能收到 SF7。



[](id:test5)
## 控制台创建设备

[](id:test2)
### 创建 HT-M00L 网关

1. 登录物联网开发平台控制台 [创建项目](https://cloud.tencent.com/document/product/1081/40290#.E6.96.B0.E5.BB.BA.E9.A1.B9.E7.9B.AE)。
2. 进入已创建的项目，单击左侧导航栏【网络管理】>【LoRa 网关管理】，进入 LoRa 网关管理页面。
3. 单击【用户网关】>【添加网关】并填写网关相关信息。
![](https://main.qcloudimg.com/raw/f5e1e1cfecc97a59a9815649944a51ec.jpg)
	- 网关名称：根据项目需要填写，本示例中填写 HT_M00L。
	- GwEUI：即网关 ID，可以在 [网关配置页](#test1) 上查看。
	- 是否公开：选择“是”，表示社区开发者可在社区网络查看该网关，并可通过这个网关进行 LoRa 节点接入；选择“否”，则仅用户自己能查看该网关。
	- 频点信息：根据具体需求选择。
	- 位置信息：在地图上选择网关位置。
4. 单击【确定添加】即可完成网关创建。

### 创建节点

1. 登录物联网开发平台控制台 [创建产品](https://cloud.tencent.com/document/product/1081/34739#.E5.88.9B.E5.BB.BA.E4.BA.A7.E5.93.81)。
2. 根据实际情况填写“产品名称”。通信方式选择“LoRaWAN”，其他保持默认即可。
<img src="https://main.qcloudimg.com/raw/7f03ca4faf5c6ddd0cf5639a1f1b041b.jpg" style="  width: 75%;
">
3. 选择已创建的产品进入，单击【数据模板】>【新建功能】创建本文需要的"温度"，"湿度"，"电池电压"三个功能，功能中的"数据类型"应与解析出的数据类型相匹配。详情请参见 [数据模板](https://cloud.tencent.com/document/product/1081/44921)。
![](https://main.qcloudimg.com/raw/ccc8811cc9e6d70b78c32cf0216722b7.jpg)
4. 单击【下一步】，进入【设备开发】>【云端解析】页面配置相应数据解析脚本。
![](https://main.qcloudimg.com/raw/fa0d6d729c4cf828ee382cab93607f18.jpg)
5. 单击【设备调试】>【新建设备】创建设备节点。
<img src="https://main.qcloudimg.com/raw/a4dfb742990d865c7d747f2330aa58a5.jpg"  style="  width: 65%;
">
 - 设备名称：支持英文、数字、下划线的组合，最多不超过48个字符。
 - DevEUI：仅支持16进制字符，长度16位。必须与 LoRaWAN 节点相对应。
 - AppKey：仅支持16进制字符，长度32位。必须与 LoRaWAN 节点相对应。
6. 单击【保存】即可完成设备节点创建。


[](id:test6)
## 配置设备（硬件操作）

[](id:test1)
### 配置网关

- **保持"USR"键处于按下状态，单次按下"RST"并松开**，待 RGB 灯变成黄绿色后，松开"USR"键。此时网关将创建一个名为"M00L_****"的 Wi-Fi。
![](https://main.qcloudimg.com/raw/cc54f8a3818aec24201387bb62fc9061.png)
- 将电脑或手机接入此 Wi-Fi，密码为 `heltec.org`，在浏览器中输入"192.168.4.1"，进入网关配置界面。
<img src="https://main.qcloudimg.com/raw/398ba989b253465232ac05f9554feb58.png" style="   width: 75%;
">
  - Wi-Fi 名称：HT-M00L 网关将接入 Wi-Fi 名称进行配置并提交后，即可通过此 Wi-Fi 连接腾讯云。
  - Wi-Fi密码 ：HT-M00L 网关将接入 Wi-Fi 密码。
  - 信道频率（Hz）：该网关 LoRa 将要监听的频率，该频率必须与服务器、节点发射频率相对应。
  - 最小扩频因子（MIN SF：7 - 12）：LoRa通信的最小扩频因子。
  - 最大扩频因子（MAX SF：MIN SF - 12)）：LoRa 通信的最大扩频因子，该值必须大于等于“最小扩频因子”。
  - 网关 ID：网关的唯一序列号，根据硬件 Mac 地址自动产生并已绑定。
  - 服务器地址：已绑定腾讯云。
  - 端口号：HT-M00L 网关与 LoRa 服务器通信的端口，一般默认1700。
  - 时区：网关所在位置的时区。

>?HT-M00L 已绑定腾讯云，服务器地址不可修改。


### 配置节点

节点部分的通信实验在基于 [CubeCell HTCC-AB01](https://heltec.org/project/htcc-ab01/)，外接 HDC1080 温湿度传感器，同时通过开发板上的 ADC 读取电池电压，并将读到的数据通过 LoRaWAN 协议发送到 HT-M00L 网关上。

CubeCell 支持 Arduino 开发环境，首先安装 [CubeCell Arduino开发环境](https://heltec-automation.readthedocs.io/zh_CN/latest/cubecell/quick_start.html)。

#### 修改节点代码

将传感器与主板连接好后，使用 [HDC1080 传感器 + LoRaWAN](https://github.com/HelTecAutomation/ASR650x-Arduino/blob/master/libraries/LoRa/examples/LoRaWAN/LoRaWAN_Sensors/LoRaWan_HDC1080/LoRaWan_HDC1080.ino) 例程。在 Arduino IDE 菜单中，单击【工具】按下图进行配置：
![](https://main.qcloudimg.com/raw/052e7f49c283912d2f3ce1b4742b2243.png)
以下三个地方需要根据实际情况进行修改：
- **Arduino 菜单中，工作频段设置为 CN470。**
![](https://main.qcloudimg.com/raw/3b8c526321cc497e2c763616b1530075.png)
- **DevEUI 和 AppKey，必须与腾讯云上节点的信息一致。**
![](https://main.qcloudimg.com/raw/9b4651678e5e6c6c2f2f4e05171f8ac0.png)
- **因为 HT-M00 是单通道网关，信道掩码必须配置为网关对应的通道。**
![](https://main.qcloudimg.com/raw/ffc7c5310b297bdb11620c711c62d84c.png)

[](id:test7)
## 数据调试

- 网关正确配置完成后，可在 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer/project/prj-p5atmkhu/gateway/list)>【网络管理】>【LoRa网关管理】>【用户网关】中看到网关处于"在线"状态。
![](https://main.qcloudimg.com/raw/8230cd436d64964ff0d327d05dc56115.png)
- 节点正确配置完成后，可在产品详情页>【设备开发】>【设备名称】>【在线调试】中看到节点的上行数据，可在"属性调试"中看到解析完成的数据。
![](https://main.qcloudimg.com/raw/3ac8e8fe2f1da6a5296a8c1017c53b43.png)


[](id:test8)
## 数据显示

### 配置面板

在产品详情页>【交互开发】>【面板配置】>【配置】页面中设置"腾讯连连"小程序 [显示面板](https://cloud.tencent.com/document/product/1081/40457#.E9.9D.A2.E6.9D.BF.E9.85.8D.E7.BD.AE)。

### 关联设备

- 节点和网关正确配置完成后，在【设备调试】进入设备列表页，单击设备右侧的【二维码】可查看该设备的"二维码"，打开"腾讯连连"小程序，通过小程序扫描设备二维码可快速添加设备。
![](https://main.qcloudimg.com/raw/de2766e4abb7b5bb01c750f2f4c4ba4e.png)
- 设备添加完成后，可在"腾讯连连"小程序点击对应设备查看设备数据。
<img src="https://main.qcloudimg.com/raw/cf901e1ff77cf1400eb655180b94d83d.png"style=" width: 55%;
">

[](id:test9)
## 配置自定义频点

本文以单信道频点计划为例进行说明。

[](id:test3)
### 创建自定义频点

1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择【公共实例】或您购买的【标准企业实例】进入项目列表页。
2. 选择某一个已新建产品的项目进入，选择左侧导航栏【网络管理】>【LoRa 网关管理】进入网关管理页面。
3. 单击【用户自定义频点】>【添加频点】进入“添加用户自定义频点”页面，填写相关信息。
<img src="https://main.qcloudimg.com/raw/e1ff00ad597b1fc1ad61a318190ef0fa.jpg" style="  width: 65%;
">
4. 单击【保存】即可创建自定义频点。


### 网关关联频点计划

您可 [创建网关](#test2) 或直接单击【编辑】修改“用户自定义频点”为您创建的 [自定义频点](#test3)。


### 设备关联频点计划

1. 选择左侧导航菜单【产品开发】进程产品列表页面，选择需要打开的产品进入产品详情页。
2. 单击【设备开发】>【编辑】进入 LoRaWAN 参数配置页面，将【用户自定义频点】选择为您创建的 [自定义频点](#test3)，关联与设备对应的频点计划。


