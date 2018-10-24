## iOS SDK广告监测模块集成指南
### 工程配置
引入 adtracker 文件夹下的 .a 文件和头文件,以及 idfa 文件夹下的 libidfa.a 到 Xcode 工程之中。

### 接口调用
>注意：
>激活后的活跃事件的上报, 请在主线程中调用。

**注册事件 **
通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化

**接口说明**

```
 (void)trackRegAccountEvent:(MTAADAccountType)accountType account:(NSString *)account
```
 
**参数说明**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|accountType|	是|	账号类型|
|account|	是	|具体的账号|
**付费事件 **

通过上报付费事件，您可以统计到每一次投放的注册转换率等标准监测指标，也能向渠道回传以获得广告投放优化。

**接口说明**
```
(void)trackUserPayEvent:(MTAADPayMoneyType)moneyType orderID:(NSString *)orderID
                   payNum:(double)payNum
                  payType:(NSString *)payType; 
```

**参数说明**

|参数名	|是否必要|	参数描述|
| :----: | :----: | :----: |
|moneyType|	是	|货币种类，支持两种：人民币、美金|
|orderID	|是|	订单ID， 或交易流水号|
|payNum	|是	|订单金额|
|payType	|是	|支付类型，如微信、支付宝、银联等|

**其他自定义事件**
若您希望上报其他自定义的用户行为，您可以参考MTA自定义事件： [自定义事件介绍](/document/product/549/13057) | [Android接口](/document/product/549/13066) | [iOS接口](/document/product/549/13067)