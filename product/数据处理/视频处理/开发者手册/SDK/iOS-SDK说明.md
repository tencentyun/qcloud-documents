## 1	开发准备
### 1.1	前期准备
1. iOS 5.0+；
2. 手机必须要有网络（GPRS、3G、Wifi网络等）；
3. 在腾讯云微视频页面上添加空间（bucket），获取项目ID（APPID）。

### 1.2	导入SDK
微视频 iOS SDK其中包括上传SDK和下载SDK，上传SDK压缩包QCloudUploadSDK.zip,下载SDK压缩包QCloudDownloadSDK.zip.
上传和下载SDK压缩包中分别包含了一个.a 静态库和一个包含头文件的文件夹Headers，解压后的内容如下：<br>
上传SDK：<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-1.jpg" alt="ios-sdk-1.jpg"><br>
下载SDK：<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-2.jpg" alt="ios-sdk-2.jpg"><br>
将解压后的QCloudUPloadSDK和QCloudDownloadSDK拖入工程目录，Xcode会自将其加入链接库列表中。<br>
注：如果只需要上传或下载功能，则只拖入对应的SDK即可。<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-3.jpg" alt="ios-sdk-3.jpg"><br>
在build Settings 中设置Other Linker Flags，加入参数--ObjC<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-4.jpg" alt="ios-sdk-4.jpg"><br>
在build Phases-&gt;Link Binary With Libraries中加入以下几个依赖库<br>
1) SystemConfiguration.framework<br>
2) CoreTelephony.framework<br>
3) MobileCoreServices.framework<br>
4) libxml2.dylib<br>
5) libz.dylib<br>
6) libstdc++.6.dylib<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-5.jpg" alt="ios-sdk-5.jpg"><br>
注：如果只需要上传或下载功能，则只需要引入对应的动态库：<br>
上传SDK依赖的系统动态库有：<br>
1) SystemConfiguration.framework<br>
2) CoreTelephony.framework<br>
3) libstdc++.6.dylib<br>
下载SDK依赖的系统动态库有：<br>
1) SystemConfiguration.framework<br>
2) CoreTelephony.framework<br>
3) MobileCoreServices.framework<br>
4) libxml2.dylib<br>
5) libz.dylib<br>

## 2	上传SDK
### 2.1	初始化
<p>先引入上传SDK的头文件“TXYUploadManager.h”，创建TXYUploadManager对象，需要执行上传类型
（图片云、文件云或视频云，在微视频服务中固定为视频云），appId，userId和签名信息。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief TXYUploadManager构造函数
* @param cloudType, 文件云、图片云、视频云
* @param persistenceId TXYUploadManager实例对应的持久化id,id必须全局唯
一,persistenceId为nil时，上传任务不持久化
* @appId 用户注册的appId
* @userId 用户注册的appId
* @sigin 签名信息
* @return TXYUploadManager实例
*/
- (instancetype)initWithPersistenceId:(TXYCloudType)cloudType
persistenceId:(NSString *)persistenceId appId:(NSString*)appId
userId:(NSString*)userId sign:(NSString*)sign;

```

<p><b>示例</b><br>
</p>

```

_uploadFileManager = [[TXYUploadManager alloc]
initWithPersistenceId:TXYCloudTypeForVideo persistenceId:@"TestDemo"
appId:appId userId:userId sign:[TXYAuthenticationMgr
shareInstance].fileSignature];

```

### 2.2	视频上传

<p>上传视频的步骤如下:<br>
1. 创建TXYFileUploadTask对象，指定文件上传的全路径（如appid/bucket），文件自定义属性，
比如只读（readonly=true），如果是视频文件，可以制定视频标题、视频描述和是否需要先审后发。<br>
2. 调用TXYUploadManager的upload方法，将TXYFileUploadTask对象传入<br>
<b>原型</b><br>
</p>

```

@interface TXYFileUploadTask: TXYUploadTask &lt;NSCoding&gt;
/** 视频文件上传目录，用户选填 */
@property (nonatomic, readonly) NSString *directory;
/** 用户自定义属性，用户选填 */
@property (nonatomic, readonly) NSString *attrs;
/** 上传视频的属性，用户选填 */
@property(nonatomic, strong) TXYVideoFileInfo *videoInfo;
/*!
* @brief 视频文件上传任务初始化函数
* @param filePath 视频文件路径，必填
* @param attrs 视频文件属性，选填
* @param filename 文件名称，必填
* @param uploadDirectory 上传视频文件到哪个目录
* @param videoInfo 视频信息
* @param msgContext 通知用户业务后台的信息，选填
* @param insert 上传动作是插入还是覆盖
* @return TXYFileUploadTask实例
*/
- (instancetype)initWithPath:(NSString *)filePath
   sign:(NSString*)sign
   bucket:(NSString *)bucket
   fileName:(NSString *)fileName
   customAttribute:(NSString *)attrs
   uploadDirectory:(NSString*)directory
   videoFileInfo:(TXYVideoFileInfo*)videoInfo
   msgContext:(NSString *)msgContext
   insertOnly:(BOOL)insert;
