## 1 注册APP
在腾讯云页面上注册APP信息，获取APPID。
## 2 工程配置
### 2.1 导入SDK
将SDK包中的libs目录合并到本地工程的libs目录，然后配置工程导入所有jar包。
上传SDK的libs目录如下：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/SDK-and-1.jpg)
PS：如果工程中含有armeabi-v7a，则上述so也需要拷贝一份到此目录下，否则由于android系统的问题在安装apk之后会找不到so。
<font color='red'>so兼容x86架构，若项目需要兼容x86，则将sdk中的so复制一份放入x86目录下即可。</font>
下载SDK的libs目录如下：
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/SDK-and-2.jpg)

### 2.2 配置manifest
SDK需要网络访问相关的一些权限，需要在manifest中进行权限声明如下所示：
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

## 3 上传SDK
### 3.1 初始化
在使用上传功能之前需要先初始化，目前支持文件、图片和视频三种业务，用户根据需求进行注册，初始化分为两步:
  1. 创建UploadManager对象
 
-  原型

```

/**
 * 业务类型
 * File–文件业务，Photo-图片业务，Video视频业务，Audio暂时未支持
 *
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
 *                       化保存未完成任务列表，以便应用退出重进后能继续进行上传；传
 *                       入为Null，则不会进行持久化保存
 */
public UploadManager(Context context, String appid, FileType fileType, String persistenceId)

```

- 示例

```

import com.tencent.upload.UploadManager;
import com.tencent.upload.Const.FileType;

// 实例化视频业务上传管理类
UploadManager  videoUploadMgr = null;
videoUploadMgr = new UploadManager(context, APPID,  FileType.Video, "qcloudvideo");

```

### 3.2 视频上传
上传视频的步骤如下:
1. 创建FileUploadTask对象
2. 调用UploadManager的upload方法，将FileUploadTask对象传入

- 原型

```

public VideoUploadTask(String bucket, String srcFilePath, String destFilePath, String bizAttr, VideoAttr videoAttr,int to_over_write, IUploadTaskListener listener);

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

- 示例

```

import com.tencent.upload.task.impl.FileUploadTask;

FileUploadTask task = new VideoUploadTask(String bucket, String srcFilePath, String destFilePath, String bizAttr, VideoAttr videoAttr,int to_over_write, IUploadTaskListener listener)
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
task.setAuth(VIDEO_SIGN);
videoUploadMgr.upload(task);  // 开始上传

```

### 3.3 暂停、恢复、取消上传
上传任务可以暂停、恢复或者取消，只需要传入相应的taskId即可，上传任务的状态变化会通过IUploadTaskListener通知。
-  原型

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

-  示例

```

int taskId= task.getTaskId();
videoUploadMgr.pause(taskId);  // 暂停上传
videoUploadMgr.resume(taskId); // 恢复上传
videoUploadMgr.cancel(taskId); // 取消上传

```

### 3.4 视频文件查询
查询视频文件的详细信息，步骤如下:
1. 通过文件url创建FileStatTask对象
2. 调用UploadManager的sendCommand方法，将FileStatTask对象传入
3. 在FileStatTask.Ilistener的回调中获取查询结果

```

/**
 * 文件查询任务，视频业务使用
 * @param file_id   查询的文件ID
 * @param fileType  查询的文件类型
 * @param bucket    查询的文件所属Bucket
 * @param listener  结果回调
 */
public FileStatTask(String file_id, FileType fileType, String bucket, IListener listener)

```

-  原型

```

// FileInfo -- 文件详细信息Key
String _file_url = "file_url";                  //文件url
String _file_fileid = "file_fileid";            //文件key
String _file_upload_time = "file_upload_time";  //上传时间
String _file_size = "file_size";                //文件大小
String _file_md5 = "file_md5";                  //存储中文件md5
String _file_type = "file_type";                //视频文件
String _video_status = "video_status";          //视频状态VideoStatus
String _video_play_time = "video_play_time";    //视频播放时长
String _video_title = "video_title";            //视频标题
String _video_desc = "video_desc";              //视频描述
String _video_cover_url = "video_cover_url";    //视频封面url

