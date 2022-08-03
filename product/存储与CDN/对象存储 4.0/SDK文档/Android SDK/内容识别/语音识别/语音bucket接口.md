

## 简介

本文档提供关于查询语音识别开通状态相关的 API 概览以及 SDK 示例代码。

| API                                                          |  说明                                  |
| ------------------------------------------------------------ | ----------------------------------------- |
| [查询语音识别开通状态](https://cloud.tencent.com/document/product/436/47598) |接口用于查询存储桶是否已开通语音识别功能。               |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API 参考](https://cos-android-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询语音识别开通状态

#### 功能说明

接口用于查询存储桶是否已开通语音识别功能。

>! COS Android SDK 版本需要大于等于 v5.9.2。
>

#### 示例代码

[//]: # (.cssg-snippet-describe-speech-buckets)
```java
        DescribeSpeechBucketsRequest request = new DescribeSpeechBucketsRequest();
        //设置第几页
        request.setPageNumber(1);
        //设置每页个数
        request.setPageSize(10);
        //设置地域信息 以“,”分隔字符串，支持 All、ap-shanghai、ap-beijing
        request.setRegions("All");
        //设置存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
        //request.setBucketNames("examplebucket-1250000000,examplebucket123-1250000000");
        //设置存储桶名称前缀，前缀搜索
        //request.setBucketName("examplebucket");
        ciService.describeSpeechBucketsAsync(request, new CosXmlResultListener() {
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult cosResult) {
                // result 查询已经开通语音识别功能的存储桶的结果
                // 详细字段请查看api文档或者SDK源码
                DescribeSpeechBucketsResult result = (DescribeSpeechBucketsResult) cosResult;
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

>? 更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/CiAsr.java) 查看。
>
