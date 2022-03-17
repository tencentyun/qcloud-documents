## 简介

本文档提供关于生成对象访问 URL 的示例代码。

>?
> - 本文档中生成的访问对象 URL 方法，仅适用于通过默认域名访问公有读对象。
> - 当对象为私有读对象时，请参见 [生成预签名 URL](https://cloud.tencent.com/document/product/436/47238) 文档生成。
> 


## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 生成对象访问链接

当对象 ACL 属性设置为“公有读”时，可以通过以下 SDK 接口生成的 URL 直接访问对象（仅支持生成 COS 默认源站域名的 URL）。

```C#
try
{
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  string bucket = "examplebucket-1250000000";
  string key = "exampleobject"; //对象键
  // 生成公有读URL
  string requestURL = cosXml.GetObjectUrl(bucket, key);
  //请求成功
  Console.WriteLine(requestURL);
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