```

-  示例

```
import com.tencent.upload.task.impl.FileStatTask;

FileStatTask task = new FileStatTask(fileId, FileType.Video, BUCKET, 
    new FileStatTask.IListener() {
        @Override
        public void onSuccess(final FileInfo result) {
            Log.i("Demo", "MD5:" + result.extendInfo.get("_file_md5") 
                + "\nWidth : " + result.extendInfo.get("_video_play_time") 
                + "\nHeight: " + result.extendInfo.get("_video_title"));
        }
        
        @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "查询结果:失败! ret:" + ret + " msg:" + msg);
    }
});

task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task);
```

### 3.5 文件删除
删除文件步骤如下:
1. 通过文件url创建FileDeleteTask对象
2. 调用UploadManager的sendCommand方法，将FileDeleteTask对象传入
3. 在FileDeleteTask.Ilistener的回调中获取查询结果文件复制
-  原型

```
/**
 * 文件删除任务，视频业务使用
 * @param file_id  删除的文件ID
 * @param fileType 删除的文件类型
 * @param bucket   删除的文件所属Bucket
 * @param listener 删除结果回调
 */
public FileDeleteTask(String file_id, FileType fileType, String bucket, IListener listener)
```

-  示例

```
import com.tencent.upload.task.impl.FileDeleteTask;

FileDeleteTask task= new FileDeleteTask(fileId, FileType.Video, BUCKET, 
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

task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task)
```

### 3.6 文件复制
复制文件步骤如下:
1. 通过文件url创建FileCopyTask对象
2. 调用UploadManager的sendCommand方法，将FileCopyTask对象传入
3. 在FileCopyTask.Ilistener的回调中获取查询结果文件复制
-  原型

```
/**
* 文件复制任务，视频业务使用
 * @param fileType    文件类型
 * @param bucket      文件所在Bucket
 * @param src_fileId  源文件的fileid
 * @param dst_fileId  复制后新文件的fileid
 * @param listener
 */
public FileCopyTask(FileType fileType, String bucket, String src_fileId, String dst_fileId, IListener listener)
```

-  示例

```
import com.tencent.upload.task.impl.FileCopyTask;

FileCopyTask task = new FileCopyTask(FileType.Video, BUCKET, fileId, 
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

task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task)
```

### 3.7 日志上报
SDK会将上传过程中的日志保存到本地文件中，以便当用户上传过程中遇到问题时可以直接通过日志文件进行详细定位分析，SDK提供了日志上报接口，可以将指定日期的日志上报到腾讯云后台。
-  原型

```
/**
 * 上报formDate到toDate对应的日志
 * @param appid     腾讯云注册的APPID
 * @param fromDate  开始上报时间（时间单位:天）
 * @param toDate    结束上报时间（时间单位:天）
 * @return 成功返回True，失败返回False
 */
public static boolean uploadLog(String appid, Date fromDate, Date toDate);
```

-  示例

```
// 上报一天前的日志
Date beginDate = new Date(System.currentTimeMillis() - 24 * 3600 * 1000);
Date endDate = beginDate; 
videoUploadMgr.uploadLog(APPID, beginDate, endDate);
```
## 4 下载SDK
### 4.1 初始化
-  函数原型

```
/**
 * 构造方法
 * @param context        Android Context
 * @param appid         腾讯云注册的APPID
 * @param persistenceId 每个Download实例需要分配一个唯一的id，该ID用于区分临时缓存
 *                          目录
 */
public Downloader(Context context, String appid, String persistenceId);
```

-  示例

```
// 实例化下载管理类
Downloader  downloader = new Downloader(this, APPID, "TestDownloader");
```

### 4.2 下载并发数
可以指定下载器最大并发数。
-   函数原型

```
/**
 * 指定下载队列的最⼤大并发数
 * @param count 并发数; 调用下载接口之后再修改则无效
 */
