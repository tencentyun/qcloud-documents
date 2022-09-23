Apache Zeppelin 是一款基于 Web 的 Notebook 产品，能够交互式数据分析。使用 Zeppelin，您可以使用丰富的预构建语言后端（或解释器）制作交互式的协作文档，例如 Scala(Apache Spark)、Python(Apache Spark)、SparkSQL、 Hive、Shell 等。

## 前提条件
- 已创建集群，并选择 Zeppelin 服务，详情参见 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。
- 在集群的 EMR 安全组中，开启22和30001端口（新建集群默认开启）及必要的内网通信网段，新安全组以 emr-xxxxxxxx_yyyyMMdd 命名，请勿手动修改安全组名称。
- 按需添加所需服务，如，Spark、Flink、HBase、Kylin。

## 登录 Zeppelin
1. 创建集群，选择 Zeppelin 服务，详情参见 [创建 EMR 集群](https://cloud.tencent.com/document/product/589/10981)。
2. 在 [EMR 控制台](https://console.cloud.tencent.com/emr) 左侧的导航栏，选择集群服务。
3. 单击 Zeppelin 所在的卡片，单击 **Web UI 地址**，访问 Web UI 页面。
4. 在 EMR 3.1.0 版本后，设置了默认登录权限，用户名密码为 admin:admin。如需更改密码，可修改配置文件/usr/local/service/zeppelin-0.8.2/conf/shiro.ini 中的 users 和 roles 选项。更多配置说明，可参见 [文档](https://shiro.apache.org/configuration.html#Configuration-INISections)。
5. 在 EMR 2.6.0和 EMR 3.3.0版本中，Zeppelin 登录已集成 Openldap 账户，只能用 Openldap 账户密码登录，新建集群后 Openldap 默认账户是 root 和 hadoop，默认密码是集群密码，且只有 root 账户拥有 zeppelin 管理员权限，有权访问解析器配置页面。

## 使用 spark 功能完成 wordcount
1. 单击页面左侧 **Create new note**，在弹出页面中创建 notebook。
 ![](https://main.qcloudimg.com/raw/c31d7b714f22b1170d9c6799572227a3.png)
2. 配置 spark 对接 EMR 的集群（spark on yarn），修改并保存配置。
![](https://main.qcloudimg.com/raw/3794475f902450a00a86e2bb00dd3c42.png)
3. 进入自己的 notebook。
 ![](https://main.qcloudimg.com/raw/d56fe984a78c0f8f59498d2c24ee5b73.png)
4. 编写 wordcount 程序，并运行如下命令：
```
val data = sc.textFile("cosn://huanan/zeppelin-spark-randomint-test")
case class WordCount(word: String, count: Integer)
val result = data.flatMap(x => x.split(" ")).map(x => (x, 1)).reduceByKey(_ + _).map(x => WordCount(x._1, x._2))
result.toDF().registerTempTable("result")
%sql select * from result
```
![](https://main.qcloudimg.com/raw/8d70fcea7197c81e2d0235cab6d77843.png)
