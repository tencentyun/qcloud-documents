TMF小程序引擎提供核心模块及扩展模块，方便使用者根据自己的情况进行接入。

## 扩展 SDK 接入及使用

扩展 SDK 是对核心 SDK 的补充，所以要使用扩展 SDK，也必须依赖核心 SDK。 为了保证 SDK 的安全稳定性，将需要权限的 API 尽可能放到扩展 SDK，TMF 小程序引擎将 SDK 拆分为核心 SDK 与扩展 SDK，后者是前者的补充，因此使用扩展 SDK 也必须依赖核心 SDK。

## TMFMiniAppExtMedia

TMFAppletExtMedia 提供 chooseMedia，chooseVideo，chooseImage 三个接口的默认实现，如果宿主 App 已经有对应能力，建议在开放接口中实现，如果需要使用 TMF 提供的多媒体选择插件，需要使用该插件。

使用方式：
``` html
pod 'TMFMiniAppSDK'
pod 'TMFMiniAppExtMedia'
```

## TMFMiniAppExtScanCode

TMFMiniAppExtScanCode 提供 wx.scanCode 的处理逻辑，如果宿主 App 本身已经有扫码识别能力，建议通过。

`TMFMiniAppSDKDelegate.scanCode:(NSDictionary *)scanPrams navigationController:(UINavigationController *)navigationController completionHandler:(MACommonCallback)completionHandler;`

对接已经正常使用的扫码模块，如果需要使用 TMF 提供的扫码功能，需要使用该插件。

使用方式：
``` html
pod 'ncnn'
pod 'TMFCodeDetector'
pod 'TMFMiniAppSDK'
pod 'TMFMiniAppExtScanCode'
```

