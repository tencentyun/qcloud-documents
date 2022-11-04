Yanagishima 是一个受欢迎的开源的连接 Presto，Hive，Spark 的 Web 应用程序，具备在线编写 SQL，查询数据，制作报表及下载数据等功能。

本文目标是指导用户如何在 Yanagishima 中集成 DLC-JDBC，以完成查询和分析 DLC 数据。
>? 本文使用的 Yanagishima 版本为tag22.0，其他版本也可按照类似方式集成。

## 增加 DLC JDBC 配置属性
在 Yanagishima 配置文件中增加如下 DLC JDBC 配置属性，配置文件路径一般为`yanagishima-22.0/conf/yanagishima.properties`。
关于 DLC JDBC 参数，以及代码样例的详细说明，可以参考 [DLC 官网文档](https://cloud.tencent.com/document/product/1342/61547)。
```properties
# dlc
hive.datasources=dlc
hive.jdbc.url.dlc=jdbc:dlc:dlc.tencentcloudapi.com?task_type=SQLTask&database_name=<DLC默认数据库名称>&datasource_connection_name=DataLakeCatalog&Region=<DLC所在地域>&data_engine_name=<DLC集群名称>&result_type=Service
hive.jdbc.user.dlc=<腾讯云 API 密钥管理中的 SecretId>
hive.jdbc.password.dlc=<腾讯云 API 密钥管理中的 Secretkey>
hive.max-result-file-byte-size=1073741824
```

## 下载 DLC JDBC 驱动
下载 [DLC JDBC 驱动 jar 包](https://dlc-jdbc-1304028854.cos.ap-beijing.myqcloud.com/dlc-jdbc-2.2.3-jar-with-dependencies.jar)，并且部署到`yanagishima-22.0/lib`目录中。

## 调整 Yanagishima 源码
因 Yanagishima 源码中未预留自定义 jdbc 配置入口，默认只支持 hive、spark jdbc 连接方式，主要的实现类为 yanagishima.service.HiveServiceImpl，所以可以对该类源码进行微调来实现连接 DLC，主要涉及两个方法的修改。
### getHiveQueryResult
在访问 dlc datasource 时，加载 DLC 驱动类。
```java
if("dlc".equals(datasource)){
	Class.forName("com.tencent.cloud.dlc.jdbc.DlcDriver");
} else {
	Class.forName("org.apache.hive.jdbc.HiveDriver");
}
```

### processData
该方法开始处，主要设置了 hive mr 的一些参数配置，在 DLC 中无需设置这些，可以屏蔽掉，代码调整如下。
```java
if(!"dlc".equals(datasource)){
	int timeout = (int) queryMaxRunTime.toMillis() / 1000;
  statement.setQueryTimeout(timeout);
  if (engine.equals(hive.name())) {
    statement.execute("set mapreduce.job.name=" + toJobName(queryId, userName));
    List<String> hiveSetupQueryList = config.getHiveSetupQueryList(datasource);
    for (String hiveSetupQuery : hiveSetupQueryList) {
      statement.execute(hiveSetupQuery);
    }
  }
}
```

## 集成效果
完成上述步骤后，重新编译 Yanagishima 并且部署启动后，可以在 Web UI 中查看 DLC 库表，执行 sql query， 以及查看数据，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bbfb852d8fe61d4b3ea3ed90d8ad16d1.png)
![](https://qcloudimg.tencent-cloud.cn/raw/1dd02515ea6647e250062e6f88e7c35a.png)
