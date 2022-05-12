对于在 Android 平台上传视频的场景，云点播提供了 Android 上传 SDK。上传流程请参见 [客户端上传指引](/document/product/266/9219)。

## 源码下载

1. [单击下载](https://liteav.sdk.qcloud.com/download/ugc/LiteAVSDK_UGC_Upload_Android.zip) Android 上传 Demo 及源码。
2. 将下载好的压缩包解压，可以看到 Demo 目录，上传源码在`Demo/app/src/main/java/com/tencent/ugcupload/demo/videoupload`目录下。

##  集成上传库和源码

1. 拷贝上传源码目录`Demo/app/src/main/java/com/tencent/ugcupload/demo/videoupload`到您的工程目录中，需要手动修改一下 package 名。
2. 参考`Demo/app/build.gradle`在您的工程中添加依赖：
    ```
    implementation 'com.qcloud.cos:cos-android-nobeacon:5.8.3'
    implementation 'com.qcloud.cos:quic:1.5.37'
    ```
>?您也可以参考 [手动集成](https://cloud.tencent.com/document/product/436/12159#.E6.96.B9.E5.BC.8F.E4.BA.8C.EF.BC.9A.E6.89.8B.E5.8A.A8.E9.9B.86.E6.88.90) 文档集成对应版本的依赖库。
3. 使用视频上传需要网络、存储等相关访问权限，可在`AndroidManifest.xml`中增加如下权限声明：
	```xml
	<uses-permission android:name="android.permission.INTERNET"/>
	<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
	<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
	<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
	<receiver android:name=".videoupload.impl.TVCNetWorkStateReceiver">
		<intent-filter>
			<!--检测网络变化的 action-->
			<action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
			<category android:name="android.intent.category.DEFAULT" />
		</intent-filter>
	</receiver>
	```

##  简单视频上传
#### 初始化上传对象

```java
TXUGCPublish mVideoPublish = new TXUGCPublish(this.getApplicationContext(), "independence_android")
```

#### 设置上传对象回调

```java
mVideoPublish.setListener(new TXUGCPublishTypeDef.ITXVideoPublishListener() {
    @Override
    public void onPublishProgress(long uploadBytes, long totalBytes) {
        mProgress.setProgress((int) (100*uploadBytes/totalBytes));
    }

    @Override
    public void onPublishComplete(TXUGCPublishTypeDef.TXPublishResult result) {
        mResultMsg.setText(result.retCode + " Msg:" + (result.retCode == 0 ? result.videoURL : result.descMsg));
    }
});
```

#### 构造上传参数

```java
TXUGCPublishTypeDef.TXPublishParam param = new TXUGCPublishTypeDef.TXPublishParam();

param.signature = "xxx";
param.videoPath = "xxx";
```
`signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

#### 调用上传

```java
int publishCode = mVideoPublish.publishVideo(param);
```

## 简单图片上传

#### 初始化上传对象

```java
TXUGCPublish mVideoPublish = new TXUGCPublish(this.getApplicationContext(), "independence_android")
```

#### 设置上传对象回调

```java
mVideoPublish.setListener(new TXUGCPublishTypeDef.ITXMediaPublishListener() {
    @Override
    public void onMediaPublishProgress(long uploadBytes, long totalBytes) {
        mProgress.setProgress((int) (100*uploadBytes/totalBytes));
    }
    @Override
    public void onMediaPublishComplete(TXUGCPublishTypeDef.TXMediaPublishResult mediaResult) {
        mResultMsg.setText(result.retCode + " Msg:" + (result.retCode == 0 ? result.videoURL : result.descMsg));
    }
});
```

#### 构造上传参数

```java
TXUGCPublishTypeDef.TXMediaPublishParam param = new TXUGCPublishTypeDef.TXMediaPublishParam();

param.signature = "xxx";
param.mediaPath = "xxx";
```

`signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

#### 调用上传

```java
int publishCode = mVideoPublish.publishMedia(param);
```

>?
>- 上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。
>- 如需上传至指定子应用下，请参见 [子应用体系 - 客户端上传](https://cloud.tencent.com/document/product/266/14574#.E5.AE.A2.E6.88.B7.E7.AB.AF.E4.B8.8A.E4.BC.A0)。
>
## 高级功能

#### 携带封面

在上传参数中带上封面路径即可。

```java
TXUGCPublishTypeDef.TXPublishParam param = new TXUGCPublishTypeDef.TXPublishParam();
param.signature = "xxx";
param.videoPath = "xxx";
param.coverPath = "xxx";
```
`signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。

#### 取消和恢复上传

取消上传，调用`TXUGCPublish`的`canclePublish()`接口。

```java
mVideoPublish.canclePublish();
```

恢复上传，用相同的上传参数（视频路径和封面路径不变），再调用一次`TXUGCPublish`的`publishVideo`。

#### 断点续传

在视频上传过程中，云点播支持断点续传，即当上传意外终止时，用户再次上传该文件，可以从中断处继续上传，减少重复上传时间。

断点续传的有效时间是1天，即同一个视频上传被中断，那么1天内再次上传可以直接从断点处上传，超过1天默认会重新上传完整视频。

上传参数中的`enableResume`为断点续传开关，默认是开启的。

#### 预上传

在实际上传过程中，很大部分的错误是由于网络连接失败或超时导致的，为优化此类问题，我们增加了预上传优化逻辑。预上传包含：HTTPDNS 解析、获取建议上传地域、探测最优上传地域。

建议您在 App 启动的时候调用`TXUGCPublishOptCenter.getInstance().prepareUpload(signature)`，预上传模块会把`<域名，IP>`映射表和最优上传地域缓存在本地，监听到网络切换时，清空缓存并自动刷新。

>!一定要在`AndroidManifest.xml`中注册网络监听模块：
```xml
<receiver android:name=".videoupload.impl.TVCNetWorkStateReceiver">
  <intent-filter>
    <!--检测网络变化的 action-->
    <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
    <category android:name="android.intent.category.DEFAULT" />
  </intent-filter>
</receiver>
```

`signature`计算规则请参见 [客户端上传签名](/document/product/266/9221)。


## 视频上传接口描述

初始化上传对象：`TXUGCPublish`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| context   | application 上下文。        | Context | 是    |
| customKey | 用于区分不同的用户，建议使用 App 的帐号 ID，方便后续定位问题。 | String  | 否    |

设置点播 appId：`TXUGCPublish.setAppId`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| appId   | 点播 appId。        | int | 是    |


上传视频：`TXUGCPublish.publishVideo`

| 参数名称  | 参数描述 | 类型                                 | 必填   |
| ----- | ---- | ---------------------------------- | ---- |
| param | 上传参数。 | TXUGCPublishTypeDef.TXPublishParam | 是    |

上传参数：`TXUGCPublishTypeDef.TXPublishParam`

| 参数名称         | 参数描述                               | 类型      | 必填   |
| ------------ | ---------------------------------- | ------- | ---- |
| signature    | [客户端上传签名](/document/product/266/9221)。 | String  | 是    |
| videoPath    | 本地视频文件路径。                           | String  | 是    |
| coverPath    | 本地封面文件路径，默认不带封面文件。                  | String  | 否    |
| enableResume | 是否启动断点续传，默认开启。                      | boolean | 否    |
| enableHttps  | 是否启动 HTTPS，默认关闭。                      | boolean | 否    |
| fileName     | 上传到腾讯云的视频文件名称，不填默认用本地文件名。 | String  | 否    |

设置上传回调：`TXUGCPublish.setListener`

| 参数名称     | 参数描述        | 类型                                       | 必填   |
| -------- | ----------- | ---------------------------------------- | ---- |
| listener | 上传进度和结果回调监听。 | TXUGCPublishTypeDef.ITXVideoPublishListener | 是    |


进度回调：`TXUGCPublishTypeDef.ITXVideoPublishListener.onPublishProgress`

| 变量名称        | 变量描述     | 类型   |
| ----------- | -------- | ---- |
| uploadBytes | 已上传的字节数。 | long |
| totalBytes  | 总字节数。     | long |

结果回调：`TXUGCPublishTypeDef.ITXVideoPublishListener.onPublishComplete`

| 变量名称   | 变量描述 | 类型                                  |
| ------ | ---- | ----------------------------------- |
| result | 上传结果。 | TXUGCPublishTypeDef.TXPublishResult |

上传结果：`TXUGCPublishTypeDef.TXPublishResult`

| 成员变量名称   | 变量说明      | 类型     |
| -------- | --------- | ------ |
| retCode  | 结果码。       | int    |
| descMsg  | 上传失败的错误描述。 | String |
| videoId  | 点播视频文件 ID。  | String |
| videoURL | 视频存储地址。    | String |
| coverURL | 封面存储地址。    | String |

预上传：`TXUGCPublishOptCenter.prepareUpload`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| signature   | [客户端上传签名](/document/product/266/9221)。        | String | 是    |

## 图片上传接口描述

初始化上传对象：`TXUGCPublish`

| 参数名称  | 参数描述                                                  | 类型    | 必填 |
| --------- | --------------------------------------------------------- | ------- | ---- |
| context   | application 上下文。                                        | Context | 是   |
| customKey | 用于区分不同的用户，建议使用 App 的帐号 ID，方便后续定位问题。 | String  | 否   |

设置点播 appId：`TXUGCPublish.setAppId`

| 参数名称 | 参数描述  | 类型 | 必填 |
| -------- | --------- | ---- | ---- |
| appId    | 点播 appId。 | int  | 是   |

上传图片：`TXUGCPublish.publishMedia`

| 参数名称 | 参数描述 | 类型                                    | 必填 |
| -------- | -------- | --------------------------------------- | ---- |
| param    | 上传参数。 | TXUGCPublishTypeDef.TXMediaPublishParam | 是   |

上传参数：`TXUGCPublishTypeDef.TXMediaPublishParam`

| 参数名称     | 参数描述                                           | 类型    | 必填 |
| ------------ | -------------------------------------------------- | ------- | ---- |
| signature    | [客户端上传签名](/document/product/266/9221)。       | String  | 是   |
| mediaPath    | 本地图片文件路径。                                   | String  | 是   |
| enableResume | 是否启动断点续传，默认开启。                         | boolean | 否   |
| enableHttps  | 是否启动 HTTPS，默认关闭。                           | boolean | 否   |
| fileName     | 上传到腾讯云的视频文件名称，不填默认用本地文件名。 | String  | 否   |

设置上传回调：`TXUGCPublish.setListener`

| 参数名称 | 参数描述               | 类型                                        | 必填 |
| -------- | ---------------------- | ------------------------------------------- | ---- |
| listener | 上传进度和结果回调监听。 | TXUGCPublishTypeDef.ITXMediaPublishListener | 是   |

进度回调：`TXUGCPublishTypeDef.ITXMediaPublishListener.onPublishProgress`

| 变量名称    | 变量描述         | 类型 |
| ----------- | ---------------- | ---- |
| uploadBytes | 已上传的字节数。 | long |
| totalBytes  | 总字节数。         | long |

结果回调：`TXUGCPublishTypeDef.ITXMediaPublishListener.onPublishComplete`

| 变量名称 | 变量描述 | 类型                                |
| -------- | -------- | ----------------------------------- |
| result   | 上传结果。 | TXUGCPublishTypeDef.TXPublishResult |

上传结果：`TXUGCPublishTypeDef.TXMediaPublishResult`

| 成员变量名称 | 变量说明           | 类型   |
| ------------ | ------------------ | ------ |
| retCode      | 结果码。             | int    |
| descMsg      | 上传失败的错误描述。 | String |
| mediaId      | 点播媒体文件文件 ID。 | String |
| mediaURL     | 媒体资源存储地址。   | String |

预上传：`TXUGCPublishOptCenter.prepareUpload`

| 参数名称  | 参数描述                                     | 类型   | 必填 |
| --------- | -------------------------------------------- | ------ | ---- |
| signature | [客户端上传签名](/document/product/266/9221)。 | String | 是   |

## 错误码

SDK 通过`TXUGCPublishTypeDef.ITXVideoPublishListene\ITXMediaPublishListener`接口来监听视频上传相关的状态。因此，可以用`TXUGCPublishTypeDef.TXPublishResult\TXMediaPublishResult`中的`retCode`来确认视频上传的情况。

| 状态码  | 在 TVCConstants 中所对应的常量         | 含义                     |
| :--: | :----------------------------- | :--------------------- |
|  0   | NO_ERROR                       | 上传成功。                   |
| 1001 | ERR_UGC_REQUEST_FAILED         | 请求上传失败，通常是客户端签名过期或者非法，需要 App 重新申请签名。                 |
| 1002 | ERR_UGC_PARSE_FAILED           | 请求信息解析失败。               |
| 1003 | ERR_UPLOAD_VIDEO_FAILED        | 上传视频失败。                 |
| 1004 | ERR_UPLOAD_COVER_FAILED        | 上传封面失败。                 |
| 1005 | ERR_UGC_FINISH_REQUEST_FAILED  | 结束上传请求失败。               |
| 1006 | ERR_UGC_FINISH_RESPONSE_FAILED | 结束上传响应错误。               |
| 1007 | ERR_CLIENT_BUSY                | 客户端正忙（对象无法处理更多请求）。      |
| 1008 | ERR_FILE_NOEXIT                | 上传文件不存在。                |
| 1009 | ERR_UGC_PUBLISHING             | 视频正在上传中。                |
| 1010 | ERR_UGC_INVALID_PARAM          | 上传参数为空。                 |
| 1012 | ERR_UGC_INVALID_SIGNATURE      | 视频上传 signature 为空。        |
| 1013 | ERR_UGC_INVALID_VIDOPATH       | 视频文件的路径为空。              |
| 1014 | ERR_UGC_INVALID_VIDEO_FILE     | 当前路径下视频文件不存在。           |
| 1015 | ERR_UGC_FILE_NAME              | 视频上传文件名太长（超过40）或含有特殊字符。 |
| 1016 | ERR_UGC_INVALID_COVER_PATH     | 视频文件封面路径不对，文件不存在。       |
| 1017 | ERR_USER_CANCEL                | 用户取消上传。       |
| 1018 | ERR_UPLOAD_VOD                 | 小于5M的文件直接上传到云点播失败。       |


