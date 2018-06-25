本文档为万象优图V2版本和V2加强版本的Android SDK文档，V1版本的Android SDK文档参见 [Android SDK_V1](/doc/product/275/Android SDK_V1)。
注意：各版本的SDK接口不能混用，具体版本说明请参照[版本说明](/doc/product/275/版本说明)。
## 1. 开发准备
腾讯云•万象优图的最新Android SDK的下载：[Android SDK](/doc/product/275/SDK下载#1.-android-sdk)。
### 1.1 前期准备
1. SDK支持Android 2.2及以上版本的手机系统；
2. 手机必须要有网络（GPRS、3G或Wifi网络等）；
3. 手机可以没有存储空间，但会使部分功能无法正常工作；
4. 在[腾讯云图片空间](http://console.cloud.tencent.com/image/bucket)页面上添加空间，获取项目ID（APPID）。
### 1.2 导入SDK
#### 1.2.1 下载Android SDK
Android SDK的下载地址为：[Android SDK](/doc/product/275/SDK下载#1.-android-sdk)。

注意：
(1). Android SDK的库文件中包含上传SDK（upload.jar）和下载SDK（download.jar）两个可选jar包，开发者可以根据需要选择性的集成。
(2). SDK中用到的SIGN，推荐使用[服务器端SDK](/doc/product/275/SDK文档#3.-.E6.9C.8D.E5.8A.A1.E5.99.A8sdk.E6.96.87.E6.A1.A3)提供的接口来生成，并由移动端向业务服务器请求。SIGN的具体生成和使用请参照[鉴权服务技术方案](/doc/product/275/签名与鉴权文档)。

#### 1.2.2 导入项目
将SDK包中的libs目录合并到本地工程的libs目录，然后配置工程导入所有jar包。
上传SDK的libs目录如下：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/androidsdk-1-2.jpg)
下载SDK的libs目录如下：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/android-sdk-2.jpg)

#### 1.2.3 配置manifest
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
## 2. API详细说明
### 2.1 上传SDK API
#### 2.1.1 初始化
在使用上传功能之前需要先初始化，初始化时只需创建UploadManager对象即可。
注意：请将FileType指定为Photo。
原型:

```
/**
  * 业务类型
  * File–文件业务，Photo-图片业务，Video视频业务，Audio暂时未支持
  */
  public enum FileType {
      File, Photo, Audio, Video, Other
  }
  /**
  * 构造方法
  * @param context
  * @param appid   腾讯云注册的APPID
  * @param fileType 业务类型
  * @param persistenceId  持久化ID，每个UploadManager需设置一个唯一的ID用于持久
  *                           化保存未完成任务列表，以便应用退出重进后能继续进行上传；传
  *                           入为Null，则不会进行持久化保存
  */
  public UploadManager(Context context, String appid, 
                       FileType fileType, String persistenceId)
```

示例:

```
import com.tencent.upload.UploadManager;
  import com.tencent.upload.Const.FileType;

  // 实例化Photo业务上传管理类
  UploadManager  photoUploadMgr = null;
  photoUploadMgr = new UploadManager(context, APPID, 
                                     FileType.Photo, "qcloudphoto");
```
#### 2.1.2 图片上传
上传一张图片的步骤如下:
1.	创建PhotoUploadTask对象；
2.	调用UploadManager的upload方法，将PhotoUploadTask对象传入。
原型:

```
 public PhotoUploadTask(String file_path, IUploadTaskListener listener);
 /** 上传回调监听器 */
 public interface IUploadTaskListener {
   // 上传成功
   void onUploadSucceed(FileInfo result);
   // 上传失败
  void onUploadFailed(int errorCode, String errorMsg);
   // 上传进度
  void onUploadProgress(long totalSize, long recvDataSize);
   // 上传任务状态变化
  void onUploadStateChange(TaskState state); 
 }
```
示例:

```
import com.tencent.upload.task.impl.PhotoUploadTask;

  PhotoUploadTask task = new PhotoUploadTask(filePath,
       new IUploadTaskListener() {
		
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
  }
  );
  task.setBucket(BUCKET); 
  task.setFileId("test_fileId_" + UUID.randomUUID()); // 为图片自定义FileID(可选)
  task.setAuth(PHOTO_SIGN);
  photoUploadMgr.upload(task);  // 开始上传
	
```
#### 2.1.3	暂停、恢复、取消上传
上传任务可以暂停、恢复或者取消，只需要传入相应的taskId即可，上传任务的状态变化会通过IUploadTaskListener通知。
原型:

```
/**
  * 暂停指定的上传任务
  * @param taskId 对应UploadTask的任务ID
  * @return 成功返回True，失败返回False；如果传入的taskId没有对应的UploadTask，则失败
  */
   public boolean pause(int taskId);
  /**
  * 恢复指定的上传任务，重新发送
  * @param taskId 对应UploadTask的任务ID
  * @return 成功返回True，失败返回False；如果传入的taskId没有对应的UploadTask，则失败
  */
   public boolean resume(int taskId);
  /**
  * 取消指定的上传任务
  * @param taskId 对应UploadTask的任务ID
  * @return 成功返回True，失败返回False；如果传入的taskId没有对应的UploadTask，则失败
  */
   public boolean cancel(int taskId);
```
示例:

```
 int taskId = task.getTaskId();
 uploadManager.pause(taskId);  // 暂停上传
 uploadManager.resume(taskId); // 恢复上传
 uploadManager.cancel(taskId); // 取消上传
```
#### 2.1.4	图片查询
查询图片文件的详细信息，步骤如下:
1.	通过文件url创建FileStatTask对象；
2.	调用UploadManager的sendCommand方法，将FileStatTask对象传入；
3.	在FileStatTask.Ilistener的回调中获取查询结果。
原型:
 
```
 /**
     * 文件查询任务
     * @param url       要查询的文件url
     * @param listener  结果回调
     */
  public FileStatTask(String url, IListener listener);
 
  /**
     * 文件查询任务
     * @param file_id   查询的文件ID
     * @param fileType  查询的文件类型
     * @param bucket    查询的文件所属bucket
     * @param listener  结果回调
     */
  public FileStatTask(String file_id, FileType fileType, String bucket, IListener listener)


  // FileInfo -- 文件详细信息Key
  String _file_url = "file_url";                    //文件url
  String _file_fileid = "file_fileid";             //文件key
  String _file_upload_time = "file_upload_time"; //上传时间
  String _file_size = "file_size";                  //文件大小
  String _file_md5 = "file_md5";                    //存储中文件md5
  String _file_type = "file_type";                 //标示文件为图片类型
  String _photo_type = "photo_type";                //图片类型1JPG、2PNG、3BMP、4WEBP
  String _photo_width = "photo_width";              //图片宽
  String _photo_height = "photo_height";            //图片高
  String _photo_bind_info = "photo_bind_info";      //图片绑定数据
```
示例:
 
```
FileStatTask filetask = new FileStatTask(fileId, FileType.Photo, BUCKET, 
      new FileStatTask.IListener() {
          @Override
          public void onSuccess(final FileInfo result) {
              Log.i("Demo", "MD5:" + result.extendInfo.get("file_md5") 
              + "\nWidth : " + result.extendInfo.get("photo_width") 
              + "\nHeight: " + result.extendInfo.get("photo_height"));
         } 
			
         @Override
         public void onFailure(final int ret, final String msg) {
             Log.e("Demo", "查询结果:失败! ret:" + ret + " msg:" + msg);
	 }
  });
  task.setAuth(PHOTO_SIGN);
  photoUploadMgr.sendCommand(filetask);
```
#### 2.1.5	图片删除
删除文件步骤如下:
1.	通过文件url创建FileDeleteTask对象；
2.	调用UploadManager的sendCommand方法，将FileDeleteTask对象传入；
3.	在FileDeleteTask.Ilistener的回调中获取查询结果文件复制。
原型:

```
 /**
     * 图片删除任务
     * @param file_id  删除的文件ID
     * @param fileType 删除的文件类型
     * @param bucket   删除的文件所属bucket
     * @param listener 删除结果回调
     */
  public FileDeleteTask(String file_id, FileType fileType, String bucket, IListener listener)
```
示例:
 
```
FileDeleteTask filetask = new FileDeleteTask(fileId, FileType.Photo, BUCKET, 
      new FileDeleteTask.IListener() {
          @Override
          public void onSuccess(Void result) {
	      Log.e("Demo", "删除结果:成功!");
          }

          @Override
          public void onFailure(final int ret, final String msg) {
              Log.e("Demo", "删除结果:失败! ret:" + ret + " msg:" + msg);
	  }
  });
  task.setAuth(PHOTO_SINGLE_SIGN);
  photoUploadMgr.sendCommand(filetask);
```
#### 2.1.6	图片复制
复制文件步骤如下:
1.	通过文件url创建FileCopyTask对象；
2.	调用UploadManager的sendCommand方法，将FileCopyTask对象传入；
3.	在FileCopyTask.Ilistener的回调中获取查询结果文件复制。
原型:
  
```
/**
     * 文件复制任务
     * @param fileType    文件类型
     * @param bucket      文件所在bucket
     * @param src_fileId  源文件的fileid
     * @param dst_fileId  复制后新文件的fileid
     * @param listener
     */
  public FileCopyTask(FileType fileType, String bucket, String src_fileId, String dst_fileId, IListener listener)
```
示例:
 
```
 FileCopyTask filetask = new FileCopyTask(FileType.Photo, BUCKET, fileId, 
      fileId + "_copy", new FileCopyTask.IListener() {
          @Override
          public void onSuccess(final String result) {
              Log.e("Demo", "复制结果:成功! url:" + result);
          }

          @Override
          public void onFailure(final int ret, final String msg) {
              Log.e("Demo", "复制结果:失败! ret:" + ret + " msg:" + msg);
          }
  });
  task.setAuth(PHOTO_SINGLE_SIGN);
  photoUploadMgr.sendCommand(filetask);
```

### 2.2	下载SDK API
#### 2.2.1	初始化
原型:

```
/**
  * 构造方法
  * @param context        Android Context
  * @param appid  	  腾讯云注册的APPID
  * @param persistenceId  每个Download实例需要分配一个唯一的id，该ID用于区分临时缓存目录
  */
  public Downloader(Context context, String appid, String persistenceId);
示例:
 // 实例化下载管理类
 Downloader  downloader = new Downloader(this, APPID, "TestDownloader");
```
#### 2.2.2	下载并发数
可以指定下载器最大并发数。
原型:

```
/**
 * 指定下载队列的最大并发数
 * @param count 并发数; 调用下载接口之后再修改则无效
 */
 public void setMaxConcurrent(int count);
```
示例:

```
 // 设置最大并发数
 downloader.setMaxConcurrent(3);
```
#### 2.2.3	长连接/断点续传
下载器提供开关，可以设定是否开启长连接和断点续传功能。
原型:

```
/**
 * 指定下载器是否支持断点续传
 * @param enable True -- 支持； False -- 不支持
 */
  public void enableHTTPRange(boolean enable);
 /**
  * 指定下载器是否⽀支持HTTP长连接
  * @param keepalive True -- 支持； False -- 不支持
  */
 public void enableKeepAlive(boolean keepalive);
```
示例:

```
 // 启动断点续传功能
 downloader.enableHTTPRange(true);
 // 启动长连接功能
 downloader.enableKeepAlive(true);
```
#### 2.2.4	图片下载
文件下载是采用异步模式进行下载，下载的进度/成功/失败/取消等信息通过DownloadListener进行回调通知。
原型:

```
 /**
 * 异步下载请求
 * @param url       要下载的文件URL
 * @param listener  下载结果监听器
 * @return       
 */
  public boolean download(String url, DownloadListener listener);
```
原型:

```

 /** 下载监听器 */
 public interface DownloadListener
   {
        public void onDownloadSucceed(String url, DownloadResult result);	
        public void onDownloadFailed(String url, DownloadResult result);     
        public void onDownloadCanceled(String url);
        public void onDownloadProgress(String url, long totalSize, float progress);
   }

```
示例:

```
DownloadListener listener = new DownloadListener() {
     @Override
     public void onDownloadSucceed(String url, DownloadResult result) {
         Log.i("Demo", "下载成功: " + result.getPath());
     }	
     @Override
     public void onDownloadProgress(String url, long totalSize, float progress) {
         long nProgress = (int) (progress * 100);
         Log.i("Demo", "下载进度: " + nProgress + "%");
     }
     @Override
     public void onDownloadFailed(String url, DownloadResult result) {
         Log.i("Demo", "下载失败: " + result. getErrorCode());
     }	
     @Override
     public void onDownloadCanceled(String url) {
         Log.i("Demo", "下载任务被取消");
     }
 };
 downloader.download(url,  listener);
```
#### 2.2.5	取消下载
原型:

```
/**
 * 取消指定的下载任务
 * @param url       下载文件地址
 * @param listener  下载结果监听器
 */
 public void cancel(String url, DownloadListener listener);
 /**
 * 取消所有下载任务
 */
 public void cancelAll();
```
示例:

```
// 取消单个下载任务: listener 为创建下载任务的时候传入的监听器
 downloader.cancel(url,  listener);
 // 取消全部下载任务 
 downloader.cancelAll();
```
#### 2.2.6	缓存查询
Downloader下载组件支持本地文件缓存
原型:

```
 /**
 * 判断指定URL对应的本地缓存文件是否存在
 * @param url 文件地址
 * @return 有本地缓存文件则返回True，否则False
 */
 public boolean hasCache(String url);	
 /**
 * 获取指定URL的本地缓存文件
 * @param url 文件地址
 * @return 缓存存在则返回对应的File，否则返回Null
 */
  public File  getCacheFile(String url);
/**
 * 清除SDK所有缓存文件
   */
 public void cleanCache();
```
示例:

```
//先检查是否有本地缓存文件
 if (mDownloader.hasCache(url)) {
     File file = mDownloader.getCacheFile(url);
     if (file != null && file.exists()) {
         Log.i("Demo", "命中缓存");
         return;
     }
 }
 // 如果需求清空本地缓存
 mDownloader.cleanCache();
```
### 2.3	Android返回码说明
SDK上传错误码说明：

错误码|	含义
---------|---------
0|	成功
-20001|	秒传成功
-20002|	任务取消
-20003|	任务暂停
-20004|	文件不存在
-20005|	文件长度不合法
-20006|	网络不可用
-20007|	服务器回包为空
-20008|	请求超时
-20011|	没有可用Session
-20012|	Session连接断开
-20013|	Session状态非法
-20014|	网络探测失败
-20100|	没有可用路由
-20101|	网络通道建立失败
-20102|	连接发送失败
-20103|	连接为空
-20104|	接收数据异常, 分包失败
-20105|	请求编码错误
-20290|	握手失败
-20291|	握手超时
-21001|	内存不足
-22000|	IO异常
-25000|	其他

SDK下载错误码说明：

错误码|	含义
---------|---------
-4	|解码失败
-3	|长度与content-length不匹配
-2	|no-cache
-1	|非法格式
1	|本地FileNotFound exception
2	|本地IO exception
3	|本地OutOfMemery error
4	|本地未知exception
5	|本地IllegalStateException
6	|本地Socket exception
7	|本地Socket Timeout exception
8	|本地ClientProtocolException
9	|本地UnknowHostException
10|	本地ConnectTimeoutException
11|	本地NoHttpResponseException
12|	本地SSLPeerUnverifiedException
13|	本地ConnectionPoolTimeoutException
14|	ConnectionClosedException
15|	网路不可用
16|	磁盘空间不足

其他错误码参见 [错误码说明](/doc/product/275/版本说明)。
