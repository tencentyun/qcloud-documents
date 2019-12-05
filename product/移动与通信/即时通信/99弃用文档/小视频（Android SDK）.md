## 集成小视频功能扩展包


从 [官网](https://cloud.tencent.com/product/im.html#sdk) 下载 IM SDK 开发包，小视频功能扩展包。IM SDK 包的功能见 [概述](https://cloud.tencent.com/document/product/269/9227)， 小视频功能扩展包各个文件功能如下。

```
ugc_ext_libs
├── arm64-v8a
│   ├── lib_imcore_ugc_ext_gyp.so
│   └── libtxrtmpsdk.so
├── armeabi
│   ├── lib_imcore_ugc_ext_gyp.so
│   └── libtxrtmpsdk.so
├── armeabi-v7a
│   ├── lib_imcore_ugc_ext_gyp.so
│   └── libtxrtmpsdk.so
├── cos-sdk-android.1.4.3.6.jar
├── imsdk_ugc_ext.jar
├── okhttp-3.2.0.jar
├── okio-1.6.0.jar
└── txrtmpsdk.jar
```

| 包名 | 描述 | 
|---------|---------|
| imsdk_ugc_ext.jar | IM SDK 小视频功能扩展 Java 封装，提供小视频上传、小视频消息收发功能 |
| txrtmpsdk.jar | 小视频功能 SDK 库 Java 封装，提供小视频录制、编辑、预览等功能<br>具体功能可以参考 [短视频 SDK 功能列表](/document/product/584/9457) |
| cos-sdk-android.1.4.3.6.jar | 对象存储 COS 相关的 jar 包 |
| okhttp-3.2.0.jar | 网络请求库 |
| okio-1.6.0.jar | 网络操作 I/O 库 |
| lib_imcore_ugc_ext_gyp.so | IM SDK 小视频功能扩展核心组件 |
| libtxrtmpsdk.so | 直播 SDK 核心组件 |

因为小视频扩展功能包只提供了 `armeabi`、`armeabi-v7a` 和 `arm64-v8a` 这三种 CPU 架构的 so 库，所以在编译的时候，最好通过 `abiFilters` 把 `x86` 架构排除掉。

```sh
# build.gradle文件

buildTypes {
	release {
		ndk {
			// 需要将 x86 架构过滤掉
			abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
		}
	}

	debug {
		ndk {
			// 需要将 x86 架构过滤掉
			abiFilters "armeabi", "armeabi-v7a", "arm64-v8a"
		}
	}
}
```

**小视频存储功能**需要在控制台开通点播服务，开通方法如下。

![](https://mc.qcloudimg.com/static/img/7830ff8639567e4a9d60923349bf5a58/image.png)

## 录制小视频
### 画面预览
`TXUGCRecord`（位于 `TXUGCRecord.java`） 负责小视频的录制功能，我们的第一个工作是先把预览功能实现。`startCameraSimplePreview` 函数用于启动预览。由于启动预览要打开摄像头和麦克风，所以这里可能会有权限申请的提示窗。

```java
mTXCameraRecord = TXUGCRecord.getInstance(this.getApplicationContext());
mTXCameraRecord.setVideoRecordListener(this);					//设置录制回调
mVideoView = (TXCloudVideoView) findViewById(R.id.video_view);	//准备一个预览摄像头画面的 TXCloudVideoView
mVideoView.enableHardwareDecode(true);
TXRecordCommon.TXUGCSimpleConfig param = new TXRecordCommon.TXUGCSimpleConfig();
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_LOW;		// 360p
param.videoQuality = TXRecordCommon.VIDEO_QUALITY_MEDIUM;		// 540p
//param.videoQuality = TXRecordCommon.VIDEO_QUALITY_HIGH;		// 720p
param.isFront = true;											//是否前置摄像头，使用 switchCamera 可以切换
mTXCameraRecord.startCameraSimplePreview(param,mVideoView);
```

### 画面特效
不管是录制前，还是录制中，您都可以使用 `TXUGCRecord` 里的特效开关来为视频画面添加一些特效，或者是对摄像头本身进行控制。

```java
//////////////////////////////////////////////////////////////////////////
//                      以下为 1.9.1 版本后均支持的特效
//////////////////////////////////////////////////////////////////////////
//
// 切换前后摄像头 参数 mFront 代表是否前置摄像头 默认前置
mTXCameraRecord.switchCamera(mFront);

// 设置美颜 和 美白 效果级别
// beautyDepth     : 美颜级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
// whiteningDepth  : 美白级别取值范围 0 ~ 9； 0 表示关闭 1 ~ 9值越大 效果越明显。
mTXCameraRecord.setBeautyDepth(beautyDepth, whiteningDepth);

// 设置颜色滤镜：浪漫、清新、唯美、粉嫩、怀旧...
// Bitmap     : 指定滤镜用的颜色查找表。注意：一定要用 png 格式！！！
// demo用到的滤镜查找表图片位于 RTMPAndroidDemo/app/src/main/res/drawable-xxhdpi/目录下。
// setSpecialRatio : 用于设置滤镜的效果程度，从 0 到 1，越大滤镜效果越明显，默认取值 0.5
mTXCameraRecord.setFilter(filterBitmap);
mTXCameraRecord.setSpecialRatio(0.5);

// 是否打开闪光灯 参数 mFlashOn 代表是否打开闪关灯 默认关闭
mTXCameraRecord.toggleTorch(mFlashOn);

//////////////////////////////////////////////////////////////////////////
//                       以下为仅特权版才支持的特效
// （由于采用优图团队的知识产权，我们无法对外免费提供，需要使用特权版 IM SDK 才能支持）
//////////////////////////////////////////////////////////////////////////

// 设置动效贴纸 motionTmplPath 动效文件路径： 空 String "" 则取消动效
mTXCameraRecord.setMotionTmp(motionTmplPath);
```


### 文件录制
调用 `TXUGCRecord` 的 `startRecord` 函数即可开始录制，调用 `stopRecord` 函数即可结束录制，`startRecord` 和 `stopRecord` 的调用一定要配对。

```java
mTXCameraRecord.startRecord();
mTXCameraRecord.stopRecord();
``` 

录制的过程和结果是通过 `TXRecordCommon.ITXVideoRecordListener`（位于 `TXRecordCommon.java` 中定义）接口反馈出来的。

- `onRecordProgress` 用于反馈录制的进度，参数`millisecond`表示录制时长，单位毫秒。
```java
@optional
void onRecordProgress(long milliSecond);
``` 

- `onRecordComplete` 反馈录制的结果，`TXRecordResult` 的 `retCode` 和 `descMsg` 字段分别表示错误码和错误描述信息，`videoPath` 表示录制完成的小视频文件路径，`coverImage` 为自动截取的小视频第一帧画面，便于在视频发布阶段使用。
```java   
@optional
void onRecordComplete(TXRecordResult result);
```     

### 文件预览
使用 [视频播放](https://cloud.tencent.com/document/product/584/9373) 即可预览刚才生成的 MP4 文件，需要在调用  `startPlay` 时指定播放类型为 [PLAY_TYPE_LOCAL_VIDEO](https://cloud.tencent.com/document/product/584/9373#step-3.3A-.E5.90.AF.E5.8A.A8.E6.92.AD.E6.94.BE.E5.99.A86) 。

## 小视频消息
### 发送小视频消息

小视频消息由 `TIMUGCElem` 定义。它是 `TIMElem` 的一个子类，也就是说小视频也是消息的一种内容。 发送小视频的过程，就是将 `TIMUGCElem` 加入到 `TIMMessage` 中，然后随消息一起发送出去。详细如下。

**`TIMUGCElem` 原型：**

```java
/**
 * 构造 UGC 消息实例
 * @since 3.1.0
 */
public TIMUGCElem() 

/**
 * 获取 UGC 消息文件 ID
 * @return 文件 ID
 * @since 3.1.0
 */
public String getFileId()

/**
 * 获取 UGC 封面
 * @return UGC 封面
 * @since 3.1.0
 */
public TIMUGCCover getCover() 

/**
 * 设置 UGC 封面，需要在发送消息的时候设置
 * @param cover UGC 封面
 * @since 3.1.0
 */
public void setCover(@NonNull TIMUGCCover cover) 

/**
* 获取 UGC 视频
 * @return UGC 视频
 * @since 3.1.0
 */
public TIMUGCVideo getVideo() 

/**
 * 设置 UGC 视频， 在发送消息的时候设置
 * @param video UGC 视频
 * @since 3.1.0
 */
public void setVideo(@NonNull TIMUGCVideo video) 

/**
 * 获取 UGC 封面图片文件路径
 * @return UGC 封面图片文件路径
 * @since 3.1.0
 */
public String getCoverPath()

/**
 * 设置 UGC 封面图片文件路径， 在发送消息的时候设置
 * @param coverPath 封面图片文件路径
 * @since 3.1.0
 */
public void setCoverPath(@NonNull String coverPath) 

/**
 * 获取 UGC 视频文件路径
 * @return 视频文件路径
 * @since 3.1.0
 */
public String getVideoPath() 

/**
 * 设置 UGC 视频文件路径，在发送消息的时候设置
 * @param videoPath 视频文件路径
 * @since 3.1.0
 */
public void setVideoPath(@NonNull String videoPath) 
```

**`TIMUGCCover` 原型：**
```java
/**
 * 构造封面实例
 * @since 3.1.0
 */
public TIMUGCCover()

/**
 * 构造封面实例
 * @param type 封面图片文件类型
 * @param width 封面图片宽度
 * @param height 封面图片高度
 * @since 3.1.0
 */
public TIMUGCCover(@NonNull String type, long width, long height)

/**
 * 获取封面图片文件类型
 * @return 封面文件类型
 * @since 3.1.0
 */
public String getType() 

/**
 * 设置封面图片文件类型，需要在发送消息的时候进行设置
 * @param type 文件类型
 * @since 3.1.0
 */
public TIMUGCCover setType(String type)

/**
 * 获取封面图片宽度
 * @return 封面图片宽度
 * @since 3.1.0
 */
public long getWidth()

/**
 * 设置封面图片宽度
 * @param width 封面图片宽度，需要在发送消息的时候进行设置
 * @since 3.1.0
 */
public TIMUGCCover setWidth(long width)

/**
 * 获取封面图片高度
 * @return 封面图片高度
 * @since 3.1.0
 */
public long getHeight() 

/**
 * 设置封面高度
 * @param height 封面高度，需要在发送消息的时候进行设置
 * @since 3.1.0
 */
public TIMUGCCover setHeight(long height)

/**
 * 获取封面URL
 * @return 封面 URL
 * @since 3.1.0
 */
public String getUrl()

/**
 * 获取封面图片文件大小
 * @return 文件大小
 * @since 3.1.0
 */
public long getSize()

/**
 * 下载封面图片
 * @param path 封面下载后保存路径
 * @param cb 回调
 * @since 3.1.0
 */
public void getImage(@NonNull String path, @NonNull TIMCallBack cb)
```

**`TIMUGCVideo` 原型：**
```java
/**
 * 构造 UGC 视频实例
 * @since 3.1.0
 */
public TIMUGCVideo()

/**
 * 构造UGC视频实例
 * @param type 视频文件类型
 * @param duration 视频时长
 * @since 3.1.0
 */
public TIMUGCVideo(@NonNull String type, long duration)

/**
 * 获取视频文件类型
 * @return 视频文件类型
 * @since 3.1.0
 */
public String getType() 

/**
 * 设置视频文件类型，需要在发送消息时设置
 * @param type 视频文件类型
 * @since 3.1.0
 */
public TIMUGCVideo setType(String type)

/**
 * 获取视频时长
 * @return 视频时长
 * @since 3.1.0
 */
public long getDuration()

/**
 * 设置视频时长，需要在发送消息时设置
 * @param duration 视频时长
 * @since 3.1.0
 */
public TIMUGCVideo setDuration(long duration) 

/**
 * 获取视频 URL
 * @return 视频 URL
 * @since 3.1.0
 */
public String getUrl()

/**
 * 获取视频文件大小
 * @return 视频文件大小
 * @since 3.1.0
 */
public long getSize()

/**
 * 下载视频
 * @param path 下载视频文件保存路径
 * @param cb 回调
 * @since 3.1.0
 */
public void getVideo(@NonNull String path, @NonNull TIMCallBack cb)
```

在消息发送期间，可以通过资源上传进度监听器 `TIMUploadProcessListener` 得到当前上传进度。进度监听器可以通过 `TIMUserConfig` 的 `setUploadProgressListener` 在登录前统一设置。

**原型：**

```java
/**
 * 设置上传进度监听器
 * @param uploadProgressListener 上传进度监听器
 */
public TIMUserConfig setUploadProgressListener(TIMUploadProgressListener uploadProgressListener)
```

**示例：**

```java
// 小视频封面文件信息
TIMUGCCover cover = new TIMUGCCover();
File file = new File(coverPath);
int height = 0, width = 0;
if (file.exists()) {
	final BitmapFactory.Options options = new BitmapFactory.Options();
	options.inJustDecodeBounds = true;
	BitmapFactory.decodeFile(coverPath, options);
	height = options.outHeight;
	width = options.outWidth;
}
cover.setHeight(height);
cover.setWidth(width);
cover.setType("PNG");

// 小视频视频文件信息
TIMUGCVideo video = new TIMUGCVideo();
video.setType("MP4");
video.setDuration(duration);

// 构建小视频 elem
TIMUGCElem elem = new TIMUGCElem();
elem.setCover(cover);
elem.setVideo(video);
elem.setCoverPath(coverPath);
elem.setVideoPath(filePath);

// 将小视频 elem 添加到消息中
TIMMessage message = new TIMMessage();
if(message.addElement(elem) != 0){
	Log.e(TAG, "addElement failed.");
	return;
}

// 发送小视频消息
TIMConversation con = TIMManager.getInstance().getConversation(TIMConversationType.Group, groupId);
con.sendMessage(message, new TIMValueCallBack<TIMMessage>() {
	@Override
	public void onError(int code, String desc) {//发送消息失败
		//错误码 code 和错误描述 desc，可用于定位请求失败原因
		//错误码 code 含义请参见错误码表
		Log.e(TAG, "sendMessage failed, code: " + code + "| desc: " + desc);
	}

	@Override
	public void onSuccess(TIMMessage msg) {
		//发送消息成功
		Log.d(TAG, "sendMessage succ");
	}
});
```


### 接收小视频消息

接收方收到消息后，可通过 `TIMMessage` 中的 `getElement` 从 `TIMMessage` 中获取所有的消息节点，其中类型为 `TIMUGCElem` 的是小视频消息节点。然后通过节点中的 `TIMUGCCover` 和 `TIMUGCVideo` 对象获取该小视频的视频和封面图片文件信息及相应文件下载。

以下示例从会话中取出10条消息，获取小视频消息并下载相应数据。**小视频解析示例：**

```java
//获取一个群组会话实例
conversation = TIMManager.getInstance().getConversation(TIMConversationType.Group, groupId);
TIMConversationExt conExt = new TIMConversationExt(conversation);
conExt.getMessage(10, null, new TIMValueCallBack<List<TIMMessage>>() {
	@Override
	public void onError(int code, String desc) {
		Log.e(tag, "get msgs failed, code: " + code + "|msg: " + desc);
	}

	@Override
	public void onSuccess(List<TIMMessage> timMessages) {
		Log.i(tag, "get msgs succ, size: " + timMessages.size());
		for(TIMMessage msg : timMessages) {
			for(int i = 0; i < msg.getElementCount(); i++){
				TIMElem elem = msg.getElement(i);
				//过滤小视频消息
				if(elem.getType() == TIMElemType.UGC){
					TIMUGCElem timUgcElem = (TIMUGCElem)elem;
					TIMUGCCover cover = timUgcElem.getCover();
					//下载小视频消息封面文件，并保存到 coverPath 指定的路径
					cover.getImage(coverPath, new TIMCallBack() {
						@Override
						public void onError(int code, String desc) {
							Log.e(tag, "download cover failed, code: " + code + "|msg: " + desc);
						}

						@Override
						public void onSuccess() {
							Log.d(tag, "download cover succ");
						}
					});

					//下载小视频消息视频文件，并保存到 videoPath 指定的路径
					TIMUGCVideo video = timUgcElem.getVideo();
					video.getVideo(videoPath, new TIMCallBack() {
						@Override
						public void onError(int code, String desc) {
							Log.e(tag, "download video failed, code: " + code + "|msg: " + desc);
						}

						@Override
						public void onSuccess() {
							Log.d(tag, "download video succ");
						}
					});
				}
			}
		}
	}
});
```
