## 简介

本文档提供关于媒体 bucket 接口的 API 概览以及 SDK 示例代码。

| API                                                          | 操作名         | 操作描述                         |
| ------------------------------------------------------------ | -------------- | -------------------------------- |
| [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通情况 | 用于查询已经开通媒体处理功能的存储桶    |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API 参考](https://cos-android-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

>! COS Android SDK 版本需要大于等于 v5.7.6。
>

#### 示例代码

[//]: # (.cssg-snippet-describe-media-buckets)
```java
GetDescribeMediaBucketsRequest request = new GetDescribeMediaBucketsRequest();
// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域
request.setRegions("ap-guangzhou,ap-beijing");
// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
request.setBucketNames("examplebucket-1250000000");
// 存储桶名称前缀，前缀搜索
request.setBucketName("example");
// 第几页
request.setPageNumber(1);
// 每页个数
request.setPageSize(20);
cosXmlService.getDescribeMediaBucketsAsync(request, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult cosResult) {
        // result 查询到的已经开通媒体处理功能的存储桶
        // 详细字段请查看api文档或者SDK源码 DescribeMediaBucketsResult类
        GetDescribeMediaBucketsResult result = (GetDescribeMediaBucketsResult) cosResult;
    }

    @Override
    public void onFail(CosXmlRequest request, CosXmlClientException clientException, CosXmlServiceException serviceException) {
        if (clientException != null) {
            clientException.printStackTrace();
        } else {
            serviceException.printStackTrace();
        }
    }
});
```

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/MediaOperation.java) 查看。
>
