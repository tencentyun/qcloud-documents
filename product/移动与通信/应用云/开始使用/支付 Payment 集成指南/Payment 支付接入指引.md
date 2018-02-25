# Payment 支付接入指引


Payment 支持微信支付和手 Q 支付的 APP 支付模式，您可以通过在移动端 APP 中集成 Payment SDK 来调起微信支付和手 Q 支付。

> [什么是 App 支付](http://kf.qq.com/faq/17060936FNZj170609vMneY3.html)


## 创建 TAC 应用

想要接入 Payment 支付功能，首先您必须在 TAC 平台上创建项目和应用，首先登录 [TAC 平台](https://console.qcloud.com/tac)，然后点击【创建项目】按钮来创建一个新的项目：

创建好项目后，点击该项目：

然后点击【创建应用】按钮来创建一个应用：

创建好应用后，您就可以开始接入 Payment 支付功能了。

## 接入微信支付

下面将详细说明如何在 TAC 平台上接入 Payment 的微信支付渠道。

### 第一步：注册微信开放平台账号并进行认证

首先登录[微信开放平台](https://open.weixin.qq.com)，点击首页右上角的【注册】按钮，注册成为微信开放平台开发者。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_login.png)

### 第二步：开发者资质认证

开放平台需进行开发者资质认证后才可申请微信支付，您可以点击【账号中心】，然后点击【开发者资质认证】来进行认证，认证费：300元/次。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_verify.png)

### 第三步：创建 APP

点击【管理中心】，然后再点击【创建移动应用】，在开放平台上创建 APP，审核通过后即可获得该应用的 AppID 以及 AppSecret。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_new_app.png)

### 第四步：提交资料申请微信支付

点击【管理中心】，选择需要申请支付功能对应的APP，在微信支付一栏中点击【申请开通】按钮，然后开始填写资料等待审核，审核时间为1-5个工作日内。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_open_pay.png)

### 第五步：开户成功，登录商户平台进行验证

资料审核通过后，请登录联系人邮箱查收商户号和密码，并登录[商户平台](https://pay.weixin.qq.com/index.php/core/home/login)填写财付通备付金打的小额资金数额，完成账户验证。（[查看验证方法](http://kf.qq.com/faq/161220mQjmYj161220n6jYN7.html)）

### 第六步：在线签署协议
本协议为线上电子协议，签署后方可进行交易及资金结算，签署完立即生效。[点此提前预览协议内容](https://pay.weixin.qq.com/index.php/public/apply_sign/protocol)。

### 第七步：配置渠道信息

打开之前在 TAC 平台上创建的应用，点击【我的米大师】，选择【渠道管理】，然后点击【开通微信支付】：

add image

填入之前申请好微信商户平台上的商户号和商户号密钥，以及微信开放平台上审核通过的应用AppID和AppKey，然后点击【确认】：

add image

### 第八步：设置支付参数

点击【我的米大师】，选择【参数配置】，点击【修改】：

add image

配置好对应的渠道信息、回调地址和平台参数后，点击【保存&预览】：

add image

> 其中回调地址是支付完成后服务器回调的地址，而平台参数则是用于鉴定来源的APP信息，安卓平台下为应用签名和应用包名，iOS平台下为Bundle Identifier。 

## 接入手 Q 支付

下面将详细说明如何在 TAC 平台上接入 Payment 的手 Q 支付。

### 第一步：在 QQ 钱包上填写资料

登录 [QQ 钱包商户平台](https://qpay.qq.com)，点击【立即接入】，然后按照指引填写相关资料，提交的资料将会在 3 ~ 5 个工作日内审核完成。资料提交后，QQ 钱包将会向商户银行账户汇一笔金额随机的验证款，以确认账户真实性。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_wallet_login.png)

### 第二步：查收开户邮件

在所有资料审核通过后，将会收到 QQ 钱包的开户邮件，包含了商户平台的登录账户和密码等重要信息。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_open_email.jpg)

### 第三步：查收款项

您提交资料后，将会收到一笔来自“财付通支付科技有限公司客户备付金”账户的随机金额款项，后续需要通过金额来对账户进行验证。 

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_money.jpg)

### 第四步：验证账户

您可以使用开户邮件中提供的登录账号和登录密码登录商户平台，然后点击【去验证】，在商户平台验证账户页面回填收到的金额，金额正确将会通过验证。
![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_verify_account.jpg)

### 第五步：在线签署协议

账户验证成功后，即可在线签署协议，确认相关信息无误后，点击【确定签署】完成协议签署。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_sign.jpg)

### 第六步：登录腾讯开放平台

首先登录[腾讯开放平台](http://open.qq.com/)，点击首页右上角的【登录】按钮进行登录。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_open_login.png)

### 第七步：创建 APP

登录腾讯开放平台后，点击【应用接入】、然后选择【应用接入】，

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_new_app_1.png)

接着点击【创建应用】按钮来创建新的应用。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_new_app_2.png)
### 第八步：在 QQ 钱包商户平台上添加应用

登录 [QQ 钱包商户平台](https://qpay.qq.com)，点击【账户管理】，选择【开发配置】，然后点击【上传材料】按钮将之前在腾讯开放平台上创建的 APP 添加到商户平台上，添加成功后，会在两个工作日内生效。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_add_app.png)

### 第九步：配置渠道信息

打开之前在 TAC 平台上创建的应用，点击【我的米大师】，选择【渠道管理】，然后点击【开通 QQ 钱包支付】：

add image

填入之前申请的 QQ 商户号上的商户号和商户号密钥，腾讯开放平台上审核通过的应用AppID和AppKey然后点击【确认】：

add image

### 第十步：设置支付参数

点击【我的米大师】，选择【参数配置】，点击【修改】：

add image

配置好对应的渠道信息、回调地址和平台参数后，点击【保存&预览】：

add image

> 其中回调地址是支付完成后服务器回调的地址，而平台参数则是用于鉴定来源的APP信息，安卓平台下为应用签名和应用包名，iOS平台下为Bundle Identifier。 














