## 1. 开发准备
腾讯云•万象优图的最新iOS SDK的下载：[iOS SDK](/doc/product/275/SDK下载#2.-ios-sdk)。
### 1.1 前期准备
1. iOS 5.0+；
2. 手机必须要有网络（GPRS、3G或Wifi网络等）；
3. 获取APPID。
### 1.2 导入SDK
1. 下载iOS SDK
iOS SDK下载地址为：[iOS SDK](/doc/product/275/SDK下载#2.-ios-sdk)。

注意:
SDK中用到的SIGN，推荐使用[服务器端SDK](/doc/product/275/SDK文档#3.-.E6.9C.8D.E5.8A.A1.E5.99.A8sdk.E6.96.87.E6.A1.A3)提供的接口来生成，并由移动端向业务服务器请求。SIGN的具体生成和使用请参照[鉴权服务技术方案](/doc/product/275/签名与鉴权文档-V1)。

2. 导入项目
图片云IOS SDK其中包括上传SDK和下载SDK，上传SDK压缩包QCloudUploadSDK.zip,下载SDK压缩包QCloudDownloadSDK.zip.上传和下载SDK压缩包中分别包含了一个.a静态库和一个包含头文件的文件夹Headers，解压后的内容如下：
上传SDK:
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-1.jpg)
下载SDK:
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-2.jpg)
将解压后的QCloudUPloadSDK和QCloudDownloadSDK拖入工程目录，Xcode会自将其加入链接库列表中。
注：如果只需要上传或下载功能，则只拖入对应的SDK即可。
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-3.jpg)

在build Settings中设置Other Linker Flags，加入参数-ObjC
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-4.jpg)

在build Phases -> Link Binary With Libraries中加入以下几个依赖库
1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	MobileCoreServices.framework
4)	libxml2.dylib
5)	libz.dylib
6)	libstdc++.6.dylib
![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/ios-sdk-5.jpg)
注：如果只需要上传或下载功能，则只需要引入对应的动态库：
上传SDK依赖的系统动态库有：
1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	libstdc++.6.dylib
下载SDK依赖的系统动态库有：
1)	SystemConfiguration.framework
2)	CoreTelephony.framework
3)	MobileCoreServices.framework
4)	libxml2.dylib
5)	libz.dylib
## 2. API详细说明
### 2.1	上传SDK API
#### 2.1.1	初始化
先引入上传SDK的头文件 “TXYUploadManager.h”，在使用上传功能之前需要先初始化，初始化分为两步:
1.	APP注册，在使用其他接口之前必须先调用此方法进行用户信息初始化（SDK中用到的SIGN，推荐使用服务器端SDK来生成，并由移动端向业务服务器请求，SIGN的具体生成和使用请参照鉴权服务技术方案）；
2.	创建TXYUploadManager对象。
函数原型:

```
 /*!
  * @brief 注册应用程序的id和签名，只需要注册一次，可更新
  * @param appid 应用程序id,必填
  * @param userId 使用者id,可选
  * @param sign 全局签名，必填
  * @return 成功返回YES，失败返回NO
 */
 + (BOOL)authorize:(NSString *)appId userId:(NSString *)userId sign:(NSString *)sign;
```
示例:
 
```
// 注册签名
 [TXYUploadManager authorize:APPID userId:USERID sign:SIGN];
 // 实例化上传管理类
 _uploadManager = [[TXYUploadManager alloc] initWithPersistenceId: @"persistenceId"];
```
#### 2.1.2	图片上传
上传一张图片的步骤如下:
1.	创建TXYPhotoUploadTask对象；
2.	调用TXYUploadManager的upload方法，将TXYPhotoUploadTask对象传入。
原型:

```
 //TXYPhotoUploadTask
 /*!
  * @brief 图片上传任务初始化函数
  * @param photoPath 图片路径，必填
  * @return TXYPhotoUploadTask实例
  */
 - (instancetype)initWithPath:(NSString *)filePath;
 //TXYPhotoUploadTask的上传API
 /*!
  * @brief 上传图片任务,需要保证已经注册了appID和sign信息
  * @param task 待上传任务
  * @param sign 本次有效的签名，不填则使用全局签名
  * @param complete 上传完成后的回调函数
  * @param progress 上传进度的回调函数
  * @param stateChange 上传任务状态变化回调函数
  * @return 添加成功返回YES，添加失败返回NO
  */
 - (BOOL)upload:(TXYUploadTask *)task
           sign:(NSString *)sign
       complete:(TXYUpCompletionHandler)complete
       progress:(TXYUpProgressHandler)progress
    stateChange:(TXYUpStateChangeHandler)stateChange;
```
示例:

