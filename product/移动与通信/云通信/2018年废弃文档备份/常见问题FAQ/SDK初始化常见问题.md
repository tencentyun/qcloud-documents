## Crash上报

云通信 SDK 默认使用 bugly 做 Crash 上报，如果 App 已经集成了 Crash 上报，则可以不使用该功能，通过调用接口禁用掉，并可以去除相应的 JAR 包和 framework。

iOS：

```
[[TIMManager sharedInstance] disableCrashReport];
```

Android：

```
TIMManager.getInstance().disableCrashReport();
```

## 关闭 imsdklog、avsdklog

imsdklog 可立即关闭，avsdklog 需要 App 重新启动后关闭

Android：

```
TIMManager.getInstance().setLogLevel
```

iOS：

```
[[TIMManager sharedInstance] setLogLevel];
```

Web：

```
webim.Log.setOn(0);
```

## 升级 1.8 出现异常

```
E/imsdk.IMMsfCoreProxy: [E]OnExchangeTicketTimeout|code: -1000 desc: 请求失败，请您稍后重试。
E/beacon: ChannelID: unknown
login imserver failed. code: 6012 errmsg: operation timeout: wait server rsp timeout or no network.
```

请按照 ReadMe.txt 中增加 Manifest 相应的配置，新版本增加了离线推送模块，必须增加设置。

## 出现 6013 SDK 未初始化错误

1.查看是否没有登录成功，就进行收发消息等其他操作。
2.查看是否登录时被其它终端踢掉，IMSDK 默认一个帐号仅能在一个终端上登录。处理方式请参考 [互踢逻辑](/doc/product/269/初始化（Android%20SDK）#.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4.EF.BC.88.E4.BA.92.E8.B8.A2.EF.BC.89)。
3.Android 请关注库文件是否未能全部加载，或是使用过程中被系统回收。

## 互踢

云通信默认情况下，一个帐号不可以在多台手机上登录，会出现互踢，详细逻辑参见 [用户被踢下线通知](/doc/product/269/1559#.E7.94.A8.E6.88.B7.E8.A2.AB.E8.B8.A2.E4.B8.8B.E7.BA.BF.E9.80.9A.E7.9F.A5)。

## 多终端同时在线

云通信允许多终端同时在线（和 QQ 的逻辑保持一致），有几种模式可以选择：
1.完全不互踢，每个终端都可以登录同一个帐号。
2.手机之间互踢，PC 之间互踢，手机和 PC 可同时在线，即最多两个终端在线（一个手机，一个 PC）。
3.不同类型手机可以同时在线，相同终端类型手机互踢，手机和 PC 可同时在线，即最多允许 3 个终端在线（一个Android、一个 iOS、一个 PC）。
4.所有终端互踢，仅允许一个设备在线。

> 如果需要多终端同时在线，需要提工单或在群里咨询技术支持人员，该功能需要付费试用。

## 日志路径

- Android：`tencent/imsdklogs/com(cn)/公司包名/imsdk_YYYYMMDD.log`

- iOS：`Library/Caches/imsdk_YYYYMMDD.log`