public void setMaxConcurrent(int count);
```

-   示例

```
// 设置最大并发数
downloader.setMaxConcurrent(3);
```

### 4.3 长连接/断点续传
下载器提供开关，可以设定是否开启长连接和断点续传功能。
-  函数原型

```
/**
 * 指定下载器是否支持断点续传
 * @param enable True -- 支持； False -- 不支持
 */
public void enableHTTPRange(boolean enable);
    
/**
 * 指定下载器是否支持HTTP长连接
 * @param keepalive True -- 支持； False -- 不支持
 */
public void enableKeepAlive(boolean keepalive);
```

-   示例

```
// 启动断点续传功能
downloader.enableHTTPRange(true);
// 启动长连接功能
downloader.enableKeepAlive(true);
```

### 4.4 视频下载
文件下载是采用异步模式进行下载，下载的进度/成功/失败/取消等信息通过DownloadListener进行回调通知。
-  函数原型

```
/**
 * 异步下载请求
 * @param url       要下载的文件URL
 * @param listener  下载结果监听器
 * @return       
 */
public boolean download(String url, DownloadListener listener);
```

-  监听器定义

```
/** 下载监听器 */
public interface DownloadListener{

    public void onDownloadSucceed(String url, DownloadResult result);

    public void onDownloadFailed(String url, DownloadResult result);

    public void onDownloadCanceled(String url);

