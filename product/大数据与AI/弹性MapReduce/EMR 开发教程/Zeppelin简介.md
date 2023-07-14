Apache Zeppelin 是一款基于 Web 的 Notebook 产品，能够交互式数据分析。使用 Zeppelin，您可以使用丰富的预构建语言后端（或解释器）制作交互式的协作文档，例如 Scala(Apache Spark)、Python(Apache Spark)、SparkSQL、 Hive、Shell 等。
>? EMR-V3.3.0及以上、EMR-V2.6.0及以上，已默认配置了 flink、hbase、kylin、livy、spark 的 Interpreter，其他版本和组件可参考 [官方文档](https://zeppelin.apache.org/) 根据 Zepplin 版本进行配置。


## 前提条件
- 已创建集群，并选择 Zeppelin 服务，详情参见 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。
- 在集群的 EMR 安全组中，开启22、30001和18000端口（新建集群默认开启22和30001）及必要的内网通信网段，新安全组以 emr-xxxxxxxx_yyyyMMdd 命名，请勿手动修改安全组名称。
- 按需添加所需服务，如，Spark、Flink、HBase、Kylin。

## 登录 Zeppelin
1. 创建集群，选择 Zeppelin 服务，详情参见 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。
2. 在 [EMR 控制台](https://console.cloud.tencent.com/emr) 左侧的导航栏，选择集群服务。
3. 单击 Zeppelin 所在的卡片，单击 **Web UI 地址**，访问 Web UI 页面。
4. 在 EMR-V2.5.0 及以前版本、EMR-V3.2.1 及以前版本，设置了默认登录权限，用户名密码为 admin:admin。如需更改密码，可修改配置文件/usr/local/service/zeppelin-0.8.2/conf/shiro.ini 中的 users 和 roles 选项。更多配置说明，可参见 [文档](https://shiro.apache.org/configuration.html#Configuration-INISections)。
5. 在 EMR-V2.6.0 及以后版本、 EMR-V3.3.0 及以后版本，Zeppelin 登录已集成 Openldap 账户，只能用 Openldap 账户密码登录，新建集群后 Openldap 默认账户是 root 和 hadoop，默认密码是集群密码，且只有 root 账户拥有 zeppelin 管理员权限，有权访问解析器配置页面。

## 使用 spark 功能完成 wordcount
1. 单击页面左侧 **Create new note**，在弹出页面中创建 notebook。
![](https://qcloudimg.tencent-cloud.cn/raw/9bd836f054e89d6e45bbc171f67611fa.png)
2. EMR-V3.3.0 及以上、EMR-V2.6.0 及以上，已默认配置 Spark 对接 EMR 的集群（Spark On Yarn）。
	- 如果您的版本是 EMR-V3.1.0、EMR-V2.5.0、EMR-V2.3.0，请参考 [文档](https://zeppelin.apache.org/docs/0.8.2/interpreter/spark.html) 进行 Spark 解释器配置。
	- 如果您的版本是 EMR-V3.2.1，请参考 [文档](https://zeppelin.apache.org/docs/0.9.0/interpreter/spark.html) 进行 Spark 解释器配置。
3. 进入自己的 notebook。
 ![](https://main.qcloudimg.com/raw/d56fe984a78c0f8f59498d2c24ee5b73.png)
4. 编写 Spark 程序，以下使用 Spark Scala 方式作为示例，其中 %spark 表示执行 Spark Scala 代码：
```
%spark

val df = spark.read.options(Map("inferSchema"->"true","delimiter"->";","header"->"true"))
.csv("file:///usr/local/service/spark/examples/src/main/resources/people.csv")
z.show(df)
df.registerTempTable("people")
```
5. 返回信息结果如图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b43decf5bc87381c7f99db8925ec47f5.png)
