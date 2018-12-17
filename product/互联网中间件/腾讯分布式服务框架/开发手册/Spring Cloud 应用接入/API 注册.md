TSF 框架在微服务注册时，会自动收集并注册微服务提供的 API 接口，用户可通过 TSF 控制台实时掌握当前微服务提供的 API 情况。API 注册功能基于 [OpenApi Specification 3.0](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) 规范注册 API 元数据信息。 用户在查看 API 接口的同时，可查看到 API 出入参数据结构信息。


## 准备工作
开始实践 API 注册功能前，请确保已完成了 [SDK 下载](https://cloud.tencent.com/document/product/649/20231)。


## 添加依赖
在 pom.xml 中添加以下代码：
```xml
<dependency>
    <groupId>com.tencent.tsf</groupId>
    <artifactId>spring-cloud-tsf-swagger</artifactId> 
    <version>1.1.2-RELEASE</version> <!-- 调整为 SDK 最新版本号 -->
    <scope>compile</scope>
</dependency>
```
添加依赖包后，TSF API 注册功能即生效。

## 配置选项
API 注册功能，基于 Swagger 原生规范来实现。提供多个配置来适配 Swagger 不同配置应用场景，可用配置如下表所示：

|配置项|类型|必填|默认值|说明|
|:-----|:-------|:----|:------|:------|
|tsf.swagger.enabled|Boolean|否|true|是否开启 TSF API 注册功能|
|tsf.swagger.basePackage|String|否|ApplicationMainClass 所在包路径|注册 API 的扫描包路径。 推荐将 ApplicationMainClass 写在外层 Package|
|tsf.swagger.excludePath|String|否|（空）|排除扫描的包路径|
|tsf.swagger.group|String|否|default|swagger docket 分组|

