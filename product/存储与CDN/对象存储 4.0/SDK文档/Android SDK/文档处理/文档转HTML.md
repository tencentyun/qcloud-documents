## 简介

本文档提供关于文档转 HTML 的 API 概览以及 SDK 示例代码。

| API                                                          | 操作描述                     |
| :----------------------------------------------------------- | :--------------------------- |
| [文档转HTML](https://cloud.tencent.com/document/product/436/54059) | 用于文档转HTML的功能       |

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参考 [SDK API 参考](https://cos-android-sdk-doc-1253960454.file.myqcloud.com/)。

## 文档转HTML

#### 功能说明

用于文档转HTML的功能，文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览。

#### 示例代码

以HTML格式预览文档

[//]: # (.cssg-snippet-document-preview-in-html)
```java
// 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
String bucket = "examplebucket-1250000000";
String cosPath = "exampleobject.pdf"; //文档位于存储桶中的位置标识符，即对象键
String localPath = "localdownloadpath"; // 保存在本地文件夹的路径
PreviewDocumentInHtmlRequest request = new PreviewDocumentInHtmlRequest(bucket,
        cosPath, localPath);
cosXmlService.previewDocumentInHtmlAsync(request, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        PreviewDocumentInHtmlResult previewDocumentInHtmlResult = (PreviewDocumentInHtmlResult) result;
        String previewFilePath = previewDocumentInHtmlResult.getPreviewFilePath();
    }
    // 如果您使用 kotlin 语言来调用，请注意回调方法中的异常是可空的，否则不会回调 onFail 方法，即：
    // clientException 的类型为 CosXmlClientException?，serviceException 的类型为 CosXmlServiceException?
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

以HTML格式链接预览文档

[//]: # (.cssg-snippet-document-preview-in-html-link)
```java
// 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
String bucket = "examplebucket-1250000000";
String cosPath = "exampleobject.pdf"; //文档位于存储桶中的位置标识符，即对象键
PreviewDocumentInHtmlLinkRequest request = new PreviewDocumentInHtmlLinkRequest(bucket,
        cosPath);
cosXmlService.previewDocumentInHtmlLinkAsync(request, new CosXmlResultListener() {
    @Override
    public void onSuccess(CosXmlRequest request, CosXmlResult result) {
        PreviewDocumentInHtmlLinkResult previewDocumentInHtmlLinkResult = (PreviewDocumentInHtmlLinkResult) result;
        String previewUrl = previewDocumentInHtmlLinkResult.getPreviewUrl();
    }
    // 如果您使用 kotlin 语言来调用，请注意回调方法中的异常是可空的，否则不会回调 onFail 方法，即：
    // clientException 的类型为 CosXmlClientException?，serviceException 的类型为 CosXmlServiceException?
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

以HTML格式直出内容预览文档到字节数组
（注意：请不要通过本接口预览大文件，否则容易造成内存溢出）

[//]: # (.cssg-snippet-document-preview-in-html-bytes)
```java
// 存储桶名称，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
String bucket = "examplebucket-1250000000";
String cosPath = "exampleobject.pdf"; //文档位于存储桶中的位置标识符，即对象键
try {
    byte[] bytes = cosXmlService.previewDocumentInHtmlBytes(bucket, cosPath);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}
```

>?更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/Android/app/src/androidTest/java/com/tencent/qcloud/cosxml/cssg/DocumentPreview.java) 查看。

