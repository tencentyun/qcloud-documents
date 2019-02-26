您可以通过以下方法主动触发异常，以测试 SDK 是否正常工作，不必花费时间等待应用出现崩溃。

## 调用测试代码产生 Crash

您可以在任意位置调用如下代码产生异常。
>**注意：**
>需要在 Crash 服务启动，也就是进行了配置以后模拟。

```
// 模拟越界访问异常
NSArray* testArray = [NSArray array];
testArray[100];
```

## 在控制台上查看异常是否上报成功

应用 Crash 后，您可以登录 [MobileLine 控制台](https://console.cloud.tencent.com/tac)，单击【异常上报】>【异常分析】，即可查看上报到控制台的异常，如果没有上报，可以查看 [常见问题](https://cloud.tencent.com/document/product/666/14825)

![](https://tacimg-1253960454.cos.ap-guangzhou.myqcloud.com/guides/crash/crash_report.png)
