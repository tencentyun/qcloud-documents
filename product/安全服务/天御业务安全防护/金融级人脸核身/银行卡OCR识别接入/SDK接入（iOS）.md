
> **说明：接入之前，请详细阅读，SDK 中的 readme 和接入指引！**

### 1. SDK 导入&配置
1.  将 SDK 文件导入到目标 project 中去,并确定**“add to target”**被勾选.
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
2. 在 build phases -> link with libraries 下加入如下依赖.
```
	CoreTelephony.framework
	AssetsLibrary.framework
	CoreMedia.framework
	AVFoundation.framework
	libc++.tbd
```
3.` Build Setting --> Enable Bitcode` 设置为 NO.
4. `Build Setting --> Linking --> other linker flag` 设置 增加` -ObjC`和` -lz linker flag`
5. SDK 中需要使用 camera，需要在` Info.plist`中添加 N`SCameraUsageDescription`为 key 的键值对。

### 2. SDK 调用
**调用详情参见 Demo 工程以及头文件 WBOCRService.h**
#### 2.1 在使用 OCR SDK 的类中引入 WBOCRService.h
```
#import <WBOCRService/WBOCRService.h>
 
@interface ViewController ()
 
// TODO:
 
@end
```
#### 2.2 启动 OCR SDK 服务
1）入口方法
```
/**
 * @brief 调起 SDK 入口方法
 
 * @param manageVc          SDK 的入口页面对应的 view controller
 * @param config            配置参数
 * @param version           接口版本号
 * @param appId             腾讯服务分配的 app_id
 * @param nonce             每次请求需要的一次性 nonce
 * @param userId            每个用户唯一的标识
 * @param sign              签名信息
 * @param orderNo           订单号
 * @param startSucceed      启动 SDK 成功回调
 * @param recognizeSucceed  识别成功回调
 * @param failed            SDK 发生异常退出后回调
 
 
 * @detail 回调信息 code 和 msg 对照表
 * ## code 退出 code
 * ## msg  退出信息描述
 
 * @detail code && msg 错误码以及描述信息参考接口文档中“错误码”章节
 *
 */

- (void)startOCRServiceWithManageVC:(nonnull UIViewController *)manageVc
                             config:(nullable WBOCRConfig *)config
                            version:(nonnull NSString *)version
                              appId:(nonnull NSString *)appId
                              nonce:(nonnull NSString *)nonce
                             userId:(nonnull NSString *)userId
                               sign:(nonnull NSString*)sign
                            orderNo:(nonnull NSString *)orderNo
                       startSucceed:(nonnull WBOCRServiceStartSucceedBlock)startSucceed
                   recognizeSucceed:(nonnull WBOCRServiceRecognizeSuccessBlock)recognizeSucceed
                             failed:(nonnull WBOCRServiceFailedBlock)failed;
```

2）WBOCRConfig 支持对 SDK 的做个性化配置，字段详情，请阅读WBOCRConfig 头文件部分注释。
3）WBOCRConfig.h
```
/*
 * @brief WBOCRConfig 类定义了 SDK 的配置信息，可以通过WBOCRConfig 单例进行读取、配置，
 *        这个步骤是可选的，如果外部没有配置信息传入，将使用默认的配置参数
 */


/**
 * @brief WBOCRSDKType定义 SDK 不同的识别模式
 
 - WBOCRSDKTypeNoraml  : 标准模式，SDK 调起成功后，先进入拍摄准备页面，待正反两面识别完成之后
 将识别信息返回到第三方 APP
 - WBOCRSDKTypeFontSide: 人像面识别模式，SDK 调起成功后，直接进入拍摄识别页面，识别身份证人像面
 识别完成之后，将本次识别结果返回第三方 APP
 - WBOCRSDKTypeBackSide: 国徽面识别模式，SDK 调起成功后，直接进入拍摄识别页面，识别身份证国徽面
 识别完成之后，将本次识别结果返回第三方 APP
 */
typedef NS_ENUM(NSInteger, WBOCRSDKType) {
    WBOCRSDKTypeIDCardNormal,
    WBOCRSDKTypeIDCardFrontSide,
    WBOCRSDKTypeIDCardBackSide,
    WBOCRSDKTypeBankCard
};
@interface WBOCRConfig : NSObject
+ (instancetype _Nonnull )sharedConfig;
/**
 * @brief 选择 SDK 接入模式为WBOCRSDKTypeBankCard，default WBOCRSDKTypeNoraml
 */
@property (nonatomic)WBOCRSDKType SDKType;

/**
 * @brief 获取 SDK 的登录接口的baseUrl，readonly
 */
@property (nonatomic,copy,readonly)NSString* _Nonnull baseUrl;

@end
```

