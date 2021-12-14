## 简介

本文档提供关于生成对象预签名链接的示例代码。

>?
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> - 关于临时密钥的获取，请参见 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。
> 


## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 生成对象预签名链接

#### 示例代码一：生成预签名 URL

[//]: # (.cssg-snippet-get-presign-download-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  // APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.appid = "1250000000";
  // 存储桶所在地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
  preSignatureStruct.region = "COS_REGION"; 
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.bucket = "examplebucket-1250000000";
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

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/ObjectPresignUrl.cs) 查看。
>

#### 示例代码二：生成预签名上传链接

[//]: # (.cssg-snippet-get-presign-upload-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  // APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.appid = "1250000000";
  // 存储桶所在地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
  preSignatureStruct.region = "COS_REGION";
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.bucket = "examplebucket-1250000000";
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

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/ObjectPresignUrl.cs) 查看。
>


#### 示例代码三：生成预签名 URL，并在签名中携带 Host

[//]: # (.cssg-snippet-get-presign-download-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  // APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.appid = "1250000000";
  // 存储桶所在地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
  preSignatureStruct.region = "COS_REGION"; 
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.bucket = "examplebucket-1250000000";
  preSignatureStruct.key = "exampleobject"; //对象键
  preSignatureStruct.httpMethod = "GET"; //HTTP 请求方法
  preSignatureStruct.isHttps = true; //生成 HTTPS 请求 URL
  preSignatureStruct.signDurationSecond = 600; //请求签名时间为600s
  preSignatureStruct.signHost = true; // 请求中签入Host，建议开启，能够有效防止越权请求，需要注意，开启后实际请求也需要携带Host请求头
  preSignatureStruct.headers = null;//签名中需要校验的 header
  preSignatureStruct.queryParameters = null; //签名中需要校验的 URL 中请求参数

  string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); 
  Console.WriteLine("requestUrl is:" + requestSignURL);

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

#### 示例代码四：生成预签名URL，并在签名中携带请求参数

[//]: # (.cssg-snippet-get-presign-download-url)
```cs
try
{
  PreSignatureStruct preSignatureStruct = new PreSignatureStruct();
  // APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.appid = "1250000000";
  // 存储桶所在地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
  preSignatureStruct.region = "COS_REGION"; 
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  preSignatureStruct.bucket = "examplebucket-1250000000";
  preSignatureStruct.key = "exampleobject"; //对象键
  preSignatureStruct.httpMethod = "GET"; //HTTP 请求方法
  preSignatureStruct.isHttps = true; //生成 HTTPS 请求 URL
  preSignatureStruct.signDurationSecond = 600; //请求签名时间为600s
  preSignatureStruct.signHost = true; // 请求中签入Host，建议开启，能够有效防止越权请求，需要注意，开启后实际请求也需要携带Host请求头
  preSignatureStruct.headers = null; // 签名中需要校验的 header
  string ci_params = "imageMogr2/thumbnail/!50p";
  preSignatureStruct.queryParameters = new Dictionary<string, string>(); // 签名中需要校验的 URL 中请求参数，以请求万象图片处理为例
  preSignatureStruct.queryParameters.Add(ci_params, null);

  string requestSignURL = cosXml.GenerateSignURL(preSignatureStruct); 
  Console.WriteLine("requestUrl is:" + requestSignURL);

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

