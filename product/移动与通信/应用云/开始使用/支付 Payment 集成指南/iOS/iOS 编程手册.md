## 支付流程

整个支付的流程分为：商品下单>客户端>调起支付>获回支付结果

## 下单

在您发起支付前，需要先在后台调用我们的 [下单接口](https://cloud.tencent.com/document/product/666/14600) 进行下单，下单成功后，服务器会给您返回本次下单的具体信息，下单服务器返回的数据示例如下：

```
{
    "ret" : 0,
    "transaction_id" : "E-180202180100144947",
    "out_trade_no" : "open_1517568769743",
    "pay_info":"data=%7B%22appid%22%3A%22TC100008%22%2C%22user_id%22%3A%22rickenwang%22%2C%22out_trade_no%22%3A%22open_1517568769743%22%2C%22product_id%22%3A%22product_test%22%2C%22pay_method%22%3A%22wechat%22%7D&sign=PplSFOrimAfU1dobsFvva09limmtk%2BIr9D5dxFwwV%2BEdjq9dROhB6fwx9hwf1H27FMT83qQdlSgHtLo52Rv97MoL7nR5xNJFph9G7Gd2KRmgJFQ2IlGfHVE%2BeekjPhRQCELt5MMbDuSEOOGJN4agMiCs9yOXJbusCYAa68bcZTOnGgfDOsbpNvpsQt9JA%2BQ%2FAVDyymXv0f6e%2BibpXlTy3Fu3lQZKzPUiiojl97Kpi4I0J6CGCWsxRp4XqWSF7k90o1NMOcbUnzJ87MSCXq5NA1iynYxrD5Cc5KusJxpy84udTtD9XzdznXpO%2BQJBoO2v0RzGGgT2OJQfgRLqsNNgzw%3D%3D"
}
```
我们强烈建议您在自己的后台服务器上下单，然后由服务器给终端返回下单信息，直接在终端进行下单操作可能会泄漏您的密钥信息。

## 调起支付
对商品完成下单后，会得到一个 pay_info, 对应前面 JSON 中 pay_info 字段的值，pay_info 实质上就是一个字符串，我们可以拿着这个 pay_info 调用 SDK 的接口去直接拉起相应的支付：

Objective-C 代码示例：
~~~
[[TACPaymentService defaultService] pay:payInfo appMeataData:nil completation:^(TACPaymentResult * result) {
    TACLogDebug(@"支付结果 %d %@", result.resultCode, result.resultMsg);
}];
~~~
Swift 代码示例：
~~~
TACPaymentService.default().pay(payInfo, appMeataData: nil) { (result:TACPaymentResult?)->Void in
    print("支付结果  ",result?.resultCode as Any,result?.resultMsg as Any)
}
~~~
## 返回支付结果
支付完成以后，结果会包装在 TACPaymentResult 对象中，在完成回调 block 里以参数传入的形式返回。它包含了如下信息：

属性|类型|描述
----|------|------------
resultCode|TACPaymentErrorCode|支付结果的返回码
payMethod|NSString*|本次支付的方式
innerCode|NSString*|系统内部 Code, 如果出错，则是系统的内部错误码
resultMsg|NSString*|结果信息
appMetadata|NSString*|额外的一些元数据



resultCode 是本次支付返回的错误码，具体有：

返回码名称 | 值 | 描述
---- | --- | ----
TACPaymentCodeSuccess | 0 | 支付流程成功
TACPaymentCodeError |  -1 | 支付流程失败
TACPaymentCodeCancel | -2 | 用户取消
TACPaymentCodeParamterError | -3 | 参数错误
TACPaymentCodeUnkown | -4 | 支付流程结果未知


## 常见问题
* 无法拉起微信支付，请按照以下步骤进行排查：
 - 微信商户号是否已经成功开通。
 - 微信开放平台上，是否已经成功开通支付能力。
 - [控制台](https://console.cloud.tencent.com) 中检查，商户号、商户号密钥是否与微信商户号的一直。AppID， AppKey 是否与微信开放平台上的一致。
 - 检查下单是否成功，pay_info 是否是有效的字符串而不是空。
 - 检查控制台日志中是否有初始化错误，或者错误码等信息。

* 支付完成后无法跳转回应用内
 - 检查 URL Scheme 是否已经设置为微信开放平台上的 APPID（以WX开头）。
 - 若是 QQ 支付，检查 URL Scheme 是否已经设置为 “qqwallet” + id 的形式，例如 qqwallet1234567。