#### 2.3  银行卡识别结果返回
银行卡识别结果返回,封装在 WBBankCardInfoModel 类中，会返回如下信息

```
/**
 * @brief 银行卡信息
 * @detail 字段含义
 - bankcardNo         银行卡号
 - bankcardValidDate  银行卡有效期(年／月，没有为空)
 - warningCode        警告码
 - warningMsg         警告码描述
 - bankcardNoPhoto    卡号图片
*/
@interface WBBankCardInfoModel : NSObject

@property (nonnull,strong,nonatomic)  NSString *bankcardNo;
@property (nullable,strong,nonatomic) NSString *bankcardValidDate;
@property (nullable,strong,nonatomic) NSString *warningCode;
@property (nullable,strong,nonatomic) NSString *warningMsg;
@property (nonnull,strong,nonatomic)  UIImage *bankcardNoPhoto;
@property (nonnull,strong,nonatomic)  UIImage *bankcardCropPhoto;

@end
```

#### 2.4 具体使用方法
具体使用方法参照 demo 工程以及 WBOCRService.h 头文件
#### 2.5 错误信息
错误信息通过 fail 回调抛出，错误码列表参见错误码描述章节或头文件。

### 3. 错误码描述
| 返回码 | 返回信息 |处理措施 |
|---------|---------|---------|		
|100101	|无网络，请确认|	确认网络正常|
|100102|	不支持 2G 网络	|更换网络环境
|100103|无相机权限|
|200101	|用户取消操作	|用户主动退出操作
|200102	|识别超时|	用户在银行卡识别过程中超过设定的阈值（20S） 无法识别，提示超时

### 4. 银行卡 OCR 识别返回结果获取及验证
#### 4.1 前端获取结果验证签名
- 为了确保前端 SDK 的结果真实性且未被篡改，合作伙伴服务端可以验证结果
- 合作伙伴 APP 端银行卡 OCR 识别SDK返回的带签名结果。
- 合作伙伴 APP 端调用其服务端接口进行签名认证，接口认证成功后继续业务流程。

##### 4.1.1 合作方后台生成签名 ####
合作方根据本次人脸验证的如下参数生成签名：

