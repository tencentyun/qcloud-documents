## 简介

本文档提供关于数据万象标准处理回调信息解析的 SDK 示例代码。

## XML 回调内容解析

### 功能说明

将数据万象公共的 XML 回调信息解析为 Java 对象。

### 使用示例

本示例用于解析回调数据，可通过获取 Unmarshallers 来进行 XML 数据的解析。
>? 您可以通过查看 COSClient 的接口获取到需要使用的 XML 解析器，也可以通过查看功能对应的查询接口实现使用的是哪个 Unmarshaller。
>

以文档预览回调信息为例，对应的查询接口为 describeDocProcessJob。
- [COSClient](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/COSClient.java) 中的代码片段，查看 invoke 方法中是使用哪个 Unmarshaller。
```java
@Override
public DocJobResponse describeDocProcessJob(DocJobRequest request) {
    this.checkCIRequestCommon(request);
    CosHttpRequest<DocJobRequest> httpRequest = this.createRequest(request.getBucketName(), "/doc_jobs/" + request.getJobId(), request, HttpMethodName.GET);
    return this.invoke(httpRequest, new Unmarshallers.DescribeDocJobUnmarshaller());
}
```
- 使用 Unmarshaller 进行解析响应内容。
```java
public static void processCINotifyResponse(String response) throws Exception {
    Unmarshallers.DescribeDocJobUnmarshaller describeDocJobUnmarshaller = new Unmarshallers.DescribeDocJobUnmarshaller();
    InputStream is = new ByteArrayInputStream(response.getBytes());
    DocJobResponse docJobResponse = describeDocJobUnmarshaller.unmarshall(is);
}
```

## JSON 回调内容解析

### 功能说明

将数据万象公共的 JSON 回调信息解析为 Java 对象。

### 使用示例

>? 
> - 本质上处理 JSON 回调是将 JSON 转为 XML 后再进行处理。
> - Demo 中使用了 org.json 将 Json 转为 XML，并未在 SDK 的 Pom 中提供该依赖，需要自行导入。
> 

以图片内容审核回调接口为例，对应的查询接口为 describeAuditingImageJob。
- [COSClient](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/COSClient.java) 中的代码片段，查看 invoke 方法中是使用哪个 Unmarshaller。
```java
@Override
public ImageAuditingResponse describeAuditingImageJob(DescribeImageAuditingRequest imageAuditingRequest) {
    rejectNull(imageAuditingRequest.getBucketName(),
            "The bucketName parameter must be specified setting the object tags");
    rejectNull(imageAuditingRequest.getJobId(),
            "The jobId parameter must be specified setting the object tags");
    CosHttpRequest<DescribeImageAuditingRequest> request = createRequest(imageAuditingRequest.getBucketName(), "/image/auditing/" + imageAuditingRequest.getJobId(), imageAuditingRequest, HttpMethodName.GET);
    return invoke(request, new Unmarshallers.ImageAuditingDescribeJobUnmarshaller());
}
```
- 将 JSON 响应转为 XML 后使用 Unmarshaller 进行解析响应内容。
```java
//回调demo
public static void processJsonCINotifyResponse(String jsonResponse) throws Exception {
    JSONObject response = new JSONObject(jsonResponse);
    JSONObject json = new JSONObject();
    json.put("Response",response);
    String xml = XML.toString(json);
    Unmarshallers.ImageAuditingDescribeJobUnmarshaller imageJobUnmarshaller = new Unmarshallers.ImageAuditingDescribeJobUnmarshaller();
    InputStream is = new ByteArrayInputStream(xml.getBytes());
    ImageAuditingResponse imageAuditingResponse = imageJobUnmarshaller.unmarshall(is);
}
```

上述示例使用的是 org.json.json，SDK 中并没有提供，如需使用请添加如下依赖。
```xml
<dependency>
    <groupId>org.json</groupId>
    <artifactId>json</artifactId>
    <version>20180130</version>
</dependency>
```
