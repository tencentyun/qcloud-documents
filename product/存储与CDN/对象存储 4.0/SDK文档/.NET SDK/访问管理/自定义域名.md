## 简介

本文档提供关于自定义域名的 API 概览以及 SDK 示例代码。

| API               | 操作名         | 操作描述                   |
| ----------------- | -------------- | -------------------------- |
| PUT Bucket domain | 设置自定义域名 | 设置存储桶的自定义域名信息 |
| GET Bucket domain | 查询自定义域名 | 查询存储桶的自定义域名信息 |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 设置自定义域名

#### 功能说明

PUT Bucket domain 用于为存储桶配置自定义域名。

#### 示例代码

[//]: # (.cssg-snippet-put-bucket-domain)
```cs
try
{
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  string bucket = "examplebucket-1250000000";
  
  DomainConfiguration domain = new DomainConfiguration();
  domain.rule = new DomainConfiguration.DomainRule();
  domain.rule.Name = "www.qq.com";
  domain.rule.Status = "ENABLED";
  domain.rule.Type = "WEBSITE";
  
  PutBucketDomainRequest request = new PutBucketDomainRequest(bucket, domain);   
  //执行请求
  PutBucketDomainResult result = cosXml.PutBucketDomain(request);
  
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

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/BucketDomain.cs) 查看。

#### 返回错误码说明

该请求可能会发生的一些常见的特殊错误如下：

| 状态码                                 | 说明                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| HTTP 409 Conflict                      | 该域名记录已存在，且请求中没有设置强制覆盖。或者该域名记录不存在，且请求中设置了强制覆盖 |
| HTTP 451 Unavailable For Legal Reasons | 该域名是中国境内域名，并且没有备案                           |

## 查询自定义域名

#### 功能说明

GET Bucket domain 用于查询存储桶的自定义域名信息。

#### 示例代码

[//]: # (.cssg-snippet-get-bucket-domain)
```cs
try
{
  // 存储桶名称，此处填入格式必须为 bucketname-APPID, 其中 APPID 获取参考 https://console.cloud.tencent.com/developer
  string bucket = "examplebucket-1250000000";
  GetBucketDomainRequest request = new GetBucketDomainRequest(bucket);   
  //执行请求
  GetBucketDomainResult result = cosXml.GetBucketDomain(request);
  
  //请求成功
  Console.WriteLine(result.domainConfiguration);
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

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/BucketDomain.cs) 查看。


#### 返回参数说明

<table>
<thead>
<tr>
<th>参数名称</th>
<th>描述</th>
<th>类型</th>
</tr>
</thead>
<tbody><tr>
<td nowrap="nowrap">x-cos-domain-txt-verification</td>
<td>域名校验信息，该字段是一个 MD5 校验值，原串格式为：<code>cos[Region][BucketName-APPID][BucketCreateTime]</code>，其中 Region 为存储桶所在地域，BucketCreateTime 为存储桶 GMT 创建时间</td>
<td>String</td>
</tr>
</tbody></table>

