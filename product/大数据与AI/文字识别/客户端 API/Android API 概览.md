Android 端文字识别 SDK 主要涉及的类有 OcrSDKKit、OcrSDKConfig、OcrType、OcrModeType、ISDKKitResultListener、ISdkOcrEntityResultListener 以及 OCR 识别返回实体类，下面对其支持的 API 做出详细说明。

### OcrSDKKit

 OcrSDKKit 是文字识别 OCR 的对外接口类，文字识别功能主要集中在这个类中。

| API                                                 | 功能描述                |
| --------------------------------------------------- | :---------------------- |
| [getInstance()](#getInstance())                     | 创建 OcrSDKKit 的单例     |
| [release()](#release())                             | 主动释放资源            |
| [getVersion()](#getVersion())                       | 获取当前 SDK 的版本号信息 |
| [initWithConfig()](#initWithConfig())               | 初始化 SDK 配置信息       |
| [updateFederationToken()](#updateFederationToken()) | 主动更新临时密钥        |
| [startProcessOcr()](#startProcessOcr())                      | 启动 OCR 识别，返回 JsonString           |
| [startProcessOcrResultEntity()](#startProcessOcrResultEntity()) | 启动 OCR 识别，返回不同模式对应实体对象 |

#### [getInstance()](id:getInstance())

```java
public static OcrSDKKit getInstance()
```
- 功能描述：
创建 OcrSDKKit 的单例。
- 返回结果：
 OcrSDKKit 的单例对象。	



#### [release()](id:release())

```java
public void release()
```

- 功能描述：
主动释放资源的方法，可在退出应用或者需要清理资源的时候调用。




#### [getVersion()](id:getVersion())

```java
public final String getVersion() 
```

- 功能描述：
获取 SDK 当前的版本号。
- 返回结果：
当前 SDK 的版本信息。




#### [initWithConfig()](id:initWithConfig())

```java
public void initWithConfig(Context context, OcrSDKConfig config)
```

- 功能描述：
初始化 SDK 信息。
- 传入参数：

| 参数类型                      | 参数名称 | 参数含义            |
| ----------------------------- | -------- | ------------------- |
| Context                       | context  | 应用的上下文信息    |
| [OcrSDKConfig](#OcrSDKConfig) | config   | SDK 配置参数的实体类 |




#### [updateFederationToken()](id:updateFederationToken())

```java
public void updateFederationToken(final String tmpSecretId, final String tmpSecretKey,final String token)
```

- 功能描述：
主动更新临时密钥信息，在您与服务器兑换得到临时密钥之后主动调用设置。
- 传入参数：

| 参数类型 | 参数名称     | 参数含义              |
| -------- | ------------ | --------------------- |
| String   | tmpSecretId  | 临时密钥 SecretId      |
| String   | tmpSecretKey | 临时密钥 SecretKey     |
| String   | token        | 兑换后的临时访问 token |




#### [startProcessOcr()](id:startProcessOcr())

```java
public void startProcessOcr(Activity activity, OcrType ocrType, CustomConfigUi customConfigUi, ISDKKitResultListener resultListener)
```

- 功能描述：
启动默认界面进行 OCR 识别，可进行部分 UI 元素的自定义配置。(**如 CustomConfigUi 传入 null，可使用默认 UI 配置**)
- 传入参数：

| 参数类型                                        | 参数名称       | 参数含义                                                     |
| ----------------------------------------------- | -------------- | ------------------------------------------------------------ |
| Activity                                        | activity       | 启动 OCR 默认界面的当前界面 Activity 对象                        |
| [OcrType](#OcrType)                             | ocrType        | 启动的 OCR 识别类型                                            |
| [CustomConfigUi](#CustomConfigUi)               | customConfigUi | 启动默认界面时候传入的界面配置参数，如需完全使用默认配置，可传入 null |
| [ISDKKitResultListener](#ISDKKitResultListener) | resultListener | 用于接收 OCR 识别结果的回调对象                                |



#### [startProcessOcrResultEntity()](id:startProcessOcrResultEntity())

```java
public <T extends OcrResult> void startProcessOcrResultEntity(Activity activity, OcrType ocrType,CustomConfigUi customConfigUi, Class<T> entity,ISdkOcrEntityResultListener<T> ocrEntityResultListener) 
```

- 功能描述：
启动默认界面进行 OCR 识别，可进行部分 UI 元素的自定义配置。(**如 CustomConfigUi 传入 null，可使用默认 UI 配置**)，根据指定不同的识别模式返回不同识别结果类型实体。
- 传入参数：

| 参数类型                                                    | 参数名称                | 参数含义                                                     |
| ----------------------------------------------------------- | ----------------------- | ------------------------------------------------------------ |
| Activity                                                    | activity                | 启动 OCR 默认界面的当前界面 Activity 对象                    |
| [OcrType](#OcrType)                                         | ocrType                 | 启动的 OCR 识别类型                                          |
| [CustomConfigUi](#CustomConfigUi)                           | customConfigUi          | 启动默认界面时候传入的界面配置参数，如需完全使用默认配置，可传入 null |
| Class < T >                                                 | entity                  | OCR 识别结果的实体类                                          |
| [ISdkOcrEntityResultListener](#ISdkOcrEntityResultListener) | ocrEntityResultListener | 用于接收 OCR 识别结果的回调对象                              |
| < T > extends OcrResult                                     | < T >                   | OCR 识别识别结果 OcrResult 的子类型                          |

OCR 识别结果的实体类，OCR 识别识别结果 OcrResult 的子类型包括：

[IdCardOcrResult](#IdCardOcrResult)、[BankCardOcrResult](#BankCardOcrResult)、[BusinessCardOcrResult](#BusinessCardOcrResult)、[MalaysiaIdCardOcrResult](#MalaysiaIdCardOcrResult)、[VinOcrResult](#VinOcrResult)、[CarLicensePlateResult](#CarLicensePlateResult)、[DriverLicenseCardResult](#DriverLicenseCardResult)、[VehicleLicenseCardResult](#VehicleLicenseCardResult)



### [OcrSDKConfig](id:OcrSDKConfig)

OcrSDKConfig 是在 OCR 初始化时需要传入的 SDK 的配置信息实体类，采用构建者 builder 的方式进行参数配置。

支持参数及其默认值如下：

| 类型                | 名称            | 含义                                                         | 默认值                                         |
| ------------------- | --------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| [OcrType](#OcrType) | OcrType         | 默认识别类型                                                 | IDCardOCR_FRONT，IDCardOCR_BACK 均代表 id_card |
| int                 | CardType        | 身份证模式时正反面0正，1反                                   | 0正面                                          |
| int                 | ModeType        | 识别模式类型：0代表手动拍摄模式，1代码自动捕获模式，2代表自动+手动模式（先使用自动超时后转为手动拍照模式） | 2代表自动 + 手动模式                           |
| int                 | AutoTimeout     | 自动捕获超时（毫秒单位，最少设置5秒，内部上限30秒）          | 20000毫秒                                      |
| String              | ResultUrl       | 发送识别请求的 ResultUrl 信息                                | https://ocr.tencentcloudapi.com/               |
| String              | secretId        | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                             |
| String              | secretKey       | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                             |
| String              | tempToken       | 请求使用的临时 token 信息                                    | 空                                             |
| boolean             | CropIdCard      | 开启身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）开关 | false                                          |
| boolean             | CropPortrait    | 开启人像照片裁剪（自动抠取身份证头像区域）                   | false                                          |
| boolean             | CopyWarn        | 开启复印件告警                                               | false                                          |
| boolean             | BorderCheckWarn | 开启边框和框内遮挡告警                                       | false                                          |
| boolean             | ReshootWarn     | 开启翻拍告警                                                 | false                                          |
| boolean             | DetectPsWarn    | 开启 PS 检测告警                                             | false                                          |
| boolean             | TempIdWarn      | 开启临时身份证告警                                           | false                                          |
| boolean             | InvalidDateWarn | 开启身份证有效日期不合法告警                                 | false                                          |
| boolean             | Quality         | 开启图片质量分数（评价图片的模糊程度）                       | false                                          |
| String              | RetImageType    | 图像预处理，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。 | 空                                             |
| boolean             | RetImage        | 马来西亚身份证是否返回图片                                   | false                                          |



### [OcrType](id:OcrType)

OcrType 是一个枚举类型，列举了当前文字识别 OCR 的 SDK 所支持业务类型的种类，大致如下：

| OcrType类型                     | 代表含义               | 对应结果实体类                                        |
| ------------------------------- | ---------------------- | ----------------------------------------------------- |
| OcrType.IDCardOCR_FRONT         | 身份证人像面识别模式   | [IdCardOcrResult](#IdCardOcrResult)                   |
| OcrType.IDCardOCR_BACK          | 身份证国徽面识别模式   | [IdCardOcrResult](#IdCardOcrResult)                   |
| OcrType.BankCardOCR             | 银行卡正面识别模式     | [BankCardOcrResult](#BankCardOcrResult)               |
| OcrType.BusinessCardOCR         | 名片卡正面识别模式     | [BusinessCardOcrResult](#BusinessCardOcrResult)       |
| OcrType.MLIdCardOCR             | 马来西亚身份证识别模式 | [MalaysiaIdCardOcrResult](#MalaysiaIdCardOcrResult)   |
| OcrType.VinOCR                  | 车辆的 VIN 识别模式      | [VinOcrResult](#VinOcrResult)                         |
| OcrType.LicensePlateOCR         | 车辆的车牌识别模式     | [CarLicensePlateResult](#CarLicensePlateResult)       |
| OcrType.DriverLicenseOCR_FRONT  | 驾驶证主页识别模式     | [DriverLicenseCardResult](#DriverLicenseCardResult)   |
| OcrType.DriverLicenseOCR_BACK   | 驾驶证副页识别模式     | [DriverLicenseCardResult](#DriverLicenseCardResult)   |
| OcrType.VehicleLicenseOCR_FRONT | 行驶证主页识别模式     | [VehicleLicenseCardResult](#VehicleLicenseCardResult) |
| OcrType.VehicleLicenseOCR_BACK  | 行驶证副页识别模式     | [VehicleLicenseCardResult](#VehicleLicenseCardResult) |



### OcrModeType

OcrModeType 是一个枚举类型，列举了卡片识别模式

| OcrModeType 类型        | 代表含义                                           |
| ---------------------- | -------------------------------------------------- |
| OCR_DETECT_MANUAL      | 手动拍摄模式                                       |
| OCR_DETECT_AUTO_MANUAL | 自动识别模式（tips：20s后提示 是否切换到手动拍摄） |




### [CustomConfigUi](id:CustomConfigUi)

此为用户自定义 UI 的配置类，当前支持配置的属性如下表所示，可以通过 javabean set 的方式设置。

| 类型    | 名称                   | 含义                                                         |
| ------- | ---------------------- | ------------------------------------------------------------ |
| boolean | isShowTitleBar         | 设置是否显示默认界面的标题栏                                 |
| String  | titleBarText           | 设置标题栏显示的文字内容                                     |
| int     | titleColor             | 设置标题栏背景颜色（0xFFFFFF类型）                           |
| String  | remindDialogText       | 设置提醒 dialog 信息文字内容                                 |
| int     | remindConfirmColor     | 设置提醒 dialog 中确认按钮（切换模式）的颜色（0xFFFFFF类型） |
| int     | cardFrameColor         | 设置卡片预览框四角选中时的颜色（0xFFFFFF类型）               |
| int     | successRemindTextColor | 设置自定捕捉或拍摄成功后，提示的文字颜色（0xFFFFFF类型）     |
| Int     | statusBarColor         | 设置状态栏背景颜色（0xFFFFFF类型）                           |
| int     | imageSelectResId       | 设置默认界面中图库中图片选择的图标资源 id                    |
| int     | lightImageOnResId      | 设置默认界面打开闪光灯的图标资源 id                          |
| int     | lightImageOffResId     | 设置默认界面关闭闪光灯的图标资源 id                          |
| int     | takePicturesResId      | 设置默认界面主动拍照按钮的图标资源 id                        |
| int     | backActionIconResId    | 设置默认界面返回按钮的图标资源id                             |
| boolean | isRemoveAlbum          | 设置默认界面是否显示相册选取按钮，默认为显示                 |
| boolean | isRemoveFlash          | 设置默认界面是否显示闪光灯点击按钮，默认显示                 |
| boolean | isLandscape            | 设置默认界面为横屏模式，默认false                            |
| boolean | isShowTips             | 设置默认界面是否显示tips框，默认true                         |
| String  | showTipsText           | 设置提醒tips的文字内容，默认“请避免识别内容折角、遮挡和反光” |
| boolean | isShowStatusBar        | 设置默认界面是否显示状态栏，默认true                         |



### [IdCardOcrResult](id:IdCardOcrResult)

身份证 OCR 识别的结果实体对象

| 类型   | 名称      | 含义     |
| ------ | --------- | -------- |
| String | name      | 姓名     |
| String | sex       | 性别     |
| String | nation    | 民族     |
| String | birth     | 出生日期 |
| String | address   | 住址     |
| String | idNum     | 身份证号 |
| String | authority | 发证机关 |
| String | validDate | 有效日期 |
| String | requestId | 请求 id   |
| String | advancedInfo | 扩展字段内容 [参考官网](https://cloud.tencent.com/document/product/866/33524) |



### [BankCardOcrResult](id:BankCardOcrResult)

银行卡 OCR 识别的结果实体对象

| 类型   | 名称      | 含义     |
| ------ | --------- | -------- |
| String | bankInfo       | 银行信息                   |
| String | cardNo         | 银行卡号                   |
| String | validDate      | 有效日期                   |
| String | requestId      | 请求id                     |
| String | cardType       | 银行卡类型                 |
| String | cardName       | 银行卡名称                 |
| String | borderCutImage | 切片图片数据，取不到为null |
| String | cardNoImage | 卡号图片数据，取不到为null |



### [BusinessCardOcrResult](id:BusinessCardOcrResult)

名片 OCR 识别的结果实体对象，主要包含一些列的 [BusinessCardItems](#BusinessCardItems) 对象。

| 类型                                            | 名称              | 含义         |
| ----------------------------------------------- | ----------------- | ------------ |
| List< [BusinessCardItems](#BusinessCardItems) > | businessCardInfos | 名片元素列表 |
| String                                          | requestId         | 请求 id       |



### [BusinessCardItems](id:BusinessCardItems)

名片 OCR 识别的基本元素，包括名称与信息。

| 类型   | 名称  | 含义     |
| ------ | ----- | -------- |
| String | name  | 子项名称 |
| String | value | 子项内容 |



### [MalaysiaIdCardOcrResult](id:MalaysiaIdCardOcrResult)

马来身份证 OCR 识别的结果实体对象

| 类型            | 名称      | 含义       |
| --------------- | --------- | ---------- |
| String          | name      | 姓名       |
| String          | idNumber  | 身份证号   |
| String          | address   | 地址       |
| String          | type      | 证件类型   |
| String          | sex       | 性别       |
| String          | birthday  | 生日       |
| List< Integer > | warn      | 警告码列表 |
| String          | requestId | 请求 id     |



### [VinOcrResult](id:VinOcrResult)

车辆的 VIN 的识别的结果实体对象

| 类型   | 名称 | 含义        |
| ------ | ---- | ----------- |
| String | vin  | 车辆的 VIN 码 |



### [CarLicensePlateResult](id:CarLicensePlateResult)

| 类型                | 名称       | 含义                         |
| ------------------- | ---------- | ---------------------------- |
| String              | number     | 车牌的字符串信息             |
| int                 | confidence | 本次识别的置信度             |
| [OcrRect](#OcrRect) | rect       | 文本行在原图片中的像素坐标框 |



### [OcrRect](id:OcrRect)

矩形坐标

| 类型 | 名称   | 含义          |
| ---- | ------ | ------------- |
| int  | x      | 左上角x的坐标 |
| int  | y      | 左上角y的坐标 |
| int  | width  | 宽度          |
| int  | height | 高度          |



### [DriverLicenseCardResult](id:DriverLicenseCardResult)

驾驶证识别的结果实体类

| 类型            | 名称              | 含义             |
| --------------- | ----------------- | ---------------- |
| String          | name              | 姓名             |
| String          | sex               | 性别             |
| String          | nationality       | 国籍             |
| String          | address           | 地址             |
| String          | dateOfBirth       | 出生日期         |
| String          | dateOfFirstIssue  | 初次领证日期     |
| String          | classType         | 准驾车类型       |
| String          | startDate         | 有效期开始的时间 |
| String          | endDate           | 有效期截止日期   |
| String          | cardCode          | 证件号           |
| String          | archivesCode      | 档案编号         |
| String          | record            | 记录             |
| String          | issuingAuthority  | 发证单位         |
| List< Integer > | recognizeWarnCode | 识别的警告码列表 |
| List< String >  | recognizeWarnMsg  | 识别的警告码说明 |



### [VehicleLicenseCardResult](id:VehicleLicenseCardResult)

行驶证识别的结果实体类

| 类型                                  | 名称              | 含义                       |
| ------------------------------------- | ----------------- | -------------------------- |
| [VehicleFrontInfo](#VehicleFrontInfo) | vehicleFrontInfo  | 行驶证的主页信息           |
| [VehicleBackInfo](#VehicleBackInfo)   | vehicleBackInfo   | 行驶证的副页信息           |
| List< Integer >                       | recognizeWarnCode | 识别的Code告警码列表和释义 |
| List< String >                        | recognizeWarnMsg  | 识别的警告码说明           |



### [VehicleFrontInfo](id:VehicleFrontInfo)

行驶证的主页的识别结果实体类

| 类型   | 名称         | 含义         |
| ------ | ------------ | ------------ |
| String | plateNo      | 号牌号码     |
| String | vehicleType  | 车辆类型     |
| String | owner        | 所有人       |
| String | address      | 住址         |
| String | useCharacter | 使用性质     |
| String | model        | 品牌型号     |
| String | vin          | 车辆识别代号 |
| String | engineNo     | 发动机编号   |
| String | registerDate | 注册日期     |
| String | IssueDate    | 发证日期     |
| String | seal         | 印章         |



### [VehicleBackInfo](id:VehicleBackInfo)

行驶证副页的识别结果实体类

| 类型   | 名称           | 含义         |
| ------ | -------------- | ------------ |
| String | plateNo        | 号牌号码     |
| String | fileNo         | 档案编号     |
| String | allowNum       | 核定人数     |
| String | totalMass      | 总质量       |
| String | curbWeight     | 整备质量     |
| String | loadQuality    | 核定载的质量 |
| String | externalSize   | 外廓尺寸     |
| String | marks          | 备注         |
| String | record         | 检验记录     |
| String | totalQuasiMass | 总牵引质量   |





### [ISDKKitResultListener](id:ISDKKitResultListener)

文字识别 OCR 识别结果的回调类，用于接收识别结果以及错误异常。

```java
/**
 * OCR 识别结果的回调类
 */
public interface ISDKKitResultListener {
    /**
     * orc 识别成功结果
     * @param response 识别结果 Json 信息
     * @param base64Str 所识别的图片 Base64 数据
     * @param requestId 此次识别请求的唯一标识符 requestId
     */
    void onProcessSucceed(String response, String base64Str, String requestId);

    /**
     * orc 识别异常
     * @param errorCode 错误码
     * @param message 异常信息
     * @param requestId 此次请求的唯一标识符 requestId
     */
    void onProcessFailed(String errorCode, String message, String requestId);
}
```

身份证正面请求返回 response 结果示例：

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

身份证反面请求返回 response 结果示例：

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

银行卡请求返回 response 结果示例：

```json
{
    "BankInfo": "招商银行(03080000)",
    "ValidDate": "07/2023",
    "CardType": "贷记卡",
    "CardName": "招商银行信用卡",
    "BorderCutImage": null,
    "CardNoImage": null,
    "WarningCode": [
      -9110
    ],
    "CardNo": "6225768888888888",
    "RequestId": "68f8fcbf-6004-0111a-ac18-6f1a9308fs100mab"
  }
```

名片请求结果返回 response 结果示例：

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

马来西亚身份证识别返回 response 结果示例：

```json
 {
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
```

车辆的 VIN 返回 response 结果示例：

```json
{
  "Response": {
    "Vin": "LBV2B25G2E5069977",
    "RequestId": "c59d9002-6c8c-426d-b57f-a8837dee2c7c"
  }
}
```

车辆的车牌返回 response 结果示例：

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

驾驶证识别的response结果示例：

```json
{
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
```

行驶证识别主页识别的response结果示例：

```json
{
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
```

行驶证识别副页识别的response结果示例：

```json
{
    "FrontInfo": null,
    "BackInfo": {
      "PlateNo": "皖AC4L50",
      "FileNo": "A00-00476807",
      "AllowNum": "5人",
      "TotalMass": "1837kg",
      "CurbWeight": "1431kg",
      "LoadQuality": "--",
      "ExternalSize": "4620×1780×1498mm",
      "TotalQuasiMass": "--",
      "Marks": "",
      "Record": "检验有效期至2015年11月皖A(4S)"
    },
    "RecognizeWarnCode": [
      -9106
    ],
    "RecognizeWarnMsg": [
      "WARN_DRIVER_LICENSE_PS_CARD"
    ],
    "RequestId": "e2ebfaa0-19d3-4d2b-9ed8-7c7c21eb2b74"
  }
```

对于返回的错误码以及错误信息，可以参考 [错误码](https://cloud.tencent.com/document/product/866/33528) 。

<span id="ISdkOcrEntityResultListener"></span>

### ISdkOcrEntityResultListener

文字识别 OCR 识别结果的回调类，用于接收识别结果的实体类以及错误异常。

```java
public interface ISdkOcrEntityResultListener<T> {

    /**
     * orc 识别成功结果
     *
     * @param t 返回实体信息
     * @param base64Str 所识别的图片 Base64 数据
     */
    void onProcessSucceed(T t, String base64Str);

    /**
     * orc 识别异常
     *
     * @param errorCode 错误码
     * @param message 异常信息
     * @param requestId 此次请求的唯一标识符 requestId
     */
    void onProcessFailed(String errorCode, String message, String requestId);
}
```



### 错误码

#### 公共错误码

| 错误码                            | 说明                                                         |
| :-------------------------------- | :----------------------------------------------------------- |
| UnsupportedOperation              | 操作不支持。                                                 |
| ResourceInUse                     | 资源被占用。                                                 |
| InternalError                     | 内部错误。                                                   |
| RequestLimitExceeded              | 请求的次数超过了频率限制。                                   |
| AuthFailure.SecretIdNotFound      | 密钥不存在。 请在控制台检查密钥是否已被删除或者禁用，如状态正常，请检查密钥是否填写正确，注意前后不得有空格。 |
| LimitExceeded                     | 超过配额限制。                                               |
| NoSuchVersion                     | 接口版本不存在。                                             |
| ResourceNotFound                  | 资源不存在。                                                 |
| AuthFailure.SignatureFailure      | 签名错误。 签名计算错误，请对照调用方式中的签名方法文档检查签名计算过程。 |
| AuthFailure.SignatureExpire       | 签名过期。Timestamp 和服务器时间相差不得超过五分钟，请检查本地时间是否和标准时间同步。 |
| UnsupportedRegion                 | 接口不支持所传地域。                                         |
| UnauthorizedOperation             | 未授权操作。                                                 |
| InvalidParameter                  | 参数错误。                                                   |
| ResourceUnavailable               | 资源不可用。                                                 |
| AuthFailure.MFAFailure            | MFA 错误。                                                   |
| AuthFailure.UnauthorizedOperation | 请求未授权。请参考 [CAM](https://cloud.tencent.com/document/product/598) 文档对鉴权的说明。 |
| AuthFailure.InvalidSecretId       | 密钥非法（不是云 API 密钥类型）。                            |
| AuthFailure.TokenFailure          | token 错误。                                                 |
| DryRunOperation                   | DryRun 操作，代表请求将会是成功的，只是多传了 DryRun 参数。  |
| FailedOperation                   | 操作失败。                                                   |
| UnknownParameter                  | 未知参数错误。                                               |
| UnsupportedProtocol               | HTTP(S)请求协议错误，只支持 GET 和 POST 请求。               |
| InvalidParameterValue             | 参数取值错误。                                               |
| InvalidAction                     | 接口不存在。                                                 |
| MissingParameter                  | 缺少参数错误。                                               |
| ResourceInsufficient              | 资源不足。                                                   |

#### 业务错误码

| 错误码                                           | 说明                                                   |
| :----------------------------------------------- | :----------------------------------------------------- |
| FailedOperation.ArrearsError                     | 帐号已欠费。                                           |
| FailedOperation.CountLimitError                  | 今日次数达到限制。                                     |
| FailedOperation.DetectFailed                     | 检测失败。                                             |
| FailedOperation.DownLoadError                    | 文件下载失败。                                         |
| FailedOperation.EmptyImageError                  | 图片内容为空。                                         |
| FailedOperation.EngineRecognizeTimeout           | 引擎识别超时。                                         |
| FailedOperation.IdCardInfoIllegal                | 身份证信息不合法（身份证号、姓名字段校验非法等）。     |
| FailedOperation.ImageBlur                        | 图片模糊。                                             |
| FailedOperation.ImageDecodeFailed                | 图片解码失败。                                         |
| FailedOperation.ImageNoBusinessCard              | 照片未检测到名片。                                     |
| FailedOperation.ImageNoIdCard                    | 图片中未检测到身份证。                                 |
| FailedOperation.ImageNoText                      | 图片中未检测到文本。                                   |
| FailedOperation.ImageSizeTooLarge                | 图片尺寸过大，请参考输出参数中关于图片大小限制的说明。 |
| FailedOperation.InvoiceMismatch                  | 发票数据不一致。                                       |
| FailedOperation.LanguageNotSupport               | 输入的 Language 不支持。                                 |
| FailedOperation.MultiCardError                   | 照片中存在多张卡。                                     |
| FailedOperation.OcrFailed                        | OCR 识别失败。                                          |
| FailedOperation.UnKnowError                      | 未知错误。                                             |
| FailedOperation.UnOpenError                      | 服务未开通。                                           |
| InvalidParameter.ConfigFormatError               | Config 不是有效的 JSON 格式。                             |
| InvalidParameter.EngineImageDecodeFailed         | 图片解码失败。                                         |
| InvalidParameter.InvalidGTINError                | 无效的 GTIN。                                           |
| InvalidParameterValue.InvalidParameterValueLimit | 参数值错误。                                           |
| LimitExceeded.TooLargeFileError                  | 文件内容太大。                                         |
| ResourceNotFound.NoInvoice                       | 发票不存在。                                           |
| ResourcesSoldOut.ChargeStatusException           | 计费状态异常。                                         |

#### SDK 本地错误码

| 错误码               | 说明                     |
| -------------------- | ------------------------ |
| OcrSdk.UserCancelOcr | 用户主动停止文字识别     |
| OcrSdk.InnerOcrError | 文字识别内部错误，请重试 |