@end

```

<p><b>示例</b><br>
</p>

```

//初始化视频文件上传对象
TXYFileUploadTask *videoTask = [[TXYFileUploadTask alloc] initWithPath:path
customAttribute:@"company=tencent"
uploadDirectory:@"/299201/ba/myfolder/"
videoFileInfo:nil msgContext:nil];
[uploadManager upload:videoTask sign:nil
complete:^(TXYTaskRsp *resp, NSDictionary *context) {
TXYFileUploadTaskRsp *fileResp = (TXYFileUploadTaskRsp *)resp;
NSLog(@"upload return=%d,%@",fileResp.retCode,fileResp.fileUrl);
}
progress:^(int64_t totalSize, int64_t sendSize, NSDictionary *context) {
}
stateChange:^(TXYUploadTaskState state, NSDictionary *context) {
    switch (state) {
        case TXYUploadTaskStateWait:
        NSLog(@"任务等待中");
        break;
    case TXYUploadTaskStateConnecting:
        NSLog(@"任务连接中");
        break;
    case TXYUploadTaskStateFail:
        NSLog(@"任务失败");
        break;
    case TXYUploadTaskStateSuccess:
        NSLog(@"任务成功");
        break;
    default:
        break;
}}];

```

### 2.3	恢复历史任务

<p>上传过程中，程序如果意外退出，那么在下次启动时，可以通过TXYUploadManager的uploadTasks获取历史任务，然后从新调
上传API来恢复历史任务。<br>
<b>示例</b><br>
</p>

```

//获取上次上传的历史任务后，重新调用upload上传
NSArray *histroyTasks =[uploadManager uploadTasks];

```

### 2.4	暂停、恢复、取消上传

<p>上传任务可以暂停、恢复或者取消，只需要传入响应的taskId即可，上传任务的状态变化会通过TXYUpStateChangeHandler回调通知<br>
<b>原型</b><br>
</p>

```

/*!
* @brief 暂停指定上传任务
* @param taskId 上传任务id @see &lt;TXYUploadTask&gt; 里的taskId
* @return 暂停成功返回YES，添加失败返回NO
*/
- (BOOL)pause:(int64_t)taskId;
/*!
* @brief 重新发送指定上传任务
* @param taskId 上传任务id @see &lt;TXYUploadTask&gt; 里的taskId
*/
- (void)resume:(int64_t)taskId;
/*!
* @brief 取消上传任务
* @param taskId 上传任务id，@see &lt;TXYUploadTask&gt; 里的taskId
* @return 取消成功返回YES，添加失败返回NO
*/
- (BOOL)cancel:(int64_t)taskId;

```

<p><b>示例</b><br>
</p>

```

TXYUploadTask* task = [taskModels objectAtIndex:index];
[uploadManager puase:task.taskId];//暂停上传
[uploadManager resume:task.taskId];//恢复上传
[uploadManager cancel:task.taskId];//取消上传

```

## 3	目录/视频管理SDK

### 3.1	创建目录

<p>创建目录步骤如下：<br>
1. 创建TXYCreateDir对象，必填的输入参数是目录的全路径，比如/appId/bucketId/MyDocument/<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYCreateDir对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调中获取访问url<br>
<b>原型</b><br>
</p>

```

@interface TXYCreateDir&nbsp;: TXYCommandTask
//是否覆盖相同名字的目录或文件
@property(nonatomic,readonly) BOOL overwrite;
//用户自定义的属性
@property(nonatomic,readonly) NSString * attrs;
- (instancetype) initWithPath:(NSString*)path
needOverWrite:(BOOL)overwrite customAttribute:(NSString*)attrs;
@end

```

<p><b>示例</b><br>
</p>

```

