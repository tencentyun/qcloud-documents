## 简介
Android SDK 提供获取对象 URL、获取请求预签名 URL 接口。

## 获取对象 URL
```java
string getAccessUrl(CosXmlRequest cosXmlRequest);
```

## 获取请求预签名 URL 

```java
String getPresignedURL(CosXmlRequest cosXmlRequest) throws CosXmlClientException;
```

#### 参数说明

|参数名称|类型|描述|
|-----|-----|----|
|cosXmlRequest|CosXmlRequest|请求对象|
|presignedUrlRequest |PresignedUrlRequest |预签名 URL 实例|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

#### PresignedUrlRequest 结构体说明

通过 PresignedUrlRequest 对象获取对应预签名请求 URL，用于发送请求。

|参数名称|类型|描述|
|-----|-----|----|
|bucket|string|COS XML API 的存储桶名称，格式为：`<BucketName-APPID>`<br>例如 examplebucket-1250000000 |
|requestMethod|string|HTTP 请求方法，例如 GET（下载）|
|cosPath |string|对象键，即对象在存储桶中的位置标识符|
|checkParameterListForSing |`Set<String>`|签名中需要验证的请求头|
|checkHeaderListForSign  |`Set<String>`|签名中需要验证的请求参数|

## 预签名请求示例

#### 上传请求示例

[//]: # (.cssg-snippet-get-presign-upload-url)
```java
try {

    String bucket = "examplebucket-1250000000"; //存储桶名称
    String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。例如 cosPath = "text.txt";
    String method = "PUT"; //请求 HTTP 方法
    PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath) {
        @Override
        public RequestBodySerializer getRequestBody() throws CosXmlClientException {
            //用于计算 put 等需要带上 body 的请求的签名 URL
            return RequestBodySerializer.string("text/plain", "this is test");
        }
    };
    presignedUrlRequest.setRequestMethod(method);

    String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

    //String urlWithSign = cosXmlService.getPresignedURL(putObjectRequest)； //直接使用PutObjectRequest

    String srcPath = new File(context.getExternalCacheDir(), "exampleobject").toString();
    PutObjectRequest putObjectRequest = new PutObjectRequest("examplebucket-1250000000", "exampleobject", srcPath);
    //设置上传请求预签名 URL
    putObjectRequest.setRequestURL(urlWithSign);
    //设置进度回调
    putObjectRequest.setProgressListener(new CosXmlProgressListener() {
        @Override
        public void onProgress(long progress, long max) {
            // todo Do something to update progress...
        }
    });
    // 使用同步方法上传
    PutObjectResult putObjectResult = cosXmlService.putObject(putObjectRequest);
} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}
```

#### 下载请求示例

[//]: # (.cssg-snippet-get-presign-download-url)
```java
try {
    String bucket = "examplebucket-1250000000"; //存储桶名称
    String cosPath = "exampleobject"; //即对象在存储桶中的位置标识符。例如 cosPath = "text.txt";
    String method = "GET"; //请求 HTTP 方法.
    PresignedUrlRequest presignedUrlRequest = new PresignedUrlRequest(bucket, cosPath);
    presignedUrlRequest.setRequestMethod(method);

    String urlWithSign = cosXmlService.getPresignedURL(presignedUrlRequest); //上传预签名 URL (使用永久密钥方式计算的签名 URL )

    //String urlWithSign = cosXmlService.getPresignedURL(getObjectRequest)； //直接使用 GetObjectRequest

    String savePath = context.getExternalCacheDir().toString(); //本地路径
    String saveFileName = "exampleobject"; //本地文件名
    GetObjectRequest getObjectRequest = new GetObjectRequest("examplebucket-1250000000", "exampleobject", savePath, saveFileName);

    // 设置上传请求预签名 URL
    getObjectRequest.setRequestURL(urlWithSign);
    // 设置进度回调
    getObjectRequest.setProgressListener(new CosXmlProgressListener() {
        @Override
        public void onProgress(long progress, long max) {
            // todo Do something to update progress...
        }
    });
    // 使用同步方法下载
    GetObjectResult getObjectResult = cosXmlService.getObject(getObjectRequest);

} catch (CosXmlClientException e) {
    e.printStackTrace();
} catch (CosXmlServiceException e) {
    e.printStackTrace();
}
```
