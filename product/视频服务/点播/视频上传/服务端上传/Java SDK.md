对于在服务端上传视频的场景，云点播提供 Java SDK 来实现。上传流程请参见 [服务端上传指引](/document/product/266/9759)。

## 集成方式

### Maven 依赖引入

在项目的 pom.xml 文件添加点播 SDK 依赖即可：

```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>2.1.1</version>
</dependency>
```

### jar 包导入

如果项目没有采用 Maven 的方式进行依赖管理，可采用如下方式，下载各个所需的 jar 包，导入项目即可：

| jar 文件         | 说明    |
| ------------ | ------------ | 
| vod_api-2.1.1.jar | 云点播 SDK。 |
| jackson-annotations-2.9.0.jar,jackson-core-2.9.7.jar,jackson-databind-2.9.7.jar,gson-2.2.4.jar       | 开源的 JSON 相关库。 |
| cos_api-5.4.10.jar            | 腾讯云对象存储服务 COS SDK。                          |
| tencentcloud-sdk-java-3.0.58.jar             | 腾讯云 API SDK。                        |
| commons-codec-1.10.jar,commons-logging-1.2.jar,log4j-1.2.17.jar,slf4j-api-1.7.21.jar,slf4j-log4j12-1.7.21.jar           | 开源日志相关库。    |
| httpclient-4.5.3.jar,httpcore-4.4.6.jar,okhttp-2.5.0.jar,okio-1.6.0.jar | 开源的 HTTP 处理库。                            |
| joda-time-2.9.9.jar | 开源时间处理库。                            |
| jaxb-api-2.3.0.jar | 开源 XML 处理库。                            |
| bcprov-jdk15on-1.59.jar | 开源加密处理库。                            |

单击 [Java SDK 关联 jar 包](https://github.com/tencentyun/vod-java-sdk/raw/master/packages/vod-sdk-jar.zip)，将下载的 jar 包导入项目中，即可使用。



##  简单上传
### 初始化一个上传客户端对象
使用云 API 密钥初始化 VodUploadClient 实例。
```
VodUploadClient client = new VodUploadClient("your secretId", "your secretKey");
```

### 构造上传请求对象
设置媒体本地上传路径。
```
VodUploadRequest request = new VodUploadRequest();
request.setMediaFilePath("/data/videos/Wildlife.wmv");
```

### 调用上传
调用上传方法，传入上传地域及上传请求。
```
try {
    VodUploadResponse response = client.upload("ap-guangzhou", request);
    logger.info("Upload FileId = {}", response.getFileId());
} catch (Exception e) {
    // 业务方进行异常处理
    logger.error("Upload Err", e);
}
```

>?上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。

## 高级功能
### 携带封面
```
VodUploadClient client = new VodUploadClient("your secretId", "your secretKey");
VodUploadRequest request = new VodUploadRequest();
request.setMediaFilePath("/data/videos/Wildlife.wmv");
request.setCoverFilePath("/data/videos/Wildlife.jpg");
try {
    VodUploadResponse response = client.upload("ap-guangzhou", request);
    logger.info("Upload FileId = {}", response.getFileId());
} catch (Exception e) {
    // 业务方进行异常处理
    logger.error("Upload Err", e);
}
```

### 指定任务流
首先 [创建任务流模板](https://cloud.tencent.com/document/product/266/33819) 并为模板命名，发起任务流时，可以使用任务流模板名设置`Procedure`参数，上传成功后会自动执行任务流。
```
VodUploadClient client = new VodUploadClient("your secretId", "your secretKey");
VodUploadRequest request = new VodUploadRequest();
request.setMediaFilePath("/data/videos/Wildlife.wmv");
request.setProcedure("Your Procedure Name");
try {
    VodUploadResponse response = client.upload("ap-guangzhou", request);
    logger.info("Upload FileId = {}", response.getFileId());
} catch (Exception e) {
    // 业务方进行异常处理
    logger.error("Upload Err", e);
}
```

### 子应用上传
传入 [子应用](/document/product/266/14574) ID，上传成功后资源只属于具体的子应用。
```
VodUploadClient client = new VodUploadClient("your secretId", "your secretKey");
VodUploadRequest request = new VodUploadRequest();
request.setMediaFilePath("/data/videos/Wildlife.wmv");
request.setSubAppId(101);
try {
    VodUploadResponse response = client.upload("ap-guangzhou", request);
    logger.info("Upload FileId = {}", response.getFileId());
} catch (Exception e) {
    // 业务方进行异常处理
    logger.error("Upload Err", e);
}
```

## 接口描述
上传客户端类`VodUploadClient`

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| secretId   | 云 API 密钥 ID。        | String | 是    |
| secretKey | 云 API 密钥 Key。 | String  | 是    |

上传请求类`VodUploadRequest`

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| MediaFilePath   | 媒体文件路径，路径为本地路径，不支持 URL 路径。        | String | 是    |
| MediaType   | 媒体文件类型，可选类型请参见 [视频上传综述](/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)，若 MediaFilePath 路径带后缀可不填。        | String | 否    |
| MediaName   | 媒体名称，若不填默认采用 MediaFilePath 的文件名。      | String | 否    |
| CoverFilePath   | 封面文件路径。        | String | 否    |
| CoverType   | 媒体文件类型，可选类型请参见 [视频上传综述](/document/product/266/9760#.E5.B0.81.E9.9D.A2.E7.B1.BB.E5.9E.8B)，若 CoverFilePath 路径带后缀可不填。        | String | 否    |
| Procedure   | 任务流，具体的任务流介绍请参见 [任务流综述](https://cloud.tencent.com/document/product/266/33475#.E4.BB.BB.E5.8A.A1.E6.B5.81)。        | String | 否    |
| ExpireTime   | 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。        | String | 否    |
| ClassId   | 分类 ID，用于对媒体进行分类管理，可通过 [创建分类](/document/product/266/31772) 接口，创建分类，获得分类 ID。        | Integer | 否    |
| SourceContext   | 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长250个字符。        | String | 否    |
| SubAppId   | 云点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID，否则无需填写该字段。        | Integer | 否    |

上传响应类`VodUploadResponse`

| 属性名称      | 属性描述                   | 类型      |
| --------- | ---------------------- | ------- |
| FileId   | 媒体文件的唯一标识。        | String |
| MediaUrl | 媒体播放地址。 | String  |
| CoverUrl | 媒体封面地址。 | String  |
| RequestId | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 | String  |

上传方法`VodUploadClient.upload(String region, VodUploadRequest request)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| region   | 上传地域，具体参考支持的 [地域列表](/document/api/266/31756#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。       | String | 是    |
| request   | 上传请求。        | VodUploadRequest | 是    |

## 错误码表
| 状态码         | 含义               |
| ----------- | ----------------- |
| InternalError       | 内部错误。 |
| InvalidParameter.ExpireTime       | 参数值错误：过期时间。 |
| InvalidParameterValue.CoverType       | 参数值错误：封面类型。     |
| InvalidParameterValue.MediaType       | 参数值错误：媒体类型。           |
| InvalidParameterValue.SubAppId       | 参数值错误：子应用 ID。              |
| InvalidParameterValue.VodSessionKey       | 参数值错误：点播会话。              |
| ResourceNotFound       | 资源不存在。              |