TXYCreateDir *createDirCommand = [[TXYCreateDir alloc]
initWithURL:@”/appId/bucketId/MyDocument/TestFolder”];
    [self.uploadManager sendCommand:createDirCommand sign:nil
complete:^(TXYTaskRsp *resp) {
        if (resp.retCode &gt;= 0)
        {
            NSLog(@"创建目录成功，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
        else
        {
            NSLog(@"创建目录失败，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
    }];

```

### 3.2	查询视频或目录

<p>查询视频或者目录的详细信息，步骤如下：<br>
1. 创建TXYStat对象，必填的输入参数是视频或者目录的全路径，比如/appId/bucketId/MyDocument/<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYFileStat对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调中获取查询结果FileDirInfo，如果是视频的话，会返回视频不同码率信息<br>
<b>原型</b><br>
</p>

```

@interface TXYStat&nbsp;: TXYCommandTask
//对象类型，目录/文件/Bucket
@property(nonatomic,readonly)TXYObjectType objectType;
- (instancetype) initWithPath:(NSString*)path
objectType:(TXYObjectType)objectType;


@interface TXYFileDirInfo&nbsp;: NSObject
//文件名和目录名
@property(nonatomic,strong) NSString *name;
//文件的大小
@property(nonatomic,assign) long long fileSize;
//文件的长度
@property(nonatomic,assign) long long fileLength;
//文件自定义属性
@property(nonatomic,strong) NSString *attrs;
//文件的摘要sha
@property(nonatomic,strong) NSString *sha;
//文件的创建时间
@property(nonatomic,assign) NSUInteger ctime;
//文件的修改时间
@property(nonatomic,assign) NSInteger mtime;
//文件的访问url
@property(nonatomic,strong) NSString *accessUrl;
//文件目录类型
@property(nonatomic,assign) TXYObjectType objectType;
//文件目录云端的路径
@property(nonatomic,strong) NSString *startPath;
//视频的信息
@property(nonatomic,strong) TXYVideoListInfo *videoListInfo;
@end


@interface TXYVideoListInfo&nbsp;: NSObject
// 不同码率转码状态
@property(nonatomic,strong) NSDictionary *transcodeStatus;
// 视频文件状态
@property(nonatomic,assign) TXYCosVideoStatus videoStatus;
// 视频时长
@property(nonatomic,assign) NSInteger timeLength;
// 转码视频url列表
@property(nonatomic,strong) NSDictionary *playUrl;
// 视频信息
@property(nonatomic,strong) TXYVideoFileInfo *videoInfo;
@end

```

### 3.3	删除视频或目录

<p>删除视频或目录步骤如下：<br>
1. 创建TXYDelete对象，必填的输入参数是视频文件目录的全路径，比如/appId/bucketId/MyDocument/，
删除对象的类型，比如command.type=TXYObjectDir<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYDelete对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调<br>
<b>原型</b><br>
</p>

```

@interface TXYDelete&nbsp;: TXYCommandTask
//对象类型，目录/视频/Bucket
@property(nonatomic,readonly)TXYObjectType objectType;
- (instancetype) initWithPath:(NSString*)path;
- (instancetype) initWithPath:(NSString*)path
objectType:(TXYObjectType)objectType;
@end
```

<p><b>示例</b><br>
</p>

```
TXYDelete *command = [[TXYDelete alloc]
initWithURL:@”appId/bucketId/MyDocument”];
    command.type = TXYObjectDir;
    [self.uploadManager sendCommand:command sign:nil complete:^(TXYTaskRsp
*resp) {
        if (resp.retCode &gt;= 0)
        {
            NSLog(@"删除目录成功，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
        else
        {
            NSLog(@"删除目录失败，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
    }];

```

### 3.4	更新视频或目录

<p>更新视频或目录步骤如下：<br>
1. 创建TXYUpdate对象，必填的输入参数：1）全路径，比如/appId/bucketId/MyDocument/，2）属性值，比如readonly=true<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYUpdate对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调中获取访问url<br>
<b>原型</b><br>
</p>

```

@interface TXYUpdate: TXYCommandTask
//用户自定义的属性,比如：company=tencent,readonly=true
@property(nonatomic,strong) NSString *attrs;
//对象类型，目录/视频/Bucket
@property(nonatomic,assign)TXYObjectType objectType;
- (instancetype) initWithPath:(NSString*)path
objectType:(TXYObjectType)objectType customAttribute:(NSString*)attrs;
@end
```

<p><b>示例</b><br>
</p>

```
TXYUpdate *command = [[TXYUpdate alloc] initWithURL:@”/appId/bucketId/dir”];
    command.type = TXYObjectDir;
    command.attrs = @”readOnly=true”;
    [self.uploadManager sendCommand:command sign:nil complete:^(TXYTaskRsp
*resp) {
        if (resp.retCode &gt;= 0)
        {
            NSLog(@"更新目录成功，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
        else
        {
            NSLog(@"更新目录失败，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
    }];

```

### 3.5	浏览目录

<p>浏览目录步骤如下：<br>
1. 创建TXYListDir对象，必填的输入参数是视频或目录的全路径，比如/appId/bucketId/MyDocument/<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYListDir对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调中获取视频目录属性FileDirInfo列表<br>
<b>原型</b><br>
</p>

```

@interface TXYListDir: TXYCommandTask
//一次拉取多少条记录
@property(nonatomic,readonly) NSUInteger num;
//拉取方式,1）拉取目录和视频 2）拉取目录 3）拉取视频
@property(nonatomic,readonly) TXYListPattern pattern;
//0正序，1反序
@property(nonatomic,readonly) BOOL order;
- (instancetype) initWithPath:(NSString*)path number:(NSUInteger)num
listPattern:(TXYListPattern)pattern order:(BOOL)order;
@end
```

<p><b>示例</b><br>
</p>

```
TXYListDir *task = [[TXYListDir alloc] initWithPath: @”/appId/bucketId/dir”
number:10 listPattern:TXYListBoth order:NO pageContext:nil];
command.num = 10;//一次查询视频目录的个数
    [self.uploadManager sendCommand:command sign:nil complete:^(TXYTaskRsp
*resp) {
        if (resp.retCode &gt;= 0)
        {
            TXYListDirCommandRsp *listResp = (TXYListDirCommandRsp *)resp;
            [strongSelf showListDirResult:listResp.fileDirInfoList];
        }
        else
        {
            NSLog(@"更新目录失败，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
    }];
```

### 3.6	前缀搜索

<p>前缀搜索目录视频的步骤如下：<br>
1. 创建TXYSearch对象，必填的输入参数是目录的前缀匹配字符串，比如/appId/bucketId/MyDocument/a，以a大头的目录及视频<br>
2. 调用TXYUploadManager的sendCommand方法，将TXYSearch对象传入<br>
3. 在sendCommand传入的TXYUpCommandCompletionHandler回调中获取视频目录属性FileDirInfo列表<br>
<b>原型</b><br>
</p>

```
@interface TXYSearch: TXYCommandTask
//一次拉取多少条记录
@property(nonatomic,readonly) NSUInteger num;
//分页浏览的上下文
@property(nonatomic,readonly) NSString *pageContext;
- (instancetype) initWithPath:(NSString*)path number:(NSUInteger)num
pageContext:(NSString*)context;
@end
```

<p><b>示例</b><br>
</p>

```
TXYSearch *task = [[TXYSearch alloc]
initWithPath:@”/appid/bucket/myfolder/a” number:10 pageContext:nil];
    [self.uploadManager sendCommand:command sign:nil complete:^(TXYTaskRsp
*resp) {
        if (resp.retCode &gt;= 0)
        {
            TXYListDirCommandRsp *listResp = (TXYListDirCommandRsp *)resp;
            [strongSelf showListDirResult:listResp.fileDirInfoList];
        }
        else
        {
            NSLog(@"更新目录失败，code:%d desc:%@", resp.retCode, resp.descMsg);
        }
    }];
```


## 4	下载SDK

### 4.1	初始化

<p><b>原型</b><br>
</p>

```
/*!
* @brief 对应用程序的id,初始化一次即可
* @param appId 应用程序id,必填
* @param userId 用户id,选填
* @return 成功返回YES，失败返回NO
*/
+ (BOOL)authorize:(NSString *)appId userId:(NSString *)userId;
```

<p><b>示例</b><br>
</p>

```
//注册签名
[TXYDownLoder authorize:APPID userId:USERID sign:SIGN];
//实例化上传管理类
downloder = [[TXYDownloader sharedInstanceWithPersistenceId:nil type:
TXYDownloadTypeFile]
```

### 4.2	下载并发数

<p>可以指定下载器最大并发数。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief 指定下载队列的最大并发数
* @param count 下载队列最大并发数,调用下载接口再修改则无效
* @return 成功返回YES，失败返回NO
*/
- (void)setMaxConcurrent:(int)count;
```

<p><b>示例</b><br>
</p>

```
//设置最大并发数
[downloader setMaxConcurrent:3];
```

### 4.3	长连接/断点续传

<p>下载器提供开关，可以设定是否开启长连接和断电续传功能。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief 指定下载是否支持断点续传
* @param enable YES表示支持，为NO表示不支持,默认为YES
* @return 成功返回YES，失败返回NO
*/
- (void)enableHTTPRange:(BOOL)enable;
/*!
* @brief 指定是否支持HTTP长连接
* @param flag YES表示支持，为NO表示不支持,默认为YES
* @return 成功返回YES，失败返回NO
*/
- (void)enableKeepAlive:(BOOL)enable;
```

<p><b>示例</b><br>
</p>

```
//启动断点续传功能
[downloader enableHTTPRange:YES];
//启动长连接功能
[downloader enableKeepAlive:YES];
```

### 4.4	文件下载

<p>文件下载是采用异步模式进行下载，下载的进度/成功/失败/取消等信息通过回调通知。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief 下载指定url的数据，并自动缓存到磁盘中，然后回调通知Target
* @param url 视频资源地址
* @param target 通知的对象
* @param succBlock 成功通知
* @param failBlock 失败通知
* @param progressBlock 进度通知,当前下载百分比
* @param param 可以指定TXYDownloaderParam族一系列参数,也可以用于透传使用者的参数
* @see &lt;TXYDownloaderParam&gt; 其中param中的key可以按照TXYDownloaderParam枚举指定
*/
- (void)download:(NSString *)url target:(id)target succBlock:(void
(^)(NSString *url, NSData *data, NSDictionary *info))succBlock failBlock:(void
(^)(NSString *url, NSError *error))failBlock progressBlock:(void (^)(NSString
*url, NSNumber *value))progressBlock param:(NSDictionary *)param;
```

<p><b>示例</b><br>
</p>

```
[[TXYDownloader sharedInstanceWithPersistenceId:nil] download:_url
target:self
succBlock:^(NSString *url, NSData *data, NSDictionary *info) {
} failBlock:^(NSString *url, NSError *error) {
} progressBlock:^(NSString *url, NSNumber *value) {
} param:self.params];
```

### 4.5	取消下载

<p><b>原型</b><br>
</p>

```
/*!
* @brief 取消target对应的下载请求
* @param url 资源地址
* @param target 通知的对象
*/
- (void)cancel:(NSString *)url target:(id)target;
/*!
* @brief 取消所有的下载请求
*/
- (void)cancelAll;
```


<p><b>示例</b><br>
</p>

```
//取消单个下载任务
[[TXYDownloader sharedInstanceWithPersistenceId:nil] cancel: url
target:self];
//取消全部下载任务
[[TXYDownloader sharedInstanceWithPersistenceId:nil] cancelAll
```

### 4.6	缓存查询

<p>TXYDownloader下载组件支持本地文件缓存，查询/获取/清除缓存文件。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief 判断指定url数据对应的本地缓存路径是否存在
* @param url 资源地址
* @return 成功返回YES，失败返回NO
*/
- (BOOL)hasCache:(NSString *)url;
/*!
* @brief 获取指定url的对应的二进制对象
* @param url 资源地址
* @return 找到了返回资源对应的NSData对象，否则返回nil
*/
- (NSData *)getCacheData:(NSString *)url;
/*!
* @brief 获取指定url的对应的本地缓存路径
* @param url 资源地址
* @return 找到了返回资源对应的本地缓存路径，否则返回nil
*/
- (NSString *)getCachePath:(NSString *)url;
/*!
* @brief 清除指定url对应的缓存
* @param url 资源地址
* @return 成功返回YES，失败返回NO
*/
- (BOOL)clearCache:(NSString *)url;
/*!
* @brief 清除所有缓存
* @return 成功返回YES，失败返回NO
*/
- (BOOL)clearCache;
//
```

<p><b>示例</b><br>
</p>

```
//先检查是否有本地缓存文件，有的话直接读取缓存文件并显示
if([[TXYDownloader sharedInstanceWithPersistenceId:nil]
hasCache:self.url]){
NSData *data = [[TXYDownloader
sharedInstanceWithPersistenceId:nil]getCacheData:self.url]
cacheImage = [UIImage imageWithData:data];
}
```

### 4.7	取消回调通知

<p>可以根据制定的url取消下载回调通知，比如下载页面不可见或者消失时，取消回调后继续下载。<br>
<b>原型</b><br>
</p>

```
/*!
* @brief 清除target下指定url的通知，不取消下载任务,继续下载
* @param urlPath 资源地址
* @param target 通知的对象
*/
- (void)clearTarget:(id)target url:(NSString *)url;
/*!
* @brief 清除指定Target所有的通知，不取消下载任务,继续下载
* @param target 通知的对象
*/
- (void)clearTarget:(id)target;
```


<!-- 
NewPP limit report
Preprocessor node count: 148/1000000
Post-expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key tencentwiki_db:pcache:idhash:1157-0!1!0!!zh-cn!2!edit=0 and timestamp 20160315125055 -->
