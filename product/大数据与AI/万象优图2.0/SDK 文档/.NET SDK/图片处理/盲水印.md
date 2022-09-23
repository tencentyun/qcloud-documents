## 简介

本文档提供关于盲水印相关的 API 概览以及 SDK 示例代码。

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 添加盲水印

### 功能说明

盲水印支持在上传时添加以及下载时添加。

### 示例代码一：上传时添加盲水印

[//]: #	".cssg-snippet-put-object-with-watermark"

```cs
PutObjectRequest request = new PutObjectRequest(bucket, key, srcPath);

JObject o = new JObject();
// 不返回原图
o["is_pic_info"] = 0;
JArray rules = new JArray();
JObject rule = new JObject();
rule["bucket"] = bucket;
rule["fileid"] = key;
//处理参数，规则参见：https://cloud.tencent.com/document/product/436/46782
rule["rule"] = "watermark/3/type/<type>/image/<imageUrl>/text/<text>/level/<level>";
rules.Add(rule);
o["rules"] = rules;

string ruleString = o.ToString(Formatting.None);
request.SetRequestHeader("Pic-Operations", ruleString);
//执行请求
PutObjectResult result = cosXml.PutObject(request);
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/PictureOperation.cs) 查看。
>

### 示例代码二：下载时添加盲水印

[//]: #	".cssg-snippet-download-object-with-watermark"

```cs
GetObjectRequest getObjectRequest = new GetObjectRequest(bucket, key, localDir, localFileName);
//处理参数，规则参见：https://cloud.tencent.com/document/product/436/46782
getObjectRequest.SetQueryParameter("watermark/3/type/<type>/image/<imageUrl>/text/<text>", null);

GetObjectResult result = cosXml.GetObject(getObjectRequest);
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/dotnet/dist/PictureOperation.cs) 查看。
>
