# Saas客户端纯应用方式接入指南

# 1.SaaS客户端接入流程

![](https://main.qcloudimg.com/raw/6bc87cb24381be162af59ece11c991af.png)

1. 控制台添加老师/学生账户信息；

2. 在控制台上提前准备上课课件；

3. 创建课堂，获取课堂ID；

4. 在1-3步骤之后，您可以拿到classID、userID和userToken等关键信息，加上腾讯云互动课堂统一分配的机构码，这样您就可以使用腾讯云互动课堂客户端进行授课上课了。


> 更多控制台的使用，可以参考[控制台使用手册]()


# 2.关键参数解释及获取方式

参数ID|参数类型|解释|获取方式
:--:|:--:|:--:|:--
company_id|int|机构码：获取机构的信息(机构名称，应用icon等)的唯一标识|申请Saas服务邮件获取 具体见
class_id|int|课堂id：获取课堂信息的唯一标识|通过云API 创建课堂获取
user_id|string|用户帐号|通过云API 创建用户获取
user_token|string|用户签名|通过云API 创建用户获取
user_sig|string|腾讯云签名 登录必要的腾讯云模块用|1如果用户把私钥托管给我们，不用填 2如果没有托管，请拿IMSDK私钥自行计算

# 3.各个端接入流程

## 3.1 桌面端
<div id="electron_location"></div>


###  安装
mac: http://dldir1.qq.com/hudongzhibo/Saas/TClass_Saas.dmg
win: http://dldir1.qq.com/hudongzhibo/Saas/TClass_Setup_Saas.exe

 在用户机器上安装互动课堂组件。在Win10上必需使用管理员权限安装。

###  使用
####  1.通过浏览器启动应用直接进入课堂 


 如果已经安装过应用，可以通过浏览器方式直接拉起来。
 
> MAC需点击启动一次才能拉起，受限electron注册网络协议。

如果没有安装，会提示下载地址。 
目前支持的浏览器有Chrome、Safari。

URL拼写规则如下 

 **https://tedu.qcloudtrtc.com/#/class/company_id/:class_id/:user_id?/:user_sig?/:user_token?**
 
```
https://tedu.qcloudtrtc.com/#/class/机构ID/房间ID/用户ID（可选）/用户Sig（可选）/用户token（可选） 

例如：
https://tedu.qcloudtrtc.com/#/class/100001/1000776477
或者：
https://tedu.qcloudtrtc.com/#/class/100001/1000776477/xxx/xxx/xxx

```


#### 2.点击启动进入课堂

  桌面点击应用启动，输入机构码、课堂ID、用户ID和用户密码加入课堂。


## 3.2 WEB端
<span id="web_location"></span>

目前WEB客户端暂时只提供纯网页方式拉起，后期会提供库方式整合

###  URL启动

```
https://tedu.qcloudtrtc.com/#/class/company_id/:class_id/:user_id?/:user_sig?/:user_token?
```

### example - 不带登录态
```
company_id(机构码) => 100001
class_id（课堂id） => 1000713668
```

https://tedu.qcloudtrtc.com/#/class/100001/1000713668


## 3.3 移动端

### 安装

Android：应用宝搜索《腾讯云互动课堂》
iOS：App Store 搜索《腾讯云互动课堂》

### 使用

参考[互动课堂 SaaS 移动端 App 使用文档](#Android_location)
