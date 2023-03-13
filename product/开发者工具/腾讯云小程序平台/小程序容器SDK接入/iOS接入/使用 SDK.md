## 调试

### 配置说明
- 在 TMFApple t初始化时设置小程序的日志输出级别，可以在终端控制台中查看到小程序的调试日志，方便定位问题。


   `#if DEBUG`


   `    [TMFAppletManager setLogLevels:TMFAppletLogLevelAll];`


   `#else`


   `    [TMFAppletManager setLogLevels:TMFAppletLogLevelNone];`


   `#endif`
   

   > **注意：**日志打印建议仅在 DEBUG 环境中进行，发布版本不要输出小程序的相关日志。
   > 

- Xcode 控制台中添加 Filter：TMFApplet。![image-20190911144940551](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/b9d4c3654ec011ed902d525400463ef7.png?q-sign-algorithm=sha1&q-ak=AKIDmXPKwSfpdWFEcOU_8lhgCPt8UBN2hQbTGfG7sdG21jxZPXq6XFUrd5oG7-4Q1x8M&q-sign-time=1678688923;1678692523&q-key-time=1678688923;1678692523&q-header-list=&q-url-param-list=&q-signature=92a0a9b515808378a91801a51b5372d72c672c89&x-cos-security-token=BR3002b2U42565JB60a8L0hq41GHy34af87faae95b5df2d7f2c038dc1d23bcadG8tPB46LUesAR5gr3Dui3tsJpPjuW6kDgcPb6lTiZlUFdWHj8ocYfTj9Qd9uR3nf5omn9o1dyqwtHwGlZtbxbyWTqMmhJf0e5wcTNliUeQthz1pSr55rlymLw5oIgWqhoyilssS_qxNUdjpm_DluMg20su2mU5zRJ82fhwRrzAhDPtp-3iMCwAYoxBrKf3KImwlHctUa-tVP11wfp1ZGxtEgTkJhfHX2iPbkBLxqokRJeheqUw-cQBync0oCLp51SScsArZoEdKcJuz1sEkrcrByX3ZFwuIxh-YpJVBn_QhW_p0UehOdij_DG0u32Hs1OLR3I2UBmBviFq8kV_Mcmz9PxnLt3d5VUt1xEl5vGsjSs4DynOTGG3OxJg6Xw3l_)

- App 中调用小程序的相关接口，在控制台中观察的相关日志输出。


### 日志级别说明

#### 日志分为 Debug、Info、Warn、Error 四个级别
``` html
/**
 @brief 日志级别
 */
typedef NS_OPTIONS(NSInteger, TMFAppletLogLevels) {
    TMFAppletLogLevelNone    = 0,            ///< 无日志
    TMFAppletLogLevelDebug   = 1,            ///< 调试帮助日志
    TMFAppletLogLevelInfo    = 1 << 1,       ///< 运行过程关键日志
    TMFAppletLogLevelWarn    = 1 << 2,       ///< 存在潜在问题日志
    TMFAppletLogLevelError   = 1 << 3,       ///< 严重错误导致系统退出日志
    TMFAppletLogLevelAll     = 0xFFFF,       ///< 全部日志
};
```

可根据日志级别在 setLogLevels 中灵活控制日志输出。比如，想输出 Debug 和 Info 的日志，可参考下面的设置：
``` html
#ifdef DEBUG
   [TMFAppletManager setLogLevels:TMFAppletLogLevelDebug|TMFAppletLogLevelInfo];
#endif
```

## SDK 初始化

### 配置文件获取

开发人员从开放平台获取对应 App 的配置文件，该配置文件是一个 json 文件，包含该 App 使用小程序平台的所有信息，将配置文件引入到项目中，并且做为资源设置在打包内容。

### 配置信息设置

根据配置文件初始化一下 TMFAppletConfig 对象，并使用 TMFAppletConfig 初始化 TMF 小程序引擎。参考如下：
``` html
//配置使用环境
NSString *filePath = [[NSBundle mainBundle] pathForResource:@"TMFConfigurations.json" ofType:nil];
if(filePath) {
    TMFAppletConfig *config  = [[TMFAppletConfig alloc] initWithFile:filePath];
    //配置设备id，用于在管理平台上根据设备标识进行小程序的灰度发布使用
    config.customizedUDID = @"udid";
    [[TMFAppletManager sharedInstance] updateConfiguration:config];
}
```

