# invokeNativePlugin

TMF小程序sdk提供接口，可实现一些开放平台api 可以直接透传给宿主App来实现，如登录，获取用户信息等；一些宿主App可以扩展，以保持ui和功能等一致性的，如扫码，分享等；也可以扩展自定义api，进行透传宿主App来实现。

## 小程序端使用方式

```javascript
 var opts = {
   api_name: '', // api名称
   success: function(res) {},
   fail: function(res) {},
   complete: function(res) {},
   data: { // 入参
      name : 'kka',
      age : 22,
      data: {...}
   }
 }
 wx.invokeNativePlugin(opts); // 调用
```

## 终端使用方式

### Android

使用方式，请参见[Android接入文档](../../../sdk-integrate/access-android.md#334-自定义jsapi)

### iOS

TMFAppletClient负责实现 TMF小程序委托接口并监听状态变化，宿主App可以实现相应接口来完成对应功能。

使用方式，请参见[iOS接入文档](../../../sdk-integrate/access-ios.md#35-自定义api处理)

#### Methods

**View onCreateLoadingView()**

```

创建加载视图，允许宿主呈现小程序/小游戏品牌和自定义显示样式，如返回空则展示默认加载视图

```
**View onCreateCapsuleView()**

```

创建胶囊按钮，允许宿主自定义胶囊按钮样式，如返回空则展示默认胶囊按钮

```
**boolean onShowMenu()**

```

点击 “...” 更多按钮时触发，如果 onCreateCapsuleView 返回空且 onShowMenu 返回 false 则显示默认菜单


```
**void onExit()**

```

点击 “〇” 退出按钮时触发，如果 onCreateCapsuleView 返回空且 onExit 返回 false 则执行默认操作


```
**boolean onAuthorize(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.authorize 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onOpenSetting(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.openSetting 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onGetSetting(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.getSetting 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onLogin(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.login 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onRefreshSession(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.checkSession 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onRequestPayment(JSONObject params, ValueCallback<JSONObject> callback)**

```

wx.requestPayment 接口实现，如返回 false 则直接通知 wx api 调用失败


```
**boolean onGetUserInfo(JSONObject params, ValueCallback<JSONObject> callback)**

```objective-c
wx.getUserInfo 接口实现，如返回 false 则直接通知 wx api 调用失败。


```

```objective-c
-(void)onGetUserInfoWithParams:(NSDictionary *)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler)handler {
    //TODO
        NSDictionary* userInfo = @{
                                   @"nickname" : @"morven",
                                   @"headimgurl" : @"https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKav1ib8qG43xy0resTpgfeCqH00vRpHicEdk0kKMxqTMMUG1WmBuAdgB2tmCf6joGVKlGbsicelhluw/0",
                                   @"sex" : @(1),
                                   @"province" : @"广东",
                                   @"city" : @"深圳",
                                   @"country" : @"中国"
                                   };
        NSMutableDictionary* result = [NSMutableDictionary dictionaryWithCapacity:1];
        NSMutableDictionary* userInfoDic = [NSMutableDictionary dictionaryWithCapacity:6];
        NSMutableDictionary* resultDataDic = [NSMutableDictionary dictionaryWithCapacity:1];
        [userInfoDic setValue:userInfo[@"nickname"] forKey:@"nickName"];
        [userInfoDic setValue:userInfo[@"headimgurl"] forKey:@"avatarUrl"];
        [userInfoDic setValue:userInfo[@"sex"] forKey:@"gender"];
        [userInfoDic setValue:userInfo[@"province"] forKey:@"province"];
        [userInfoDic setValue:userInfo[@"city"] forKey:@"city"];
        [userInfoDic setValue:userInfo[@"country"] forKey:@"country"];
    
        NSData *data=[NSJSONSerialization dataWithJSONObject:userInfoDic options:NSJSONWritingPrettyPrinted error:nil];
    
        [resultDataDic setValue:[[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding] forKey:@"data"];
        [result setValue:resultDataDic forKey:@"data"];
        [result setValue:@"getUserInfo:ok" forKey:@"errMsg"];
        
    if (handler) {
        //success
        handler(result, nil);
    }
}
```



**boolean onShareAppMessage(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.shareAppMessage 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onNavigateToMiniProgram(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.navigateToMiniProgram 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onScanCode(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.scanCode 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onOpenDocument(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.openDocument 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onOpenLocation(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.openLocation 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onChooseLocation(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.chooseLocation 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onPreviewImage(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.rviewImage 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onChooseImage(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.chooseImage 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onChooseVideo(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.chooseVideo 接口实现，如返回 false 则直接通知 wx api 调用失败


```

**boolean onShowToast(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.showToast 和 wx.showLoading 接口实现，如返回 false 则使用默认样式展示


```

**boolean onHideToast(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.hideToast 和 wx.hideLoading 接口实现，如返回 false 则使用默认样式展示


```

**boolean onShowModal(JSONObject params, ValueCallback<JSONObject> callback)**

```
wx.showModal 接口实现，如返回 false 则使用默认样式展示


```

**boolean onLaunchApp(JSONObject params, ValueCallback<JSONObject> callback)**

```
实现自定义 wx msLaunchApp，通知拉起三方 app，如返回 false 则直接通知 wx api 调用失败 ，返回 true，需要 client 端实现 相应的功能，建议异步回调，具体用法可以参考 demo 代码
```

**boolean onInvokeWebAPI(String event, JSONObject params, ValueCallback<JSONObject> callback)**

```
实现自定义 wx api，如返回 false 则直接通知 wx api 调用失败


```

```objective-c
- (BOOL)onInvokeWebAPIWithEvent:(NSString*)event params:(NSDictionary*)params callbackHandler:(WebAPICallbackHandler _Nullable)handler {
    NSLog(@"onInvokeWebAPIWithEvent, event:%@, params:%@", event, params);
    if (handler) {
        handler(@{@"errMsg" : @"onInvokeWebAPIWithEvent"}, nil);
    }
    return YES;
}
```

**boolean onReportEvent(String event, Map<String, String> params)**

```
事件上报，事件如下:
 1 启动小程序，event:MS_EVENT_LAUNCH，params 的 key:pagePath,d;
 2 小程序使用时长，event:MS_EVENT_USE_TIME，params 的 key:useTime, startId, appId，useTime 的单位是毫秒; 3 成功启动小程序，event:MS_EVENT_LAUNCH_SUCCESS，params 的 key:appId
 4 打开小程序内的页面，event:MS_EVENT_OPEN_PAGE，params 的 key:pagePath, appId
 5 启动小程序失败，event:MS_EVENT_LAUNCH_FAIL，params 的 key:pagePath, reason, appId
```

