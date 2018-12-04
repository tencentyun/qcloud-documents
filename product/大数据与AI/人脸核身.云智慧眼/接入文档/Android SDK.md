## App 业务流程框架图
![图片](https://main.qcloudimg.com/raw/db7d05d7d96a43c1295e2e5dac65933d.png)
蓝色部分主要由腾讯云开发，部署在腾讯侧；橙色部分由业务方开发对接，部署在调用方。

## SDK 功能
* 版本号：V3.0
* 功能：实名核身整体流程，包括身份证OCR识别和活体检测功能。

### 文件说明

**AuthSdk.jar**：封装了实名核身的流程，包括了身份证 OCR 识别和活体检测功能。
**AuthSdk.aar**：封装了实名核身的流程，包括了身份证 OCR 识别和活体检测功能，以及所有需要的资源。
**res**：包含了 SDK 所使用的资源文件。
**assets**：包含了协议内容文件。目前使用的是《测试实名核身用户须知》。
**libcurl.so libUlsFunction.so libulsTracker_native.so**：人脸定位库
**AuthDemo**：提供了实名核身接口调用方法及从后台拉取活体检测详细信息的方法。接入时可参考 Demo，这里提供了两个 Demo，对应两种接入方式。

### 开发运行环境
SDK 版本 minSdkVersion 为15，支持 Android4.0及以上版本。

## 接入流程
您可通过两种方式接入服务：
- 使用 aar 方式，可以在 Android Studio 中使用。（推荐）
- 使用 jar 包+资源的方式，可以用在 Eclipse和Android Studio 中。  

### 使用 aar 接入方式
参见 authdemo，SDK 接入流程如下：
**1. 添加 aar 包**
将 AuthSdk.aar 包添加到接入方 App 的 libs 目录下，如 Demo 所示

**2. 配置 build**
在接入方 App 的 build.gradle 中进行如下配置：
```js
//使用aar时必须要设置的
repositories {
    flatDir {
        dirs 'libs'
    }
}
dependencies {
    compile fileTree(include: ['*.jar'], dir: 'libs')
    compile (name:'AuthSdk', ext:'aar')
    compile 'com.android.support:appcompat-v7:23.4.0'
}
```

**3. 初始化 SDK 接口**
在程序的 Application 中或在调用 SDK 之前初始化 SDK，设置相关配置，包括后台服务 URL 及分配给业务方的 AppId 和 SecretKey，具体参考 AuthDemo。
```java
AuthConfig.Builder configBuilder = new AuthConfig.Builder(serverUrl, appid, R.class.getPackage().getName());
```

**4. 调用实名核身**
```java
AuthSDKApi.startMainPage(this, configBuilder.build(), mListener);
```

**5. 根据实名核身返回的 token，从后台拉取活体检测详细信息**
通过token可以从后台拉取实名核身活体检测的详细信息，具体调用接口和方法参见后台接口和Demo。

**6. 混淆说明**
在混淆文件增加，参考 Demo 混淆文件
```
xml
#不去掉无用方法，有些方法是给外部提供使用的
#-dontshrink
-optimizationpasses 5
-dontusemixedcaseclassnames
-dontskipnonpubliclibraryclassmembers
-dontskipnonpubliclibraryclasses
-dontpreverify
-verbose
-optimizations !code/simplification/arithmetic,!field/*,!class/merging/*
-dontwarn android.support.**
-dontwarn android.support.**
-ignorewarnings                # 抑制警告
# For BatteryStats
-dontwarn android.os.**
-dontwarn android.app.**
-keep class android.support.** { *; }
-keep class android.support.** { *; }
-keep class android.** {
    <fields>;
    <methods>;
}
-keep class com.android.** {
    <fields>;
    <methods>;
}
-keep public class * extends android.app.Activity
-keep public class * extends android.app.Application
-keep public class * extends android.content.BroadcastReceiver
-keepattributes *Annotation*
-keepattributes InnerClasses
-keepattributes Signature
-keepclasseswithmembernames class * {
    native <methods>;
}
-keepclasseswithmembers class * {
    public <init>(android.content.Context, android.util.AttributeSet);
}
-keepclasseswithmembers class * {
    public <init>(android.content.Context, android.util.AttributeSet, int);
}

-keepclassmembers class * extends android.app.Activity {
   public void *(android.view.View);
}
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}
-assumenosideeffects class android.util.Log {
    public static *** e(...);
    public static *** w(...);
    public static *** i(...);
    public static *** d(...);
    public static *** v(...);
}
#不混淆资源类
-keep class **.R$* {
*;
}
# AuthSdk
-keep class com.tencent.authsdk.AuthSDKApi { *; }
-keep class com.tencent.authsdk.callback.IdentityCallback { *; }
-keep class com.tencent.youtufacetrack.** { *; }
-keep class com.tencent.authsdk.IDCardInfo {*;}
-keep class com.tencent.authsdk.IDCardInfo$Builder { *; }
```

### 使用 jar 包+资源接入方式
参见 authdemo_jar，SDK 接入流程如下：
**1. 设置权限及Manifest配置**
在接入方 App 的 AndroidManifest.xml 中进行如下配置，具体可参见 AuthDemo
权限设置：
```xml
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <!-- 使用音视频录制的权限 -->
    <uses-permission android:name="android.permission.RECORD_VIDEO" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <!-- 使用相机及自动对焦功能的权限 -->
    <uses-permission android:name="android.permission.CAMERA" />

    <uses-feature android:name="android.hardware.camera" />
    <uses-feature android:name="android.hardware.camera.autofocus" />
    <!-- 监听来电 -->
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.PROCESS_OUTGOING_CALLS" />

```

Activity添加：
```xml
 <activity
     android:name="com.tencent.authsdk.activity.MainSdkActivity"
     android:launchMode="singleTask"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" >
 </activity>
 <activity
     android:name="com.tencent.authsdk.activity.IdcardOcrActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.IdcardOcrResultActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.CameraActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.AlbumActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.CropImageActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" >
 </activity>
 <activity
     android:name="com.tencent.authsdk.activity.IdentityDetectActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.RecordActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.LiveDetectActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.DetectResultActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
 <activity
     android:name="com.tencent.authsdk.activity.PhoneVerityActivity"
     android:screenOrientation="portrait"
     android:theme="@style/SDKAppTheme" />
```

**2. 添加 jar 包和资源**
参照 AuthDemo，将 AuthSDK.jar 添加到接入方 App 的 libs 目录下，将 res 目录下的资源文件添加到接入方 App 的 res 下的相应目录下，以及 assets 目录下的文件添加到 App 的 assets 下，将 libcurl.so、libUlsFunction.so、libulsTracker_native.so 添加到 jniLibs 下。

**3. 初始化 SDK 及调用实名核身接口**
具体流程跟上面 aar 接入方式中的 3-6 步骤一致，不再赘述。


## 实名信息拉取接口
由接入方自己实现。

### 1）接口

https://iauth-sandbox.wecity.qq.com/new/cgi-bin/getdetectinfo.php

### 2)  描述
拉取实名详细信息接口。回包内容较大，建议异步拉取视频和照片的数据。回包内容已加密，详细算法参看加解密算法。
### 3)  方法 
POST
### 4)  HTTP请求格式
**a、头部信息**

| 要求   | 参数名       | 类型     | 参数说明            |
| :--- | :-------- | :----- | :-------------- |
| 必选   | signature | String | 接口签名，具体见签名算法4.1 |

**signature生成算法，请查看签名算法。**

**b、请求包体**

| 要求   | 参数名        | 类型     | 参数说明             | 取值说明                                     |
| :--- | :--------- | :----- | :--------------- | :--------------------------------------- |
| 必选   | token      | string | 上一个接口返回的token序列号 |                                          |
| 必选   | appid      | string | 分配的appid         |                                          |
| 可选   | info_type  | int    | 获取信息类型           | 不传时,默认带上所有文件buffer；;传”0”表示获取所有信息，含文件buffer；;“1”为传文本信息，不含文件buffer。 |

**c、请求包体示例**
```js
{
	"token":"{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}",
	"appid":"xxxx"
} 
```
### 5)  返回值说明

| 字段        | 类型     | 说明                 |
| :-------- | :----- | :----------------- |
| errorcode | int    | 返回状态码,0表示成功，非0值为出错 |
| errormsg  | String | 返回错误描述             |
| data      | String | BASE64数据（加密数据）        |

**b、返回示例**
```js
{
    "errorcode": 0,
    "errormsg": "success",
    "data": "base64(aes密文)"
}
```
解密data后对应的数据如下：
```js
{
    "ID": "4501111994xxxxxxxx",

    "name": "张三",

    "phone": "159********",

    "sex": "男",

    "nation": "汉",

    "ID_address": "广东省深圳市南山区*****",

    "ID_birth": "xxxx",

    "ID_authority": "***公安局",

    "ID_valid_date": "xxxx.xx.xx-xxxx.xx.xx",

    "validatedata": 3344,//数字模式活体检测录制视频读取，动作模式此参数为空

    "frontpic": "身份证正面照片的base64编码",

    "backpic": "身份证反面照片的base64编码",

    "video": "视频的base64编码",

    "videopic1": "视频截图1的base64编码",

    "videopic2": "视频截图2的base64编码",

    "videopic3": "视频截图3的base64编码"，

    "yt_errorcode":0,//最终结果错误码

    "yt_errormsg":"成功"，//最终结果错误描述

    "livestatus": 0,//活体检测错误码

    "livemsg": "OK",//活体检测错误描述

    "comparestatus": 0,//活体比对错误码

    "comparemsg": "OK",//活体比对错误描述

    "type": 0//auth传入的type参数
}
```
其中type为对外接口扩展参数中的type,默认为0（即首次实名验证）


## 鉴权算法
### 签名

上述提供的API接口，通过签名来验证请求的合法性。开发者通过将签名授权给调用方，使其具备使用API接口的能力。 密钥的获取及签名的生成方法如下：

#### Step 1 获取应用appid、密钥secretkey和过期时间expired

应用appid:   用来标识唯一的应用；

密钥secretkey:   使用加密算法时使用的秘钥；

expired:    当次请求的时间戳的有效时间；

#### Step 2 拼接有效签名串

a=xxxxx&m=xxxxxxx&t=1427786065&e=600

a为appid

m为调用的apiName，

t为当前时间戳，是一个符合UNIX Epoch时间戳规范的数值，单位为秒

e为此签名的凭证有效期，是一个符合UNIX Epoch时间戳规范的数值，单位为秒,

同appid和secretkey一样，由API提供方给定。

拼接有效签名串的结果,下文称之为orignal

#### Step 3 生成签名串

(1)API提供方 使用 HMAC-SHA1 算法对请求进行签名。

(2)签名串需要使用 Base64 编码。

根据签名方法signature= Base64(HMAC-SHA1(secretkey, orignal) + original)，其中secretkey为Step1获取，orignal为Step2中拼接好的签名串，对orignal使用HMAC-SHA1算法进行签名，然后将orignal附加到签名结果的末尾，再进行Base64编码，得到最终的sign。 

注：此处使用的是标准的Base64编码，不是urlsafe的Base64编码，请注意。 以 JAVA 语言为例,其他语言均有类似算法. JAVA语言的示例代码见附件。

#### Step 4 使用签名串
将Step 3生成的signature，填充到http请求的head头部的signature字段中即可。

#### NodeJS参考代码
```js
var crypto = require('crypto');
var signExpired = 600;//有效期一般为600s
//生成签名
function getAppSign(apiName, appId, appSecretKey, signExpired) {
    if (!apiName || !appId || !appSecretKey || !signExpired)
        return '';
    var now = parseInt(Date.now() / 1000);
    var plainText = 'a=' + appId + '&m=' + apiName + '&t=' + now + '&e=' + signExpired;
    var data = new Buffer(plainText, 'utf8');
    var res = crypto.createHmac('sha1', appSecretKey).update(data).digest();
    var bin = Buffer.concat([res, data]);
    var sign = bin.toString('base64');
    return sign;
}
```

### 参数校验

#### 参数签名校验算法
md5(参数1-参数2-...-私钥key)
#### 说明
参数顺序使用“-”拼接，拼接后的字符串，再最后拼接上SIG_KEY(authkey),然后字符串md5,取32位小写字符串 
#### NodeJS参考代码
```js
var crypto = require('crypto');
var SIG_KEY = "authkey";
//生成sig 参数顺序要按照文档上的顺序
function getHashSig(postBody) {
    var datas = JSON.parse(postBody);
    var sigData = datas["sig"];
    var srcData = "";
    for (var index in datas) {
        if (index != 'sig')
            srcData += datas[index] + '-';
    }
    srcData += SIG_KEY;
    return  crypto.createHash('md5').update(srcData).digest('hex');
}
```

#### PHP参考代码
```js
/**
* 计算签名
* @param $apiName
* @param $secretKey 接口签名
* @param $plainText 拼接有效签名串
* @return array|string
*/
static function getAppSign($apiName,$secretKey,$plainText) {
    if (empty($apiName)) {
        return array("ret"=>-1,"msg"=>"apiName error","signature"=>"");
    }

    $bin = hash_hmac("SHA1", $plainText, $secretKey, true);
    $bin = $bin.$plainText;
    $sign = base64_encode($bin);
    return $sign;
}
```

## 加解密算法
### AES 256算法
使用项目提供的AES解密秘钥解密
#### NodeJS 代码参考

AES-256-ECB + PKCS7
```js
function encryptAes256ECBPKCS7(data, secretKey) {
    try {
        let iv = "";
        var clearEncoding = 'utf8';
        var cipherEncoding = 'base64';
        var cipherChunks = [];
        var cipher = crypto.createCipheriv('aes-256-ecb', secretKey, iv);
        cipher.setAutoPadding(true);
        cipherChunks.push(cipher.update(data, clearEncoding, cipherEncoding));
        cipherChunks.push(cipher.final(cipherEncoding));
        return cipherChunks.join('');
    } catch (e) {
        console.error(e);
        return "";
    }
}

function decryptAes256ECBPKCS7(data, secretKey) {
    try {
        if (!data) {
            return "";
        }
        let iv = "";
        var clearEncoding = 'utf8';
        var cipherEncoding = 'base64';
        var cipherChunks = [];
        var decipher = crypto.createDecipheriv('aes-256-ecb', secretKey, iv);
        decipher.setAutoPadding(true);
        let buff = data.replace('\r', '').replace('\n', '');
        cipherChunks.push(decipher.update(buff, cipherEncoding, clearEncoding));
        cipherChunks.push(decipher.final(clearEncoding));
        return cipherChunks.join('');
    } catch (e) {
        console.error(e);
        return "";
    }
}
```
#### PHP 代码参考

AES-256-ECB +PKCS7
```js
/**
 * 利用openssl做AES加密解密
 */
class AES{
    /**
     * 加密然后base64转码
     * @param $str
     * @param $key
     * @return string
     */
    function aes256ecbEncrypt($str,$key) {
        $data = openssl_encrypt($str,'AES-256-ECB', $key, OPENSSL_RAW_DATA);
        $data = base64_encode($data);
        return $data;
    }

    /**
     * 解密
     * @param String $encryptedText 二进制的密文
     * @param String $key 密钥
     * @return String
     */
    function aes256ecbDecrypt($encryptedText, $key) {
        $decrypted = openssl_decrypt(base64_decode($encryptedText), 'AES-256-ECB', $key, OPENSSL_RAW_DATA);
        return $decrypted;
    }
}
```
#### C# 代码参考

AES-256-ECB +PKCS7
```js
/// <summary>
///  AES 解密 秘钥32位
/// </summary>
/// <param name="str"></param>
/// <param name="key"></param>
/// <returns></returns>
public static string AesDecrypt(string str, string key)
    {
        if (string.IsNullOrEmpty(str)) return null;
        Byte[] toEncryptArray = Convert.FromBase64String(str);

        System.Security.Cryptography.RijndaelManaged rm = new System.Security.Cryptography.RijndaelManaged
        {
            Key = Encoding.UTF8.GetBytes(key),
            Mode = System.Security.Cryptography.CipherMode.ECB,
            Padding = System.Security.Cryptography.PaddingMode.PKCS7
        };

        System.Security.Cryptography.ICryptoTransform cTransform = rm.CreateDecryptor();
        Byte[] resultArray = cTransform.TransformFinalBlock(toEncryptArray, 0, toEncryptArray.Length);

        return Encoding.UTF8.GetString(resultArray);
    }

/// <summary>
///  AES 加密 秘钥32位
/// </summary>
/// <param name="str"></param>
/// <param name="key"></param>
/// <returns></returns>
public static string AesEncrypt(string str, string key)
{
    if (string.IsNullOrEmpty(str)) return null;
    Byte[] toEncryptArray = Encoding.UTF8.GetBytes(str);

    System.Security.Cryptography.RijndaelManaged rm = new System.Security.Cryptography.RijndaelManaged
    {
        Key = Encoding.UTF8.GetBytes(key),
        Mode = System.Security.Cryptography.CipherMode.ECB,
        Padding = System.Security.Cryptography.PaddingMode.PKCS7
    };

    System.Security.Cryptography.ICryptoTransform cTransform = rm.CreateEncryptor();
    Byte[] resultArray = cTransform.TransformFinalBlock(toEncryptArray, 0, toEncryptArray.Length);

    return Convert.ToBase64String(resultArray, 0, resultArray.Length);
}

```