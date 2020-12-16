### 手动集成 SDK 后，设置QCloudCOSXMLEndPoint实例的regionName会crash`：[__NSCFConstantString matchesRegularExpression:]: unrecognized selector sent to instance xxx`

原因：
    matchesRegularExpression 是NSString的分类提供的方法。
    Objective-C链接器不会为每个方法建立符号表，只是为类建立了符号表。sdk是静态库，如果静态库中定义了一份已经存在的类的分类，系统就会认为这个类已经存在，则不会将类和类的分类的代码整合起来，在最后的可执行代码中，就会缺少分类中的方法。

解决办法：
1. 在target->Build Settings->All->Other Linker Flags中添加-Objc和-all_load两个参数
2. -ObjC会将静态库中的类和分类都加载到最后的可执行文件中，但是如果库中只有分类没有类的话，这个参数就会失效，就需要-all_load ,该参数会把所有找到的目标文件都加到可执行文件中。

### 集成 SDK 发送请求之后抛出异常：`您没有配置默认的OCR服务配置，请配置之后再调用该方法或者您没有配置Key为 'xxx' 的OCR服务配置，请配置之后再调用该方法`？

原因：sdk 所有的请求都依赖于一个QCloudCOSXMLServeice和QCloudCOSTransferMangerService(上传的高级接口依赖于该实例)，如果在发送请求之前没有注册对应的service会抛出该异常

解决办法：通过以下代码注册请求所需要的service实例，并确保该实例在请求发出前已存在
```iOS
    QCloudServiceConfiguration *configuration = [QCloudServiceConfiguration new];
    configuration.appID = "AppId";
    configuration.signatureProvider = self;
    QCloudCOSXMLEndPoint *endpoint = [[QCloudCOSXMLEndPoint alloc] init];
    endpoint.regionName = @"region";
    endpoint.useHTTPS = YES;
    configuration.endpoint = endpoint;

    [QCloudCOSXMLService registerDefaultCOSXMLWithConfiguration:configuration];
    [QCloudCOSTransferMangerService registerDefaultCOSTransferMangerWithConfiguration:configuration];
```


### 集成 SDK 后抛出如下异常：`3. 默认的COSXMLService已存在，如有新的配置，请通过 registerCOSXMLWithConfiguration:withKey:重新注册`？

原因：在 SDK 中，不同的COSXMLService实例对应不同的配置（配置信息可以参考相关属性），如regionName为ap-guangzhou和ap-beijing是两个不同的配置，需要注册两个不同的service，如果在用ap-guangzhou注册了了一个一个service之后，将其region又改成ap-guangzhou重新注册就会触发该异常。

解决办法：
1. 默认的service即通过`registerDefaultCOSXMLWithConfiguration：`不需要指定key
2. 通过以下代码注册一个新的service
```iOS
//判断要注册的key是否存在，
    if(![QCloudCOSXMLService hasServiceForKey:@"要注册的key"]){
    //不存在注册一个新的servide
        [QCloudCOSXMLService registerCOSXMLWithConfiguration:configuration withKey:@"要注册的key"]
    }
```

### 集成 SDK 之后运行，代理`- (void)signatureWithFields:(QCloudSignatureFields *)fileds request:urlRequest:compelete:`没有被调用

原因：该代理方法是获取秘钥/签名的方法，为了最大程度的保证秘钥的有效性（调用过早签名容易过期），SDK会在请求发出之前即`[task resume]`之前才会调用。
解决办法：
1. 请确保该代理方法所在的类在请求发出之前不会被销毁，建议将该代理方法在一个单例类中实现。
2. 是否在创建`QCloudServiceConfiguration实例之后`，设置其`signatureProvider`，比如`configuration.signatureProvider = self(self为实现代理方法所在的类)`
3. 如果以上都没问题，请检查是否发送请求。

### SDK 能否缓存和复用秘钥，在秘钥过期之后重新请求新的秘钥？

sdk 提供了QCloudCredentailFenceQueue来实现秘钥的缓存和复用，具体使用方法请参考文档[快速入门](https://cloud.tencent.com/document/product/436/11280)

### 通过 SDK 的高级接口 `QCloudCOSXMLUploadObjectRequest` 抛出异常：`不支持设置该类型的body，支持的类型为NSData、QCloudFileOffsetBody、NSURL`?

原因与解决办法：sdk目前只支持设置以下三种类型的body
1. NSURL：文件的本地路径，通过[NSURL fileURLWithPath:@"文件在本地的路径"]初始化一个URL
2. NSData:二进制数据
3. QCloudFileOffsetBody:分片的body，开发者一般不需要关心该类型，属于SDK 高级接口内部使用的body类型


### 通过 SDK 的高级接口 `QCloudCOSXMLUploadObjectRequest` 上传系统图库中的视频或者文件，断点续传失败，报错`The specified Content-Length is zero`?

原因以及解决办法： SDK 只支持续传沙盒中的文件，如需使用断点续传的功能，请先将文件移到沙盒中

### `集成 SDK 之后，调用上传接口上传的文件大小和本地的文件不一致`
原因以及解决办法：请确保您设置好body之后，本地文件不会发生改变，比如文件在压缩过程中或者还没有完成写入之前调用了上传接口触发了上传，SDK就会以当时的文件大小为准进行分片进行上传，从而导致上传到cos上的文件和本地文件大小不一致。

### 集成 SDK 之后，调用上传接口，上传成功之后的文件大小为0
解决办法：
1. 如果上传路径是文件在系统图库的路径，请检查是否有读取该文件的权限。例如：`file:///var/mobile/Media/DCIM/101APPLE/`这个路径无法直接访问，需要通过Photos框架里的request方法获取照片
2. 如果app要兼容iOS11，在上传图库视频的时候在调用`[[PHImageManager defaultManager] requestPlayerItemForVideo:asset options:option resultHandler:^(AVPlayerItem *playerItem, NSDictionary *info) {
    //及时将文件移到沙盒中或者保存playerItem
    }];`方法获取playerItem之后将其保存起来，或者在该回调中将要上传的文件移到app的沙盒中。因为iOS11中playerItem被销毁之后，文件的读权限就会失效，从而导致上传的文件大小为0。
    
3. 如果上传的是app的沙盒中的文件，请检查上传的文件是否在沙盒的tmp文件加下，比如` /var/mobile/Containers/Data/Application/0BFBB3FE-0FD0-46CB-ADDE-DDE08F6D62C3/tmp/`，该目录下的文件会被系统随时清理，请将要上传的文件移到安全的目录，保证文件在上传的过程中不会被清理，更多关于沙盒的描述请参考[File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)

### 集成 SDK 后使用高级接口上传报错`上传过程中MD5校验与本地不一致，请检查本地文件在上传过程中是否发生了变化：分片上传过程中，每上传完一个分片就会校验这个分片的md5和本地片的md5是否一致，不一致就报错`

原因：该错误发生在上传大于1MB的文件的情况下，超过1MB的文件 SDK 在上传时会根据将文件分成若干个1MB的文件进行分片上传，在上传完每一个分片之后会用后台返回的etag和本地文件的分片进行对比，如果发现不一致会抛出该错误。

解决办法：请检查文件在上传的过程中是否发生改变
