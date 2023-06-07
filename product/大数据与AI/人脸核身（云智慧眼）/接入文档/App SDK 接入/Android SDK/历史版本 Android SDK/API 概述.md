Android 端慧眼 SDK 主要涉及的类主要包含 HuiYanAuth、AuthConfig、HuiYanAuthResultListener、CreateFaceIdToken 以及 PageColorStyle，下面对其支持的 API 做出详细说明。
 
## HuiYanAuth
HuiYanAuth 为慧眼 SDK 的对外接口类，主要逻辑也都是调用此类完成。

| API                                                          | 功能描述                          |
| ------------------------------------------------------------ | --------------------------------- |
| [init()](#init())                                            | 初始化接口                        |
| [release()](#release())                                      | 资源释放接口                      |
| [setFaceIdTokenCreateFunction()](#setFaceIdTokenCreateFunction()) | 设置主动获取客户 FaceIdToken 的接口 |
| [startHuiYanAuth()](#startHuiYanAuth())                      | 启动活体核身检测的接口            |

### init()
```java
public static void init(Context context)
```
功能介绍：慧眼 SDK 的初始化接口。
传入参数：

| 参数类型 | 参数名称 | 参数含义        |
| -------- | -------- | --------------- |
| Context  | context  | App 的上下文信息 |



### release()
```java
public static void release() 
```
功能介绍：慧眼 SDK 资源释放的接口。


### setFaceIdTokenCreateFunction()
```java
public static void setFaceIdTokenCreateFunction(CreateFaceIdToken createFunction)
```
功能介绍：设置主动获取客户 FaceIdToken 的接口。
传入参数：

| 参数类型                                | 参数名称       | 参数含义                      |
| --------------------------------------- | -------------- | ----------------------------- |
| [CreateFaceIdToken](#CreateFaceIdToken) | createFunction | 主动获取客户 FaceIdToken 的回调 |


### startHuiYanAuth()
```java
public static void startHuiYanAuth(AuthConfig authConfig, HuiYanAuthResultListener listener) 
```

功能介绍：启动活体核身检测的接口。
传入参数：

| 参数类型                                              | 参数名称   | 参数含义                   |
| ----------------------------------------------------- | ---------- | -------------------------- |
| [AuthConfig](#AuthConfig)                             | authConfig | 启动活体核身的参数         |
| [HuiYanAuthResultListener](#HuiYanAuthResultListener) | listener   | 接受活体核身检测的结果回调 |


## AuthConfig
AuthConfig 是在启动慧眼 SDK 时的配置实体类，主要包含了以下属性。

| 类型                              | 名称                 | 含义                                 | 默认值                                   |
| --------------------------------- | -------------------- | ------------------------------------ | ---------------------------------------- |
| PageColorStyle                    | pageColorStyle       | 此次人脸核身检测的配色               | PageColorStyle.Light                     |
| String                            | authLicense          | 客户申请的用户核审授权的 License 文件名 | 空                                       |
| long                              | authTimeOutMs        | 设置活体检测的超时时间               | 10000毫秒（10秒）                        |
| String                            | useCustomerModelPath | 客户自定义的模型文件夹地址           | 空（如果为空需要依赖模型 aar）            |
| [CustomerConfig](#CustomerConfig) | customerConfig       | 客户自定义的一些内容                 | null                                     |
| [LanguageStyle](#LanguageStyle)   | languageStyle        | 核身页面显示的语言                   | LanguageStyle.SIMPLIFIED_CHINESE（简中） |
| boolean                           | isOpenLog            | 是否记录关键 log                      | true                                     |



## PageColorStyle
默认核身界面默认配色的枚举类，当前主要包括了两种配色，白色系与黑暗色系。

| PageColorStyle 类型   | 含义       |
| -------------------- | ---------- |
| PageColorStyle.Light | 亮色调配色 |
| PageColorStyle.Dark  | 暗色调配色 |



## CustomerConfig

| 类型    | 名称                 | 含义                                                         | 默认值 |
| ------- | -------------------- | ------------------------------------------------------------ | ------ |
| String  | authTips             | 核身页面客户自定义的提示信息（如有敏感信息则不会显示）       | 空     |
| int     | authTipsTextColor    | 核身页面客户自定义的提示信息的颜色（0xFFFFFF类型）           | -1     |
| boolean | isHiddenResultRage   | 设置是否需要隐藏核身结果页（隐藏的话，则不会显示结果页，直接进行回调） | false  |
| boolean | isHiddenErrorDialog  | 设置是否隐藏错误的dialog                                     | false  |
| boolean | isHiddenProtocolPage | 设置是否隐藏协议展示的页面                                   | false  |


## LanguageStyle
核身界面模式显示的语言类型，当前主要包括了，自动（跟随系统）、英文与简体中文。

| 类型                              | 含义             |
| --------------------------------- | ---------------- |
| LanguageStyle.AUTO                | 自动根据系统语言 |
| LanguageStyle.ENGLISH             | 英语             |
| LanguageStyle.SIMPLIFIED_CHINESE  | 简体中文         |
| LanguageStyle.TRADITIONAL_CHINESE | 繁体中文         |



## CreateFaceIdToken
用于提供给客户使用的获取 FaceIdToken 的接口类，客户需要返回客户获取到的 FaceIdToken 的值。
```java
HuiYanAuth.setFaceIdTokenCreateFunction(new CreateFaceIdToken() {
    @Override
    public String getCustomerFaceIdToken() {
        // 补充获取FaceIdToken的逻辑，返回客户获得到的faceIdToken
        return currentToken;
    }
});
```


## HuiYanAuthResultListener
用于接受活体核身认证的结果监听类。
```java
public interface HuiYanAuthResultListener {

    /**
     * 核身通过
     *
     * @param faceIdToken 本次核身使用的faceIdToken
     */
    void onSuccess(String faceIdToken);

    /**
     * 识别失败
     *
     * @param errorCode 错误码
     * @param errorMsg 错误信息
     * @param faceIdToken 本次核身使用的faceIdToken
     */
    void onFail(int errorCode, String errorMsg, String faceIdToken);
}
```


## 错误码
这里是 SDK 在失败回调中的错误码，目前慧眼 SDK 包含的错误码与其含义如下：

| 错误码                                | 错误码值 | 错误码含义                                                   |
| ------------------------------------- | -------- | ------------------------------------------------------------ |
| HY_NETWORK_ERROR                      | 210      | 网络请求出现异常                                             |
| HY_LOCAL_REF_FAILED_ERROR             | 211      | 本地初始化 SDK 时，检测失败，常见异常不存在 license 文件或者 license 过期 |
| HY_USER_CANCEL_ERROR                  | 212      | 用户主动取消核身流程                                         |
| HY_INNER_ERROR_CODE                   | 213      | SDK 内部产生的异常，终止了核身流程                            |
| HY_DO_NOT_CHANGE_ERROR                | 214      | 在核身过程中切换应用发生终止流程的异常                       |
| HY_CAMERA_PERMISSION_ERROR            | 215      | 获取摄像头过程中发生异常                                     |
| HY_INIT_SDK_ERROR                     | 216      | 未调用 init()方法，直接调用了                                 |
| HY_VERIFY_LOCAL_ERROR                 | 217      | 本地人脸检测失败                                             |
| HY_PERMISSION_CHECK_ERROR             | 218      | 本地 SDK 所需要的权限不足                                      |
| HY_APP_STOP_ERROR                     | 219      | 集成者主动终止核身流程，startAuthByLightData的reflectSequence 为 null 时 |
| HY_CHECK_LIVE_DATA_ERROR              | 220      | 传入的光线序列参数校验失败                                   |
| HY_INITIALIZATION_PARAMETER_EXCEPTION | 221      | 在未获取设备配置的前提下，直接调用了设置光线序列参数的方法时，会出现的异常 |
| HY_VERIFY_LOCAL_TIME_OUT              | 222      | 本地核身动作检测超时                                         |
| HY_PREPARE_TIME_OUT                   | 223      | 准备过程超时（启动摄像头到第一次检测到人脸的时间超时）       |
| HY_CHECK_PERMISSION_ERROR             | 224      | SDK内部申请摄像头权限失败                                    |
| HY_ACTION_REFLECTIVE_SDK_ERROR        | 228      | 内部算法本地检测识别失败                                     |


