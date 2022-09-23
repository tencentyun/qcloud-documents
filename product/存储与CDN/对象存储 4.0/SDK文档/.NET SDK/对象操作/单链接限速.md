## 简介

本文档提供关于调用上传下载接口时对链接进行限速。

## 使用说明

限速值设置范围为**819200 - 838860800**，单位默认为 bit/s，即100KB/s - 100MB/s，如果超出该范围将返回400错误。

#### 示例代码一：上传时对单链接限速

[//]: # (.cssg-snippet-upload-object-traffic-limit)
```cs
TransferConfig transferConfig = new TransferConfig();

// 初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXml, transferConfig);

// 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
string bucket = "examplebucket-1250000000";
string cosPath = "dir/exampleObject"; // 对象键
string srcPath = @"temp-source-file";//本地文件绝对路径

PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
putObjectRequest.LimitTraffic(8 * 1024 * 1024); // 限制为1MB/s

COSXMLUploadTask uploadTask = new COSXMLUploadTask(putObjectRequest);

uploadTask.SetSrcPath(srcPath);

await transferManager.UploadAsync(uploadTask);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/TransferUploadObject.cs) 查看。

#### 示例代码二：下载时对单链接限速

[//]: # (.cssg-snippet-download-object-traffic-limit)
```cs
TransferConfig transferConfig = new TransferConfig();

// 初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXml, transferConfig);

// 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
string bucket = "examplebucket-1250000000";
string cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键
string localDir = System.IO.Path.GetTempPath();//本地文件夹
string localFileName = "my-local-temp-file"; //指定本地保存的文件名

GetObjectRequest request = new GetObjectRequest(bucket, 
        cosPath, localDir, localFileName);
request.LimitTraffic(8 * 1024 * 1024); // 限制为1MB/s

COSXMLDownloadTask downloadTask = new COSXMLDownloadTask(request);
await transferManager.DownloadAsync(downloadTask);
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/TransferDownloadObject.cs) 查看。

