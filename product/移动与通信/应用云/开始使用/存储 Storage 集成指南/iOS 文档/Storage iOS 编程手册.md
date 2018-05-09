
## 准备工作
 

如果这是您首次向应用添加 Storage，请先在移动开发平台（MobileLine）的控制台中关联您的应用：
 
1.安装 [移动开发平台（MobileLine） SDK](https://console.cloud.tencent.com/tac)。
2.在 [移动开发平台（MobileLine）控制台](https://console.cloud.tencent.com/tac) 中，将您的应用添加到您的移动开发平台（MobileLine）项目中。
3.参考 [Storage 配置文档](https://console.cloud.tencent.com/tac)，配置并初始化 Storage。


## 使用 Storage 进行文件操作


您的文件存储在 COS 存储桶中，此存储桶中的文件以分层结构存储，就像本地硬盘中的文件系统一样，通过创建对文件的引用，您的应用可以获得对相应文件的访问权限。之后，借助所创建的这些引用，您可以上传或下载数据、获取或更新元数据，也可以删除文件。引用可以指向特定的文件，也可以指向层次结构中更高层级的节点。


### 创建引用
引用可以看作是指向云端文件的指针：要上传、下载或删除文件或要获取或更新文件的元数据，请创建引用。由于引用属于轻型项目，因此您可以根据需要创建任意多个引用，引用还可以在多个操作中复用。

引用是使用 TACStorageService 服务并调用其 referenceWithPath 或者 rootReference 方法创建的：(其中reference是TACStorageReference类的一个实例）

Objective-C 代码示例：
~~~ 
[TACStorageService defaultStorage].credentailFenceQueue.delegate = self;
self.reference = [[TACStorageService defaultStorage] referenceWithPath:@"test-file/test.png"];
~~~

Swift 代码示例：
~~~
TACStorageService.defaultStorage().credentailFenceQueue.delegate = self
self.reference = TACStorageService.defaultStorage().reference(withPath: "test-file/test.png")
~~~

#### 引用导航

您还可以使用 parent 和 root 方法在我们的文件层次结构中向上导航，parent 可向上导航一级，而 root 可直接导航到根目录：

Objective-C 代码示例：
~~~
imagesRef = [spaceRef parent];
// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
TACStorageReference *rootRef = [spaceRef root];
~~~

Swift 代码示例：
~~~
let imageRef = spaceRef?.parent()
// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
let rootRef = spaceRef?.root()
~~~

child、parent 和 root 可以多次链接到一起，每次都会返回一个引用，root 的 parent 是例外，它是 nil：

Objective-C 代码示例：
~~~
TACStorageReference *earthRef = [[spaceRef parent] child:@"earth.jpg"];
// nilRef is nil, since the parent of root is nil
TACStorageReference *nilRef = [[spaceRef root] parent];
~~~

Swift 代码示例：
~~~
let earthRef = spaceRef?.parent().child("earth.jpg")
// nilRef is nil, since the parent of root is nil
let nilRef = spaceRef?.root().parent()
~~~
### 上传文件

有了引用之后，您可以通过两种方式将文件上传到 COS：

* 从内存中的数据上传。
* 从代表设备上某个文件的路径上传。

#### 从内存中的数据上传

~~~
/**
 上传一段内存数据（NSData类型）到当前的COS路径上去

 @param data 需要上传的NSData数据
 @param meteData 当前数据的元信息
 @param completion 结果回调
 @return TACStorageUploadTask对象
 */
- (TACStorageUploadTask*) putData:(NSData*)data
                         metaData:(nullable TACStorageMetadata*)meteData
                       completion:(nullable void (^)(TACStorageMetadata *_Nullable metadata,
                                                     NSError *_Nullable error))completion;
~~~

Objective-C 代码示例：
~~~
NSData *data = [NSData dataWithContentsOfFile:@"rivers.jpg"];
// Create a reference to the file you want to upload
TACStorageReference *riversRef = [storageRef child:@"images/rivers.jpg"];
// Upload the file to the path "images/rivers.jpg"
TACStorageUploadTask *uploadTask = [riversRef putData:data
                                             metadata:nil
                                           completion:^(TACStorageMetadata *metadata,
                                                        NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    NSURL *downloadURL = metadata.downloadURL;
  }
}];
[TACStorageUploadTask enqueue];
~~~

Swift 代码示例：
~~~
let data = NSData.init(contentsOfFile: "rivers.jpg")
// Upload the file to the path "images/rivers.jpg"
let riversRef = storageRef?.child("images/rivers.jpg")
let uploadTask = riversRef?.put(data! as Data, metaData: nil, completion: { (metadata:TACStorageMetadata?, error:Error?) in
 if error != nil{
   // Uh-oh, an error occurred!
 }else{
  // Metadata contains file metadata such as size, content-type, and download URL.
  let downloadURL = metadata?.downloadURL
 }            
})
uploadTask?.enqueue()
~~~

#### 从文件中上传


~~~~
/**
 上传一个文件到当前的COS路径上去

 @param file 需要上传的文件
 @param meteData 当前数据的元信息
 @param completion 结果回调
 @return TACStorageUploadTask对象
 */
- (TACStorageUploadTask*) putFile:(NSURL*)file
                         metaData:(nullable TACStorageMetadata*)meteData
                       completion:(nullable void (^)(TACStorageMetadata *_Nullable metadata,
                                                     NSError *_Nullable error))completion;

~~~~

Objective-C 代码示例：
~~~
// File located on disk
NSURL *localFile = [NSURL URLWithString:@"path/to/image"];
// Create a reference to the file you want to upload
TACStorageReference *riversRef = [storageRef child:@"images/rivers.jpg"];
// Upload the file to the path "images/rivers.jpg"
TACStorageReference *uploadTask = [riversRef putFile:localFile metadata:nil completion:^(TACStorageMetadata *metadata, NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    NSURL *downloadURL = metadata.downloadURL;
  }
}];
[uploadTask enqueue];
~~~

Swift 代码示例：
~~~
// File located on disk
let localFile = NSURL.init(string: "path/to/image")
// Create a reference to the file you want to upload
let riversRef = storageRef?.child("images/rivers.jpg")
// Upload the file to the path "images/rivers.jpg"
let uploadTask = riversRef?.putFile(localFile! as URL, metaData: nil, completion: { (metadata:TACStorageMetadata?, error:Error?) in
 if error != nil{
  // Uh-oh, an error occurred!
 }else{
  // Metadata contains file metadata such as size, content-type, and download URL.
  let downloadURL = metadata?.downloadURL
 }
})
uploadTask?.enqueue()
~~~
#### 添加文件元数据
在文件上传时可以传入元数据，当需要附带一些特殊的信息（例如 Content-Disposition 头部，或者加入自定义的头部）时，可以通过附带在元数据里，随着文件一起上传。例如上传时希望加入一个值为 x-cos-meta-test 的头部时，可以参考下面的例子：

Objective-C 代码示例：
```
TACStorageReference* ref = [[TACStorageService defaultStorage] rootReference];
  ref = [ref child:@"object-test"];
  NSString* content = @"file-content";
   __block TACStorageMetadata* metaData = [[TACStorageMetadata alloc] init];
   metaData.customMetadata = @{@"x-cos-meta-test":@"testCustomHeader"};//加入自定义头部
   TACStorageUploadTask* uploadTask = [ref putData:[content dataUsingEncoding:NSUTF8StringEncoding] metaData:metaData completion:^(TACStorageMetadata * _Nullable metadata, NSError * _Nullable error) {
       //result
}];
[uploadTask enqueue];
```

Swift 代码示例：
```
var ref = TACStorageService.defaultStorage().rootReference()
ref = ref?.child("object-test")
let content = "file-content"
let metaData = TACStorageMetadata.init()
metaData.customMetadata = ["x-cos-meta-test":"testCustomHeader"]//加入自定义头部
let uploadTask = ref?.put(content.data(using: String.Encoding.utf8)!, metaData: metaData, completion:{ (metadata:TACStorageMetadata?, error:Error?) in
 //result
})
uploadTask?.enqueue()
```
#### 监听任务状态
不管是上传还是下载任务，都可以通过下面的方法来监听任务的状态。其中 status 传入希望监听的状态，当对应的状态变更时会调用 handler 进行回调。例如如果希望监听任务的进度，那么 status 可以传入 TACStorageTaskStatusProgress 。
```
- (TACStorageHandler) observeStatus:(TACStorageTaskStatus)status handler:(void (^)(TACStorageTaskSnapshot * ))handler
```   

例（监听一个下载任务的进度）：

Objective-C 代码示例：
```
TACStorageReference* ref = [[TACStorageService defaultStorage] referenceWithPath:@"hello"];
NSURL* url = @"file-local-url";
TACStorageDownloadTask* download = [ref downloadToFile:url completion:^(NSURL * _Nullable URL, NSError * _Nullable error) {
    // finish callback
}];
[download observeStatus:TACStorageTaskStatusProgress handler:^(TACStorageTaskSnapshot *snapshot) {
      NSLog(@"下载任务进度：%f"snapshot.progress.fractionCompleted > 0.3)
];
[download enqueue];
```

Swift 代码示例：
```
let ref = TACStorageService.defaultStorage().rootReference()
let url = URL.init(string: "file-local-url")
let downLoad = ref?.download(toFile: url! as URL, completion: { (url:URL?, error:Error?) in
 // finish callback
})
downLoad?.observeStatus(TACStorageTaskStatus.progress, handler: { (snapshot:TACStorageTaskSnapshot?) in
 print("下载任务进度: ",snapshot?.progress.fractionCompleted as Any)
})
downLoad?.enqueue()
```
#### 管理上传
对于较大的文件（1MB以上）会采取分块上传的形式，上传时会将文件切分成 1 MB 大小的数个块，然后并行进行上传。对于这类型的上传可以实现暂停和续传。 

Objective-C 代码示例：
```
NSString* mb4bfile = @"file-local-path";
TACStorageReference* ref = [[TACStorageService defaultStorage] referenceWithPath:@"hello"];
__block TACStorageMetadata* result;
TACStorageUploadTask* task = [ref putFile:[NSURL fileURLWithPath:mb4bfile] metaData:nil completion:^(TACStorageMetadata *     _Nullable metadata, NSError * _Nullable error) {
 //完成回调
}];
[task enqueue];
//上传还没完成时
//暂停上传
[task pause];
//暂停下载
[task resume];
//取消上传
[task cancel];
```

Swift 代码示例：
```
let mb4bfile = "file-local-path"
let ref = TACStorageService.defaultStorage().reference(withPath: "hello")
var result:TACStorageMetadata?
let task = ref?.putFile(URL.init(fileURLWithPath: mb4bfile), metaData: nil, completion: { (metadata:TACStorageMetadata?, error:Error?) in
  //完成回调
})
task?.enqueue()
//上传还没完成时 
//暂停上传
task?.pause()
 //暂停下载
task?.resume()
//取消上传
task?.cancel()
```
#### 删除文件
删除文件时，只需要对其引用直接调用 deleteWithCompletion: 方法即可，参考下面的例子：

Objective-C 代码示例：
```
TACStorageReference* ref = [[TACStorageService defaultStorage] referenceWithPath:@"test"];
[ref deleteWithCompletion:^(NSError * _Nullable error) {
    if (nil == error) {
      //删除成功
    } ;
  }];
```

Swift 代码示例：
```
let ref = TACStorageService.defaultStorage().reference(withPath: "test")
ref?.delete(completion: { (error:Error?) in
  if nil == error{
    //删除成功
}
})
```
