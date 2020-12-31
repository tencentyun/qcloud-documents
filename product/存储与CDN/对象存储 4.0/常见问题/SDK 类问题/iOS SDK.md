### 手动集成 SDK 后，设置 QCloudCOSXMLEndPoint 实例的 regionName，抛出异常 `[__NSCFConstantString matchesRegularExpression:]: unrecognized selector sent to instance xxx`，该如何处理？

原因：matchesRegularExpression 是 NSString 的分类提供的方法。Objective-C 链接器不会为每个方法建立符号表，只是为类建立了符号表。sdk 是静态库，如果静态库中定义了一份已经存在的类的分类，系统就会认为这个类已经存在，则不会将类和类的分类的代码整合起来，在最后的可执行代码中，就会缺少分类中的方法。

解决办法：
1. 在 target->Build Settings->All->Other Linker Flags 中添加-Objc 和-all_load 两个参数。
2. -ObjC 会将静态库中的类和分类都加载到最后的可执行文件中，但是如果库中只有分类没有类的话，这个参数就会失效，就需要-all_load，该参数会把所有找到的目标文件都加到可执行文件中。

### 集成 SDK 发送请求之后抛出异常 `您没有配置默认的 OCR 服务配置，请配置之后再调用该方法或者您没有配置 Key 为 'xxx' 的 OCR 服务配置，请配置之后再调用该方法`，该如何处理？

原因：sdk 所有的请求都依赖于一个 QCloudCOSXMLServeice 和 QCloudCOSTransferMangerService(上传的高级接口依赖于该实例)，如果在发送请求之前没有注册对应的 service 会抛出该异常。

解决办法：通过以下代码注册请求所需要的 service 实例，并确保该实例在请求发出前已存在。

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


### 集成 SDK 后抛出异常 `默认的 COSXMLService 已存在，如有新的配置，请通过 registerCOSXMLWithConfiguration:withKey:重新注册`，该如何处理？

原因：在 SDK 中，不同的 COSXMLService 实例对应不同的配置（配置信息可以参考相关属性），例如 regionName 为 ap-guangzhou 和 ap-beijing 是两个不同的配置，需要注册两个不同的 service，如果在用 ap-guangzhou 注册了一个 service 之后，将其 region 又改成 ap-guangzhou 重新注册就会触发该异常。

解决办法：
1. 默认的 service 即通过`registerDefaultCOSXMLWithConfiguration：`不需要指定 key。
2. 通过以下代码注册一个新的 service：
```iOS
//判断要注册的key是否存在，
    if(![QCloudCOSXMLService hasServiceForKey:@"要注册的key"]){
    //不存在注册一个新的servide
        [QCloudCOSXMLService registerCOSXMLWithConfiguration:configuration withKey:@"要注册的key"]
    }
```

### 集成 SDK 之后运行，代理`- (void)signatureWithFields:(QCloudSignatureFields *)fileds request:urlRequest:compelete:`没有被调用，该如何处理？

原因：该代理方法是获取密钥/签名的方法，为了最大程度的保证密钥的有效性（调用签名过早容易过期），SDK 会在请求发出之前即`[task resume]`之前才会调用。

解决办法：
1. 请确保该代理方法所在的类在请求发出之前不会被销毁，建议将该代理方法在一个单例类中实现。
2. 是否在创建`QCloudServiceConfiguration实例之后`，设置其`signatureProvider`，比如`configuration.signatureProvider = self(self为实现代理方法所在的类)`。
3. 如果以上都没问题，请检查是否发送请求。

### SDK 能否缓存和复用密钥，在密钥过期之后重新请求新的密钥，该如何处理？

sdk 提供了 QCloudCredentailFenceQueue 来实现密钥的缓存和复用，具体使用方法请参考 [快速入门](https://cloud.tencent.com/document/product/436/11280) 文档。

### 通过 SDK 的高级接口 `QCloudCOSXMLUploadObjectRequest` 抛出异常 `不支持设置该类型的body，支持的类型为 NSData、QCloudFileOffsetBody、NSURL`，该如何处理？

sdk 目前只支持设置以下三种类型的 body：
1. NSURL：文件的本地路径，通过[NSURL fileURLWithPath:@"文件在本地的路径"]初始化一个 URL。
2. NSData：二进制数据。
3. QCloudFileOffsetBody：分块的 body，开发者一般不需要关心该类型，属于 SDK 高级接口内部使用的 body 类型。


### 通过 SDK 的高级接口 `QCloudCOSXMLUploadObjectRequest` 上传系统图库中的视频或者文件，断点续传失败，报错`The specified Content-Length is zero`，该如何处理？

SDK 只支持续传沙盒中的文件，如需使用断点续传的功能，请先将文件移到沙盒中。

### 集成 SDK 后，调用上传接口上传的文件大小和本地的文件不一致，该如何处理？

请确保您设置好 body 之后，本地文件不会发生改变，比如文件在压缩过程中或者还没有完成写入之前调用了上传接口触发了上传，SDK 就会以当时的文件大小为准进行分块进行上传，从而导致上传到 cos 上的文件和本地文件大小不一致。

### 集成 SDK 之后，调用上传接口，上传成功之后的文件大小为0，该如何处理？

解决办法：
1. 如果上传路径是文件在系统图库的路径，请检查是否有读取该文件的权限。例如：`file:///var/mobile/Media/DCIM/101APPLE/`这个路径无法直接访问，需要通过 Photos 框架里的 request 方法获取照片。
2. 如果 app 要兼容 iOS11，在上传图库视频时再调用`[[PHImageManager defaultManager] requestPlayerItemForVideo:asset options:option resultHandler:^(AVPlayerItem *playerItem, NSDictionary *info) {
    //及时将文件移到沙盒中或者保存 playerItem
    }];`方法获取 playerItem 之后将其保存起来，或者在该回调中将要上传的文件移到 app 的沙盒中。因为 iOS11中 playerItem 被销毁之后，文件的读权限就会失效，从而导致上传的文件大小为0。
3. 如果上传的是 app 的沙盒中的文件，请检查上传的文件是否在沙盒的 tmp 文件夹下，比如` /var/mobile/Containers/Data/Application/0BFBB3FE-0FD0-46CB-ADDE-DDE08F6D62C3/tmp/`，该目录下的文件会被系统随时清理，请将要上传的文件移到安全的目录，保证文件在上传的过程中不会被清理，更多关于沙盒的描述请参考 [File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)。

### 集成 SDK 后使用高级接口上传报错`上传过程中MD5校验与本地不一致，请检查本地文件在上传过程中是否发生了变化：分块上传过程中，每上传完一个分块就会校验这个分块的 md5和本地片的 md5是否一致，不一致就报错`，该如何处理？

原因：该错误发生在上传大于1MB的文件的情况下，超过1MB的文件使用 SDK 上传时会根据将文件分成若干个1MB的文件进行分块上传，在上传完每一个分块之后会用后台返回的 etag 和本地文件的分块进行对比，如果发现不一致会抛出该错误。

解决办法：请检查文件在上传的过程中是否发生改变。


### SDK 能否使用 CDN 加速域名进行访问？

支持，请根据您所使用的编程语言，并参见对应的 [SDK 文档](https://cloud.tencent.com/document/sdk) 进行操作。
