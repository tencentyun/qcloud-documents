智能扫码的 API 主要涉及 QBarCodeKit、ScanCodeDetectView 以及回调接口类，下面对其支持的 API 作出说明。

### QBarCodeKit

 QBarCodeKit 是智能扫码的对外接口类，智能扫码对外的功能大多在此接口类中包括，基础 API 如下。

| API                                               | 功能描述                                   |
| ------------------------------------------------- | ------------------------------------------ |
| [getInstance()](#getInstance())                   | 创建 QBarCodeKit 的单例                      |
| [getVersion()](#getVersion())                     | 获取 SDK 当前的版本号                        |
| [initQBarCodeKit()](#initQBarCodeKit())           | 初始化 SDK，并完成鉴权认证                  |
| [startDefaultQBarScan()](#startDefaultQBarScan()) | 启动 SDK 提供的默认界面进行扫码              |
| [decodeImageWithQBar()](#decodeImageWithQBar())   | 可以识别传入图片中存在的二维码、条形码信息 |

<span id="getInstance()"></span>
#### getInstance()

```java
public static QBarCodeKit getInstance()
```

功能描述：

创建 QBarCodeKit 的单例。

返回结果：

QBarCodeKit 的单例对象。


<span id="getVersion()"></span>
#### getVersion()

```java
public String getVersion()
```

功能描述：

获取 SDK 当前的版本号。

返回结果：

当前 SDK 的版本信息。


<span id="initQBarCodeKit()"></span>
#### initQBarCodeKit()

```java
public void initQBarCodeKit(String secretId, String secretKey, final Context context, final OnSdkKitInitCallback callback
```

功能描述：

初始化 SDK，并完成鉴权认证操作。

传入参数：

**secretId** 用户在后台申请的 secretId 信息

**secretKey** 用户在后台申请后获取的专属密钥信息

**context** 当前环境的上下文信息

**callback** 初始化与鉴权的结果回调类 [OnSdkKitInitCallback](#OnSdkKitInitCallback)


<span id="startDefaultQBarScan()"></span>
#### startDefaultQBarScan()

```java
public void startDefaultQBarScan(Activity context, QBarSdkCallback callback)
```

功能描述：

启动 SDK 提供的默认界面进行扫码，并通过回调获取扫码结果。

传入参数：

**context** 调用该函数界面的 Activity 对象用来启动默认扫码界面

**callback**  用来接收扫码结果的回调类 [QBarSdkCallback](#QBarSdkCallback)。


<span id="decodeImageWithQBar()"></span>
#### decodeImageWithQBar()

```java
public List<ScanResult> decodeImageWithQBar(Bitmap bitmap, Context context)
```

功能描述：

识别传入图片中存在的二维码、条形码信息。

传入参数：

**bitmap** 需要识别的图像信息

**context** 当前应用的上下文信息

返回结果：

**List<ScanResult>**	ScanResult 图片识别结果的列表

ScanResult 包含属性及含义：

**String data** 识别到的内容信息

**String charset** 内容包含的字符集

**String typeName** 所扫描图片包含的二维码类型



### ScanCodeDetectView

ScanCodeDetectView 是智能扫码 SDK 提供的一个支持扫码的 View 组件，主要目的是为了满足用户将扫码功能嵌入到自定义界面的需求。基本 API 介绍如下。

| API                                             | 功能描述                                     |
| ----------------------------------------------- | -------------------------------------------- |
| [setScanCallBack()](#setScanCallBack())         | 为 ScanCodeDetectView 设置扫码回调接收类       |
| [setScanTipsTVText()](#setScanTipsTVText())     | 主动在 ScanCodeDetectView 上显示 tips 信息       |
| [showNoContentResult()](#showNoContentResult()) | 主动在 ScanCodeDetectView 上显示无识别结果提示 |
| [onCreate()](#onCreate())                       | 生命周期 onCreate 对应方法                     |
| [onResume()](#onResume())                       | 生命周期 onResume 对应方法                     |
| [onPause()](#onPause())                         | 生命周期 onPause 对应方法                      |
| [onStop()](#onStop())                           | 生命周期 onStop 对应方法                       |
| [onDestroy()](#onDestroy())                     | 生命周期 onDestroy 对应方法                    |


<span id="setScanCallBack()"></span>
#### setScanCallBack()

```java
public void setScanCallBack(QBarSdkCallback callback)
```

功能描述：

为 ScanCodeDetectView 设置扫码回调接收类。

传入参数：

**callBack** 识别结果接收回调类 [QBarSdkCallback](#QBarSdkCallback)。


<span id="setScanTipsTVText()"></span>
#### setScanTipsTVText()

```java
public void setScanTipsTVText(String text)
```

功能描述：

主动在 ScanCodeDetectView 上显示 tips 信息。

传入参数：

**text** 需要显示 tips 的信息。


<span id="showNoContentResult()"></span>
#### showNoContentResult()

```java
public void showNoContentResult() 
```

功能描述：

主动在 ScanCodeDetectView 上显示无识别结果的提示。	


<span id="onCreate()"></span>
#### onCreate()

```java
public void onCreate() 
```

功能描述：

生命周期 onCreate 对应方法，需在界面的对应生命周期函数内调用。


<span id="onResume()"></span>
#### onResume()

```java
public void onResume()
```

功能描述：

生命周期 onResume 对应方法，需在界面的对应生命周期函数内调用。


<span id="onPause()"></span>
#### onPause()

```java
public void onPause()
```

功能描述：

生命周期 onPause 对应方法，需在界面的对应生命周期函数内调用。


<span id="onStop()"></span>
#### onStop()

```java
public void onStop()
```

功能描述：

生命周期 onStop 对应方法，需在界面的对应生命周期函数内调用。


<span id="onDestroy()"></span>
#### onDestroy()

```java
public void onDestroy()
```

功能描述：

生命周期 onDestroy 对应方法，需在界面的对应生命周期函数内调用。



### 回调类说明

<span id="OnSdkKitInitCallback"></span>
#### OnSdkKitInitCallback

智能扫码初始化接口的回调类，接收初始化鉴权认证的结果。

```java
/**
 * The interface On sdk kit init callback.
 */
public interface OnSdkKitInitCallback {
    /**
     * On init result.
     *
     * @param errCode the error code
     * @param errMsg  the error msg
     */
    void onInitResult(String errCode, String errMsg);
}
```


<span id="QBarSdkCallback"></span>
#### QBarSdkCallback

智能扫码使用默认界面扫码的回调类，接收扫码结果信息。

```java
/**
 * The interface Q bar sdk callback.
 */
public interface QBarSdkCallback {

    /**
     * 如果只一个码，解码结果回调
     *
     * @param result 数据
     */
    void onIdentityResult(ScanResult result);

    /**
     * 扫码过程中出现的异常
     * @param errorCode 错误码
     * @param errorMsg 错误信息
     */
    void onFail(int errorCode, String errorMsg);
}
```

ScanResult 包含属性及含义：
- **String data** 识别到的内容信息。
- **String charset** 内容包含的字符集。
- **String typeName** 所扫描图片包含的二维码类型。
