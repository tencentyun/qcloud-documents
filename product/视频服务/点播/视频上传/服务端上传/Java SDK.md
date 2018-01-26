## 简介

用于服务端上传的Java SDK，可向腾讯云点播系统上传视频和封面文件。

## 集成方式

### Maven依赖引入

在项目的pom.xml文件添加点播SDK依赖即可：

```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>1.1.0</version>
</dependency>
```

### jar包导入

如果项目没有采用Maven的方式进行依赖管理，可采用下述方式，下载各个所需的jar包，导入项目即可：

| jar文件         | 说明    |
| ------------ | ------------ | 
| vod_api-1.1.0.jar | 点播SDK |
| jackson-annotations-2.8.0.jar,jackson-core-2.8.5.jar,jackson-databind-2.8.5.jar       | 一组优秀的开源json库 |
| cos_api-5.1.9.jar            | 腾讯云对象存储服务（COS）SDK                          |
| qcloud-java-sdk-2.0.1.jar             | 腾讯云API SDK                        |
| commons-codec-1.10.jar,commons-logging-1.2.jar,log4j-1.2.17.jar,slf4j-api-1.7.21.jar,slf4j-log4j12-1.7.21.jar           | 一组优秀的开源日志库    |
| httpclient-4.5.3.jar,httpcore-4.4.6.jar,httpmime-4.5.2.jar | 一组优秀的开源http处理库                            |
| joda-time-2.9.6.jar | 一款优秀的开源时间处理库                            |

为了提高开发效率，已将所需jar包打包好了，[点击下载](https://github.com/tencentyun/vod-java-sdk/raw/master/packages/vod-sdk-jar.zip)。

## 上传步骤

###  第一步：初始化VodApi
使用云API密钥初始化VodApi实例：
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
```

### 第二步：调用upload方法进行上传

在SDK中提供几种upload方法的重载，针对不同的上传场景：

#### 上传视频
方法签名

```
public VodUploadCommitResponse upload(String videoPath) throws Exception
```

方法参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| videoPath | 视频路径 |  String | 

方法返回值
**VodUploadCommitResponse**

|  名称         | 描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| fileId | 视频文件ID |  String | 
| video | 视频相关信息 |  UrlModel | 
| cover | 封面相关信息 |  UrlModel | 

**UrlModel**

|  名称         | 描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| url | 对应访问Url |  String | 
| verify_content | 校验文本 |  String | 

示例
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv");
System.out.println(response.getFileId());
```

#### 上传视频附带封面
方法签名
```
public VodUploadCommitResponse upload(String videoPath, String coverPath) throws Exception
```

方法参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| videoPath | 视频路径 |  String | 
| coverPath | 封面路径 |  String | 

方法返回值
**同上**

示例
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg");
System.out.println(response.getFileId());
```

#### 上传视频指定任务流
方法签名
```
public VodUploadCommitResponse upload(String videoPath, String coverPath, String procedure) throws Exception
```

方法参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| videoPath | 视频路径 |  String | 
| coverPath | 封面路径 |  String | 
| procedure | 任务流 |  String | 

方法返回值
**同上**

示例
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", "QCVB_SimpleProcessFile(1, 1)");
System.out.println(response.getFileId());
```

#### 上传视频附带其他参数
方法签名
```
public VodUploadCommitResponse upload(String videoPath, String coverPath, Map<String, Object> extraParams) throws Exception
```

方法参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| videoPath | 视频路径 |  String | 
| coverPath | 封面路径 |  String | 
| extraParams | 任务流 |  Map | 

extraParams支持下述参数

| 参数名称         | 参数描述    | 类型 |
| ------------ | ------------ |  ------------ | 
| sourceContext | 用户自定义上下文 |  String | 
| storageRegion | 指定存储地区 |  String | 
| procedure | 任务流 |  String | 


方法返回值
**同上**

上传到指定区域示例
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
Map<String, Object> extraParams = new HashMap<String, Object>();
extraParams.put("storageRegion", "tj");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", extraParams);
System.out.println(response.getFileId());
```

## 错误码列表

| 错误码         | 说明                |
| ----------- | ----------------- |
| 31001       | 用户请求session_key错误 |
| 31002       | 用户请求中的VOD签名重复     |
| 31003       | 上传文件不存在           |
| 32001       | 服务错误              |