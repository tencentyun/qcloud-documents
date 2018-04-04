

## 准备工作

Payment 支持微信支付和手 Q 支付的 [APP 支付](http://kf.qq.com/faq/17060936FNZj170609vMneY3.html)模式，您可以通过在移动端 APP 中集成 Payment SDK 来调起微信支付和手 Q 支付。


## 配置微信支付

您需要先在 [微信开放平台](https://open.weixin.qq.com) 和 [微信商户平台](https://pay.weixin.qq.com/index.php/core/home/login) 上申请好相关信息，然后才能给应用配置微信支付功能。下面将详细说明如何在 MobileLine 平台上配置 Payment 的微信支付渠道。

### 第一步：注册微信开放平台账号并进行认证

登录 [微信开放平台](https://open.weixin.qq.com)，单击首页右上角的【注册】按钮，注册成为微信开放平台开发者。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_login.png)

### 第二步：开发者资质认证

开放平台需进行开发者资质认证后才可申请微信支付，可通过单击【账号中心】>【开发者资质认证】来进行认证，认证费：300 元/次。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_verify.png)

### 第三步：创建 App
 
单击【管理中心】>【创建移动应用】，在开放平台上创建 App，审核通过后即可获得该应用的 AppID 以及 AppSecret。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_new_app.png)

### 第四步：提交资料申请微信支付
 
单击【管理中心】，选择需要申请支付功能对应的 App，在微信支付一栏中单击【申请开通】按钮，然后开始填写资料等待审核，审核时间为 1 - 5 个工作日内。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_wechat_open_pay.png)

### 第五步：开户成功，登录商户平台进行验证

资料审核通过后，请登录联系人邮箱查收商户号和密码，并登录 [商户平台](https://pay.weixin.qq.com/index.php/core/home/login) 填写财付通备付金打的小额资金数额，完成账户验证（[查看验证方法](http://kf.qq.com/faq/161220mQjmYj161220n6jYN7.html)）。
### 第六步：在线签署协议
本协议为线上电子协议（[点此提前预览协议内容](https://pay.weixin.qq.com/index.php/public/apply_sign/protocol)），签署后方可进行交易及资金结算，签署完立即生效。

### 第七步：配置渠道信息

打开之前在 [MobileLine 平台](https://console.cloud.tencent.com/tac)上创建的应用，单击【我的米大师】>【渠道管理】，然后单击【开通微信支付】：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_add_wechat_pay.png?raw=true)

填入之前申请好微信商户平台上的商户号和商户号密钥，以及微信开放平台上审核通过的应用 AppID 和 AppKey，然后单击【确认】。

### 第八步：设置支付参数
 
单击【我的米大师】>【参数配置】，单击【修改】：

![confirm](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_confirm_conf2.png?raw=true)

配置好对应的渠道信息、回调地址和平台参数后，单击【保存&预览】：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_input_config.png?raw=true)

到此，您即已经完成了微信支付的配置。

> **注意：**
> 其中回调地址是支付完成后服务器回调的地址，而平台参数则是用于鉴定来源的 App 信息，安卓平台下为应用签名和应用包名，iOS 平台下为 Bundle Identifier。 

## 配置手 Q 支付

您需要先在 [QQ 钱包商户平台](https://qpay.qq.com) 和 [腾讯开放平台](http://open.qq.com/) 上申请好相关信息，然后才能给应用配置 QQ 支付功能。下面将详细说明如何在 MobileLine 平台上配置 Payment 的手 Q 支付。

### 第一步：在 QQ 钱包上填写资料

登录 [QQ 钱包商户平台](https://qpay.qq.com)，点击【立即接入】，然后按照指引填写相关资料，提交的资料将会在 3 ~ 5 个工作日内审核完成。资料提交后，QQ 钱包将会向商户银行账户汇一笔金额随机的验证款，以确认账户真实性。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_wallet_login.png?raw=true)

### 第二步：查收开户邮件

在所有资料审核通过后，将会收到 QQ 钱包的开户邮件，包含了商户平台的登录账户和密码等重要信息。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_open_email.jpg)

### 第三步：查收款项

您提交资料后，将会收到一笔来自“财付通支付科技有限公司客户备付金”账户的随机金额款项，后续需要通过金额来对账户进行验证。 

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_money.jpg?raw=true)

### 第四步：验证账户

您可以使用开户邮件中提供的登录账号和登录密码登录商户平台，然后单击【去验证】，在商户平台验证账户页面回填收到的金额，金额正确将会通过验证。
![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_verify_account.jpg)

### 第五步：在线签署协议

账户验证成功后，即可在线签署协议，确认相关信息无误后，单击【确定签署】完成协议签署。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_sign.jpg)

### 第六步：登录腾讯开放平台

首先登录 [腾讯开放平台](http://open.qq.com/)，单击首页右上角的【登录】按钮进行登录。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_open_login.png)

### 第七步：创建 App
 
登录腾讯开放平台后，单击【应用接入】>【应用接入】，

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_new_app_1.png)

接着单击【创建应用】按钮来创建新的应用。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_new_app_2.png?raw=true)
### 第八步：在 QQ 钱包商户平台上添加应用

登录 [QQ 钱包商户平台](https://qpay.qq.com)，单击【账户管理】>【开发配置】，然后单击【上传材料】按钮将之前在腾讯开放平台上创建的 App 添加到商户平台上，添加成功后，会在两个工作日内生效。

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_qq_add_app.png)

### 第九步：配置渠道信息

打开之前在 [MobileLine 平台](https://console.cloud.tencent.com/tac)上创建的应用，单击【我的米大师】>【渠道管理】，然后单击【开通 QQ 钱包支付】：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_new_qq_pay.png)

填入之前申请的 QQ 商户号上的商户号和商户号密钥，腾讯开放平台上审核通过的应用 AppID 和 AppKey 然后点击【确认】。

### 第十步：设置支付参数

点击【我的米大师】>【参数配置】，单击【修改】：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_confirm_conf2.png?raw=true)


配置好对应的渠道信息、回调地址和平台参数后，单击【保存&预览】：

![](http://tac-android-libs-1253960454.cosgz.myqcloud.com/resources/payment_input_config.png)

到此，您即已经完成了 QQ 支付的配置。

> **注意：**
>其中回调地址是支付完成后服务器回调的地址，而平台参数则是用于鉴定来源的 App 信息，安卓平台下为应用签名和应用包名，iOS 平台下为 Bundle Identifier。 














