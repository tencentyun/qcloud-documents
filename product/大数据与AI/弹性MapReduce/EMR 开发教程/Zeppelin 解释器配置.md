本文以 Zepplin 0.91 以上版本为例，主要介绍常见 Zeppelin 解析的配置以及验证方法。
## Spark 解析器
#### 配置
```
SPARK_HOME: /usr/local/service/spark
spark.master: yarn
spark.submit.deployMode: cluster
spark.app.name: zeppelin-spark
```
#### 验证
1. 先把 wordcount.txt 文件上传到 emr hdfs 的/tmp 路径下。
2. 通过 core-site.xml 找到 fs.defaultFS 配置项值 hdfs://HDFS45983。
3. 在 notebook 中执行 spark 相关代码。
```
%spark
val data = sc.textFile("hdfs://HDFS45983/tmp/wordcount.txt")
case class WordCount(word: String, count: Integer)
val result = data.flatMap(x => x.split(" ")).map(x => (x, 1)).reduceByKey(_ + _).map(x => WordCount(x._1, x._2))
result.toDF().registerTempTable("result")

%sql 
select * from result
```

## Flink 解析器
#### 配置
```
FLINK_HOME: /usr/local/service/flink

flink.execution.mode: yarn
```
#### 验证
```
%flink
val data = benv.fromElements("hello world", "hello flink", "hello hadoop")
data.flatMap(line => line.split("\\s"))
             .map(w => (w, 1))
             .groupBy(0)
             .sum(1)
             .print()
```

## HBase 解析器
#### 配置
```
hbase.home: /usr/local/service/hbase

hbase.ruby.sources: lib/ruby

zeppelin.hbase.test.mode: false
```
>! 此解析器依赖的 jar 包已集成到集群/usr/local/service/zeppelin/local-repo 路径下，因此不用配置 dependencies，如需已定义 jar 包才需配置dependencies。

#### 验证
```
%hbase
help 'get'

%hbase
list
```

## Livy 解析器
#### 配置
```
zeppelin.livy.url: http://ip:8998
```
#### 验证
```
%livy.spark
sc.version

%livy.pyspark
print "1"

%livy.sparkr
hello <- function( name ) {
    sprintf( "Hello, %s", name );
}
hello("livy")
```

## Kylin 解析器
#### 配置
1. 在 Kylin 控制台页面中新建一个 default 的 Project。
2. 配置 zeppelin 的 kylin interpreter。
```
kylin.api.url: http://ip:16500/kylin/api/query

kylin.api.user: ADMIN

kylin.api.password: KYLIN

kylin.query.project: default
```
#### 验证
```
%kylin(default)

select count(*) from table1
```

## JDBC 解析器
### 1. MySQL 解析器配置
```
default.url: jdbc:mysql://ip:3306

default.user: xxx

default.password: xxx

default.driver: com.mysql.jdbc.Driver
```
>! 此解析器依赖的 jar 包已集成到集群/usr/local/service/zeppelin/local-repo 路径下，因此不用配置 dependencies，如需已定义 jar 包才需配置 dependencies。
>
验证
```
%mysql
show databases

```

### 2. Hive 解析器配置
```
default.url: jdbc:hive2://ip:7001

default.user: hadoop

default.password: 

default.driver: org.apache.hive.jdbc.HiveDriver
```
>! 此解析器依赖的 jar 包已集成到集群/usr/local/service/zeppelin/local-repo 路径下，因此不用配置 dependencies，如需已定义 jar 包才需配置 dependencies。
>
#### 验证
```
%hive
show databases

%hive
use default;
show tables;
```

### 3. Presto 解析器配置
```
default.url: jdbc:presto://ip:9000?user=hadoop

default.user: hadoop

default.password:

default.driver: io.prestosql.jdbc.PrestoDriver
```
>! 此解析器依赖的 jar 包已集成到集群/usr/local/service/zeppelin/local-repo 路径下，因此不用配置 dependencies，如需已定义 jar 包才需配置 dependencies。
>
#### 验证
```
%presto
show catalogs;

%presto
show schemas from hive;

%presto
show tables from hive.default;
```

更多版本及解析器配置请参考 [Zeppelin 官网文档](https://zeppelin.apache.org/docs/0.9.0/interpreter/jdbc.html)。
