## Storage 编程使用指南

## 开始之前


如果这是您首次向应用添加 Storage，请完成以下步骤：

在 应用云 控制台中关联您的应用

1. 安装 [应用云 SDK]()。
2. 在 [应用云 控制台]()中，将您的应用添加到您的 应用云 项目中。
3. 参考 [Storage 配置文档]()，配置并初始化  Storage


## 使用 Storage 进行文件操作


您的文件存储在 COS 存储桶中。此存储桶中的文件以分层结构存储，就像本地硬盘中的文件系统一样。通过创建对文件的引用，您的应用可以获得对相应文件的访问权限。然后，借助所创建的这些引用，您可以上传或下载数据、获取或更新元数据，也可以删除文件。引用可以指向特定的文件，也可以指向层次结构中更高层级的节点。


### 创建引用
要上传、下载或删除文件，或要获取或更新文件的元数据，请创建引用。引用可以看作是指向云端文件的指针。由于引用属于轻型项目，因此您可以根据需要创建任意多个引用。引用还可以在多个操作中复用。

引用是使用 TACStorageService 服务并调用其 referenceWithPath 或者 rootReference 方法创建的。


~~~
[TACStorageService defaultStorage].credentailFenceQueue.delegate = self;
self.reference = [[TACStorageService defaultStorage] referenceWithPath:@"test-file/test.png"];
~~~



#### 引用导航

您还可以使用 parent 和 root 方法在我们的文件层次结构中向上导航。parent 可向上导航一级，而 root 可直接导航到根目录。



~~~
imagesRef = [spaceRef parent];

// Root allows us to move all the way back to the top of our bucket
// rootRef now points to the root
TACStorageReference *rootRef = [spaceRef root];
~~~


child、parent 和 root 可以多次链接到一起，每次都会返回一个引用。root 的 parent 是例外，它是 nil。

~~~
TACStorageReference *earthRef = [[spaceRef parent] child:@"earth.jpg"];

// nilRef is nil, since the parent of root is nil
TACStorageReference *nilRef = [[spaceRef root] parent];
~~~

### 上传文件

有了引用之后，您可以通过两种方式将文件上传到 COS：

1. 从内存中的数据上传
2. 从代表设备上某个文件的路径上传



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

实例：

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


实例：

~~~
// File located on disk
NSURL *localFile = [NSURL URLWithString:@"path/to/image"];

// Create a reference to the file you want to upload
FIRStorageReference *riversRef = [storageRef child:@"images/rivers.jpg"];

// Upload the file to the path "images/rivers.jpg"
TACStorageReference *uploadTask = [riversRef putFile:localFile metadata:nil completion:^(TACStorageMetadata *metadata, NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    NSURL *downloadURL = metadata.downloadURL;
  }
}];

~~~
