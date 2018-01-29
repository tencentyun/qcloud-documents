# 应用云 Payment 服务 Android 接入指南


## 发起支付

集成好 payment 服务后，您只需要三步即可发起支付流程，具体代码如下：

```
// 1、获取 TACPaymentService 实例
TACPaymentService paymentService = TACPaymentService.getInstance();

// 2、初始化 PaymentRequest 实例
String userId = "xiaoming";
String payInfo = "你需要后台调用下单接口来获取支付信息，终端不直接下单";

PaymentRequest paymentRequest = new PaymentRequest(userId, payInfo);

// 3、通过 TACPaymentService 实例发起支付
paymentService.launchPayment(context, paymentRequest, new TACPaymentCallback() {
    @Override
    public void onResult(int resultCode, PaymentResult result) {}
});

```

## 添加自定义信息

在发起支付时，您可以添加自定义信息。

```
String key = "name";
String value = "xiaoming";
paymentRequest.addMetaData(key, value);

```

该次支付结束后，回调中 PaymentResult 对象会携带您添加的自定义信息。

```
public void onResult(int resultCode, PaymentResult result) {
	
    Map<String, String> metaData = result.getMetaData();
}
```