```
//初始化图片上传对象
  TXYPhotoUploadTask *photoTask = [[TXYPhotoUploadTask alloc] initWithPath:photoPath];
  [uploadManager upload:photoTask 
                   sign:nil 
               complete:^(TXYTaskRsp *resp, NSDictionary *context) {
                   TXYPhotoUploadTaskRsp *photoResp = (TXYPhotoUploadTaskRsp *)resp;
                   NSLog(@"upload return=%d",photoResp.retCode);
               }
               progress:^(int64_t totalSize, int64_t sendSize, NSDictionary *context) {
               }
            stateChange:^(TXYUploadTaskState state, NSDictionary *context){
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
               }
            }];
```
#### 2.1.3	恢复历史任务
上传过程中，程序如果意外退出，那么在下次启动的时候,可以通过TXYUploadManager的uploadTasks恢获取历史任务，然后重新调上传API来恢复历史任务。
示例:

```
 // 获取上次上传的历史任务后，重新调用upload上传
 NSArray *histroyTasks =[uploadManager uploadTasks];
```
#### 2.1.4	暂停、恢复、取消上传
上传任务可以暂停、恢复或者取消，只需要传入相应的taskId即可，上传任务的状态变化会通过TXYUpStateChangeHandler回调通知。
原型:

```
/*!
 * @brief  暂停指定上传任务
 * @param  taskId 上传任务id @see <TXYUploadTask> 里的taskId
 * @return 暂停成功返回YES，添加失败返回NO
 */
- (BOOL)pause:(int64_t)taskId;
/*!
 * @brief  重新发送指定上传任务
 * @param  taskId 上传任务id @see <TXYUploadTask> 里的taskId
 */
- (void)resume:(int64_t)taskId;
/*!
 * @brief  取消上传任务
 * @param  taskId 上传任务id，@see <TXYUploadTask> 里的taskId
 * @return 取消成功返回YES，添加失败返回NO
```
示例:

```
 TXYUploadTask* task = [taskModels objectAtIndex:index];
 [uploadManager puase:task.taskId];// 暂停上传
 [uploadManager resume:task.taskId];//恢复上传
 [uploadManager cancel:task.taskId];//取消上传
```
#### 2.1.5	图片查询
查询图片文件的详细信息，步骤如下:
1.	通过文件url创建TXYFileStatCommand对象；
2.	调用TXYUploadManager的sendCommand方法，将TXYFileStatCommand对象传入；
3.	在sendCommand传入的TXYUpCommandCompletionHandler回调中获取查询结果。
原型:

```
 /*!
  * @brief 初始化方法
  * @param commandURL 要操作的URL
  * @return TXYCommandTask实例
  */
 - (instancetype)initWithURL:(NSString *)commandURL;
```
示例:

```
 fileStatCommand= [[TXYFileStatCommand alloc] initWithURL:url];
 [_uploadManager sendCommand:fileStatCommand 
                        sign:nil
                    complete:^(TXYTaskRsp *resp) {
                        if (resp.retCode >= 0 ){
                            //成功
                        } else {
                            //失败
                        }
                   }];
```
#### 2.1.6	图片删除
删除文件步骤如下:
1.	通过文件url创建TXYFileDeleteCommand对象；
2.	调用TXYUploadManager的sendCommand方法，将TXYFileDeleteCommand对象传入；
3.	在sendCommand传入的TXYUpCommandCompletionHandler回调中获取复制文件。
示例:

```
 fileDeleteCommand= [[TXYFileDeleteCommand alloc] initWithURL:url];
 [_uploadManager sendCommand: fileDeleteCommand 
                        sign:nil
                    complete:^(TXYTaskRsp *resp) {
                        if (resp.retCode >= 0 ){
                            //成功
                        } else {
                           //失败
                        }
                    }];
```
#### 2.1.7	图片复制
复制文件步骤如下:
1.	通过文件url创建TXYFileCopyCommand对象；
2.	调用TXYUploadManager的sendCommand方法，将TXYFileCopyCommand对象传入；
3.	在sendCommand传入的TXYUpCommandCompletionHandler回调中获取复制文件。
示例:

```
fileCopyCommand= [[TXYFileCopyCommand alloc] initWithURL:url];
[_uploadManager sendCommand:fileCopyCommand 
                       sign:nil
                   complete:^(TXYTaskRsp *resp) {
                       if (resp.retCode >= 0 ){
                           //成功
                       } else {
                           //失败
                       } 
                  }];
```
### 2.2	下载SDK API
#### 2.2.1	初始化
函数原型:

```
/*!
* @brief TXYDownloader构造函数
* @param persistenceId 值不同表示缓存目录不同，为nil内部会自动创建一个缓存目录统一管理
* @return TXYDownloader实例
*/
+ (instancetype)sharedInstanceWithPersistenceId:(NSString *)persistenceId;
```
示例

```
TXYDownloader *downloader = [TXYDownloader sharedInstanceWithPersistenceId:nil]
   [downloader download:[self appendSignBehindURL:self.url]
                 target:self
              succBlock:^(NSString *url, NSData *data, NSDictionary *info) {
                  UIImage *image = [UIImage imageWithData:data];
              }
              failBlock:^(NSString *url, NSError *error) {
              }
          progressBlock:^(NSString *url, NSNumber *value) {
          }
                  param:nil];
```
#### 2.2.2	下载并发数
可以指定下载器最大并发数。
函数原型:

