### Access Methods

1. Link libautotrack.a to the project as shown below:
![](//mc.qcloudimg.com/static/img/a82f1d8517e113a7a68f82ff250af175/image.png)

2. Go to the App configuration page of MTA frontend to view the visualized event tracking identifier.
![](//mc.qcloudimg.com/static/img/b0ea1ff9b407d1a0fbc239f8991dd2ee/image.png)

3. Add URL Types in the project configuration.
```
Identifier: <Anything>
URL Schemes: The identifier in step 2
Role: <Default>
```
![](//mc.qcloudimg.com/static/img/1644996d749edcc04ac9a71bb04768ce/image.jpg)

4. Refer to MTADemo to add the codes for visualized event tracking initialization in the AppDelegate method.

```
- (BOOL)application:(UIApplication *)app
    openURL:(NSURL *)url
    options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options;
```

```
- (BOOL)application:(UIApplication *)app
    openURL:(NSURL *)url
    options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {

    // Visualized event tracking codes
    if ([MTAAutoTrack handleAutoTrackURL:url])
        return YES;


    // Original codes
    // ...
    return NO;
}
```

5. Go to the official site of [Mobile Tencent Analytics](http://mta.qq.com), enter the corresponding App, enter the visualized event tracking analysis page on the left, and then operate by following the web page prompts as shown in the figure below:
![](//mc.qcloudimg.com/static/img/c5eb897666304713f6dd4d96e64ce464/image.png)