### 其他初始化动作

使用者可根据需要，设置开放接口实现实例。如果需要集成扩展模块时，初始化扩展 API 准备，设置地区或者帐号信息，方便进行灰度推送时使用。
``` html
 //重载部分可在宿主实现的api
  [[TMFAppletManager sharedInstance] setClient:[TMFAppletEmbedder new]];
  
//准备扩展api
  [[TMFAppletExtClient sharedClient] prepareExtensionApis];
      
  //设置当前设备的一些属性，方便进行小程序灰度等的操作
  [[TMFAppletManager sharedInstance] updateAreaInfoWithCountry:@"中国" Province:@"北京市" City:@"朝阳区"];//地区信息
  [[TMFAppletManager sharedInstance] updateCustomizedUserID:@"zhangsan"];//用户帐号
```

## 小程序管理 API

### 打开小程序
- **打开普通小程序**


   打开小程序时，会先判断本地是否有缓存的小程序，如果没有，则会自动从远程服务器上下载小程序，然后打开。如果有缓存的小程序，则会先打开本地小程序，然后在后台校验服务器端是否有新版本。


   如果有新版本，则下载新版小程序，下次打开时，就会使用新版小程序。如果没有新版本，则仍使用原版本。


   打开时也可能通过指定参数，强制进行小程序检查更新，当有更新时就用新的版本，如果无新版本时使用本地缓存的版本。

   ``` html
   /// 打开指定小程序
   /// @param appId 启动的request
   /// @param parentVC 父页面
   - (void)launchAppplet:(NSString*)appId inParentViewController:(UIViewController *)parentVC;
   
   /// 打开指定小程序
   /// @param options 启动的参数
   /// @param parentVC 父页面
   - (void)launchWithOptions:(NSDictionary*)options inParentViewController:(UIViewController *)parentVC;
   ```

   options 支持的参数列表：

<table>
<tr>
<td rowspan="1" colSpan="1" >名称<br></td>

<td rowspan="1" colSpan="1" >必须</td>

<td rowspan="1" colSpan="1" >类型</td>

<td rowspan="1" colSpan="1" >作用</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" ><br>appId<br></td>

<td rowspan="1" colSpan="1" ><br>YES<br></td>

<td rowspan="1" colSpan="1" ><br>字符串<br></td>

<td rowspan="1" colSpan="1" ><br>指定打开小程序的小程序 id<br></td>
</tr>

<tr>
<td rowspan="1" colSpan="1" ><br>ignorebuiltin<br></td>

<td rowspan="1" colSpan="1" ><br>NO<br></td>

<td rowspan="1" colSpan="1" ><br>数值<br></td>

<td rowspan="1" colSpan="1" ><br>是否打开小程序时强制进行更新检查，设置任意值时即检查，不设置时走默认打开逻辑<br></td>
</tr>
</table>

- **打开二维码小程序**


   TMF 支持两种模式打开二维码小程序：

  - **打开指定二维码小程序**：支持直接调用二维码小程序接口打开。

  - **解析二维码小程序**：调用者判断当前二维码是否支持解析，如支持返回解析内容，则可调用标准打开二维码小程序。

      ``` html
      /// 打开指定二维码小程序
      /// @param qrData 二维码数据
      /// @param parentVC 父页面
      /// @return BOOL 结果，可正常处理二维码返回YES
      - (BOOL)launchAppletWithQrCode:(NSString *)qrData inParentViewController:(UIViewController *)parentVC;
      
      /// 解析二维码小程序
      /// @param qrData 二维码数据
      /// @return NSDictionary 结果，正常二维码返回识别结果，使用这个结果可直接使用launchWithOptions打开，不支持二维码返回nil
      - (NSDictionary *)checkAppletWithQrCode:(NSString *)qrData;
      ```

