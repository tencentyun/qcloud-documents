## 前提条件
### 准备 AppId
验证码接入前，需要先在 [验证码控制台](https://console.cloud.tencent.com/captcha) 中注册获取 AppId 和 AppSecret。
### SDK 包介绍和运行环境
- 单击 [下载 iOS SDK]()。
- SDK 工具包目录结构说明：
```
.
├── sdk                # TCWebCodesSDK.framework
└── demo            # 示例工程,演示了如何使用TCWebCodesSDK.framework
```
本 SDK 运行环境与项目要求：适用于 iOS8 及以上的系统版本。

## 接入步骤
1. 首先在工程中导入 SDK 库：
```
TCWebCodesSDK.framework
```
2. 在需要加载验证码的地方，引入头文件：
```
#import <TCWebCodesSDK/TCWebCodesBridge.h>
```
3. 接入验证码。
```
/**
@param appid，在验证码接入平台注册申请；
@param callback，为回调函数，验证码验证完成后回调该函数将结果带回
*/
[[TCWebCodesBridge sharedBridge]loadTencentCaptcha:self.view appid:@"***" callback:^(NSDictionary *resultJSON) {
    if(0==[resultJSON[@"ret"] intValue]) {
        /**
        验证成功
        返回内容：
        resultJSON[@"appid"]为回传的业务appid
        resultJSON[@"ticket"]为验证码票据
        resultJSON[@"randstr"]为随机串
        */
    } else {
        /**
        验证失败
        返回内容：
        ret=-1001为验证码js加载错误
        ret=-1002一般为网络错误
        ret=-1为返回票据数据解析错误，业务可根据需要重试处理
        ret的其他返回值，为验证失败，例如用户主动关闭了验证码弹框
        */
    }
}];
```

至此，验证码客户端接入已完成，您可以继续完成 [后台 API 接入]() 。
## API 解析
1. 返回单例。
```
//返回单例
 + (instancetype)sharedBridge;
```
2. 加载 H5 验证码。
```
/**
 @param view，需要加载验证码的视图
 @param appid，业务申请接入验证码时分配的appid
 @param callback，验证码验证结果回调， 成功/失败可以通过 resultJSON[@"ret"] 判断，0为成功，非0为失败
 */
 - (void) loadTencentCaptcha:(UIView*)view appid:(NSString*)appid  callback:(void (^)(NSDictionary *resultJSON))callback;
```
3. 设置验证码的显示位置。
```
/**
 @note，该接口为可选接口，需在loadTencentCaptcha之前调用。不调该接口时，验证码的中心点将默认为<loadTencentCaptcha>中view的中心位置
 @param center，验证码的中心点坐标
 */
 - (void)setCaptchaPosition:(CGPoint)center;
```
使用举例：
```
[[TCWebCodesBridge sharedBridge] setCaptchaPosition:CGPointMake(self.view.bounds.size.width*0.5, self.view.bounds.size.height*0.4)];
[[TCWebCodesBridge sharedBridge] loadTencentCaptcha:self.view appid:@"**** callback:^(NSDictionary *resultJSON) {
    [self showResultJson:resultJSON];
}];
```
4. 设置 NSLog 开关。
```
/**
默认开关为关闭状态，打开后可在控制台输出一些验证码加载过程或出错信息
 @note，该接口为可选接口，一般在接入遇到问题时打开用于辅助调试。需在loadTencentCaptcha之前调用
 @param enable，开关状态，YES时打开，NO为关闭
 */
 - (void)setLogState:(BOOL)enable;
```
使用举例：
```
[[TCWebCodesBridge sharedBridge] setLogState:YES;
[[TCWebCodesBridge sharedBridge] loadTencentCaptcha:self.view appid:@"**** callback:^(NSDictionary *resultJSON) {
    [self showResultJson:resultJSON];
}];
```
