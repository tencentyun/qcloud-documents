对于在Android平台上传视频的场景，腾讯云点播提供了Android上传SDK来实现。上传的流程可以参见[客户端上传指引](/document/product/266/9219)。


## 包依赖与客户端配置

拷贝发布源代码(目录：Demo/app/src/main/java/com/tencent/ugcupload/demo/videoupload)到您的工程目录中，需要手动修改一下package名。

将下载下来的Demo/app/libs/upload目录下的所有jar包集成到您的项目中，建议您保留upload目录结构，方便以后对库进行更新。

依赖库说明：

| jar文件                       | 说明                                       |
| --------------------------- | ---------------------------------------- |
| cos-xml-android-sdk-1.2.jar | 腾讯云对象存储服务（COS）的文件上传包， 此组件用于短视频上传(TXUGCPublish)功能 |
| qcloud-core-1.2.jar         | 腾讯云对象存储服务（COS）的文件上传包， 此组件用于短视频上传(TXUGCPublish)功能 |
| okhttp-3.8.1.jar            | 一款优秀的开源 http 组件                          |
| okio-1.13.0.jar             | 一款优秀的开源网络 I/O 组件                         |
| xstream-1.4.7.jar           | 一款优秀的开源序列化组件                             |
| fastjson-1.1.62.android.jar | 一款优秀的开源json组件                            |


使用短视频发布需要网络、存储等相关的一些访问权限，可在 AndroidManifest.xml 中增加如下权限声明：

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## 如何上传一个视频

### 使用示例

初始化一个发布对象

```java
TXUGCPublish mVideoPublish = new TXUGCPublish(this.getApplicationContext(), "carol_android")
```

设置发布对象的回调

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

调用发布

```java
int publishCode = mVideoPublish.publishVideo(param);
```

### 接口描述

初始化发布对象TXUGCPublish

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| context   | application 上下文        | Context | 是    |
| customKey | 用于区分不同的用户，建议使用app的账号id | String  | 否    |


发布参数TXUGCPublishTypeDef.TXPublishParam

| 参数名称         | 参数描述                                     | 类型      | 必填   |
| ------------ | ---------------------------------------- | ------- | ---- |
| signature    | 点播签名 | String  | 是    |
| videoPath    | 本地视频文件路径                                 | String  | 是    |
| coverPath    | 本地封面文件路径，默认不带封面文件                        | String  | 否    |
| enableResume | 是否启动断点续传，默认开启                            | boolean | 否    |

### 输出返回

publishVideo参数检查不通过会直接返回非0错误码，具体的错误码可以在TVCConstants.java中查看

发布进度回调。uploadBytes是上传字节数，totalBytes是总字节数

```java
void onPublishProgress(long uploadBytes, long totalBytes);
```

发布完成回调。如果成功，会返回视频文件fileid、url等信息；失败则返回失败错误码和错误信息。

```java
void onPublishComplete(TXPublishResult result);
public final static class TXPublishResult {
    public int    retCode;                                                  //错误码
    public String descMsg;                                                  //错误描述信息
    public String videoId;                                                  //视频文件Id
    public String videoURL;                                                 //视频播放地址
    public String coverURL;                                                 //封面存储地址
};
```

### 如何携带封面

在发布参数中带上封面路径即可。

### 如何取消、恢复上传

取消上传，调用TXUGCPublish的canclePublish()。

```java
mVideoPublish.canclePublish();
```

恢复上传，用相同的发布参数（视频路径和封面路径不变）再调用一次TXUGCPublish的publishVideo。

### 如何断点续传

发布参数中的enableResume，是否开启断点续传。默认是开启的。
在断点续传开启的情况下，只要待上传的文件路径、文件内容没有发生变化，SDK内部会自己实现断点续传，外部不用做特殊处理。


## FAQ
### APP后台如何知道是哪个用户上传了视频？
### 如果在上传完成后自动发起转码、拼接、剪辑、截图等视频处理操作？
