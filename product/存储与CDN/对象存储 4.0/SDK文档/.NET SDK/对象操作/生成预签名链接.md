## 简介

本文档提供关于生成对象预签名链接的示例代码。

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 生成对象预签名链接

#### 示例代码一：生成预签名上传链接

[//]: # (.cssg-snippet-get-presign-upload-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  preSignatureStruct.appid = "1250000000";//腾讯云账号 APPID
  preSignatureStruct.region = "COS_REGION"; //存储桶地域
  preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
  preSignatureStruct.key = "exampleobject"; //对象键
  preSignatureStruct.httpMethod = "PUT"; //HTTP 请求方法
  preSignatureStruct.isHttps = true; //生成 HTTPS 请求 URL
  preSignatureStruct.signDurationSecond = 600; //请求签名时间为 600s
  preSignatureStruct.headers = null;//签名中需要校验的 header
  preSignatureStruct.queryParameters = null; //签名中需要校验的 URL 中请求参数

  //上传预签名 URL (使用永久密钥方式计算的签名 URL)
  string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct);

  string srcPath = @"temp-source-file";//本地文件绝对路径
  PutObjectRequest request = new PutObjectRequest(null, null, srcPath);
  //设置上传请求预签名 URL
  request.RequestURLWithSign = requestSignURL;
  //设置进度回调
  request.SetCosProgressCallback(delegate (long completed, long total)
  {
    Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
  });
  //执行请求
  PutObjectResult result = cosXml.PutObject(request);
  //请求成功
  Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
  //请求失败
  Console.WriteLine("CosClientException: " + clientEx);
}
catch (COSXML.CosException.CosServerException serverEx)
{
  //请求失败
  Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/ObjectPresignUrl.cs) 查看。

#### 示例代码二：生成预签名下载链接

[//]: # (.cssg-snippet-get-presign-download-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  preSignatureStruct.appid = "1250000000";//腾讯云账号 APPID
  preSignatureStruct.region = "COS_REGION"; //存储桶地域
  preSignatureStruct.bucket = "examplebucket-1250000000"; //存储桶
  preSignatureStruct.key = "exampleobject"; //对象键
  preSignatureStruct.httpMethod = "GET"; //HTTP 请求方法
  preSignatureStruct.isHttps = true; //生成 HTTPS 请求 URL
  preSignatureStruct.signDurationSecond = 600; //请求签名时间为600s
  preSignatureStruct.headers = null;//签名中需要校验的 header
  preSignatureStruct.queryParameters = null; //签名中需要校验的 URL 中请求参数

  string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); 

  //下载请求预签名 URL (使用永久密钥方式计算的签名 URL)
  string localDir = System.IO.Path.GetTempPath();//本地文件夹
  string localFileName = "my-local-temp-file"; //指定本地保存的文件名
  GetObjectRequest request = new GetObjectRequest(null, null, localDir, localFileName);
  //设置下载请求预签名 URL
  request.RequestURLWithSign = requestSignURL;
  //设置进度回调
  request.SetCosProgressCallback(delegate (long completed, long total)
  {
    Console.WriteLine(String.Format("progress = {0:##.##}%", completed * 100.0 / total));
  });
  //执行请求
  GetObjectResult result = cosXml.GetObject(request);
  //请求成功
  Console.WriteLine(result.GetResultInfo());
}
catch (COSXML.CosException.CosClientException clientEx)
{
  //请求失败
  Console.WriteLine("CosClientException: " + clientEx);
}
catch (COSXML.CosException.CosServerException serverEx)
{
  //请求失败
  Console.WriteLine("CosServerException: " + serverEx.GetInfo());
}
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/ObjectPresignUrl.cs) 查看。

