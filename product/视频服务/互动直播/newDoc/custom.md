## 功能定制

如果您的业务场景非常特殊，翻遍完我们的文档和demo代码，都不能满足需求。<br/>
您可以自己拿到im sdk和avsdk的接口，自由操作信令、群组、音视频接口进行定制。<br/>

* Android

#####获取IM管理器实例

```
TIMManager imManager = ILiveSDK.getTIMManager();
```

查看Android IMSDK接口的详细信息请点击[这里](https://www.qcloud.com/document/product/269/1557)

#####获取AV上下文实例

```
AVContext avContext = ILiveSDK.getAVContext();
```

查看Android AVSDK接口的详细信息请点击[这里](https://www.qcloud.com/document/product/268/3823)

* ios


#####获取IM管理器实例

```
TIMManager *imManager = [[ILiveSDK getInstance] getTIMManager];
```

查看IOS IMSDK接口的详细信息请点击[这里](https://www.qcloud.com/document/product/269/1565)

#####获取AV上下文实例

```
QAVContext *avContext = [[ILiveSDK getInstance] getAVContext];
```

查看IOS AVSDK接口的详细信息请点击[这里](https://www.qcloud.com/document/product/268/3824)


**注意事项：**请在ILiveSDK初始化并登录后再使用以上接口。


## 您是壕不差钱现在就是要快快快上线产品？

抱歉，文档里没有解决方案<br/>
不过，我们给您准备了服务绿色通道，请加QQ：3358225043 （请注明企业名称+互动直播）