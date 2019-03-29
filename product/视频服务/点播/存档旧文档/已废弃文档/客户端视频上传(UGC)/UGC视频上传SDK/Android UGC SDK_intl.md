## SDK Integration
[Click to Download](https://mc.qcloudimg.com/static/archive/ab5853a171024359000887545e260c2c/tvcsdk_201611041102.zip)Android UGC SDK. Unzip the zip package, configure the project and import the jar packages:

>* tvcsdk.jar
>* okio-1.6.0.jar
>* okhttp-3.2.0.jar
>* cos-sdk-android-1.4.2.jar

SDK needs some permissions related to network access. The following permission entries should be included in AndroidManifest.xml:

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

## Local Video Upload

### Step 1: Create Upload Object

```java
TVCClient client = new TVCClient(getApplicationContext(), SecretId, Signature);
```

Parameter Name | Parameter Type | Parameter Description
:-- | :-- | :--
context | Context | Context
secretId | String | Private key
signature | String | Upload signature acquired from the server

### Step 2. Create Upload Configuration

```java
TVCUploadInfo info = new TVCUploadInfo(fileType, videoPath, coverType, coverPath);
```

Parameter Name | Parameter Type | Parameter Description
:-- | :-- | :--
fileType | String | Video file type. mp4 and flv are supported
filePath | String | Video file path
coverType | String | Cover image type, which must be jpg. Leave an empty string if you don't wish to upload image
coverPath | String | Cover image path. Leave an empty string if you don't wish to upload image


### Step3: Upload Video

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

