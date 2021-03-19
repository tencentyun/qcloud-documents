
本文为您介绍如何开通 Google Assistant 语音智能服务，实现通过 Google Home 音箱对智能设备的控制。

## 限制条件  

#### 激活设备对接 Google Assistant 仅支持在以下地区
- 美国

#### 语音技能支持语言

- 英语
- 中文（部分语义）

## 控制台开通第三方语音技能服务

### 步骤1：确认产品范围和功能

新建产品时，产品品类需选择平台指定支持的品类，若选择其他品类或自定义将无法使用语音技能服务。
<img src="https://main.qcloudimg.com/raw/620d3f0bb3ade3a15b0e8ae2a748d85d.png" style="width:85%;"></img>
您可以通过下表，查看支持的品类和功能是否满足您的产品开发。  

| 支持的品类                   | 支持的功能（状态获取&指令） |
| ---------------------------- | --------------------------- |
| 智慧生活—电工照明—灯         | 开关、颜色调节、亮度调节    |
| 智慧生活—电工照明—开关面板   | 开关                        |
| 智慧生活—电工照明—插座       | 开关                        |
| 智慧生活—电工照明—窗帘       | 开关、百分比调节            |
| 智慧生活—家用电器—香薰机     | 开关                        |
| 智慧生活—家用电器—扫地机器人 | 开关                        |
| 智慧生活—家用电器—风扇       | 开关                        |


>?腾讯云物联网平台关于 Google Assistant 支持的品类或功能，后续将会支持更多，若您有接入需求，您可以在腾讯云官网通过 [在线客服](https://cloud.tencent.com/act/event/connect-service)，描述您的产品需求并提交开通申请，我们将安排相关工作人员与您进行对接。

### 步骤2：申请开通 Google Assistant 服务

1. 登录 [物联网开发平台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F)，地区选择美国，创建项目及产品，详情请参考 [产品定义](https://cloud.tencent.com/document/product/1081/34739)。
![](https://main.qcloudimg.com/raw/beca495cb2aec4218f6aa3e6eab9b723.jpg)
2. 单击项目进入项目详情界面，单击【语音技能】>【Google Assistant】> 【申请开通】，进入申请界面。 
![](https://main.qcloudimg.com/raw/8b67d2cc1ace18ccea3a19a090b8dcd9.png)
3. 选择需要开通的产品，填写申请信息后，还需勾选“我了解并同意《开发者须知与授权》”，单击【提交申请】，我们将安排相关工作人员与您进行对接。
 - **选择产品**：该项目下创建的产品。
 - **其他需求描述**：最多不超过250个字符。
![](https://main.qcloudimg.com/raw/9573d9c3c13c6be2bb3b7b2792866b57.png)
4. 申请通过后，您也可以在【选择产品】处新增您该项目下的产品。
![](https://main.qcloudimg.com/raw/9efd773c43fbf6b1fca1b5099a250f42.png)
5. 选择需要添加的产品，单击【确定】。
![img](https://main.qcloudimg.com/raw/44bd971e38b9612ee991a510eb533119.jpg)
6. 添加产品审核通过后，即可生效语音技能。

>?使用腾讯连连小程序进行设备调试，配网绑定您的设备后，可根据下方消费者使用步骤，绑定 Google Home，即可实现音箱控制设备的功能。

## 消费者使用

### 前提条件
1. 拥有一台 Google Home 设备，以及 Google Home App 的登录账号。
2. 拥有一台及以上物联网开发平台发布的智能设备，且使用微信小程序“腾讯连连”绑定该设备。
3. 可以访问 Google 服务的 Wi-Fi 网络。

### 使用步骤

1. 用户使用微信小程序“腾讯连连”绑定物联网开发平台发布的智能设备产品。  
>!使用微信小程序“腾讯连连”登录的用户，**需要前往个人中心绑定手机号或者邮箱号并且设置密码**，路径为选择【我的】>【个人信息】，进入账号与安全页面，即可绑定手机号或者邮箱号。
>
2. **将已绑定的设备改为英文名**，例如：my light，修改后的名称避免使用符号。**设备修改路径为**：小程序【首页】>【选择指定产品名称】>【打开设备详情】>【点击设备名称】，修改后单击【保存】即可。 
![](https://main.qcloudimg.com/raw/2afdb7d496c5775f0e6f19e46ca5590f.png)
3. 下载安装 Google Home 或者 Google Assistant App 并绑定 Google Home 智能音箱；。
4. 在 Google Home App 主页上点击【+】按钮添加设备，选择【Set up devices】列表下的【Works with Google】。搜索并选择“tencentlianlian”，登录腾讯连连的账号进行账号绑定，授权设备的控制权。绑定成功后，您的设备会显示在 Home Control 的 Devices 列表中。 
![](https://main.qcloudimg.com/raw/cf75d247f613e4b3fbe6f2771aa0361e.jpg)

使用 Google Home 音箱控制产品，支持的功能例句可参考下表。

| 品类       | 功能                     | 语音例句（以实际使用场景为准）                               |
| ---------- | ------------------------ | ------------------------------------------------------------ |
| 灯         | 开关、颜色调节、亮度调节 | Hey/Ok Google，turn on bedroom light<br/>Hey/Ok Google，turn off bedroom light<br/>Hey/Ok Google，set bedroom light to blue<br/>Hey/Ok Google，brighten bedroom light |
| 开关面板   | 开关                     | Hey/Ok Google，turn on the switch<br />Hey/Ok Google，turn off the switch |
| 插座       | 开关                     | Hey/Ok Google，turn on the socket<br />Hey/Ok Google，turn off the socket |
| 窗帘       | 开关、百分比调节         | Hey/Ok Google，turn on the curtain<br />Hey/Ok Google，turn off the curtain<br />Hey/Ok Google，open/close the curtain 50% |
| 香薰机     | 开关                     | Hey/Ok Google，turn on the Aroma<br />Hey/Ok Google，turn off the Aroma |
| 扫地机器人 | 开关                     | Hey/Ok Google，turn on the worker<br />Hey/Ok Google，turn off the worker |
| 风扇       | 开关                     | Hey/Ok Google，turn on the fan<br />Hey/Ok Google，turn off the fan  |



