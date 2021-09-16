
本实例中使用第三方平台 Amazon Alexa 实现语音智能服务，关于 Alexa 详细的官方文档，详情请参见 [Amazon Alexa 文档](https://developer.amazon.com/en-US/docs/alexa/smarthome/understand-the-smart-home-skill-api.html)。
## 限制条件  

#### 激活设备对接 Amazon Alexa 仅支持以下地区
 - 美国 
 
#### 语音技能仅支持以下语言
 - 英语
 
## 控制台开通第三方语音技能服务

### 步骤1：确认产品范围和功能

新建产品时，产品品类需选择平台指定支持的品类，若选择其他品类或自定义将无法使用语音技能服务。
<img src="https://main.qcloudimg.com/raw/620d3f0bb3ade3a15b0e8ae2a748d85d.png" style="width: 85%;"></img>
您可以通过下表，查看支持的品类和功能是否满足您的产品开发。  

| 支持的品类                   | 支持的功能                         |
| ---------------------------- | ---------------------------------- |
| 智慧生活—电工照明—灯         | 开关、亮度调节、颜色调节、色温调节 |
| 智慧生活—电工照明—开关面板   | 开关                               |
| 智慧生活—电工照明—插座       | 开关                               |
| 智慧生活—电工照明—窗帘       | 开关、百分比调节                   |
| 智慧生活—家用电器—香薰机     | 开关                               |
| 智慧生活—家用电器—扫地机器人 | 开关                               |
| 智慧生活—家用电器—空气净化器 | 开关、风速（调大调小）、模式       |

>?腾讯云物联网开发平台关于 Amazon Alexa 支持的品类或功能，后续将会支持更多，若您有接入需求，您可以在腾讯云官网通过 [在线客服](https://cloud.tencent.com/act/event/connect-service)，描述您的产品需求并提交开通申请，我们将安排相关工作人员与您对接。

### 步骤2：申请开通 Amazon Alexa 服务
1. 登录 [物联网开发控制台](https://console.cloud.tencent.com/iotexplorer) ，地区选择美国东部，创建项目及产品，详情请参考 [产品定义](https://cloud.tencent.com/document/product/1081/34739)。
![](https://main.qcloudimg.com/raw/beca495cb2aec4218f6aa3e6eab9b723.jpg)
2. 单击项目进入项目详情界面，单击【语音技能】>【Amazon Alexa】> 【申请开通】，进入申请界面。
![](https://main.qcloudimg.com/raw/a0ae4021c39481a32343b093d399596f.png)
3. 选择需要开通的产品，填写申请信息后，还需勾选“我了解并同意《开发者须知与授权》”，单击【提交申请】，我们将安排相关工作人员与您进行对接。
 - **选择产品**：该项目下创建的产品。
 - **其他需求描述**：最多不超过250个字符。
![](https://main.qcloudimg.com/raw/7e24d064dda314a144546fcdd5bef5e9.jpg)
4. 申请通过后，您也可以在【选择产品】处新增您该项目下的产品。
![](https://main.qcloudimg.com/raw/40a6f521191f0c8826d7be7e83688f0e.png)
5. 选择需要添加的产品，单击【确定】。
![](https://main.qcloudimg.com/raw/44bd971e38b9612ee991a510eb533119.jpg)
6. 添加产品审核通过后，即可生效语音技能。


>?使用腾讯连连小程序进行设备调试，配网绑定您的设备后，可根据下方 [消费者使用](#test) 步骤，绑定 Amazon Alexa，即可实现音箱控制设备的功能。
<span id="test"></span>
## 消费者使用

### 前提条件

1. 拥有一台 Alexa 设备，以及 Amazon Alexa 可正常使用的账号。
2. 拥有一台及以上物联网开发平台发布的智能设备，且使用微信小程序“腾讯连连”绑定该设备。
3. 拥有可以顺畅访问 Amazon 服务的 Wi-Fi 网络。

### 操作步骤

1. 用户使用微信小程序“腾讯连连”绑定物联网开发平台发布的智能设备产品。  
>!使用微信小程序“腾讯连连”登录的用户，**需要前往个人中心绑定手机号或者邮箱号并且设置密码**，路径为选择【我的】>【个人信息】，进入账号与安全页面，即可绑定手机号或者邮箱号。
2. **将已绑定的设备改为英文名**，例如：my light，修改后的名称避免使用符号。**设备修改路径为**：小程序【首页】>【选择指定产品名称】>【打开设备详情】>【点击设备名称】，修改后单击【保存】即可。
![](https://main.qcloudimg.com/raw/e8435a54626e368c856f2d734fc04120.png)
3. 拥有一台 Amazon Alexa 智能音箱，下载 Amazon Alexa App 并绑定该音箱。
4. Amazon Alexa App 登录腾讯连连的账号，授权设备的控制权。打开菜单，选择【Skill&Games】，发现腾讯连连，选择后进行账号绑定。
![](https://main.qcloudimg.com/raw/4614a7c2280f29e23102e07c6474de5e.png)
5. 控制设备前，Amazon Alexa 音箱需要先发现设备。您可以对 Amazon Alexa 音箱说：“Alexa, discover devices。”
>!若是在腾讯连连中修改了产品名称，则在 Amazon Alexa 音箱中需要重新绑定设备。

使用 Amazon Alexa 音箱控制产品，支持的功能例句可参考下表。

| 品类       | 功能                         | 语音例句（以实际使用场景为准）                               |
| :--------- | :--------------------------- | ------------------------------------------------------------ |
| 灯         | 开关                         | Alexa, turn on the light<br />Alexa, turn off the light       |
| 开关面板   | 开关                         | Alexa, turn on the switch<br />Alexa, turn off the switch    |
| 插座       | 开关                         | Alexa, turn on the socket<br />Alexa, turn off the socket    |
| 窗帘       | 开关、百分比调节             | Alexa, turn on  curtain<br />Alexa, turn off  curtain<br />Alexa, open\|close the curtain 50% |
| 香薰机     | 开关                         | Alexa, turn on the Aroma<br />Alexa, turn off the Aroma      |
| 扫地机器人 | 开关                         | Alexa, turn on the worker<br />Alexa, turn off the worker    |
| 空气净化器 | 开关、风速（调大调小）、模式 | Alexa, turn on the purifier<br />Alexa, turn off the purifier<br />Alexa, set the purifier FanSpeed to 3<br />Alexa, set the purifier  to 3<br />Alexa, setFanSpeed |