```
 /*!
 * @brief 指定下载队列的最大并发数
 * @param count 下载队列最大并发数,调用下载接口再修改则无效
 * @return 成功返回YES，失败返回NO
 */
 - (void)setMaxConcurrent:(int)count;
```
示例

```
 // 设置最大并发数
 [downloader setMaxConcurrent:3];
```
#### 2.2.3	长连接/断点续传
下载器提供开关，可以设定是否开启长连接和断点续传功能。
函数原型:

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
示例:

```
// 启动断点续传功能
[downloader enableHTTPRange:YES];
// 启动长连接功能
[downloader enableKeepAlive:YES];
```
#### 2.2.4	图片下载
文件下载是采用异步模式进行下载，下载的进度/成功/失败/取消等信息通过回调通知。
函数原型:

```
 /*!
 * @brief 下载指定url的数据，并自动缓存到磁盘中，然后回调通知Target
 * @param url 图片资源地址
 * @param target 通知的对象
 * @param succBlock 成功通知
 * @param failBlock 失败通知
 * @param progressBlock 进度通知,当前下载百分比
 * @param param 可以指定TXYDownloaderParam族一系列参数,也可以用于透传使用者的参数
 * @see <TXYDownloaderParam> 其中param中的key可以按照TXYDownloaderParam枚举指定
 */
- (void)download:(NSString *)url 
          target:(id)target 
       succBlock:(void (^)(NSString *url, NSData *data, NSDictionary *info))succBlock 
       failBlock:(void (^)(NSString *url, NSError *error))failBlock 
   progressBlock:(void (^)(NSString *url, NSNumber *value))progressBlock 
           param:(NSDictionary *)param;
```
示例:

```
[[TXYDownloader sharedInstanceWithPersistenceId:nil] download:_url target:self
                                                    succBlock:^(NSString *url, NSData *data, NSDictionary *info) {

                                                  } failBlock:^(NSString *url, NSError *error) {
                                              } progressBlock:^(NSString *url, NSNumber *value) {
                                                      } param:self.params];
```
#### 2.2.5	取消下载
函数原型:

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
示例:

```
  // 取消单个下载任务
  [[TXYDownloader sharedInstanceWithPersistenceId:nil] cancel: url target:self];
  // 取消全部下载任务 
  [[TXYDownloader sharedInstanceWithPersistenceId:nil] cancelAll
```
#### 2.2.6	缓存查询
TXYDownloader下载组件支持本地文件缓存,查询/获取/清除缓存文件
函数原型:

```
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
```
```
示例:

```
  //先检查是否有本地缓存图片文件，有的话直接读取缓存文件并显示
  if([[TXYDownloader sharedInstanceWithPersistenceId:nil] hasCache:self.url]){
      NSData *data = [[TXYDownloader     sharedInstanceWithPersistenceId:nil]getCacheData:self.url]
      cacheImage = [UIImage imageWithData:data];
  }
```
#### 2.2.7	取消回调通知
可以根据指定的url取消掉下载回调通知，比如下载页面不可见或者消失时，取消回调后继续下载。

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
### 2.3	iOS返回码说明
上传错误码：

错误码 |	含义
---------|---------
-290	 |	网络连接失效
-20101	 |	解包失败
-20102 |	服务器连接错误
-20103|	数据收发超时
-20104|	控制包收取超时
-20105|	命令字不支持
-20106|	服务器返回偏移错误
-20107|	上传的文件内容为空
-20001|	链接超时
-20002|	地址不可达
-20003|	Socket被重置
-20004|	Socket连接错误
-20005|	读取数据长度过大
-20006|	读取数据长度太小
-20007|	发送数据出错
-20008|	Ip地址解析出错
-20009|	网络出错
-20010|	握手包打包解包出错
-20011|	握手超时
-20013|	Socket缓存不足
-20014|	网络不可达

下载错误码：

错误码|	含义
---------|---------
-1	|无效的图片格式
-2	|无需缓存的图片
-3	|长度不一致
-4	|WEBP解码错误
1	|连接失败
2	|请求超时
3	|认证错误
4	|请求取消
5	|创建网络请求失败
6	|内部创建请求失败
7	|密钥出错
8	|文件管理出错
9	|过度重定向
10|	未被处理异常
11|	压缩错误
12|	网络流错误
80001|	文件类型不一致
80002	|Range不匹配
80003	|返回位置为0
80004	|长度不匹配
80005	|断点续传返回非206状态码
80006	|修改时间不匹配
90001	|获取下载临时文件失败
90002	|校验文件失败

其他返回码参见 [返回码说明](/doc/product/275/返回码说明)。