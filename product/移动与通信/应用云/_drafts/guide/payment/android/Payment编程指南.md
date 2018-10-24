## 手动集成 SDK

如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包
 
- 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip) 并解压。
- 下载 [移动开发平台（MobileLine） Payment 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-payment-1.0.0.zip) 并解压。
                             
### 2. 集成 jar 包

将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。资源文件中只包含了微信支付渠道的 jar 包，如果您需要同时接入 QQ 支付，那么必须将 [mqqopenpay.jar](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/mqqopenpay.jar) 也添加到您工程的 `libs` 目录。

### 3. 集成 资源文件
 
- 将Payment 资源包中的 `assets` 目录下的文件拷贝到您工程的 `assets` 目录下
- 将Payment 资源包中的 `res` 目录下的所有文件拷贝到您工程的 `res` 目录下，注意 `values.xml` 需要和您原来的字符串文件合并。

### 4. 修改 AndroidManifest.xml 文件

首先添加如下 `permission` 声明：

```
<!-- 必选权限 -->
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.GET_TASKS"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

<!-- 可选权限 -->
<uses-permission android:name="android.permission.CHANGE_WIFI_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
```

然后添加如下 `Activity` 声明：

```
<activity
    android:name="com.tencent.openmidas.proxyactivity.APMidasPayProxyActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:configChanges="orientation|keyboardHidden|screenSize"
    android:process=":openMidas"
    android:screenOrientation="portrait"/>
<activity
    android:name="com.tencent.openmidas.wx.APMidasWXPayActivity"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
android:process=":openMidas"
android:exported="true" />
<activity
    android:name="com.tencent.openmidas.qq.APMidasQQWalletActivity"
    android:launchMode="singleTop"
    android:theme="@android:style/Theme.Translucent.NoTitleBar"
    android:configChanges="orientation|keyboardHidden"
    android:process=":openMidas"
    android:exported="true" >
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.BROWSABLE"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <data android:scheme="qwallet100703379"/>
    </intent-filter>
</activity>
```

## 集成 QQ 支付

无论您是采用 gradle 远程依赖还是手动集成的方式来接入 Payment 服务，如果您需要接入 QQ 支付，那么您都必须手动添加 [mqqopenpay.jar](http://tac-android-libs-1253960454.cosgz.myqcloud.com/jars/mqqopenpay.jar) 到您工程的 `libs` 目录。

> ** 注意：**
> 因为 `mqqopenpay.jar` 没有上传到 jcenter 仓库下，因此在 gradle 远程依赖的方式下我们暂时无法自动帮您添加。

## 商品下单

在您发起支付前，需要先在后台调用我们的 [下单接口](https://cloud.tencent.com/document/product/666/14600) 进行下单，下单成功后，服务器会给您返回本次下单的具体信息，下单服务器返回的数据示例如下：

```
{
    "ret" : 0,
    "transaction_id" : "E-180202180100144947",
    "out_trade_no" : "open_1517568769743",
    "pay_info" :"data=%7B%22appid%22%3A%22TC100008%22%2C%22user_id%22%3A%22rickenwang%22%2C%22out_trade_no%22%3A%22open_1517568769743%22%2C%22product_id%22%3A%22product_test%22%2C%22pay_method%22%3A%22wechat%22%7D&sign=PplSFOrimAfU1dobsFvva09limmtk%2BIr9D5dxFwwV%2BEdjq9dROhB6fwx9hwf1H27FMT83qQdlSgHtLo52Rv97MoL7nR5xNJFph9G7Gd2KRmgJFQ2IlGfHVE%2BeekjPhRQCELt5MMbDuSEOOGJN4agMiCs9yOXJbusCYAa68bcZTOnGgfDOsbpNvpsQt9JA%2BQ%2FAVDyymXv0f6e%2BibpXlTy3Fu3lQZKzPUiiojl97Kpi4I0J6CGCWsxRp4XqWSF7k90o1NMOcbUnzJ87MSCXq5NA1iynYxrD5Cc5KusJxpy84udTtD9XzdznXpO%2BQJBoO2v0RzGGgT2OJQfgRLqsNNgzw%3D%3D"
}
```
我们强烈建议您在自己的后台服务器上下单，然后由服务器给终端返回下单信息，直接在终端进行下单操作可能会泄漏您的密钥信息。

## 初始化支付请求

每次发起支付前，您必须先初始化一个 ```PaymentRequest``` 支付请求对象。

**支付请求 ```PaymentRequest```**

参数名称 | 参数描述 | 类型 | 备注
---- | --- | ---- | ----
userId | 发起支付的 userId | String  | 最好和下单时的 user_id 保持一致
payInfo | 支付信息 |  String | 下单接口返回的 pay_info 字段

每次初始化支付请求都必须先进行下单获取支付信息，同一个支付信息不可以多次使用，初始化示例代码如下：

```
// 1、向您自己的服务器请求下单信息，也即下单服务器返回的 pay_info 字段。
//   请您自己根据实际情况自己设计和实现 getPayInfoFromServer() 方法
String payInfo = getPayInfoFromServer();

// 2、初始化 PaymentRequest 实例
String userId = "tencent";
PaymentRequest paymentRequest = new PaymentRequest(userId, payInfo);

```

## 发起支付请求

初始化好支付请求 ```paymentRequest``` 后，您就可以通过 ```TACPaymentService``` 实例来发起支付请求了，具体示例代码如下：

```
// 1、获取 TACPaymentService 实例
TACPaymentService paymentService = TACPaymentService.getInstance();

// 2、通过 TACPaymentService 实例发起支付
paymentService.launchPayment(context, paymentRequest, new TACPaymentCallback() {
    @Override
    public void onResult(int resultCode, PaymentResult paymentResult) {
    
        // 支付码 resultCode
        // 支付结果 paymentResult
    }
});

```

## 返回支付结果

在您发起支付后，SDK 会最终给您返回流程错误码 ```resultCode``` 和支付结果 ```PaymentResult```。

**流程错误码```resultCode```**

错误码名称 | 值 | 描述
---- | --- | ----
PAYRESULT_SUCC | 0 | 支付流程成功
PAYRESULT_ERROR |  -1 | 支付流程失败
PAYRESULT_CANCEL | -2 | 用户取消
PAYRESULT_PARAMERROR | -3 | 参数错误
PAYRESULT_UNKNOWN | -4 | 支付流程结果未知

**支付结果 ```PaymentResult```**

参数名称 | 参数描述 | 类型
---- | --- | ----
code | 内部错误码 | String 
message | 错误信息 |  String 
metaData  | 自定义拓展信息 | Map\<String, String\> 


## 添加自定义信息

在发起支付时，您可以添加自定义信息。

```
String key = "name";
String value = "xiaoming";
paymentRequest.addMetaData(key, value);

// other code
   ...

```

该次支付结束后，回调中 PaymentResult 对象会携带您添加的自定义信息。

```
public void onResult(int resultCode, PaymentResult result) {
	
    Map<String, String> metaData = result.getMetaData();
}
```
