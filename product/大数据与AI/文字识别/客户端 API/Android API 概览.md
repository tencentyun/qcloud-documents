Android 端文字识别 SDK 主要涉及的类有 OcrSDKKit、OcrSDKConfig、OcrType、OcrModeType 以及 ISDKKitResultListener，下面对其支持的 API 做出详细说明。

### OcrSDKKit

 OcrSDKKit 是文字识别 OCR 的对外接口类，文字识别功能主要集中在这个类中。

| API                                                 | 功能描述                |
| --------------------------------------------------- | :---------------------- |
| [getInstance()](#getInstance())                     | 创建 OcrSDKKit 的单例     |
| [release()](#release())                             | 主动释放资源            |
| [getVersion()](#getVersion())                       | 获取当前 SDK 的版本号信息 |
| [initWithConfig()](#initWithConfig())               | 初始化 SDK 配置信息       |
| [updateFederationToken()](#updateFederationToken()) | 主动更新临时密钥        |
| [startProcessOcr()](#startProcessOcr())             | 启动 OCR 识别             |

<span id="getInstance()"></span>
#### getInstance()

```java
public static OcrSDKKit getInstance()
```

功能描述：

​    创建 OcrSDKKit 的单例。

返回结果：

​    OcrSDKKit 的单例对象。	



<span id="release()"></span>
#### release()

```java
public void release()
```

功能描述：

​    主动释放资源的方法，可在退出应用或者需要清理资源的时候调用。



<span id="getVersion()"></span>
#### getVersion()

```java
public final String getVersion() 
```

功能描述：

​	获取 SDK 当前的版本号。

返回结果：

​	当前 SDK 的版本信息。



<span id="initWithConfig()"></span>
#### initWithConfig()

```java
public void initWithConfig(Context context, OcrSDKConfig config)
```

功能描述：

​    初始化 SDK 信息。

传入参数：

| 参数类型                      | 参数名称 | 参数含义            |
| ----------------------------- | -------- | ------------------- |
| Context                       | context  | 应用的上下文信息    |
| [OcrSDKConfig](#OcrSDKConfig) | config   | SDK 配置参数的实体类 |



<span id="updateFederationToken()"></span>
#### updateFederationToken()

```java
public void updateFederationToken(final String tmpSecretId, final String tmpSecretKey,
                                  final String token)
```

功能描述：

​    主动更新临时密钥信息，在您与服务器兑换得到临时密钥之后主动调用设置。

传入参数：

| 参数类型 | 参数名称     | 参数含义              |
| -------- | ------------ | --------------------- |
| String   | tmpSecretId  | 临时密钥 SecretId      |
| String   | tmpSecretKey | 临时密钥 SecretKey     |
| String   | token        | 兑换后的临时访问 token |



<span id="startProcessOcr()"></span>
#### startProcessOcr()

```java
public void startProcessOcr(Activity activity, OcrType ocrType,
                                CustomConfigUi customConfigUi, ISDKKitResultListener resultListener)
```

功能描述：

​    启动默认界面进行 OCR 识别，可进行部分 UI 元素的自定义配置。(**如 CustomConfigUi 传入 null，可使用默认 UI 配置**)

传入参数：

| 参数类型                                        | 参数名称       | 参数含义                                                     |
| ----------------------------------------------- | -------------- | ------------------------------------------------------------ |
| Activity                                        | activity       | 启动 OCR 默认界面的当前界面 Activity 对象                        |
| [OcrType](#OcrType)                             | ocrType        | 启动的 OCR 识别类型                                            |
| [CustomConfigUi](#CustomConfigUi)               | customConfigUi | 启动默认界面时候传入的界面配置参数，如需完全使用默认配置，可传入 null |
| [ISDKKitResultListener](#ISDKKitResultListener) | resultListener | 用于接收 OCR 识别结果的回调对象                                |

 

<span id="OcrSDKConfig"></span>
### OcrSDKConfig

OcrSDKConfig 是在 OCR 初始化时需要传入的 SDK 的配置信息实体类，采用构建者 builder 的方式进行参数配置。

支持参数及其默认值如下：

| 类型                | 名称            | 含义                                                         | 默认值                                       |
| ------------------- | --------------- | ------------------------------------------------------------ | -------------------------------------------- |
| [OcrType](#OcrType) | OcrType         | 默认识别类型                                                 | IDCardOCR_FRONT，IDCardOCR_BACK 均代表 id_card |
| int                 | CardType        | 身份证模式时正反面0正，1反                                   | 0正面                                        |
| int                 | ModeType        | 识别模式类型：0代表手动拍摄模式，1代码自动捕获模式，2代表自动+手动模式（先使用自动超时后转为手动拍照模式） | 2代表自动 + 手动模式                           |
| int                 | AutoTimeout     | 自动捕获超时（毫秒单位，内部上限30秒）                       | 10000毫秒                                    |
| String              | ResultUrl       | 发送识别请求的 ResultUrl 信息                                  | https://ocr.tencentcloudapi.com/             |
| String              | secretId        | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                           |
| String              | secretKey       | 请求使用的密钥信息（如果使用固定密钥模式，可传入固定密钥）   | 空                                           |
| String              | tempToken       | 请求使用的临时 token 信息                                      | 空                                           |
| boolean             | CropIdCard      | 开启身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）开关 | false                                        |
| boolean             | CropPortrait    | 开启人像照片裁剪（自动抠取身份证头像区域）                   | false                                        |
| boolean             | CopyWarn        | 开启复印件告警                                               | false                                        |
| boolean             | BorderCheckWarn | 开启边框和框内遮挡告警                                       | false                                        |
| boolean             | ReshootWarn     | 开启翻拍告警                                                 | false                                        |
| boolean             | DetectPsWarn    | 开启 PS 检测告警                                               | false                                        |
| boolean             | TempIdWarn      | 开启临时身份证告警                                           | false                                        |
| boolean             | InvalidDateWarn | 开启身份证有效日期不合法告警                                 | false                                        |
| boolean             | Quality         | 开启图片质量分数（评价图片的模糊程度                         | false                                        |
| String              | RetImageType    | 图像预处理，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。 | 空                                           |
| boolean             | RetImage        | 马来西亚身份证是否返回图片                                   | false                                        |


<span id="OcrType"></span>
### OcrType

OcrType 是一个枚举类型，列举了当前文字识别 OCR 的 SDK 所支持业务类型的种类，大致如下：

| OcrTyp e类型             | 代表含义               |
| ----------------------- | ---------------------- |
| OcrType.IDCardOCR_FRONT | 身份证人像面识别模式   |
| OcrType.IDCardOCR_BACK  | 身份证国徽面识别模式   |
| OcrType.BankCardOCR     | 银行卡正面识别模式     |
| OcrType.BusinessCardOCR | 名片卡正面识别模式     |
| OcrType.MLIdCardOCR     | 马来西亚身份证识别模式 |



### OcrModeType

OcrModeType 是一个枚举类型，列举了卡片识别模式

| OcrModeType 类型        | 代表含义                                           |
| ---------------------- | -------------------------------------------------- |
| OCR_DETECT_MANUAL      | 手动拍摄模式                                       |
| OCR_DETECT_AUTO_MANUAL | 自动识别模式（tips：20s后提示 是否切换到手动拍摄） |



<span id="CustomConfigUi"></span>
### CustomConfigUi

此为用户自定义 UI 的配置类，当前支持配置的属性如下表所示，可以通过 javabean set 的方式设置。

| 类型    | 名称                   | 含义                                                       |
| ------- | ---------------------- | ---------------------------------------------------------- |
| boolean | isShowTitleBar         | 设置是否显示默认界面的标题栏                               |
| String  | titleBarText           | 设置标题栏显示的文字内容                                   |
| int     | titleColor             | 设置标题栏背景颜色（0xFFFFFF类型）                         |
| String  | remindDialogText       | 设置提醒 dialog 信息文字内容                                 |
| int     | remindConfirmColor     | 设置提醒 dialog 中确认按钮（切换模式）的颜色（0xFFFFFF类型） |
| int     | cardFrameColor         | 设置卡片预览框四角选中时的颜色（0xFFFFFF类型）             |
| int     | successRemindTextColor | 设置自定捕捉或拍摄成功后，提示的文字颜色（0xFFFFFF类型）   |
| int     | imageSelectResId       | 设置默认界面中图库中图片选择的图标资源 id                   |
| int     | lightImageOnResId      | 设置默认界面打开闪光灯的图标资源 id                         |
| int     | lightImageOffResId     | 设置默认界面关闭闪光灯的图标资源 id                         |
| int     | takePicturesResId      | 设置默认界面主动拍照按钮的图标资源 id                       |



<span id="ISDKKitResultListener"></span>
### ISDKKitResultListener

文字识别 OCR 识别结果的回调类，用于接收识别结果以及错误异常。

```java
/**
 * OCR 识别结果的回调类
 */
public interface ISDKKitResultListener {
    /**
     * orc识别成功结果
     * @param response 识别结果 Json 信息
     * @param base64Str 所识别的图片 Base64 数据
     * @param requestId 此次识别请求的唯一标识符 requestId
     */
    void onProcessSucceed(String response, String base64Str, String requestId);

    /**
     * orc识别异常
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

身份证反面请求返回response结果示例：

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

银行卡请求返回response结果示例：

```json
{
    "CardNo": "6225760088888888",
    "BankInfo": "招商银行(03080000)",
    "ValidDate": "08/2022",
    "RequestId": "46ab2e62-11e3-4d04-9fab-0abe18e7c927"
 }
```

名片请求结果返回response结果示例：

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

对于返回的错误码以及错误信息，可以参考 [错误码](https://cloud.tencent.com/document/product/866/33528) 。