### 关闭小程序
``` html
///关闭当前的小程序
///@param animated 是否显示动画
- (void)closeCurrentApplet:(BOOL)animated;
```

### 结束小程序

小程序被关闭后，并没有真的结束，而是在后台挂起。2分钟内再次打开小程序时，会立即将小程序切换至前台运行。 所以，如果我们希望小程序关闭后，立刻被结束掉，可以根据实际情况调用以下 API 来结束单个小程序。
``` html
///删除内存中的某个小程序
///@param appId 小程序id
- (void)clearMemeryApplet:(NSString *)appId;
```

### 删除小程序

由于小程序的运行，会将小程序包和小程序信息缓存在本地，以后打开时速度会非常快。如果想要将小程序的所有信息都删除，那么可以调用以下 API 删除某个小程序或者删除所有小程序。
``` html
///从本地缓存中删除小程序
///@param appId 小程序id
///@return BOOL 结果
- (BOOL)removeAppletFromLocal:(NSString *)appId;


///清空本地缓存的小程序信息
- (void)clearLocalApplets;
```

### 获取小程序信息

#### 获取当前正在运行的小程序信息
``` html
/// 获取当前正在运行的小程序对象
/// @return TMFAppletInfo 小程序信息
- (TMFAppletInfo *)currentApplet;
```

#### 获取本地缓存的所有小程序信息
``` html
///获取本地缓存的所有小程序信息
///@return 小程序数组<TMFAppletInfo>
- (NSArray *)getAppletsFromLocalCache;
```

#### 获取本地缓存的指定小程序信息
``` html
/// 获取本地的小程序信息
///@return 小程序信息<TMFAppletInfo>
- (TMFAppletInfo *)getAppletInfoFromLocalCache:(NSString *)appId;
```

### 打开二维码小程序

根据识别到二维码内容，打开小程序，包括公共发布小程序、预览调试小程序、管制台配置链接等。
``` html
/// 打开指定二维码小程序
/// @param qrData 二维码数据
/// @param parentVC 父页面
/// @return BOOL 结果，可正常处理二维码返回YES
- (BOOL)launchAppletWithQrCode:(NSString *)qrData inParentViewController:(UIViewController *)parentVC completion:(void (^)(NSError *error))completion;
```

### 搜索小程序

可以根据关键词搜索目前小程序平台上已经发布的小程序列表。
``` html
/// 搜索小程序
/// @param name 搜索名称关键词
/// @param completion 搜索结果
- (void)searchAppletsWithName:(NSString *)name
      completion:(void (^)(NSArray<TMFAppletSearchInfo *> * _Nullable, NSError * _Nullable))completion;
```

## 开放接口处理

TMF 小程序提供一系列的开放接口，可以方便宿主 App 进行定制及使用宿主 App 已有的能力，实现步骤如下：

### 新建类实现 TMFAppletClient 协议
``` html
@interface TMFAppletEmbedder : NSObject <TMFAppletClient>
@end
```

### 实现 TMFAppletClient 中想要宿主实现的接口
``` html
@implementation TMFAppletEmbedder

- (void)onClose:(NSString *)appId {
    NSLog(@"TMFApplet id:%@ onClose",appId);
    [[TMFAppletManager sharedInstance] clearMemeryApplet:appId];
}

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
@end
```

### 通过小程序管理类设置进小程序引擎
``` html
[[TMFAppletManager sharedInstance] setClient:[TMFAppletEmbedder new]];
```

### 目前已经支持可扩展的接口列表

#### 开放接口列表

本部分内容需要宿主 App 实现后才可以正常使用
``` html
- (void)onAuthorizeWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onLoginWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onOpenSettingWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onGetSettingWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onRequestPaymentWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onGetUserInfoWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
```

#### ui 相关元素

