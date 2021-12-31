iOS 端文字识别 SDK 主要涉及的类有 OcrSDKKit、OcrSDKConfig、CustomConfigUI、OcrCommmDef，下面对其支持的 API 做出详细说明。

### OcrSDKKit

 OcrSDKKit 是文字识别 OCR 的对外接口类，文字识别功能主要集中在这个类中。

| API                                                 | 功能描述                |
| --------------------------------------------------- | :---------------------- |
| [sharedInstance()](#shareInstance)                  | 创建 OcrSDKKit 的单例     |
| [clearInstance()](#clearInstance)                 | 主动释放资源            |
| [getVersion()](#getVersion())                       | 获取当前 SDK 的版本号信息 |
| [loadSDKConfig](#loadSDKConfig)                   | 初始化 SDK 配置信息       |
| [updateFederationToken()](#updateFederationToken()) | 主动更新临时密钥        |
| [startProcessOcr()](#startProcessOcr())             | 启动 OCR 识别             |

[](id:shareInstance)

#### sharedInstance()

```c
+ (nonnull instancetype)sharedInstance;
```

- 功能描述：
创建 OcrSDKKit 的单例。
- 返回结果：
OcrSDKKit 的单例对象。	


[](id:clearInstance)
#### clearInstance()

```c
/// 清理 SDK 资源
+ (void)clearInstance;
```

- 功能描述：
主动释放资源的方法，可在退出应用或者需要清理资源的时候调用。


[](id:getVersion())
#### getVersion()

```c
- (NSString *_Nonnull)getVersion;
```

- 功能描述：
获取 SDK 当前的版本号。
- 返回结果：
当前 SDK 的版本信息。


[](id:loadSDKConfig)
#### loadSDKConfig()

```c
/// SDKKIt 加载 OCR 配置信息 这里使用的密钥为固定密钥，当使用临时密钥时，secretId secretKey 填入 nil 空值
/// @param secretId  Secret id
/// @param secretKey Secret key
/// @param ocrConfig ocr 配置类
- (int)loadSDKConfigWithSecretId:(NSString *)secretId withSecretKey:(NSString *)secretKey withConfig:(OcrSDKConfig *)ocrSDKConfig;
```

- 功能描述：
初始化 SDK 信息。
- 传入参数：

| 参数类型                          | 参数名称       | 参数含义               |
| --------------------------------- | -------------- | ---------------------- |
| [OcrSDKConfig](#OcrSDKConfig)     | ocrSDKConfig   | SDK 配置参数的实体类    |
| [OcrSDKUIConfig](#OcrSDKUIConfig) | ocrSDKUIConfig | SDK UI 配置参数的实体类 |
| NSString                          | secretId       | SecretId 密钥          |
| NSString                          | secretKey      | SecretKey 密钥         |


[](id:updateFederationToken())
#### updateFederationToken()

```c
/// @param tmpSecretId 临时 SecretId
/// @param tmpSecretKey 临时密钥信息
/// @param token 临时兑换 token
- (void)updateFederationToken:(NSString *_Nonnull) tmpSecretId withTempSecretKey:(NSString *_Nullable)tmpSecretKey withToken:(NSString *_Nonnull)token;
```

- 功能描述：
主动更新临时密钥信息，在您与服务器兑换得到临时密钥之后主动调用设置。
- 传入参数：

| 参数类型 | 参数名称     | 参数含义              |
| -------- | ------------ | --------------------- |
| NSString | tmpSecretId  | 临时密钥 SecretId      |
| NSString | tmpSecretKey | 临时密钥 SecretKey     |
| NSString | token        | 兑换后的临时访问 token |


[](id:startProcessOcr())
#### startProcessOcr()

```c
/// 启动 SDK 模块，运行带有 UI 界面的功能识别模块
/// @param ocrType  识别模式
/// @param CustomConfigUI ocrUI 配置类 当传入 nil 时使用默认配置
/// @param onProcessSucceed  成功回调 block
/// @param onProcessFailed 失败回调 block
- (void)startProcessOcr:(int)ocrType withSDKUIConfig:(CustomConfigUI *)customConfigUI withProcessSucceedBlock:(OcrSDKKitProcessSucceedBlock _Nonnull)onProcessSucceed withProcessFailedBlock:(OcrSDKKitProcessFailedBlock _Nonnull)onProcessFailed;
```

- 功能描述：
启动 OCR 识别
- 传入参数：

| 参数类型                          | 参数名称         | 参数含义          |
| --------------------------------- | ---------------- | ----------------- |
| [OcrType](#OcrType)               | ocrType          | 启动的 OCR 识别类型 |
| [CustomConfigUI](#CustomConfigUI) | customConfigUI   | ocrUI 配置类       |
| OcrSDKKitProcessSucceedBlock      | onProcessSucceed | 识别成功的回调    |
| OcrSDKKitProcessFailedBlock       | onProcessFailed  | 识别失败的回调    |

[](id:OcrSDKConfig)
### OcrSDKConfig

OcrSDKConfig 是在 OCR 初始化时需要传入的 SDK 的配置信息实体类。

支持参数及其默认值如下：

| 类型                        | 名称            | 含义                                                         | 默认值                                         |
| :-------------------------- | :-------------- | :----------------------------------------------------------- | :--------------------------------------------- |
| [OcrType](#OcrType)         | OcrType         | 默认识别类型                                                 | IDCardOCR_FRONT，IDCardOCR_BACK 均代表 id_card |
| [OcrModeType](#OcrModeType) | ModeType        | 识别模式类型：OCR_DETECT_MANUAL 代表手动拍摄模式，OCR_DETECT_AUTO_MANUAL 代码自动捕获模式 20s未检测提示是否切换至手动拍摄 | OCR_DETECT_MANUAL 默认值                       |
| long                        | auto_timeout_ms | 自动捕捉模式下自动切换至手动拍照模式的超时时间(5000ms<`auto_timeout_ms`<180000ms) | 20000ms                                        |
| BOOL                        | CropIdCard      | 开启身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）开关 | NO                                             |
| BOOL                        | CropPortrait    | 开启人像照片裁剪（自动抠取身份证头像区域）                   | NO                                             |
| BOOL                        | CopyWarn        | 开启复印件告警                                               | NO                                             |
| BOOL                        | BorderCheckWarn | 开启边框和框内遮挡告警                                       | NO                                             |
| BOOL                        | ReshootWarn     | 开启翻拍告警                                                 | NO                                             |
| BOOL                        | DetectPsWarn    | 开启 PS 检测告警                                             | NO                                             |
| BOOL                        | TempIdWarn      | 开启临时身份证告警                                           | NO                                             |
| BOOL                        | InvalidDateWarn | 开启身份证有效日期不合法告警                                 | NO                                             |
| BOOL                        | Quality         | 开启图片质量分数（评价图片的模糊程度）                       | NO                                             |
| BOOL                        | MultiCardDetect | 是否开启多卡证检测                                           | NO                                             |
| BOOL                        | ReflectWarn     | 是否开启反光告警                                             | NO                                             |
| NSString                    | RetImageType    | 图像预处理，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。 | 空                                             |
| BOOL                        | RetImage        | 马来西亚身份证接口是否返回图片                               | NO                                             |


[](id:CustomConfigUI)
### CustomConfigUI

CustomConfigUI 是在启动 SDK 模块时需要传入的 SDK 的 UI 配置信息实体类。

支持参数及其默认值如下：

| 类型     | 名称               | 含义                           | 默认值                                |
| -------- | ------------------ | ------------------------------ | ------------------------------------- |
| BOOL     | isShowTips         | 是否显示中间提示语             | YES                                   |
| NSString | tipsShowText       | 中间提示语内容(限制15个中文字) | "请避免识别内容折角、遮挡和反光"      |
| NSString | remindDialogText   | dialog 模式转换提示文字        | "未能识别证件，是否切换模式拍照上传?" |
| UIColor  | remindConfirmColor | dialog 模式转换提示,按钮颜色   | RGBA：5 106 1 1                       |
| UIColor  | cardFrameColor     | 卡片框选中颜色                 | RGBA：5 106 1 1                       |
| UIImage  | takePictureImage   | 拍照按钮图标 80x80             | 默认图标                              |
| UIImage  | lightONImage       | 打开手电筒按钮图标 40x40       | 默认图标                              |
| UIImage  | lightOFFImage      | 关闭手电筒按钮图标40x40        | 默认图标                              |
| UIImage  | albumImage         | 相册按钮图标40x40              | 默认图标                              |
| BOOL     | isShowAlbumBtn     | 是否显示相册按钮               | YES                                   |
| BOOL     | isHorizontal       | 是否横屏显示                   | NO                                    |

[](id:OcrType)
### OcrType

OcrType 是一个枚举类型，列举了当前文字识别 OCR 的 SDK 所支持业务类型的种类，大致如下：

| OcrType 类型             | 代表含义               |
| ----------------------- | ---------------------- |
| OcrType.IDCardOCR_FRONT | 身份证人像面识别模式   |
| OcrType.IDCardOCR_BACK  | 身份证国徽面识别模式   |
| OcrType.BankCardOCR     | 银行卡正面识别模式     |
| OcrType.BusinessCardOCR | 名片卡正面识别模式     |
| OcrType.MLIdCardOCR     | 马来西亚身份证识别模式 |
| OcrType.LicensePlateOCR | 汽车车牌识别模式 |
| OcrType.VinOCR | 汽车VIN码识别模式 |
| OcrType.VehicleLicenseOCR_FRONT | 行驶证主页识别模式 |
| OcrType.VehicleLicenseOCR_BACK | 行驶证副页识别模式 |
| OcrType.DriverLicenseOCR_FRONT | 驾驶证主页识别模式 |
| OcrType.DriverLicenseOCR_BACK | 驾驶证副页识别模式 |



[](id:OcrModeType)
### OcrModeType

OcrModeType 是一个枚举类型，列举了卡片识别模式

| OcrModeType 类型        | 代表含义                                           |
| ---------------------- | -------------------------------------------------- |
| OCR_DETECT_MANUAL      | 手动拍摄模式                                       |
| OCR_DETECT_AUTO_MANUAL | 自动识别模式（tips：20s后提示 是否切换到手动拍摄） |



### 识别结果回调

文字识别 OCR 识别结果的回调类，用于接收识别结果以及错误异常。

```java
///SDKKit 处理成功回调接口
///@param resultInfo 会根据不同的工作模式返回对应下的成功信息（一般都是网络回包 json 字段）
///@param reserved 预留位
typedef void (^OcrSDKKitProcessSucceedBlock)(id _Nonnull resultInfo, UIImage *resultImage,id _Nonnull reserved);

/// SDKKIt 处理失败回调接口
/// @param error 处理过程中触发的异常错误
/// @param reserved 预留位
///tips
typedef void (^OcrSDKKitProcessFailedBlock)(NSError *_Nonnull error, id _Nullable reserved);
```


>?
> 用户取消文字识别退出会在 OcrSDKKitProcessFailedBlock 回调
> - domain: "OcrSdk.UserCancelOcr" - code: 200101
> - NSLocalizedDescription : "用户主动停止文字识别"


身份证正面请求返回 resultInfo 结果示例：

```json
{
    "Name": "李明",
    "Sex": "男",
    "Nation": "汉",
    "Birth": "1987/1/1",
    "Address": "北京市石景山区高新技术园腾讯大楼",
    "IdNum": "440524******010014",
    "Authority": "",
    "ValidDate": "",
    "AdvancedInfo": "{}",
    "RequestId": "ab2c132e-9e1c-43d3-b0ef-9b4d80f00330"
 }
```

身份证反面请求返回 resultInfo 结果示例：

```json
{
    "Name": "",
    "Sex": "",
    "Nation": "",
    "Birth": "",
    "Address": "",
    "IdNum": "",
    "Authority": "赵县公安局",
    "ValidDate": "2010.07.21-2020.07.21",
    "AdvancedInfo": "{}",
    "RequestId": "0d394478-6d4d-48fc-8b19-552415bf46de"
 }
```

银行卡请求返回 resultInfo 结果示例：

```json
{
    "CardNo": "6225760088888888",
    "BankInfo": "招商银行(03080000)",
    "ValidDate": "08/2022",
    "RequestId": "46ab2e62-11e3-4d04-9fab-0abe18e7c927"
 }
```

名片请求结果返回 resultInfo 结果示例：

```json
{
    "BusinessCardInfos": [
      {
        "Name": "姓名",
        "Value": "艾米"
      },
      {
        "Name": "职位",
        "Value": "视觉设计师"
      },
      {
        "Name": "部门",
        "Value": "社交平台部"
      },
      {
        "Name": "公司",
        "Value": "Tencent腾讯"
      },
      {
        "Name": "地址",
        "Value": "深圳市南山区高新技术园科技中一路腾讯大厦"
      },
      {
        "Name": "邮箱",
        "Value": "ab***fg@tencent.com"
      },
      {
        "Name": "手机",
        "Value": "+86-133****5678"
      },
      {
        "Name": "QQ",
        "Value": "1234567"
      },
      {
        "Name": "微信",
        "Value": "amy001"
      }
    ],
    "RetImageBase64": "",
    "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs6h"
 }

```

马来西亚身份证请求结果返回 resultInfo 结果示例：

```json
{
  "Response": {
    "Name": "KAVIN ONG KHI MN",
    "ID": "710716-08-6085",
    "Address": "NO 11 PERSIARN PERAJRIT 4 TAMA PERAK 31400 IPOH ERAK",
    "Sex": "LEAKI",
    "Birthday": "",
    "Warn": [],
    "Image": "",
    "AdvancedInfo": "{\"ID\":{\"Confidence\":\"1.0000\"},\"Name\":{\"Confidence\":\"0.9996\"},\"Address\":{\"Confidence\":\"0.9997\"},\"Sex\":{\"Confidence\":\"0.9999\"}}",
    "Type": "MyKad",
    "RequestId": "c969da05-54e3-4d0a-a55d-b3ef90d4ebf5"
  }
}
```

车牌识别请求结果返回 resultInfo 结果示例：

```json
{
  "Response": {
    "Number": "京N0L9U8",
    "Confidence": 99,
    "Rect": {
      "X": 217,
      "Y": 233,
      "Width": 170,
      "Height": 21
    },
    "RequestId": "210103d3-db06-4691-abe0-c0853aae606b"
  }
}
```

车辆 VIN 码识请求结果返回 resultInfo 结果示例：

```json
{
  "Response": {
    "Vin": "LBV2B25G2E5069977",
    "RequestId": "c59d9002-6c8c-426d-b57f-a8837dee2c7c"
  }
}
```

行驶证主页和副页请求结果返回 resultInfo 结果示例：

```json
{
  "Response": {
    "FrontInfo": {
      "PlateNo": "沪AA1234",
      "VehicleType": "小型轿车",
      "Owner": "李明",
      "Address": "上海市徐汇区田林路397号腾云大厦6F",
      "UseCharacter": "非营运",
      "Model": "别克牌SGM7151LAAA",
      "Vin": "ABCDEFGH123456789",
      "EngineNo": "8B54321",
      "RegisterDate": "2011-10-10",
      "IssueDate": "",
      "Seal": "上海市公安局交通警寨总队"
    },
    "BackInfo": null,
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "820916b4-b391-40a8-9203-7ae87e3f1954"
  }
}
```

驾驶证主页和副页请求结果返回 resultInfo 结果示例：

```json
{
  "Response": {
    "Name": "李明",
    "Sex": "男",
    "Nationality": "中国",
    "Address": "上海市徐汇区田林路397号腾云大厦6F",
    "DateOfBirth": "1987-01-01",
    "IssuingAuthority": "上海市公安局交通警察总队",
    "DateOfFirstIssue": "2011-10-01",
    "Class": "C1",
    "StartDate": "2011-10-01",
    "EndDate": "2017-10-01",
    "CardCode": "440524198701010014",
    "ArchivesCode": "",
    "Record": "",
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "4ba2958b-e7cf-41c2-aafe-fdc985307f63"
  }
}
```

对于返回的错误码以及错误信息，可以参考 [错误码](https://cloud.tencent.com/document/product/866/33528)。

```json
{
  "Response": {
    "Error": {
      "Code": "AuthFailure.SignatureFailure",
      "Message": "The provided credentials could not be validated. Please check your signature is correct."
		},
  	"RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
 	}
}
```