    public void onDownloadProgress(String url, long totalSize, float progress);

}
```

-   示例

```
DownloadListener listener = new DownloadListener() {
    @Override
    public void onDownloadSucceed(String url, DownloadResult result) {
        Log.i("Demo", "下载成功: " + result.getPath());
    }
    
    @Override
    public void onDownloadProgress(String url, long totalSize, float progress)
    {
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

### 4.5 取消下载
-  函数原型

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

-  示例

```
// 取消单个下载任务: listener 为创建下载任务的时候传入的监听器
downloader.cancel(url,  listener);
// 取消全部下载任务 
downloader.cancelAll();
```

### 4.6 缓存查询
Downloader下载组件支持本地文件缓存
-   函数原型

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

-  示例

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

### 4.7 日志上报
SDK会将下载过程中的日志保存到本地文件中，以便当用户上传过程中遇到问题时可以直接通过日志文件进行详细定位分析，SDK提供了日志上报接口，可以将指定日期的日志上报到腾讯云后台。
-  原型

```
/**
 * 上报formDate到toDate对应的日志
 * @param appid     腾讯云注册的APPID
 * @param fromDate  开始上报时间（时间单位:天）
 * @param toDate    结束上报时间（时间单位:天）
 * @return 成功返回True，失败返回False
 */
public static boolean uploadLog(String appid, Date fromDate, Date toDate);
```

-   示例

```
// 上报一天前的日志
Date beginDate = new Date(System.currentTimeMillis() - 24 * 3600 * 1000);
Date endDate = beginDate; 
Downloader.uploadLog(APPID, beginDate, endDate);
```

## 5 文件SDK
### 5.1 初始化
见[3.1初始化](https://cloud.tencent.com/doc/product/314/Android-SDK%E8%AF%B4%E6%98%8E#3.1-.E5.88.9D.E5.A7.8B.E5.8C.96)章节
-   示例

```
import com.tencent.upload.UploadManager;
import com.tencent.upload.Const.FileType;

// 实例化Video业务上传管理类
UploadManager  videoUploadMgr = null;
videoUploadMgr = new UploadManager(context, APPID, FileType.Video, "qcloudvideo");
```

### 5.2 创建目录
创建目录步骤如下:
1. 通过文件path创建DirCreateTask对象
2. 调用UploadManager的sendCommand方法，将DirCreateTask对象传入
3. 在DirCreateTask.Ilistener的回调中获取查询结果文件复制
-   原型

```
/**
 * 文件删除任务，视频业务使用
 * @param fileType      业务类型
 * @param bucket        bucket
 * @param path          相对路径
 * @param bizAttr       目录属性 
 * @param listener      结果回调
 */
public DirCreateTask (FileType fileType, String bucket, String path, 
                       String bizAttr, IListener listener)
```

-  示例

```
import com.tencent.upload.task.impl.DirCreateTask;

DirCreateTask task = null
task = new DirCreateTask(FileType.Video, BUCKET, path, bizAttr, 
    new DirCreateTask.IListener(){
    @Override
    public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
        Log.e("Demo", "目录创建结果:成功! accessUrl:" + result. accessUrl);
    }

    @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "目录创建结果:失败! ret:" + ret + " msg:" + msg);
    }
});
    
task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task);
```

### 5.3 拉取目录
拉取目录步骤如下:
1. 通过path创建DirListTask对象
2. 调用UploadManager的sendCommand方法，将DirListTask对象传入
3. 在DirListTask.Ilistener的回调中获取查询结果文件复制
-   原型

```
public class Dentry {
    public final static int MORE = -1;                              //更多…
    public final static int DIR = ObjectType._eObjectDir;           //目录对象
    public final static int FILE = ObjectType._eObjectDir;          //文件对象
    public final static int BUCKET = ObjectType._eObjectBucket; //bucket对象
    public final static int VIDEO = ObjectType._eObjectVideo;       //视频对象

    // 拉取文件选项
    public final static int ListBoth = ListPattern._eListBoth;     //拉取文件和目录
    public final static int ListDirOnly = ListPattern._eListDirOnly; //只拉取目录
    public final static int ListFileOnly = ListPattern._eListFileOnly;//只拉取文件

    public Dentry();     //构造DIR对象类型
    public Dentry(int type);
    public VideoInfo getVideoInfo();// 如果是VIDEO对象类型，
    // 则返回视频相关信息，否则返回null
    
    public int type = 0;                //对象类型
    public String sha = "";               //sha信息
    public String path = "";            //相对路径
    public String name = "";            //对象名称
    public String accessUrl = "";       //访问URL
    public String attribute = "";       //对象属性

    public long fileSize = 0;           //文件长度
    public long fileLength = 0;         //文件长度
    public long createTime = 0;         //创建时间
    public long modifyTime = 0;         //修改时间
}

```
	
-  原型	

```
// 视频相关属性
public class VideoAttr {
    public String title = "";          // 视频title
    public String desc = "";           // 视频描述
    public long timeLen = 0;           // 视频时长
    public boolean isCheck = true;    // 0：先发后审，1：先审后发;
}

// 视频相关信息
public class VideoInfo {

    //微视频新增
    //--------------
    //f10：手机
    //f20：标清
    //f30：高清
    //--------------
    public static final int F0 = VideoFormat._eF0;
    public static final int F10 = VideoFormat._eF10;
    public static final int F20 = VideoFormat._eF20;
    public static final int F30 = VideoFormat._eF30;

    //-----------------------
    //- 描述：原视频状态
    //-----------------------
    public static final int DEFAULT = CosVideoStatus._eDEFAULT;        //默认状态
    public static final int UPLOADING = CosVideoStatus._eUPLOADING;   //视频入库中
    public static final int CHECKPASS = CosVideoStatus._eCHECKPASS;  //审核通过
    public static final int CHECKNOTPASS = CosVideoStatus._eCHECKNOTPASS;//审核不通过
    public static final int CHECKFAIL = CosVideoStatus._eCHECKFAIL; //审核失败

    //-----------------------
    //- 描述：不同码率视频状态
    //-----------------------
    public static final int INVALID = TranscodeStat._eINVALID;    //默认状态
    public static final int TRANSCODING = TranscodeStat._eTRANSCODING; //转码中
    public static final int TRANSCODEDONE = TranscodeStat._eTRANSCODEDONE; //转码成功
    public static final int TRANSCODEFAIL = TranscodeStat._eTRANSCODEFAIL; //转码失败

    //-----------------------
    //- 描述：属性修改标记
    //-----------------------
    public static final int MaskBizAttr = FileModifyFlag._eMaskBizAttr;
    public static final int MaskTitle = FileModifyFlag._eMaskTitle;
    public static final int MaskDesc = FileModifyFlag._eMaskDesc;
    public static final int MaskAll = FileModifyFlag._eMaskAll;

    public int videoStatus = VideoInfo.DEFAULT;     // 视频状态
    public VideoAttr videoAttr;                     // 视频属性
    public Map<Integer, String> playUrlList;        // 转码视频url列表
    public Map<Integer, Integer> transStatus;       // 不同码率转码状态
}
```
	
-  原型	

```
/**
 * 拉取目录任务，视频业务使用
 * @param fileType      业务类型
 * @param bucket        bucket
 * @param path          相对路径
 * @param num           拉多少记录
 * @param pattern       拉取方式,目录和文件一起拉的时候，先拉取目录再拉取文件
 * @param order         0-正序  1-反序
 * @param content       首次拉取必须清空，拉取下一页时需要传入上次一拉去时返回的content
 * @param listener      结果回调
 */
public DirListTask (FileType fileType, String bucket, String path, int num, 
                int pattern, boolean order, String content, IListener listener)

```
	
-   示例	

```
import com.tencent.upload.task.impl.DirListTask;

String content = ""; // 第一次拉取目录传入空，拉取path下一页时填入result.content
DirListTask task = null
task = new DirListTask(FileType.Video, BUCKET, path, 10, Dentry.ListBoth, false, content
    new DirListTask.IListener() {
    @Override
    public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
            ArrayList<Dentry> dirList = result.inodes;
            String strEntryList = "";
            for (Dentry entry : dirList) {
               strEntryList += entry.path + "\n";
            }
        if (result.hasMore) {
               // 存在下一页保存当前页的状态信息
               String content = result.content;
            }
        Log.e("Demo", "目录拉取结果:成功! \n" + strEntryList);
    }

    @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "目录拉取结果:失败! ret:" + ret + " msg:" + msg);
    }
});
task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task);
```
	
### 5.4 前缀搜索
前缀搜索步骤如下:
1. 通过path+前缀创建DirListTask对象
2. 通过DirListTask对象的setPrefixSearch(true)开启前缀搜索
3. 调用UploadManager的sendCommand方法，将DirListTask对象传入
4. 在DirListTask.Ilistener的回调中获取查询结果文件复制
-    原型	

```
/**
 * DirListTask任务前缀搜索开关
 * @param prefixSearch      true-开启  false-关闭
*/
public void setPrefixSearch(boolean prefixSearch)
```
	
- 	 示例

```
import com.tencent.upload.task.impl.DirListTask;

String content = ""; // 第一次拉取目录传入空，拉取path下一页时填入result.content
DirListTask filetask = null
task = new DirListTask(FileType.Video, BUCKET, path, 10, Dentry.ListBoth, false, content, new DirListTask.IListener() {
    @Override
    public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
            ArrayList<Dentry> dirList = result.inodes;
            String strEntryList = "";
            for (Dentry entry : dirList) {
               strEntryList += entry.path + "\n";
            }
        if (result.hasMore) {
                // 存在下一页保存当前页的状态信息
                String content = result.content;
            }
        Log.e("Demo", "目录拉取结果:成功! \n" + strEntryList);
    }

    @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "目录拉取结果:失败! ret:" + ret + " msg:" + msg);
    }
});

task .setPrefixSearch(true);
task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task);
```
	
### 	5.5 文件上传
上传文件的步骤如下:
1. 创建FileUploadTask对象
2. 调用UploadManager的upload方法，将FileUploadTask对象传入
-   原型

```
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
	
-   原型	

```
/**
 * 文件任务
 * @param bucket        bucket
 * @param srcFilePath   本地绝对路径
 * @param destFilePath  远程相对路径
 * @param bizAttr       文件私有属性 
 * @param listener      上传结果回调
 */

public FileUploadTask(String bucket, String srcFilePath, String destFilePath, 
                       String bizAttr, IUploadTaskListener listener);
```
	
-  示例

```
import com.tencent.upload.task.impl.FileUploadTask;
import com.tencent.upload.task.IUploadTaskListener;

FileUploadTask task = new FileUploadTask(BUCKET, filePath, destPath, "", 
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
    public void onUploadFailed(final int errorCode, final String errorMsg) {
            Log.i("Demo", "上传结果:失败! ret:" + errorCode + " msg:" + errorMsg);
    }
});

task.setAuth(VIDEO_SIGN);
videoUploadMgr.upload(task);  // 开始上传
```
	
### 5.6 视频上传
上传视频的步骤如下:
1. 创建VideoUploadTask对象
2. 调用UploadManager的upload方法，将VideoUploadTask对象传入
-   原型

```
/**
 * 视频上传任务
 * @param bucket        bucket
 * @param srcFilePath   本地绝对路径
 * @param destFilePath  远程相对路径
 * @param bizAttr       文件私有属性，选填
 * @param videoAttr     视频私有属性，选填
 * @param listener      文件上传结果监听器，选填
 */
public VideoUploadTask(String bucket, String srcFilePath, String destFilePath, 
        String bizAttr, VideoAttr videoAttr, IUploadTaskListener listener)
```

-  视频上传示例

```
import com.tencent.upload.task.VideoAttr;
import com.tencent.upload.task.VideoInfo;
import com.tencent.upload.task.impl.FileUploadTask;
import com.tencent.upload.task.IUploadTaskListener;

VideoAttr videoAttr = new VideoAttr();
videoAttr.isCheck = false;
videoAttr.title = fileName;
videoAttr.desc = "cos-video-desc" + fileName;

VideoUploadTask task = new VideoUploadTask(BUCKET, filePath, destPath, 
    "", videoAttr, new IUploadTaskListener() {
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
    public void onUploadFailed(final int errorCode, final String errorMsg) {
            Log.i("Demo", "上传结果:失败! ret:" + errorCode + " msg:" + errorMsg);
    }
});


task.setAuth(VIDEO_SIGN);
videoUploadMgr.upload(task);  // 开始上传
```

### 5.7 暂停、恢复、取消上传
见[3.3暂停、恢复、取消上传](http://cloud.tencent.com/doc/product/314/Android-SDK%E8%AF%B4%E6%98%8E#3.3-暂停、恢复、取消上传)章节
### 5.8 对象查询
查询Bucket、目录、文件等对像的详细信息，步骤如下:
1. 通过path和ObjectType创建ObjectStatTask对象
2. 调用UploadManager的sendCommand方法，将ObjectStatTask对象传入
3. 在ObjectStatTask.Ilistener的回调中获取查询结果。
-  原型

```
/**
 * 文件查询任务，视频业务使用
 * @param fileType  业务类型
 * @param bucket    bucket
 * @param path       相对路径
 * @param type       对像类型
 * @param listener  结果回调
 */
public ObjectStatTask(FileType fileType, String bucket, String path, 
                       int type, IListener listener);
```

-    示例

```
import com.tencent.upload.task.impl.ObjectStatTask;

ObjectStatTask task = null;
task = new ObjectStatTask(FileType.Video, BUCKET, path, Dentry.Dir, 
    new ObjectStatTask.IListener() {
        @Override
        public void onSuccess(final ObjectStatTask.CmdTaskRsp result) {
            Dentry dentry = result.inode;
        String info = "name:" + dentry.name;
        info += " sha:" + dentry. sha;
        info += " path:" + dentry. path;
        info += " type:" + dentry. type;
            info += " accessUrl:" + dentry.accessUrl;
            info += " attribute:" + dentry. attribute;
        info += " fileSize:" + dentry. fileSize;
            info += " fileLength:" + dentry.fileLength;
            info += " createTime:" + dentry.createTime;
            info += " modifyTime:" + dentry.modifyTime;
            Log.i("Demo", info);
        }

    @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "查询结果:失败! ret:" + ret + " msg:" + msg);
    }
});
task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(task);
```

### 5.9 对象更新
更新Bucket、目录、文件等对像步骤如下:
1. 通过文件path、ObjectType和attr创建ObjectUpdateTask对象
2. 调用UploadManager的sendCommand方法，将ObjectUpdateTask对象传入
3. 在ObjectUpdateTask.Ilistener的回调中获取删除对像结果。
-   原型

```
/**
 * 文件删除任务，File和Video业务使用
 * @param fileType  业务类型
 * @param bucket    bucket
 * @param path       相对路径
 * @param type       对像类型
 * @param attr       对像属性
 * @param listener  结果回调
 */
