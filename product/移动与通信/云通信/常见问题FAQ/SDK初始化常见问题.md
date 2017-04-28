## crash上报
云通信SDK默认使用bugly做crash上报，如果App已经集成了Crash上报，则可以不使用该功能，通过调用接口禁用掉，并可以去除相应的jar包和framework
iOS
```
[[TIMManager sharedInstance] disableCrashReport];
```
Android
```
TIMManager.getInstance().disableCrashReport();
```

## 关闭imsdklog、avsdklog
imsdklog可立即关闭，avsdklog需要app重新启动后关闭
Android
```
TIMManager.getInstance().setLogLevel
```
iOS
```
[[TIMManager sharedInstance] setLogLevel];
```
Web
```
webim.Log.setOn(0);
```
## 1.7升级1.8出现异常

> E/imsdk.IMMsfCoreProxy: [E]OnExchangeTicketTimeout|code: -1000 desc: 请求失败，请你稍后重试。
E/beacon: ChannelID: unknown
login imserver failed. code: 6012 errmsg: operation timeout: wait server rsp timeout or no network.

请按照ReadMe.txt中增加Manifest相应的配置，新版本增加了离线推送模块，必须增加设置

## 出现6013 SDK未初始化错误
1.查看是否没有登录成功，就进行收发消息等其他操作
2.查看是否登录时被其它终端踢掉，IMSDK默认一个账号仅能在一个终端上登录。处理方式请参考[互踢逻辑](/doc/product/269/初始化（Android%20SDK）#5-.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4.EF.BC.88.E4.BA.92.E8.B8.A2.EF.BC.89)
3.Android请关注库文件是否未能全部加载，或是使用过程中被系统回收

## 互踢
云通信默认情况下，一个账号不可以在多台手机上登陆，会出现互踢
详细逻辑可见[这里](/doc/product/269/初始化（Android%20SDK）#5-.E7.94.A8.E6.88.B7.E7.8A.B6.E6.80.81.E5.8F.98.E6.9B.B4.EF.BC.88.E4.BA.92.E8.B8.A2.EF.BC.89)

## 多终端同时在线
云通信允许多终端同时在线（和QQ的逻辑保持一致），有几种模式可以选择
1.完全不互踢，每个终端都可以登录同一个账号
2.手机之间互踢，pc之间互踢，手机和pc可同时在线，即最多两个终端在线（一个手机，一个PC）
3.不同类型手机可以同时在线，相同终端类型手机互踢，手机和PC可同时在线，即最多允许3个终端在线（一个Android、一个iOS、一个PC）
4.所有终端互踢，仅允许一个设备在线
如果需要多终端同时在线，需要提工单或在群里咨询技术支持人员，该功能需要付费试用

## 日志路径
Android：tencent/imsdklogs/com(cn)/公司包名/imsdk_YYYYMMDD.log
iOS：Library/Caches/imsdk_YYYYMMDD.log