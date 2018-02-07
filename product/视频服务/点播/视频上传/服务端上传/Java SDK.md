对于在服务端上传视频的场景，腾讯云点播提供了 Java SDK 来实现。上传的流程可以参见 [服务端上传指引](/document/product/266/9759)。

## 集成方式

### Maven依赖引入

在项目的pom.xml文件添加点播SDK依赖即可：

```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>1.1.1</version>
</dependency>
```

### jar包导入

如果项目没有采用Maven的方式进行依赖管理，可采用下述方式，下载各个所需的jar包，导入项目即可：

| jar文件         | 说明    |
| ------------ | ------------ | 
| vod_api-1.1.0.jar | 点播SDK |
| jackson-annotations-2.8.0.jar,jackson-core-2.8.5.jar,jackson-databind-2.8.5.jar       | 开源的JSON相关库 |
| cos_api-5.1.9.jar            | 腾讯云对象存储服务（COS）SDK                          |
| qcloud-java-sdk-2.0.1.jar             | 腾讯云API SDK                        |
| commons-codec-1.10.jar,commons-logging-1.2.jar,log4j-1.2.17.jar,slf4j-api-1.7.21.jar,slf4j-log4j12-1.7.21.jar           | 开源日志相关库    |
| httpclient-4.5.3.jar,httpcore-4.4.6.jar,httpmime-4.5.2.jar | 开源的http处理库                            |
| joda-time-2.9.6.jar | 开源时间处理库                            |

为方便客户使用，可点击下载下面提供的链接，将下载的jar包导入项目中，即可使用：

[点播Java SDK关联jar包](https://github.com/tencentyun/vod-java-sdk/raw/master/packages/vod-sdk-jar.zip)


##  简单视频上传
### 初始化一个上传对象
使用云API密钥初始化VodApi实例
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
```

### 调用上传
传入视频地址进行上传
```
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv");
System.out.println(response.getFileId());
```

## 高级功能
### 携带封面
调用upload的重载方法，传入封面地址
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg");
System.out.println(response.getFileId());
```

### 指定任务流
调用upload的重载方法，传入任务流参数，具体的任务流介绍参考[任务流综述](/document/product/266/11700)，视频上传成功后会自动执行任务流
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", "QCVB_SimpleProcessFile(1, 1)");
System.out.println(response.getFileId());
```

###  指定上传区域
调用upload的重载方法，传入指定的地域标识，即可将视频上传指定的区域，详见[服务端上传指引](/document/product/266/9759)。
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
Map<String, Object> extraParams = new HashMap<String, Object>();
extraParams.put("storageRegion", "tj");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", extraParams);
System.out.println(response.getFileId());
```

## 接口描述
初始化上传对象 `VodApi`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| secretId   | 云API密钥ID        | String | 是    |
| secretKey | 云API密钥Key | String  | 是    |

上传方法 `VodApi.upload(String videoPath)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| videoPath   |视频路径        | String | 是    |

上传重载方法 `VodApi.upload(String videoPath, String coverPath)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| videoPath   |视频路径        | String | 是    |
| coverPath   |封面路径        | String | 是    |

上传重载方法 `VodApi.upload(String videoPath, String coverPath, String procedure)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| videoPath   |视频路径        | String | 是    |
| coverPath   |封面路径        | String | 是    |
| procedure | 任务流 |  String | 是    |

上传重载方法 `VodApi.upload((String videoPath, String coverPath, Map<String, Object> extraParams)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| videoPath   |视频路径        | String | 是    |
| coverPath   |封面路径        | String | 是    |
| extraParams | 任务流 |  Map | 是    |

extraParams支持下述参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| sourceContext | 用户自定义上下文 |  String | 
| storageRegion | 指定存储地区 |  String | 
| procedure | 任务流 |  String | 

上传结果 `VodUploadCommitResponse`

| 成员变量名称   | 变量说明      | 类型     |
| -------- | --------- | ------ |
| code  | 结果码       | int    |
| message  | 上传失败的错误描述 | String |
| fileId  | 点播视频文件Id  | String |
| video | 视频存储信息    | Object |
| video.url | 视频存储地址    | String |
| video.verify_content | 视频存储校验信息    | String |
| cover | 封面存储信息    | Object |
| cover.url | 封面存储地址    | String |
| cover.verify_content | 封面存储校验信息    | String |

## 错误码列表
调用SDK上传后， 可以利用  `VodUploadCommitResponse` 中的 code 来确认视频上传的情况

| 状态码         | 含义               |
| ----------- | ----------------- |
| 0       | 上传成功 |
| 31001       | 用户请求session_key错误 |
| 31002       | 用户请求中的VOD签名重复     |
| 31003       | 上传文件不存在           |
| 32001       | 服务错误              |