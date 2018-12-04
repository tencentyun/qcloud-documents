# 腾讯实名核身SDK说明文件 -- iOS端



## 一、App业务流程框架图
![图片](https://main.qcloudimg.com/raw/db7d05d7d96a43c1295e2e5dac65933d.png)
**其中，蓝色部分主要由腾讯侧开发，部署在腾讯侧；橙色部分由调用方开发对接，部署在调用方。**

## 二、SDK功能说明

* 版本号：V3.0
* 功能：实名核身整体流程，包括身份证OCR识别和活体检测功能。

### 2.1 文件说明

**SDK包含了以下文件:**

**AuthSDK.framework**  封装了实名认证的流程，包括了身份证OCR识别和活体检测功能。

**opencv2.framework和ULSMultitrackeriOSSDK.framework** 是人脸识别引擎SDK

**face_shape.ref ULSGPUAssets.bin authsdk.bundle ULSFaceTrackerAssets.bundle ** 均为资源文件

**注**:   协议文件在AuthSDK.framework/authsdk.bundle/protocol.txt中，可以根据需要修改。（其他资源文件，如首页banner也可根据需求替换authsdk.bundle中图片）


## 三、接入流程

#### 1 . 添加framework

  将AuthSDK.framework拷贝到项目根目录Framework中（目录可自定义），在TARGETS-Build Phases-Link Binary with Libraries 点击“+”，弹出添加列表后，点击“Add Other…”,从Framework文件夹中添加AuthSDK.framework到工程中。同理，添加SDK中的所有文件添加到工程中。

![图片](https://main.qcloudimg.com/raw/d606a2f1e2190a37b9cab56a9ab264bf.png)

保证下图中的内部framework添加到工程中：

![图片](https://main.qcloudimg.com/raw/efef4d0a70e51506fe00db6b33b35be3.png)

#### 2 . 添加AuthSDK.framework中资源文件
在工程界面右键弹出菜单中选择"Add Files To..."，从文件夹Framework->AuthSDK.framework中将资源文件authsdk.bundle添加到工程中。

![图片](https://main.qcloudimg.com/raw/faeef2472185a9912c9e4f02a8d23177.png)

#### 3 . 添加需要的编译选项
在TARGETS-Build Settings-Other Linker Flags 中添加如下内容： -ObjC 。
C++ Language Dialect设置为C++11 [-std=c++11]
C++ Standard Library设置为libc++

![图片](https://main.qcloudimg.com/raw/f04e1c91f36c3785329adb9d99f5d409.png)

#### 4 . 添加权限声明

在工程info.plist中增加如下字串:

	<key>NSPhotoLibraryUsageDescription</key>
	<string>需要您的同意才能读取照片库</string>
	<key>NSCameraUsageDescription</key>
	<string>需要您的同意才能使用摄像头</string>
	<key>NSMicrophoneUsageDescription</key>
	<string>需要您的同意才能使用麦克风</string>

Xcode9以上版本需要添加：

	<key>NSPhotoLibraryAddUsageDescription</key>
	<string>需要您的同意才能读取照片库</string>

以下配置当服务器使用http访问时需要配置，否则不需要

	<key>NSAppTransportSecurity</key>
	<dict>
			<key>NSAllowsArbitraryLoads</key>
	    	<true/>
	</dict>


   	 	

#### 5 . 初始化SDK接口
在程序中import sdk，并初始化，设置分配的APPID。

```objc
#import <AuthSDK/AuthSDK.h>

```

注：目前Demo中使用的是测试URL，接入时可修改成正式服务URL（传nil时，使用测试服务器）

```objc
@property (nonatomic) AuthSDK * sdk;
```

```objc
_sdk = [[AuthSDK alloc] initWithServerURL:nil]
[_sdk setAppId:@"4396" appSecretKey:@"416df0300bd4043fb4d4df5c00b3e280"];

```

#### 6 . 获取signature
接入方需要在服务端实现获取signature的接口，客户端通过接口拉取到signature，在下面调用SDK接口的时候需要传入。


#### 7 . 调用实名认证接口
```objc
[_sdk startAuth:nil name:_nameText.text idNum:_idNumText.text token:_token.text parent:self delegate:self signature:_signature isSecondVerify:YES];
```



#### 
## 四 通过token获取实名核身详细信息

由接入方自己实现。

### 1）接口

https://iauth-sandbox.wecity.qq.com/new/cgi-bin/getdetectinfo.php

### 2)  描述
拉取实名详细信息接口。回包内容已加密，详细算法参看7 加解密算法。
### 3)  方法 
POST
### 4)  HTTP请求格式
**a、头部信息**

| 要求   | 参数名       | 类型     | 参数说明            | 取值说明 |
| :--- | :-------- | :----- | :-------------- | :--- |
| 必选   | signature | String | 接口签名，具体见签名算法4.1 |      |

**signature生成算法，请查看6 鉴权算法。**

**b、请求包体**

| 要求 | 参数名     | 类型   | 参数说明                    | 取值说明                                                     |
| :--- | :--------- | :----- | :-------------------------- | :----------------------------------------------------------- |
| 必选 | token      | string | 上一个接口返回的token序列号 |                                                              |
| 必选 | appid      | string | 分配的appid                 |                                                              |
| 可选 | crypt_type | int    | 加密算法类型                | 不传时，默认使用AES 256加密算法;<br>“1”为使用RSA；<br>”2”为使用AES-256-CBC(IV为空)+PKCS7填充;<br>"3"为使用AES-256-ECB+PKCS7填充 |
| 可选 | info_type  | int    | 获取信息类型                | 不传时,默认带上所有文件buffer；<br>传”0”表示获取所有信息，含文件buffer；<br>“1”为传文本信息，不含文件buffer。 |

**c、请求包体示例**
```js
{
	"token":"{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}",
	"appid":"xxxx",
} 
```
### 5)  返回值说明

| 字段        | 类型     | 说明                 |
| :-------- | :----- | :----------------- |
| errorcode | int    | 返回状态码,0表示成功，非0值为出错 |
| errormsg  | String | 返回错误描述             |
| data      | String | 图片为BASE64数据        |

**b、返回示例**
```js
{
    "errorcode": 0,
    "errormsg": "success",
    "data": "rsa密文"
}
```
RSA公钥解密data后对应的数据如下：
```js
{
    "ID": "4501111994xxxxxxxx",
    "name": "张三",
    "phone": "159********",
    "sex": "男",
    "nation": "汉",
    "ID_address": "广东省深圳市南山区***",
    "ID_birth": "xxxx",
    "ID_authority": "***公安局",
    "ID_valid_date": "xxxx.xx.xx-xxxx.xx.xx",
    "validatedata": "3344",
    "frontpic": "身份证正面照片的base64编码",
    "backpic": "身份证反面照片的base64编码",
    "video": "视频的base64编码",
    "videopic1": "视频截图1的base64编码",
    "videopic2": "视频截图2的base64编码",
    "videopic3": "视频截图3的base64编码",
    "yt_errorcode": 0,
    "yt_errormsg": "通过",
    "livestatus": 0,
    "livemsg": "OK",
    "comparestatus": 0,
    "comparemsg": "OK",
    "sim": 78,
    "type": 0
}
```
其中type为对外接口扩展参数中的type,默认为0（即首次实名验证）


# 6 鉴权算法
## 6.1 签名

上述提供的API接口，通过签名来验证请求的合法性。开发者通过将签名授权给调用方，使其具备使用API接口的能力。 密钥的获取及签名的生成方法如下：

### Step 1 获取应用appid、密钥secretkey和过期时间expired

应用appid:   用来标识唯一的应用；

密钥secretkey:   使用加密算法时使用的秘钥；

expired:    当次请求的时间戳的有效时间；

### Step 2 拼接有效签名串

a=xxxxx&m=xxxxxxx&t=1427786065&e=600

a为appid

m为调用的api名，

t为当前时间戳，是一个符合UNIX Epoch时间戳规范的数值，单位为秒

e为此签名的凭证有效期，是一个符合UNIX Epoch时间戳规范的数值，单位为秒,

同appid和secretkey一样，由API提供方给定。

拼接有效签名串的结果,下文称之为orignal

### Step 3 生成签名串

(1)API提供方 使用 HMAC-SHA1 算法对请求进行签名。

(2)签名串需要使用 Base64 编码。

根据签名方法signature= Base64(HMAC-SHA1(secretkey, orignal) + original)，其中secretkey为Step1获取，orignal为Step2中拼接好的签名串，对orignal使用HMAC-SHA1算法进行签名，然后将orignal附加到签名结果的末尾，再进行Base64编码，得到最终的sign。 

注：此处使用的是标准的Base64编码，不是urlsafe的Base64编码，请注意。 以 JAVA 语言为例,其他语言均有类似算法. JAVA语言的示例代码见附件。

### Step 4 使用签名串
将Step 3生成的signature，填充到http请求的head头部的signature字段中即可。

### NodeJS参考代码
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

## 6.2 参数校验

### 参数签名校验算法
md5(参数1-参数2-...-私钥key)
### 说明
参数顺序使用“-”拼接，拼接后的字符串，再最后拼接上SIG_KEY(authkey),然后字符串md5,取32位小写字符串 
### NodeJS参考代码
```
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

# 7 加解密算法
## 7.1 AES 256算法
使用项目提供的AES解密秘钥解密
**NodeJS 代码参考**

### AES-256-CBC + PKCS7
```js
var crypto = require('crypto');
var fs = require('fs');
var NodeRSA = require('node-rsa');

//AES加密
function encryptAes256(data, secretKey) {
    try {
        let key = new Buffer(secretKey);
        var cipher = crypto.createCipher("aes-256-cbc", key);
        cipher.setAutoPadding(true);
        var decryptedData = cipher.update(data, 'utf8', 'base64');
        decryptedData += cipher.final('base64');
        return decryptedData;
    } catch (e) {
        console.error(e);
        return "";
    }
}
//AES解密
function decryptAes256(data, secretKey) {
    try {
        let key = new Buffer(secretKey);
        var cipher = crypto.createDecipher("aes-256-cbc", key);
        cipher.setAutoPadding(true);
        var decryptedData = cipher.update(data, 'base64', 'utf8');
        decryptedData += cipher.final('utf8');
        return decryptedData;
    } catch (e) {
        return "";
    }
}
```

### AES-256-ECB + PKCS7
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