
## 配置

在使用 Payment 支付前，您必须先开通支付渠道，然后配置好相关参数，才能成功发起支付请求。

### 开通支付渠道

#### 操作步骤

**1. 进入渠道管理页**

登录 [控制台](https://console.cloud.tencent.com/tac)，然后点击左侧导航【我的米大师】，然后在上方导航栏中点击【渠道管理】。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_1_.png?raw=true)

**2. 填写渠道信息**

进入渠道管理页后，如果您创建的是 Android 应用，那么会看到【开通微信支付】和【开通QQ钱包支付】两个按钮（如下图所示），如果您创建的是 IOS 应用，那么您也会看到 【开通IAP支付】按钮。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_2.png)

接下来，您需要点击【开通微信支付】或者【开通QQ钱包支付】，填写渠道配置信息：

<img src="http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_3_.png" width="50%" height="50%">

填写好渠道信息后，点击【确定】。

#### 相关信息说明

**商户号**

商户号需要在根据您开通的支付渠道在 [微信商户平台](https://pay.weixin.qq.com/index.php/core/home/login) 或者 [QQ 钱包商户平台](https://qpay.qq.com) 上申请，申请的方式请参见 [这里](https://github.com/tencentyun/qcloud-documents/edit/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E5%BA%94%E7%94%A8%E4%BA%91/%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8/%E6%94%AF%E4%BB%98%20Payment%20%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Payment%20%E6%94%AF%E4%BB%98%E6%B8%A0%E9%81%93%E9%85%8D%E7%BD%AE%E6%8C%87%E5%BC%95.md) 。

**商户号密钥**

申请商户号成功后，商户平台会给您生成一个商户号密钥，这是您的机密信息，请不要泄露。

**AppID**

在开通支付前，您需要根据开通的渠道在 [微信开放平台](https://open.weixin.qq.com) 或者 [腾讯开放平台](http://open.qq.com/) 上注册，并创建一个应用，创建好应用后请将其 AppId 拷贝过来，同样可以参见 [这里](https://github.com/tencentyun/qcloud-documents/edit/master/product/%E7%A7%BB%E5%8A%A8%E4%B8%8E%E9%80%9A%E4%BF%A1/%E5%BA%94%E7%94%A8%E4%BA%91/%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8/%E6%94%AF%E4%BB%98%20Payment%20%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Payment%20%E6%94%AF%E4%BB%98%E6%B8%A0%E9%81%93%E9%85%8D%E7%BD%AE%E6%8C%87%E5%BC%95.md)。

**AppKey**

请您将创建好的应用 appKey 一并拷贝过来，这也是您的机密信息，请不要泄露。

### 配置参数

#### 操作步骤

**1. 进入参数配置页**

配置好渠道信息并点击【确认】后，会提示您进入参数配置页，您也可以点击左侧导航栏【我的米大师】，然后选择上侧导航栏中的【参数配置】，然后点击右上角的【修改】来进入参数配置页。

**2. 填写配置信息**

配置项如下：

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_4.png)

填好配置信息后，点击【保存 & 预览】进入下一步。

**3. 发布上线**

如果您所有的参数验证完成，并且准备发布上线，您可以点击【发布上线】按钮发布到线上。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_4_.png)

#### 相关信息说明

**主回调地址**

发布上线后，每次支付成功后，Payment 后台会回调这个地址，通知您的服务器已经支付成功。

**备回调地址**

备用的线上回调地址。

**沙箱回调地址**

在您未发布上线前，Payment 后台的回调地址。

**应用签名**

如果您创建的是 Android 应用，那么需要填入您应用的签名值，这里必须和开放平台上注册应用时的签名值保持一致。您可以用如下示例命令生成应用签名，这里假设您的签名文件 `alias` 为 `androiddebugkey`，签名文件的路径为 `~/.android/debug.keystore`。

`keytool -exportcert -list -v -alias androiddebugkey -keystore ~/.android/debug.keystore`

命令生成的 `SHA1` 值即为您的应用签名。

**应用包名**

如果您创建的是 Android应用，那么需要填入您的包名，这里也必须和开放平台上的包名保持一致。

## 数据查询与分析

### 交易查询

#### 交易详情

点击右侧导航栏中的【交易查询】，然后选择上方导航栏中的【交易详情】，您可以通过支付时间段、支付状态、支付渠道来查询对应的交易信息。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_5_.png)

#### 账单报表

点击右侧导航栏中的【交易查询】，然后选择上方导航栏中的【账单报表】，您可以通过支付时间段、支付状态、支付渠道来查询对应的账单报表。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_6.png)

### 数据分析

#### 查看分析数据

点击右侧导航栏中的【数据分析】，您可以查看所有用户支付数据的分析情况。

![](http://tacimg-1253960454.cosgz.myqcloud.com/guides/payment/console_payment_7.png)

#### 相关信息说明 

|名称|意义|
|:--:|:--|
|支付金额|所有用户支付的总金额数|
|支付笔数|所有用户支付的笔数|
|支付UV|支付的用户总数|
|ARPU|平均每个用户支付的金额数|





