

## 操作场景

使用 ESP8266 腾讯云定制模组模拟一款智能灯，配合“腾讯连连”小程序实现设备接入，物联网开发平台可以远程控制灯的亮度、颜色、开关，并实时获取智能灯上报到开发平台的数据。

本文档主要指导您如何在物联网开发平台控制台接入智能灯。



## 前提条件

为了通过下面的步骤快速理解该业务流程，需要做好以下准备工作：
- 申请物联网开发平台服务。
- 安装 Python3 和 pyserial/paho-mqtt 模块。
- 准备一个 ESP8266 腾讯云定制模组，详情请参见 [腾讯云 IoT AT ESP8266 定制固件及说明](https://github.com/tencentyun/qcloud-iot-esp-wifi)。
- 下载 [腾讯云 IoT AT 指令模组测试工具](https://github.com/tencentyun/qcloud-iot-esp-wifi/tree/master/qcloud-iot-at-esp8266/QCloud_IoT_AT_Test_Tool)。



## 操作步骤

### 控制台操作
#### 创建项目和产品
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择【新建项目】。
2. 在新建项目页面，填写项目基本信息。
   - 项目名称：输入“智能灯演示”或其他名称。
   - 项目描述：按照实际需求填写项目描述。
![](https://main.qcloudimg.com/raw/321ab15978adf7bac3a89a083ca28d94.png)
3. 项目新建成功后，即可新建产品。

#### 新建产品
1. 进入该项目的产品列表页面，单击【新建产品】。
2. 在新建产品页面，填写产品基本信息。
  - 产品名称：输入“智能灯”或其他产品名称。
  - 产品类型：选择“智慧生活—电工照明—灯”。 
  - 设备类型：选择“设备”。
  - 认证方式：选择“密钥认证”。
  - 通信方式：选择“Wi-Fi”。
  - 其他都为默认选项。
  ![](https://main.qcloudimg.com/raw/70011f6b66a765ea99bd6da38dd37a47.png)
3. 产品新建成功后，您可在产品列表页查看到“智能灯”。


#### 创建数据模板
选择“智能灯”类型后，系统会自动生成标准功能。
![](https://main.qcloudimg.com/raw/1492c0e46bf33700d3e95e30284e87bb.png)



#### 交互开发配置
配置产品在小程序端的控制面板、配网引导、快捷入口，若不配置则使用系统默认配置。
![](https://main.qcloudimg.com/raw/3c467f9b8fbe1fd49dfd20f79c6ada90.jpg)



#### 创建测试设备
在设备调试页面中，单击【新建设备】，设备名为 dev001。
![img](https://main.qcloudimg.com/raw/d9910d3eaa5a130454e25708e5e05355.png)



### 模组测试工具操作

#### 模组设置
将模组接入 PC，识别到对应的串口。
![](https://main.qcloudimg.com/raw/39fcab900358d173e841c5a0f122e33e.png)

如果不能正确识别，需要手动更新串口驱动程序。



#### 设置模组进入配网模式

1. 在控制台创建设备的产品 ID、设备名称、设备密钥，写入模组测试工具的配置文件“Tool_Config.ini”里面的[ IE—DEV1 ]。
```
 ;设备产品ID
 Product_ID = YOUR_PRODUCT_ID
 ;设备名字
 Device_Name = device1
 ;设备密钥
 Device_Key = YOUR_DEVICE_KEY
```
2. 在模组测试工具的配置文件“Tool_Config.ini”中可配置需要创建的 softAP 热点名称和密码。
```
 ; WiFi模组创建softAP热点信息
 SAP_SSID = ESP8266-SoftAP
 SAP_PSWD = 12345678
```
完成配置后，保存文件。
3. 在命令行窗口，输入指令，使模组进入 softAP 配网模式。
```
python.exe .\QCloud_IoT_AT_Test_Tool.py -p COM7 -a ESP8266 -m wifi
```



### 腾讯连连添加设备

1. 使用“腾讯连连”扫描【交互开发】 > 【配网引导】中的二维码。
2. 选择目标 Wi-Fi，并输入密码，单击【下一步】。
3. 单击【在小程序内连接】，在小程序内连接设备热点。
4. 选择设备热点，并输入密码，开始配网。
5. 配网成功后，命令行窗口能看到模组打印如下内容：
```
softAp boarding and connection success
```
![](https://main.qcloudimg.com/raw/252964dbb9b9d7021f9e0d958e409d6b.jpg)


### 查看设备状态
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，选择【产品开发】>【设备调试】，可查看到设备 "dev001" 的状态为“上线”状态，表示模组已成功连接上开发平台。
2. 单击【调试】，可进入设备详情页。
![](https://main.qcloudimg.com/raw/229018e428ac4c578af1782c18f96084.jpg)
3. 单击【设备名称】>【设备属性】，可查询设备上报到开发平台的最新数据及历史数据。
  - 当前上报数据的最新值：会显示设备上报的最新数据。
  - 当前上报数据的更新时间：显示数据的更新时间。




### 模拟上报数据
命令行窗口模拟真实设备上报数据。
 -  首次直接单击【回车键】，随机更新一次属性功能数据上报云端。
 - 后续输入【update】会进行一次 template 数据的随机更新。
![](https://main.qcloudimg.com/raw/3fe0342aae76eb6e1da4eb108eae1b34.png)

### 查看设备通信日志
单击【设备日志】，可查询该设备某段时间范围的所有上下行数据。
  - 上行：上行指设备端上报到开发平台的数据。
  - 下行：下行指从开发平台下发到设备的数据。
![](https://main.qcloudimg.com/raw/545c7b1615cd3214fbc27033362a0e17.png)



### 在线调试

1. 当模组成功连接到物联网开发平台后，您可在控制台【设备调试】列表，单击【调试】，进入在线调试。
![](https://main.qcloudimg.com/raw/290c3580de8d7e7d0a89c3da7544c996.png)
2. 将亮度设置为50，颜色设置为“Red”，单击【发送】。
3. 通信日志会显示如下日志，表示成功下发了指令到设备端。
![](https://main.qcloudimg.com/raw/720b6dfb2047d7766cb2490089ec570f.png)
4. 查看命令行窗口，可查看到模组成功接收到下发的数据。
![](https://main.qcloudimg.com/raw/0f0035ab33cb588f8d4be0015be38362.png)