本部分内容，在 TMF 小程序引擎中已经有默认实现，宿主 App 可以可以根据自己的需要重新实现覆盖原默认实现。
``` html
//web-view组件可使用宿主自定义的webview
- (WKWebView*)onCreateWebView;
//自定义loadingview视图
- (UIView*)onCreateLoadingView;
//自定义胶囊视图
- (UIView*)onCreateCapsuleView;
//自定义胶囊视图样式
- (void)onSetCapsuleViewStyleWithView:(UIView*)view withStyle:(NSString*)style;
//右上角更多按钮点击事件
- (void)onShowMenu:(NSString *)appId;

- (void)onShowToastWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onHideToastWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onShowLoadingWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onHideLoadingWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onShowModalWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
```

#### 媒体相关内容

本部分内容，小程序引擎或者扩展引擎中有默认实现，宿主 App 可以根据自己的需要重新实现。
``` html
- (void)onScanCodeWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onOpenDocumentWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onOpenLocationWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onChooseLocationWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onPreviewImageWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onChooseImageWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onChooseVideoWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
- (void)onChooseMediaWithParams:(NSDictionary*)params inApp:(NSString *)appId callbackHandler:(WebAPICallbackHandler _Nullable)handler;
```

#### 事件通知回调

本部分内容，为小程序生命周期函数中部分事件通知回调，宿主 App 可以在对应的事件发生时添加自己的处理逻辑。
``` html
//小程序切到前台回调
- (void)didShow:(NSString *)appId;
//小程序切到后台回调
- (void)didHide:(NSString *)appId;
//小程序关闭回调
- (void)onClose:(NSString *)appId;
//request发出时回调
- (void)willSendRequest:(NSMutableURLRequest*)request inApp:(NSString *)appId;
```

### 自定义 API 处理

TMF 小程序引擎提供自定义 API 处理，开发者可以自定义 API 实现，在小程序中进行调用，App 中实现方式如下：
``` html
- (BOOL)onInvokeWebAPIWithEvent:(NSString*)event params:(NSDictionary*)params inApp:(NSString *)appId  callbackHandler:(WebAPICallbackHandler _Nullable)handler {
    NSLog(@"onInvokeWebAPIWithEvent, event:%@, params:%@", event, params);
    //具体event对应的处理逻辑，待处理完成后调用hanler返回处理信息，回调内容中，必须包括errMsg字段，成功值为event:ok,失败时为event:fail
    if (handler) {
        handler(@{@"errMsg" : [NSString stringWithFormat:@"%@:ok",event]}, nil);
    }
    return YES;
}
```

## 扩展 SDK

TMF 小程序引擎提供核心模块及扩展模块，方便使用者根据自己的情况进行接入。

### 扩展 SDK 接入及使用

扩展 SDK 是对核心 SDK 的补充，所以要使用扩展 SDK，也必须依赖核心 SDK。 为了保证 SDK 的安全稳定性，将需要权限的 API 尽可能放到扩展 SDK，TMF 小程序引擎将 SDK 拆分为核心 SDK 与扩展 SDK，后者是前者的补充，因此使用扩展 SDK 也必须依赖核心 SDK。

引入模块：

`pod 'TMFAppletExt'`

在小程序引擎初始化后，初始化扩展 SDK：

`[[TMFAppletExtClient sharedClient] prepareExtensionApis];`

### TMFAppletExtMedia

TMFAppletExtMedia 提供 chooseMedia、chooseVideo、chooseImage 三个接口的默认实现，如果宿主 App 已经有对应能力，建议在开放接口中实现，如果需要使用 TMF 提供的多媒体选择插件，需要使用该插件。

使用方式：
``` html
pod 'TZImagePickerController'
pod 'TMFApplet'
pod 'TMFAppletExt'
pod 'TMFAppletExtScanCode'
```

### 地图相关扩展

TMF 小程序提供地图需要依赖第三方地图 SDK 实现，包括 openLocation、choosePoi、chooseLocation 及 map 组件能力。

目前小程序扩展组件提供接入腾讯地图提供相应的能力，需要开发者自行去腾讯地图开发者官网注册提供相就信息。

引入方式：
``` html
pod 'TMFApplet'
pod 'TMFAppletExt'
pod 'TMFAppletQMap'
```

使用方式需要初始化设置腾讯地图申请的相关的当前 App 对应的 AppKey 信息：

`[TMFAppletQMapComponent setQMapApiKey:MAP_QQ_KEY];`