public ObjectUpdateTask(FileType fileType, String bucket, String path, String attr,
```

-  示例

```
import com.tencent.upload.task.impl.ObjectUpdateTask;
ObjectUpdateTask task = null; task = new ObjectUpdateTask (FileType.Video, BUCKET, path, Dentry.Dir, attr,
   new ObjectUpdateTask.IListener() {
   @Override
   public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
       Log.e("Demo", "更新结果:成功!");
   }
   
   @Override
   public void onFailure(final int ret, final String msg) {
       Log.e("Demo", "更新结果:失败! ret:" + ret + " msg:" + msg);
   }
});
task.setAuth(VIDEO_SIGN); videoUploadMgr.sendCommand(task);
```

### 5.10 对象删除
删除Bucket、目录、文件等对像步骤如下:
1. 通过文件path和ObjectType创建ObjectDeleteTask对象
2. 调用UploadManager的sendCommand方法，将ObjectDeleteTask对象传入
3. 在ObjectDeleteTask.Ilistener的回调中获取删除对像结果。
- 原型

```
/**
 * 文件删除任务，视频业务使用
 * @param fileType  业务类型
 * @param bucket    bucket
 * @param path       相对路径
 * @param type       对像类型
 * @param listener  结果回调
 */
public ObjectDeleteTask(FileType fileType, String bucket, String path, int type, IListener listener)
```

-  示例

```
import com.tencent.upload.task.impl.ObjectDeleteTask;

