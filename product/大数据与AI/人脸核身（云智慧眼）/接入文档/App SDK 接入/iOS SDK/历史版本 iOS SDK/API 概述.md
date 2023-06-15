iOS 端慧眼 SDK 主要涉及的类主要包含 HuiYanAuthSDKKit、AuthConfig，下面对其支持的 API 做出详细说明。

## HuiYanAuthSDKKit
HuiYanAuthSDKKit 为慧眼 SDK 的对外接口类，主要逻辑也都是调用此类完成。

| API                                                          | 功能描述                          |
| ------------------------------------------------------------ | --------------------------------- |
| [\+ (instancetype)sharedInstance;](#sharedInstance)          | 获取 SDK 实例                       |
| [\+ (void)clearInstance;](#clearInstance)                    | 资源释放接口                      |
| [-(int)setFaceIdTokenCreateFunction:](#setFaceIdTokenCreateFunction:) | 设置主动获取客户 FaceIdToken 的接口 |
| [-(void)startHuiYanAuth:](#startHuiYanAuth:)                 | 启动活体核身检测的接口            |

### sharedInstance;
```objective-c
/// 获取SDK实例
+ (nonnull instancetype)sharedInstance;
```

功能介绍：慧眼 SDK 获取 SDK 实例。

### clearInstance;
```objective-c
/// 清理SDK资源
+ (void)clearInstance;
```
功能介绍：慧眼 SDK 释放 Instance 的接口。

### setFaceIdTokenCreateFunction:
```objective-c
/// 设置 FaceIdToken
///@param onFaceIdTokenCreateFunction 获取FaceIdToken block
- (int)setFaceIdTokenCreateFunction:(FaceIdTokenCreateFunction _Nonnull)onFaceIdTokenCreateFunction;
```
功能介绍：设置主动获取客户 FaceIdToken 的接口。
传入参数：

| 参数类型                                                | 参数名称                  | 参数含义                      |
| ------------------------------------------------------- | ------------------------- | ----------------------------- |
| [FaceIdTokenCreateFunction](#FaceIdTokenCreateFunction) | FaceIdTokenCreateFunction | 主动获取客户 FaceIdToken 的回调 |



### startHuiYanAuth:
```objective-c
/// 启动SDK模块，运行带有UI界面的功能识别模块
/// @note 请在View加载完毕后调用该接口
/// @param authConfig SDK需要运行的配置
/// @param onProcessSucceed 识别成功回调
/// @param onProcessFailed 识别失败回调
- (void)startHuiYanAuthWithAuthConfig:(AuthConfig * _Nonnull)authConfig
          withProcessSucceedBlock:(TXYSDKKitProcessSucceedBlock _Nonnull)onProcessSucceed
           withProcessFailedBlock:(TXYSDKKitProcessFailedBlock _Nonnull)onProcessFailed;
```

功能介绍：启动活体核身检测的接口。
传入参数：

| 参数类型                                                     | 参数名称         | 参数含义               |
| ------------------------------------------------------------ | ---------------- | ---------------------- |
| [AuthConfig](#AuthConfig)                                    | authConfig       | 启动活体核身的参数配置 |
| [TXYSDKKitProcessSucceedBlock](#TXYSDKKitProcessSucceedBlock) | onProcessSucceed | SDKKIt 处理成功回调接口 |
| [TXYSDKKitProcessFailedBlock](#TXYSDKKitProcessFailedBlock)  | onProcessFailed  | SDKKIt 处理失败回调接口 |



## AuthConfig
AuthConfig 是在启动慧眼 SDK 时的配置实体类，主要包含了以下属性。

| 类型                              | 名称           | 含义                                    | 默认值 |
| --------------------------------- | -------------- | --------------------------------------- | ------ |
| NSString                          | licensePath    | 客户申请的用户核审授权的License文件路径 | 空     |
| [CustomerConfig](#CustomerConfig) | customerConfig | 客户自定义配置信息                      | 空     |



## CustomerConfig
AuthConfig 是在启动慧眼 SDK 时的配置实体类，主要包含了以下属性。

| 类型     | 名称               | 含义                            | 默认值 |
| -------- | ------------------ | ------------------------------- | ------ |
| NSString | authTips           | 核身时的提示信息(不超过100字符) | 空     |
| UIColor  | authTipsTxtColor   | 提示信息文字颜色                | 空     |
| BOOL     | isHiddenResultPage | 是否核身显示结果页              | YES    |
| long     | authTimeoutMs      | 设置活体超时时间                | 10000  |
| BOOL     | isLiveDataEncrypt  | 是否对活体数据加密              | NO     |



## FaceIdTokenCreateFunction
用于提供给客户使用的获取 FaceIdToken 的接口类，客户需要返回客户获取到的 FaceIdToken 的值。
```java
/// 用户设置主动刷新 返回FaceIDToken
typedef NSString *_Nullable(^FaceIdTokenCreateFunction)(void);
//设置FaceIdToken
[[HuiYanSDKKit sharedInstance] setFaceIdTokenCreateFunction:^NSString *{
      return faceIdToken;
}];
```

## TXYSDKKitProcessSucceedBlock
用于接受活体核身认证的结果成功监听 block。
```objective-c
/// SDKKIt处理成功回调接口
/// @param resultInfo 核身成功
/// @param retFaceidToken 返回FaceIdToken
typedef void (^TXYSDKKitProcessSucceedBlock)(id _Nonnull resultInfo, id _Nullable retFaceidToken);
```

## TXYSDKKitProcessFailedBlock
用于接受活体核身认证的结果失败监听 block。
```objective-c
/// SDKKIt处理失败回调接口
/// @param error 处理过程中触发的异常错误
/// @param retFaceidToken 返回FaceIdToken
typedef void (^TXYSDKKitProcessFailedBlock)(NSError *_Nonnull error, id _Nullable retFaceidToken);
```

## 错误码

| 错误码                      | 错误码值 | 错误码含义                                                   |
| --------------------------- | -------- | ------------------------------------------------------------ |
| HY_NETWORK_ERROR            | 272      | 网络请求出现异常                                             |
| HY_LOCAL_REF_FAILED_ERROR   | 273      | 本地初始化 SDK 时，本地检测失败，常见异常不存在 license 文件或者 license 过期 |
| HY_USER_CANCEL_ERROR        | 274      | 用户主动取消核身流程                                         |
| HY_INNER_ERROR_CODE         | 275      | SDK 内部产生的异常，终止了核身流程                            |
| HY_DO_NOT_CHANGE_ERROR      | 276      | 在核身过程中切换应用发生终止流程的异常                       |
| HY_CAMEREA_PERMISSION_ERROR | 277      | 获取摄像头过程中发生异常                                     |
| HY_INIT_SDK_ERROR           | 278      | 未调用 init()方法，直接调用了启动检测                         |
| HY_VERIFY_LOCAL_ERROR       | 279      | 本地人脸检测失败                                             |
| HY_SDK_VEDIO_CUT_ERR        | 282      | 本地合身视频采集失败                                         |
| HY_SDK_TURING_TOKEN_GET_ERR | 283      | 设备风险模块调用失败                                         |

