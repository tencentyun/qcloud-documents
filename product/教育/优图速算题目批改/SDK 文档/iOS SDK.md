## 概述
数学作业批改（Homework Correction-Math，HCM）是腾讯云推出的速算题目智能批改产品。在过去，速算作业的批改需要教师做基础性、重复性的工作，消耗大量的时间；腾讯云针对此场景推出数学作业批改服务，支持各种数学公式和符号识别，能识别竖式、分式、脱式以及四则运算多种题型。
TAISDK 是一款封装了腾讯云教育 AI 能力的 SDK，通过集成 SDK，用户可以快速接入相关产品功能，如数学作业批改、智聆口语评测等。  

## 前提条件
**获取密钥**：SecretId 和 SecretKey 是使用 SDK 的安全凭证，您可以在**[访问管理](https://console.cloud.tencent.com/cam/overview)**>**云 API 密钥**>**[API 密钥管理](https://console.cloud.tencent.com/cam/capi)**中获取该凭证。
![](https://main.qcloudimg.com/raw/273b67bc4d38af6cb9999e9f4663d268.png) 

## 集成 SDK 

### 1. 导入 SDK
从 [Demo 源码](https://github.com/TencentCloud/tencentcloud-sdk-ios-soe) 中获取 SDK 并导入到工程。
![](https://main.qcloudimg.com/raw/ae5557cc5aea1795ca2ffc18032e5f4c/20191231002.png)


### 2. 调用接口
声明并定义对象：
```objc
@property (strong, nonatomic) TAIMathCorrection *mathCorrection;
self.mathCorrection = [[TAIMathCorrection alloc] init];
```
初始化参数：
```objc
TAIMathCorrectionParam *param = [[TAIMathCorrectionParam alloc] init];
param.sessionId = [[NSUUID UUID] UUIDString];
param.appId = @"";
param.imageData = UIImageJPEGRepresentation(_imageView.image, 0);
param.secretId = @"";
param.secretKey = @"";
[self.mathCorrection correction:param callback:^(TAIError *error, TAIMathCorrectionRet *result) {
    //成功返回TAIMathCorrectionRet
}];
```

### 3. 签名
SecretKey 属于安全敏感参数，线上版本一般由业务后台生成 [临时 SecretKey](https://cloud.tencent.com/document/api/598/13895) 或者 SDK 外部签名返回到客户端。
- 内部签名：SDK 内部通过 SecretId 和 SecretKey 计算签名，用户无需关心签名细节。
- 外部签名：SDK 外部通过调用 getStringToSign 获取签名字符串，然后根据 [签名规则-计算签名](https://cloud.tencent.com/document/product/884/30657#3.-.E8.AE.A1.E7.AE.97.E7.AD.BE.E5.90.8D) 进行签名。

```objc
//获取签名所需字符串
- (NSString *)getStringToSign:(NSInteger)timestamp;
```

>!时间戳 timestamp 必须和 TAIEvaluationParam 参数的 timestamp 一致。

## 参数说明

### 公共参数
TAICommonParam 参数说明：

| 参数|类型|必填|说明 |
|---|---|---|---|
|appId|NSString|是|AppID|
|timeout|NSInteger|否|超时时间，默认30秒|
|secretId|NSString|是|密钥 ID|
|secretKey|NSString|内部签名：必填|密钥 Key|
|signature|NSString|外部签名：必填|签名|
|timestamp|NSInteger|外部签名：必填|秒级时间戳|

TAIError 参数说明：

| 参数|类型|说明 |
|---|---|---|
|code|TAIErrCode|错误码|
|desc|NSString|错误描述|
|requestId|NSString|请求 ID，定位错误信息|

### 数学作业批改参数
TAIMathCorrectionParam 参数说明：

| 参数|类型|必填|说明 |
|---|---|---|---|
|sessionId|NSString|是|一次批改唯一标识|
|imageData|NSData|是|图片数据|

TAIMathCorrectionRet 参数说明：

| 参数|类型|说明 |
|---|---|---|
|sessionId|NSString|一次批改唯一标识|
|formula|NSString|算式|
|items|NSArray<TAIMathCorrectionItem *>|算式结果|


TAIMathCorrectionItem 参数说明：

| 参数|类型|说明 |
|---|---|---|
|result|BOOL|算式结果|
|rect|CGRect|算式坐标|
|formula|NSString|算式字符串|















