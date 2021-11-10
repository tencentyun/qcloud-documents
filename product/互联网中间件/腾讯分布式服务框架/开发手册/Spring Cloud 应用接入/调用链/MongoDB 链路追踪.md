考虑到 spring-data-mongodb 库的易用性，TSF 目前只对 `spring-boot-starter-data-mongodb` 进行支持，在引用 spring-boot-starter-data-mongodb 时不要指定版本，只需要整个工程依赖 parent pom 即可，示例如下：

```xml
<parent>
	<groupId>com.tencent.tsf</groupId>
	<artifactId>spring-cloud-tsf-dependencies</artifactId>
	<version>tsf的版本号（1.14以后开始支持 MongoDB）</version>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-data-mongodb</artifactId>
	 </dependency>
</parent>
```

`spring-boot-starter-data-mongodb` 的版本即是 parent pom 文件管理的 mongoldb starter 的版本。在代码中具体使用时，引入MongoTemplate，然后使用其方法即可。

- 如果需要制定 MongoDB 连接的 URI，需要满足以下格式：
```shell
mongodb://host[:port1][/[database][?options]] #暂时只支持单节点 MongonDB
```
也可以不用填写，即默认 host 是本机，默认端口27017。

- 如果通过其他方式引入 MongoDB 客户端，例如直接 `new MongoClient(host,port)`，则在 TSF 的链路中将无法查看到相应的信息。
