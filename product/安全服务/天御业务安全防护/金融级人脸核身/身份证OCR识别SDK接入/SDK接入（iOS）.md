### 1. SDK导入&&配置
1. 将WBOCRService.framework以及WBWallet.bundle添加到项目中
2. Build Setting --> Linking --> other linker flag 设置 增加 -ObjC和-lzlinker flag
3. SDK中需要使用camera，需要在 Info.plist中添加 NSCameraUsageDescription为key的键值对
4. Build Phases --> Link Binary With Libraries 增加 AssetsLibrary.framework、AVFoundation.framework 、CoreTelephony.framework 、CoreMedia.framework 和 WBOCRService.framework

### 2. SDK 调用
调用详情参见Demo工程以及头文件WBWebOCRService.h
1.在使用OCR SDK的类中引入WBWebOCRService.h
```
#import <WBOCRService/WBWebOCRService.h>
 
@interface ViewController ()
 
// TODO:
 
@end
```

2.启动OCR SDK服务
1) 入口方法
```
/**
* @brief 调起SDK入口方法

* @param manageVc          SDK的入口页面对应的view controller
* @param config            配置参数
* @param version           接口版本号
* @param appId             腾讯服务分配的app_id
* @param nonce             每次请求需要的一次性nonce
* @param userId            每个用户唯一的标识
* @param sign              签名信息
* @param orderNo           订单号
* @param startSucceed      启动SDK成功回调
* @param recognizeSucceed  识别成功回调
* @param failed            SDK发生异常退出后回调
 
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
2) WBWebOCRConfig支持对SDK的做个性化配置，字段详情，请阅读WBWebOCRConfig头文件部分注释
3）WBWebOCRConfig.h
```
/*
 * @brief WBWebOCRConfig类定义了SDK的配置信息，可以通过WBWebOCRConfig单例进行读取、配置，
 *        这个步骤是可选的，如果外部没有配置信息传入，将使用默认的配置参数
 */


/**
 * @brief WBOCRSDKType定义SDK不同的识别模式
 
 - WBOCRSDKTypeNoraml  : 标准模式，SDK调起成功后，先进入拍摄准备页面，待正反两面识别完成之后
   将识别信息返回到第三方APP
 - WBOCRSDKTypeFontSide: 人像面识别模式，SDK调起成功后，直接进入拍摄识别页面，识别身份证人像面
   识别完成之后，将本次识别结果返回第三方APP
 - WBOCRSDKTypeBackSide: 国徽面识别模式，SDK调起成功后，直接进入拍摄识别页面，识别身份证国徽面
   识别完成之后，将本次识别结果返回第三方APP
 */
typedef NS_ENUM(NSInteger, WBOCRSDKType) {
    WBOCRSDKTypeNoraml,
    WBOCRSDKTypeFontSide,
    WBOCRSDKTypeBackSide
};

@interface WBWebOCRConfig : NSObject

+ (instancetype _Nonnull )sharedConfig;

/**
 * @brief 选择SDK接入模式，default WBOCRSDKTypeNoraml
 */
@property (nonatomic)WBOCRSDKType SDKType;
/**
 * @brief 设置身份证照片预览页面上的水印信息，default @"仅供本次业务使用"
 */
@property (nonatomic,copy)NSString * _Nullable waterMarking;

/**
 * @brief 获取SDK的登录接口的baseUrl，readonly
 */
@property (nonatomic,copy,readonly)NSString* _Nonnull baseUrl;

@end
```

3.SDK返回识别结果,封装在WBIDCardInfoModel类中，会返回如下信息
```
/*
 * @brief WBIDCardInfoModel类封装了身份证的正反面信息
 *        SDK会将识别结果包装成一个WBIDCardInfoModel实例，通过回调block通知第三方
 
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
 - ocrId         ocr Id，每次识别的唯一标识，和本次业务相关
 - sign	           返回的签名信息
 
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
@property (nonnull,strong,nonatomic) NSString *ocrId;
@property (nonnull,strong,nonatomic) NSString *sign;

/// 正反面识别结果截图信息
@property (nonnull,strong,nonatomic) UIImage* frontFullImg;
@property (nonnull,strong,nonatomic) UIImage* backFullImg;

@end
```

4.具体使用方法参照demo工程以及WBWebOCRService.h头文件
5.错误信息通过fail回调抛出，错误码列表参见错误码描述章节或头文件。

### 3.错误码描述

| 返回码 | 返回信息 | 处理措施 |
|---------|---------|---------|
| 100101 | 无网络，请确认 | 确认网络正常 |
| 100102 | 不支持2G网络 | 更换网络环境 |
| 100103 | 无相机权限 |  |
| 200101| 用户取消操作 | 用户主动退出操作 |
| 200102 | 识别超时 |用户在身份证正反面识别过程中超过设定的阈值（20S）无法识别，提示超时 |