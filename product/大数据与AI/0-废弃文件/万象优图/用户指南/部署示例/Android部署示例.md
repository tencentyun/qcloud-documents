## 1 环境准备

本文档以eclipse+Android插件为例，开发者需准备好相应的开发环境。

## 2 SDK集成

1. 下载Android SDK

Android SDK的下载地址为：[Android SDK](/doc/product/275/SDK下载)。

2. 导入项目

将SDK包中的libs目录合并到本地工程的libs目录，然后配置工程导入所有jar包。

上传SDK的libs目录如下：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/androidsdk-1-2.jpg)

下载SDK的libs目录如下：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/android-sdk-2.jpg)

3. 配置manifest
SDK需要网络访问相关的一些权限，需要在manifest中进行权限声明如下所示:

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## 3 测试

以下程序全部来自于Demo，这里做部分说明。Demo的下载地址为：Android Demo（Android SDK中的Demo和此Demo相同）。

>注意：如果开发者想根据demo做简单测试，请将demo中的项目信息修改为自己的项目信息。具体修改方法如下：
(1) 进入package com.tencent.cloud.demo.common中的class BizService；
(2) 修改BizService中的APPID(项目ID)，BUCKET（空间名称）为自己的项目信息；
(3) 确保开发者自己的测试鉴权服务器中的项目信息和(2)中的项目信息一致。

程序在使用万象SDK服务之前必须注册，进行用户信息初始化，注册所需要的签名因安全因素需要放在开发者服务器上面，由终端在需要使用的时候向开发者服务器请求，开发者服务器鉴权服务部署参考[鉴权服务部署示例](/doc/product/275/如何接入#2.2-.E4.B8.80.E8.88.AC.E6.8E.A5.E5.85.A5)。

### 3.1 向业务服务器请求sign

在体验的程序中的请求sign代码在UpdateSignTask 中，代码如下：

```
  HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
  InputStream in = urlConnection.getInputStream();
            
  byte[] mSocketBuf = new byte[4* 1024];
  ByteArrayOutputStream baos = new ByteArrayOutputStream();
  int count = 0;
  while ((count = in.read(mSocketBuf, 0, mSocketBuf.length)) > 0) {
     baos.write(mSocketBuf, 0, count);
  }            
            
  String config = new String(baos.toByteArray());
  JSONObject jsonData = new JSONObject(config);
  String configContent = jsonData.getString("sign");
```
	
### 3.2 注册

代码在BizService中。

```
UploadManager.authorize(APPID, USERID, FileType.Photo, PHOTO_SIGN);
```

### 3.3 使用万象服务，下面以上传为例说明

```
  UploadTask task = new PhotoUploadTask(filePath,new IUploadTaskListener() {
      @Override
      public void onUploadSucceed(final FileInfo result) {
          Log.i("Demo", "upload succeed: " + result.url);
      }
			
      @Override
      public void onUploadStateChange(TaskState state) {
      }
			
      @Override
      public void onUploadProgress(long totalSize, long sendSize){
          long p = (long) ((sendSize * 100) / (totalSize * 1.0f));
          Log.i("Demo", "上传进度: " + p + "%");
      }
			
      @Override
      public void onUploadFailed(final int errorCode, final String errorMsg){
          Log.i("Demo", "上传结果:失败! ret:" + errorCode + " msg:" + errorMsg);		
      }
  });
  task.setBucket(BizService.BUCKET);  // 设置Bucket(可选)
  task.setFileId("test_fileId_" + UUID.randomUUID()); // 为图片自定义FileID(可选)
  cuploadManager.upload(task);  // 开始上传
	
```

其他功能同理，具体代码详情见demo。