## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

| API                                                          | 操作名             | 操作描述                           |
| ------------------------------------------------------------ | ------------------ |---------------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况	  | 用于查询已经开通媒体处理功能的存储桶     |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API](https://cos-dotnet-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询媒体处理开通情况

#### 功能说明

DescribeMediaBuckets 接口用于查询已经开通媒体处理功能的存储桶。

>?
> - DescribeMediaBuckets 接口从 5.4.24 版本开始支持，下载新版 SDK 前往 [Releases](https://github.com/tencentyun/qcloud-sdk-dotnet/releases) 或参见 [快速入门](https://cloud.tencent.com/document/product/436/32819)。
> - 查看版本更新日志，请前往 [GitHub](https://github.com/tencentyun/qcloud-sdk-dotnet/blob/master/CHANGELOG.md)。
>


#### 示例代码

[//]: #	".cssg-snippet-DescribeMediaBucketModel"

```cs
using COSXML.Model.CI;
using COSXML.Auth;
using System;
using COSXML;

namespace COSSnippet
{
    public class DescribeMediaBucketModel {

      private CosXml cosXml;

      DescribeMediaBucketModel() {
        CosXmlConfig config = new CosXmlConfig.Builder()
          .SetRegion("COS_REGION") // 设置默认的地域, COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224 
          .Build();
        
        string secretId = "SECRET_ID";   // 云 API 密钥 SecretId, 获取 API 密钥请参照 https://console.cloud.tencent.com/cam/capi
        string secretKey = "SECRET_KEY"; // 云 API 密钥 SecretKey, 获取 API 密钥请参照 https://console.cloud.tencent.com/cam/capi
        long durationSecond = 600;          //每次请求签名有效时长，单位为秒
        QCloudCredentialProvider qCloudCredentialProvider = new DefaultQCloudCredentialProvider(secretId, 
          secretKey, durationSecond);
        
        this.cosXml = new CosXmlServer(config, qCloudCredentialProvider);
      }

      /// 获取开通了万象功能的 Buckets 列表
      public void DescribeMediaBucket()
      {
        //.cssg-snippet-body-start:[DescribeMediaBucket]
        DescribeMediaBucketsRequest request = new DescribeMediaBucketsRequest();
        // 执行请求
        DescribeMediaBucketsResult result = cosXml.DescribeMediaBuckets(request);
        Console.WriteLine(result.GetResultInfo());
        // 遍历Bucket列表
        for (int i = 0; i < result.mediaBuckets.MediaBucketList.Count; i++)
        {
          Console.WriteLine(result.mediaBuckets.MediaBucketList[i].BucketId);
          Console.WriteLine(result.mediaBuckets.MediaBucketList[i].Region);
          Console.WriteLine(result.mediaBuckets.MediaBucketList[i].CreateTime);
        }
        //.cssg-snippet-body-end
      }

      static void Main(string[] args)
      {
        DescribeMediaBucketModel m = new DescribeMediaBucketModel();
        /// 获取媒体Buckets列表
        m.DescribeMediaBucket();
        // .cssg-methods-pragma
      }
    }
}

```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/blob/master/dotnet/dist/DescribeMediaBucket.cs) 查看。
>