参数 | 说明
---|--- 
app_id |腾讯服务分配的app_id 
order_no	| 订单号，本次人脸验证合作伙伴上送的订单号，唯一标识。
api ticket	|合作伙伴服务端缓存的tikcet,注意是sign 类型，具体见[Access Token获取](https://cloud.tencent.com/document/product/295/10118?=cn)获取规则
- 将 app_id、order_no、连同 ticket(SIGN) 共三个参数的值进行字典序排序
将排序后的所有参数字符串拼接成一个字符串进行 SHA1 编码
SHA1 编码后的 40 位字符串作为签名(sign)
示例代码及用法
```
示例：
请求参数：
app_id = appId001
order_no= userID19959248596551
ticket= duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoe
```

- 字典排序后的参数为：
```
[appId001, duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoe, test1480921551481]
```
- 拼接后的字符串为：
```
 appId001duSz9ptwyW1Xn7r6gYItxz3feMdJ8Na5x7JZuoxurE7RcI5TdwCE4KT2eEeNNDoetest1480921551481
```
- 计算 SHA1 得到签名：
```
B02CEBEB07F792B2F085E8CB1E7BA9EC19284F54 该字串就是最终生成的签名 (40位)，不区分大小写。
```

##### 4.1.2 比对签名
  合作方服务端生成的签名与SDK返回的签名比对，如果相同即可信任 SDK 的刷脸结果。
> ** 注：合作方必须定时刷新 ticket(SIGN) 保证远程身份认证后台缓存有该合作方的 ticket(SIGN)，否则后台无法生成签名值。

#### 4.2 合作伙伴服务端查询结果
合作伙伴服务端生成签名，并调用银行卡 OCR 识别服务端查询结果，鉴权完成后返回结果（服务端上送 order_no 和 app_id 查询）。
##### 4.2.1 合作方后台生成签名
合作方根据本次人脸验证的如下参数生成签名：

参数 | 说明
---|--- 	
app_id|	腾讯服务分配的 app_id
order_no	|订单号，本次人脸验证合作伙伴上送的订单号，唯一标识。
version|	默认值：1.0.0
api ticket	|合作伙伴服务端缓存的 tikcet,注意是 sign 类型，具体见[Access Token获取](https://cloud.tencent.com/document/product/295/10118?cn)获取规则
nonceStr|	32位随机字符串,字母和数字
- 生成一个 32 位的随机字符串(字母和数字)  nonceStr，将 app_id、order_no、version 连同 ticket、nonceStr 共五个参数的值进行字典序排序再 SHA1 编码生成签名。具体签名算法见章节7。

##### 4.2.2 银行卡 OCR 识别结果查询接口
请求URL：https://idasc.webank.com/api/server/getBankCardOcrResult
请求方法:GET
请求参数：

参数	|说明	|类型	|长度|	是否必填
---|--- 
app_id|	腾讯服务分配的 app_id	|字符串	|腾讯服务分配|	必填，腾讯服务分配的 app_id
order_no	|订单号|	字符串	|32	|必填，合作方订单的唯一标识
get_file	|是否需要获取银行卡OCR图片文件	|字符串	|1	|非必填，值为1则返回文件；其他则不返回。
nonce	|随机数	|字符串	|32	|必填
version	|版本号	|字符串	|20	|必填，默认值：1.0.0
sign	|签名值	|字符串|	40	|必填，使用上面生成的签名。
 **请求示例：**
https://idasc.webank.com/api/server/getOcrResult?app_id=xxx&nonce=xxx&order_no=xxx&version=1.0.0&sign=xxx&get_file=xxxx
	
返回参数：

参数|	类型|	说明
---|--- 
code	|string|	“0”说明银行卡识别成功
msg|	string|	返回结果描述
orderNo|	string	|订单编号
bankCardNo|	string	|resultCode为0返回:银行卡号
bankCardValidDate	|string|	resultCode为0返回:银行卡有效期
bankcardCropPhoto|	Base 64 string|	银行卡切边图片
bankcardNoPhoto	|Base 64 string	|银行卡卡号切边图片
orginBankcardPhoto	|Base 64 string	|识别原始图片
warnCode	|string	|银行卡警告码，在银行卡日期失效或者过期会提示；当frontCode为0时才会出现告警码，告警码的含义请参考“通用响应码”-“银行卡识别响应码”
operateTime|	string	|做OCR的操作时间

>** 注意：
- 银行卡照片信息作为存证，合作伙伴可以通过此接口拉取识别结果和文件，需要注意请求参数的get_file需要设置为1；如果不上送参数或者参数为空，默认不返回照片信息。
- 照片均为 base64 位编码，其中照片解码后格式一般为 jpg。
- 对于银行卡识别有日期失效或者过期的情况，请参考 frontWarnCode和backWarnCode 告警码。（见银行卡识别响应码码）
