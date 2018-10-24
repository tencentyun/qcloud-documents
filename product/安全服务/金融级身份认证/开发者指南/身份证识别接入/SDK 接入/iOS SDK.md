> **注意：**
>
> **接入之前，请详细阅读 SDK 中的 readme 和接入指引！**

### 1. SDK 导入&配置
1. 将 SDK 文件导入到目标 project 中去,并确定**“add to target”**被勾选.
```
	├── WBOCRService.bundle
	|
	├── WBOCRService.framework
	│   
	├── include
	│   └── recdetect.h
	├── librecdetect.a
	└── opencv2.framework
```

2. 在 【build phases】 >【link with libraries】下加入如下依赖。
```
  CoreTelephony.framework
  AssetsLibrary.framework
  CoreMedia.framework
  AVFoundation.framework
  libc++.tbd
```
3. 【Build Setting】>【Enable Bitcode】 设置为 NO.
4. 【Build Setting】>【 Linking】 > 【other linker flag】设置增加 `-ObjC` 和 `-lz linker flag`
5. SDK 中需要使用 camera，需要在` Info.plist `中添加 `NSCameraUsageDescription`为 key 的键值对。

### 2. SDK 调用
调用详情参见 Demo 工程以及头文件 `WBOCRService.h`

#### 2.1 在使用 OCR SDK 的类中引入 `WBOCRService.h`

```
#import <WBOCRService/WBOCRService.h>
 
@interface ViewController ()
 
// TODO:
 
@end
```

#### 2.2 启动 OCR SDK服务

1. 入口方法

```
/**
* @brief 调起 SDK 入口方法

* @param manageVc          SDK 的入口页面对应的 view controller
* @param config            配置参数
* @param version           接口版本号
* @param appId             腾讯服务分配的 app_id
* @param nonce             每次请求需要的一次性 nonce
* @param userId            每个用户唯一的标识
* @param sign              签名信息
* @param orderNo           订单号
* @param startSucceed      启动 SDK 成功回调
* @param recognizeSucceed  识别成功回调
* @param failed            SDK 发生异常退出后回调
 
 */
- (void)startWebOCRServiceWithManageVC:(nonnull UIViewController *)manageVc
                                config:(nullable WBWebOCRConfig *)config
                               version:(nonnull NSString *)version
                                 appId:(nonnull NSString *)appId
                                 nonce:(nonnull NSString *)nonce
                                userId:(nonnull NSString *)userId
                                  sign:(nonnull NSString*)sign
                               orderNo:(nonnull NSString *)orderNo
                          startSucceed:(nullable WBOCRServiceStartSucceedBlock)startSucceed
                      recognizeSucceed:(nullable WBOCRServiceRecognizeSuccessBlock)recognizeSucceed
                                failed:(nullable WBOCRServiceFailedBlock)failed;
```
2. `WBWebOCRConfig` 支持对 SDK 的做个性化配置，字段详情，请阅读` WBWebOCRConfig `头文件部分注释
3. `WBWebOCRConfig.h`
```
/*
 * @brief WBWebOCRConfig 类定义了 SDK 的配置信息，可以通过 WBWebOCRConfig 单例进行读取、配置，
 *        这个步骤是可选的，如果外部没有配置信息传入，将使用默认的配置参数
 */


/**
 * @brief WBOCRSDKType 定义 SDK 不同的识别模式
 
 - WBOCRSDKTypeNoraml  : 标准模式，SDK 调起成功后，先进入拍摄准备页面，待正反两面识别完成之后
   将识别信息返回到第三方 APP
 - WBOCRSDKTypeFontSide: 人像面识别模式，SDK 调起成功后，直接进入拍摄识别页面，识别身份证人像面
   识别完成之后，将本次识别结果返回第三方 APP
 - WBOCRSDKTypeBackSide: 国徽面识别模式，SDK 调起成功后，直接进入拍摄识别页面，识别身份证国徽面
   识别完成之后，将本次识别结果返回第三方 APP
 */
typedef NS_ENUM(NSInteger, WBOCRSDKType) {
    WBOCRSDKTypeNoraml,
    WBOCRSDKTypeFontSide,
    WBOCRSDKTypeBackSide
};

@interface WBWebOCRConfig : NSObject

+ (instancetype _Nonnull )sharedConfig;

/**
 * @brief 选择 SDK 接入模式，default WBOCRSDKTypeNoraml
 */
@property (nonatomic)WBOCRSDKType SDKType;
/**
 * @brief 设置身份证照片预览页面上的水印信息，default @"仅供本次业务使用"
 */
@property (nonatomic,copy)NSString * _Nullable waterMarking;

/**
 * @brief 获取 SDK 的登录接口的 baseUrl，readonly
 */
@property (nonatomic,copy,readonly)NSString* _Nonnull baseUrl;

@end
```

#### 2.3 身份证识别结果,封装在` WBIDCardInfoModel `类中，会返回如下信息

```
/*
 * @brief WBIDCardInfoModel 类封装了身份证的正反面信息
 *        SDK会将识别结果包装成一个 WBIDCardInfoModel 实例，通过回调 block 通知第三方
 
 * @detail 字段含义
 - idcard        公民身份号码
 - name          姓名
 - sex           性别
 - nation        民族
 - address       住址
 - birth         出生
 - authority     签发机关
 - validDate     有效期限
 - frontFullImg  国徽面截图
 - backFullImg   人像面截图
 - orderNo       订单号，和本次业务相关 
 - sign	           返回的签名信息
- warning         识别结果警告
 
 */

@interface WBIDCardInfoModel : NSObject


/// 身份证人像面信息
@property (nonnull,strong,nonatomic) NSString *idcard;
@property (nonnull,strong,nonatomic) NSString *name;
@property (nonnull,strong,nonatomic) NSString *sex;
@property (nonnull,strong,nonatomic) NSString *nation;
@property (nonnull,strong,nonatomic) NSString *address;
@property (nonnull,strong,nonatomic) NSString *birth;

/// 身份证国徽面信息
@property (nonnull,strong,nonatomic) NSString *authority;
@property (nonnull,strong,nonatomic) NSString *validDate;

/// 本次业务相关信息
@property (nonnull,strong,nonatomic) NSString *orderNo; 
@property (nonnull,strong,nonatomic) NSString *sign;

/// 正反面识别结果截图信息
@property (nonnull,strong,nonatomic) UIImage* frontFullImg;
@property (nonnull,strong,nonatomic) UIImage* backFullImg;

/// warning，正反面识别结果对应的警告信息
@property (nonnull,strong,nonatomic) NSString *frontWarning;
@property (nonnull,strong,nonatomic) NSString *backWarning;
@end
```
> **注意**
> 具体使用方法参照 demo 工程以及 `WBOCRService.h` 头文件
> 错误信息通过 fail 回调抛出，错误码列表参见错误码描述章节或头文件。

### 3. 错误码描述

| 返回码    | 返回信息      | 处理措施                                |
| ------ | --------- | ----------------------------------- |
| 100101 | 无网络，请确认   | 确认网络正常                              |
| 100102 | 不支持 2G 网络 | 更换网络环境                              |
| 100103 | 无相机权限     |                                     |
| 200101 | 用户取消操作    | 用户主动退出操作                            |
| 200102 | 识别超时      | 用户在身份证正反面识别过程中超过设定的阈值（20S）无法识别，提示超时 |

上一步：[SDK 启动](https://cloud.tencent.com/document/product/655/13846)