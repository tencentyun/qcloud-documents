TMF 小程序引擎提供扩展机制允许宿主 App 自定义 API 供小程序调用，具体实现步骤如下：
1. 自定义类。

2. 类实现中引入头文件 #import "TMAExternalJSPlugin.h"。

3. 注册 api。


   参考用例：

   ``` html
   #import "NativePluginTest.h"
   #import "TMAExternalJSPlugin.h"
   #import "TMFMiniAppInfo.h"
   
   @implementation NativePluginTest
   
   TMA_REGISTER_EXTENAL_JSPLUGIN;
   
   //自定义api demo，使用External JSAPI
   TMAExternalJSAPI_IMP(test) {
       TMFMiniAppInfo *appInfo = context.tmfAppInfo;
       NSDictionary *data = params[@"data"];
       
       NSLog(@"************ invokeNativePlugin test,appId:%@,data is %@",appInfo.appId, data);
   
       TMAExternalJSPluginResult *pluginResult = [TMAExternalJSPluginResult new];
       pluginResult.result = @{};
       [context doCallback:pluginResult];
       return pluginResult;
   }
   
   @end
   ```
4. 小程序中使用。

   ``` html
   wx.invokeNativePlugin({'api_name':'test','data':'this is a test data'})
   ```

