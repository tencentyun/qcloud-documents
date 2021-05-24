## SaaS 客户端接入流程
![](https://main.qcloudimg.com/raw/6bc87cb24381be162af59ece11c991af.png)
1. 在控制台添加老师/学生账户信息；
2. 在控制台上提前准备上课课件；
3. 创建课堂，获取课堂编号；
4. 完成1 - 3步骤后，您可获得 classID、userID 和 userToken 等关键信息以及腾讯云互动课堂统一分配的机构码，这样您就可以使用腾讯云互动课堂客户端进行授课上课了。

更多控制台的使用，可以参考 [控制台使用手册](https://cloud.tencent.com/document/product/680/37505)。

## 参数详解

参数 ID|参数类型|解释|获取方式
:--:|:--:|:--:|:--
company_id|int|机构码：获取机构的信息（机构名称，应用图标等）的唯一标识。|申请 SaaS 服务邮件获取。具体请参见 [开通指南](https://cloud.tencent.com/document/product/680/41461)。
class_id|int|课堂编号：获取课堂信息的唯一标识。|通过云 API 预约课堂获取。具体请参见 [云 API-预约课堂](https://cloud.tencent.com/document/product/680/37540#.E9.A2.84.E7.BA.A6.E8.AF.BE.E5.A0.82)。
user_id|string|帐号。|通过云 API 创建账号获取。具体请参见 [云 API-创建账号](https://cloud.tencent.com/document/product/680/37540#.E5.88.9B.E5.BB.BA.E8.B4.A6.E5.8F.B7)。
user_token|string|用户签名。|通过云 API 创建账号获取。具体请参见 [云 API-创建账号](https://cloud.tencent.com/document/product/680/37540#.E5.88.9B.E5.BB.BA.E8.B4.A6.E5.8F.B7)。
user_sig|string|腾讯云签名，登录必要的腾讯云模块用。|1. 如果用户把私钥托管给我们，则不用填。<br>2. 如果没有托管，请使用 IMSDK 私钥自行计算。具体请参见 [如何计算 UserSig](https://cloud.tencent.com/document/product/647/17275)。

## 各端接入流程

### 桌面端
<div id="electron_location"></div>

####  安装
mac：[下载地址](http://dldir1.qq.com/hudongzhibo/Saas/TClass_Saas.dmg)。
win：[下载地址](http://dldir1.qq.com/hudongzhibo/Saas/TClass_Setup_Saas.exe)。
>!在用户机器上安装互动课堂组件。在 Win10 上必须使用管理员权限安装。

####  使用
1. 通过浏览器启动应用进入课堂
如果应用已安装，可通过浏览器直接拉起。如果未安装，会提示下载地址。目前支持的浏览器有 Chrome、Safari。
>?因受到 electron 注册网络协议的限制，MAC 需点击启动后才可拉起。

 URL 拼写规则如下：
```
https://tedu.qcloudtrtc.com/#/class/company_id/:class_id/:user_id?/:user_sig?/:user_token?
```
示例如下：
```
https://tedu.qcloudtrtc.com/#/class/机构编号/课堂编号/账号（可选）/用户签名（可选）/密码（可选） 
例如：
https://tedu.qcloudtrtc.com/#/class/100001/1000776477
或者：
https://tedu.qcloudtrtc.com/#/class/100001/1000776477/xxx/xxx/xxx
```
2. 单击启动进入课堂
  桌面单击应用启动，输入机构编号、课堂编号、账户和密码加入课堂。

### Web 端
<span id="web_location"></span>

目前 Web 客户端暂时只提供纯网页方式拉起，后期会提供库方式整合。

####  URL 启动

```
https://tedu.qcloudtrtc.com/#/class/company_id/:class_id/:user_id?/:user_sig?/:user_token?
```

#### example - 不带登录态
```
company_id(机构码) => 100001
class_id（课堂编号） => 1000713668
```

单击 [登录互动课堂](https://tedu.qcloudtrtc.com/#/class/100001/1000713668)。

### 移动端

#### 安装

Android：应用宝搜索【腾讯云互动课堂】。
iOS：App Store 搜索【腾讯云互动课堂】。

#### 使用

参考互动课堂 SaaS [移动端使用文档](https://cloud.tencent.com/document/product/680/37519)。
