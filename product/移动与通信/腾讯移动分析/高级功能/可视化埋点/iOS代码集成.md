### 接入方法

1.将 libautotrack.a 链接到工程中，如下图：
![](//mc.qcloudimg.com/static/img/a82f1d8517e113a7a68f82ff250af175/image.png)

2.前往 MTA 前台的应用配置页面查看可视化埋点标识符。
![](//mc.qcloudimg.com/static/img/b0ea1ff9b407d1a0fbc239f8991dd2ee/image.png)

3.在工程配中添加 URL Types。
```
Identifier: <随意填写>
URL Schemes: 第二步中的标识符
Role: <默认值>
```
![](//mc.qcloudimg.com/static/img/1644996d749edcc04ac9a71bb04768ce/image.jpg)

4.参考 MTADemo，在 AppDelegate 的方法中添加初始化可视化埋点的代码。

```
- (BOOL)application:(UIApplication *)app
    openURL:(NSURL *)url
    options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options;
```

```
- (BOOL)application:(UIApplication *)app
    openURL:(NSURL *)url
    options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {

    // 可视化埋点代码
    if ([MTAAutoTrack handleAutoTrackURL:url])
        return YES;


    // 原有代码
    // ...
    return NO;
}
```

5.前往腾讯 [移动分析官网](http://mta.qq.com)，进入对应应用，在左侧进入可视化埋点分析页面，按照网页提示进行操作，如图所示：
![](//mc.qcloudimg.com/static/img/c5eb897666304713f6dd4d96e64ce464/image.png)