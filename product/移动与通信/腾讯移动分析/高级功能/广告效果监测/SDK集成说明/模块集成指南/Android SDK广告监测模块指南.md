## Android SDK广告监测模块集成指南
### 接口调用

**注册事件**
通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化。

**接口说明：**
```
tatService.trackRegAccountEvent(Context context,String user ，AccountType type);
```
**参数说明：**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|context	|是	|当前上下文
|user|	是	|用户名，最多64个字符|
|type|	是	|目前支持手机号(" mobile ")、邮箱(" mail ")、微信ID(" WX")、QQ号("QQ").<br> 如：StatConfig.AccountType.WX

**付费事件**
通过上报付费事件，您可以统计到每一次投放的LTV值从而衡量您的投资回报率。

**接口说明：**
```
StatService.trackPayEvent(Context context, String cy, String id, double money, CurrencyType type);
```
**参数说明：**

|参数名|	是否必要	|参数描述|
| :-----: | :------: | :--------:|
|context	|是	|当前上下文|
|cy	|是	|支付方式（最多64个字符）.如（"wx"、"Alipay"）等|
|id	|是	|订单号等（最多64个字符）.如（"88888999955542"）等|
|money	|是|	金额.如（88.8）|
|type|	是	|目前支持两种：CNY人民币("CNY")、USD美金("USD")。如StatConfig.CurrencyType.CNY|

**其他自定义事件**
若您希望上报其他自定义的用户行为，您可以参考MTA自定义事件： [自定义事件介绍](/document/product/549/13057) | [Android接口](/document/product/549/13066) | [iOS接口](/document/product/549/13067)