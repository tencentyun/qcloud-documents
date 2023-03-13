## 配置文件获取

开发人员从开放平台获取对应App的配置文件，该配置文件是一个json文件，包含该App使用小程序平台的所有信息，将配置文件引入到项目中，并且做为资源设置在打包内容。具体操作，请参见[获取配置文件](https://write.woa.com/document/88668404863496192)。

## 配置信息设置

根据配置文件初始化一下 TMFAppletConfig 对象，并使用 TMFAppletConfig 初始化 TMF 小程序引擎。

参考代码：
``` html
 //配置使用环境
       NSString *filePath = [[NSBundle mainBundle] pathForResource:@"tmf-ios-configurations" ofType:@"json"];
       if(filePath) {
           TMAServerConfig *config  = [[TMAServerConfig alloc] initWithFile:filePath];
           //配置设备id，用于在管理平台上根据设备标识进行小程序的灰度发布使用
        	 config.customizedUDID = @"udid";
           [[TMFMiniAppSDKManager sharedInstance] setConfiguration:config];
       } 
```

## 其它初始化动作

使用者可根据需要，设置开放接口实现实例。如果需要集成扩展模块时，初始化扩展 API 准备。设置地区或者帐号信息，方便进行灰度推送时使用。
``` html
//设置小程序引擎代理类实现，详细参见3.3部分
[TMFMiniAppSDKManager sharedInstance].miniAppSdkDelegate = [MIniAppDemoSDKDelegateImpl sharedInstance];

//设置当前设备的一些属性，方便进行小程序灰度等的操作
[[TMFMiniAppSDKManager sharedInstance] updateAreaInfoWithCountry:@"中国" Province:@"北京市" City:@"朝阳区"];//地区信息
[[TMFMiniAppSDKManager sharedInstance] updateCustomizedUserID:@"zhangsan"];//用户帐号
```

