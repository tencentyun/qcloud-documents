## 简介

Android平台的客户端上传SDK，可向腾讯云点播系统上传视频和封面文件。

## 集成方式

下载[Android UGC SDK](http://download-1252463788.cossh.myqcloud.com/RTMPSDKAndroidSimple2.0.2.2801.zip)，导入所需的jar包:

>* tvcsdk.jar
>* okio-1.6.0.jar
>* okhttp-3.2.0.jar
>* cos-sdk-android-1.4.2.jar

SDK需要一些网络访问相关的权限，需在**AndroidManifest.xml**中增加如下权限说明:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## 本地视频上传步骤

### 第一步：初始化

初始化上传对象，指定上传主体的上下文、密钥和签名信息。

| 参数名称 | 必填 | 类型 | 含义 |
| --- | --- | --- | --- |
| context | 是 | Context | 上下文，可以填getApplicationContext() |
| secretId | 是 | String | [云API密钥](https://console.qcloud.com/capi)的Secret ID |
| signature | 是 | String | 从APP服务器获取的[客户端上传签名](/document/product/266/9221) |
| timeout | 否 | Integer | 网络请求超时时间，默认为8秒 |

```java
TVCClient client = new TVCClient(context, secretId, signature);
```

### 第二步：指定上传目标

指定上传目标的参数有视频和封面信息。如果只上传视频，则封面信息参数填空字符串。

| 参数名称 | 必填 |类型 | 含义 |
| --- | --- | --- | --- |
| videoType | 是 | String | 视频文件类型 |
| videoPath | 是 | String | 视频文件路径 |
| coverType| 否 | String | 封面图片类型 |
| coverPath| 否 | String | 封面图片路径 |

仅上传视频：

```java
TVCUploadInfo info = new TVCUploadInfo(videoType, videoPath, "", "");
```

同时上传视频和封面：

```java
TVCUploadInfo info = new TVCUploadInfo(videoType, videoPath, coverType, coverPath);
```

### 第三步：执行上传操作

```java
client.uploadVideo(info, new TVCUploadListener() {
            @Override
            public void onSucess(String fileId, String videoUrl, String coverUrl) {
                Log.v(TAG, "上传成功的视频文件ID: " + fileId);
                Log.v(TAG, "上传视频的播放地址：" + playUrl);
                Log.v(TAG, "上传封面的展示地址：" + videoUrl);
            }

            @Override
            public void onFailed(int errCode, String errMsg) {
                Toast.makeText(MainActivity.this, 
                       "错误码：" + errCode + " 错误信息：" + errMsg, 
                       Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onProgress(long currentSize, long totalSize) {
                double percent = (double) currentSize / (double) totalSize;
                NumberFormat nt = NumberFormat.getPercentInstance();
                nt.setMinimumFractionDigits(2);
                Log.i("上传进度", "上传进度：" + nt.format(percent));
            }
        });
```
