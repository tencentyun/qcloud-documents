## SDK集成
[单击下载 Android UGC SDK](https://mc.qcloudimg.com/static/archive/51854b2dd574bda851bad6221238e967/ugcupload.zip)。解压zip包，配置工程导入其中的jar包和so:

>* okio-1.6.0.jar
>* okhttp-3.2.0.jar
>* cos-sdk-android.1.4.3.6.jar
>* sha1utils.jar
>* ugcupload.jar
>* libTXSHA1.so

SDK需要网络访问相关的一些权限，需要在AndroidManifest.xml中增加如下权限说明:

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

## 本地视频上传

### Step 1：创建上传对象

```java
TVCClient client = new TVCClient(getApplicationContext(), SecretId, Signature);
```

参数名称|参数类型|参数说明
:--|:--|:--
context|Context|上下文
scretId|String|密钥
signature|String|从服务端获取的上传签名

### Step 2：创建上传配置

```java
TVCUploadInfo info = new TVCUploadInfo(fileType, videoPath, coverType, coverPath);
```

参数名称|参数类型|参数说明
:--|:--|:--
fileType|String|视频文件类型，支持mp4, flv
filePath|String|视频文件路径
coverType|String|封面图片类型，必须为jpg，如果不上传则填空字符串
coverPath|String|封面图片路径，如果不上传则填空字符串


### Step3：视频上传

```java
client.uploadVideo(info, new TVCUploadListener() {
            @Override
            public void onSucess(String fileId, String playUrl, String coverUrl) {
                Log.v(TAG, "uploadVideo->fileId:"+fileId);
                Log.v(TAG, "uploadVideo->playUrl:"+playUrl);
                Log.v(TAG, "uploadVideo->coverUrl:"+coverUrl);
            }

            @Override
            public void onFailed(int errCode, String errMsg) {
                Toast.makeText(MainActivity.this, "err " + errCode + ""
                        + errMsg, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onProgress(long currentSize, long totalSize) {
                double percent = (double) currentSize / (double) totalSize;
                NumberFormat nt = NumberFormat.getPercentInstance();
                nt.setMinimumFractionDigits(2);
                Log.i("onProgess", "onProgress: " + nt.format(percent));
            }
        });
```