ObjectDeleteTask task= null;
task = new ObjectDeleteTask(FileType.Video, BUCKET, path, Dentry.Dir, 
    new ObjectDeleteTask.IListener() {

    @Override
    public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
        Log.e("Demo", "删除结果:成功!");
    }

    @Override
    public void onFailure(final int ret, final String msg) {
        Log.e("Demo", "删除结果:失败! ret:" + ret + " msg:" + msg);
    }
});

task.setAuth(VIDEO_SIGN);
videoUploadMgr.sendCommand(filetask);
```

## 6 返回码定义

<table style="display:table;width:80%;">
<tr>
<th width="120"><b>错误码</b>
</th><th width="180"><b>含义</b>
</th></tr>
<tr>
<td> -5999
</td><td> 参数错误
</td></tr>
<tr>
<td> -5998
</td><td> 签名格式错误
</td></tr>
<tr>
<td> -5997
</td><td> 后端网络错误
</td></tr>
<tr>
<td> -5996
</td><td> HTTP请求方法错误
</td></tr>
<tr>
<td> -5995
</td><td> 文件大小错误
</td></tr>
<tr>
<td> -5994
</td><td> url参数解析不匹配
</td></tr>
<tr>
<td> -5993
</td><td> multipart/formdata参数错误
</td></tr>
<tr>
<td> -5992
</td><td> 请求参数错误
</td></tr>
<tr>
<td> -5991
</td><td> 分片过大
</td></tr>
<tr>
<td> -5990
</td><td> 找不到filecontent
</td></tr>
<tr>
<td> -5989
</td><td> 上传失败
</td></tr>
<tr>
<td> -5988
</td><td> cgi初始化错误
</td></tr>
<tr>
<td> -5987
</td><td> wup编码失败
</td></tr>
<tr>
<td> -5986
</td><td> wup解码失败
</td></tr>
<tr>
<td> -5985
</td><td> 获取路由失败
</td></tr>
<tr>
<td> -5984
</td><td> sha1不匹配
</td></tr>
<tr>
<td> -5983
</td><td> 错误的session
</td></tr>
<tr>
<td> -5982
</td><td> 建立连接错误
</td></tr>
<tr>
<td> -5981
</td><td> 建立连接错误
</td></tr>
</table>






