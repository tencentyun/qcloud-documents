


## 背景信息 

本实例中使用 Amazon Alexa，详细的官方文档请参见 [Amazon Alexa文档](https://developer.amazon.com/en-US/docs/alexa/smarthome/understand-the-smart-home-skill-api.html)。

## 限制条件  ![]()

**仅支持在以下地区激活设备对接 Amazon Alexa**    

- 中国大陆  
- 美国  

## 控制台开通第三方语音技能服务

### 步骤1：确认产品范围和功能

您可以通过下表，查看支持的品类和功能是否满足您的产品开发。  
>!语音技能语言暂时仅支持**英语**。

| 支持的品类 | 支持的功能       |
| ---------- | ---------------------------------- |
| 灯         | 开关、亮度调节、颜色调节、色温调节 |
| 开关面板   | 开关                               |
| 插座       | 开关                               |
| 窗帘       | 开关、百分比调节                   |
| 香薰机     | 开关                               |
| 扫地机器人 | 开关                               |
| 空气净化器 | 开关、风速（调大调小）、模式       |

>?腾讯云物联网开发平台关于 Amazon Alexa 支持的品类或者功能，将会逐渐的增加，若您有接入需求，您可以在 [腾讯云物联网开发平台](https://cloud.tencent.com/act/event/connect-service) 描述您的产品需求并提交开通申请，工作人员将会与您进行对接。

### 步骤2：申请开通 Amazon Alexa 服务
#### 新建项目
1. 登录 [物联网开发平台控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fiotexplorer)。
2. 点击新建项目，填写项目名称和项目描述：
 - 项目名称：中文、英文、数字、下划线的组合，最多不超过20个字符。
 - 项目描述：按照实际需求填写项目描述。
![](https://main.qcloudimg.com/raw/a696eca1c331421602e5d099c985d252.jpg)
3. 项目基本信息填写完成后，单击【保存】，即可完成新建项目。
4. 项目新建成功后，即可新建产品。

#### 创建产品
1. 进入该项目的产品列表页面，单击【新建产品】.
2. 在新建产品页面，填写产品基本信息。
  - 产品名称：中文、英文、数字、下划线的组合，最多不超过20个字符。
  - 产品品类：随意选择。
  - 设备类型：随意选择。
  - 认证方式：随意选择。
  - 通信方式：随意选择。
  - 数据协议：默认为“数据模板”。
  - 描述：最多不超过80个字符
![](https://main.qcloudimg.com/raw/5632337cf6b43546f83d4cf9a92a18dd.png)
3. 产品信息填写完成后，单击【保存】，即可完成新建产品。
4. 产品新建成功后，可在产品列表页查看到“智能灯”。
![](https://main.qcloudimg.com/raw/cea75c03773aed81f9061da302e9fb3d.png)

#### 申请开通
1. 单击【语音技能】>【Amazon Alexa】> 【申请开通】，进入申请界面

2. 选择需要开通的产品，填写申请信息后提交，我们将会有工作人员与您进行对接。

<img src="https://main.qcloudimg.com/raw/a84ec653178f17db7ae39e6639a56d13.png" alt="image-20200628100119804" style="zoom:50%;" />

<img src="https://main.qcloudimg.com/raw/0fd30fc5f7a35b14e0e3ad85447da0bf.png" alt="image-20200628100119804" style="zoom:50%;" />

3. 申请通过后，您也可以在【选择产品】处新增您该项目下的产品。
<img src="https://main.qcloudimg.com/raw/1c084a735b0759f8a18658b7d787bfc2.png" alt="image-20200628100119804" style="zoom:50%;" />
5. 添加产品审核通过后，即可生效语音技能。
<img src="https://main.qcloudimg.com/raw/e921c49d125051666a80c99eb274d69a.png" alt="image-20200628100119804" style="zoom:50%;" />

2.3使用腾讯连连小程序进行设备调试，配网绑定您的设备后，可根据下方消费者使用步骤，绑定Amazon Alexa，即可实现音箱控制设备的功能。

## 消费者使用

### 前提条件

1. 拥有一台alexa设备，以及Amazon alexa可的登录账号
2. 拥有一台及以上物联网开发平台发布的智能设备，且使用微信小程序“腾讯连连”绑定该设备；
3. 可以顺畅访问 Amazon 服务的 Wi-Fi 网络。

### 使用步骤

1.用户使用微信小程序“腾讯连连”绑定物联网开发平台发布的智能设备产品。  

**注意**：使用微信小程序“腾讯连连”登录的用户，**需要前往个人中心绑定手机号或者邮箱号并且设置密码**，路径为选择我的-->点击个人信息-->进入账号与安全，即可绑定手机号或者邮箱号。

2.**将已绑定的设备改为英文名**，例如：my light，修改后的名称避免使用符号。  

**设备修改路径为**：小程序首页选择指定产品名称-->打开设备详情-->点击设备名称，修改后保存即可。

<img src="https://main.qcloudimg.com/raw/eb124d32c90837a38a4a78f836a1be7a.png" alt="image-20200628100119804" style="zoom:50%;" />

2.拥有一台Amazon Alexa智能音箱，下载Amazon Alexa APP并绑定该音箱。

3.Amazon Alexa APP登录腾讯连连的账号，授权设备的控制权。打开菜单，选择Skill&Games，发现腾讯连连，选择后进行账号绑定。

<img src="https://main.qcloudimg.com/raw/bd8cc505e1454b438a656faba2c23f9b.png" alt="image-20200628100119804" style="zoom:50%;" />

4.控制设备前，Amazon alexa音箱需要先发现设备。您可以对Amazon alexa音箱说：Alexa, discover devices。注意：若是在腾讯连连中修改了产品名称，则在Amazon alexa音箱中需要重新绑定设备。

4.使用Amazon Alexa音箱控制产品，支持的功能例句可参考下表

| 品类       | 功能                         | 语音例句（以实际使用场景为准）                               |
| :--------- | :--------------------------- | ------------------------------------------------------------ |
| 灯         | 开关                         | Alexa, turn on the light<br />Alexa, turn of the light       |
| 开关面板   | 开关                         | Alexa, turn on the switch<br />Alexa, turn off the switch    |
| 插座       | 开关                         | Alexa, turn on the socket<br />Alexa, turn off the socket    |
| 窗帘       | 开关、百分比调节             | Alexa, turn on  curtain<br />Alexa, turn off  curtain<br />Alexa, open\|close the curtain 50% |
| 香薰机     | 开关                         | Alexa, turn on the Aroma<br />Alexa, turn off the Aroma      |
| 扫地机器人 | 开关                         | Alexa, turn on the worker<br />Alexa, turn off the worker    |
| 空气净化器 | 开关、风速（调大调小）、模式 | Alexa, turn on the purifier<br />Alexa, turn off the purifier<br />Alexa, set the purifier FanSpeed to 3<br />Alexa, set the purifier  to 3<br />Alexa, setFanSpeed |



