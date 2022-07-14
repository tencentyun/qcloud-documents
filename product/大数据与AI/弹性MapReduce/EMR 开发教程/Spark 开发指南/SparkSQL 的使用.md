Spark 为结构化数据处理引入了一个称为 Spark SQL 的编程模块。它提供了一个称为 DataFrame 的编程抽象，并且可以充当分布式 SQL 查询引擎。

## 1. 开发准备
确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择了 Spark 组件。
 
## 2. 使用 SparkSQL 交互式控制台
在使用 SparkSQL 之前请登录 EMR 集群的 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入 EMR 命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入目录 `/usr/local/service/spark`：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/spark
```
通过如下命令您可以进入 SparkSQL 的交互式控制台：
```
[hadoop@10spark]$ bin/spark-sql --master yarn --num-executors 64 --executor-memory 2g
```
其中 --master 表示您的 master URL，--num-executors 表示 executor 数量，--executor-memory 表示 executor 的储存容量。以上参数也可以根据您的实际情况作出修改，您也可以通过 `sbin/start-thriftserver.sh` 或者 `sbin/stop-thriftserver.sh` 来启动或者停止一个 SparkSQLthriftserver。

**下面介绍一些 SparkSQL 的基本操作：**
- 新建一个数据库并查看：
```
spark-sql> create database sparksql;
Time taken: 0.907 seconds
spark-sql> show databases;
default
sparksql
test
Time taken: 0.131 seconds, Fetched 5 row(s)
```
- 在新建的数据库中新建一个表，并进行查看：
```
spark-sql> use sparksql;
Time taken: 0.076 seconds
spark-sql> create table sparksql_test(a int,b string);
Time taken: 0.374 seconds
spark-sql> show tables;
sparksql_test	false
Time taken: 0.12 seconds, Fetched 1 row(s)
```
- 向表中插入两行数据并查看：
```
spark-sql> insert into sparksql_test values (42,'hello'),(48,'world');
Time taken: 2.641 seconds
spark-sql> select * from sparksql_test;
42	hello
48	world
Time taken: 0.503 seconds, Fetched 2 row(s)
```

更多命令行参数使用教程请参考 [社区文档](http://spark.apache.org/docs/latest/sql-programming-guide.html)。

## 3. 使用 Maven 创建工程
首先下载并安装 Maven，配置好 Maven 的环境变量，如果您使用 IDE，请在 IDE 中设置好 Maven 相关配置。


### 新建一个 Maven 工程
在命令行下进入您想要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：
```
mvn    archetype:generate    -DgroupId=$yourgroupID    -DartifactId=$yourartifactID
-DarchetypeArtifactId=maven-archetype-quickstart
```
其中 $yourgroupID 即为您的包名。$yourartifactID 为您的项目名称， maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。
创建成功之后，在`D://mavenWorkplace`目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：
```
simple
　　　---pom.xml　　　　核心配置，项目根下
　　　---src
　　　　　---main　　　　　　
　　　　　　　---java　　　　 Java 源码目录
　　      　---resources　   Java 配置文件目录
　　　　---test
　　　　　　---java　　　　测试源码目录
　　　　　　---resources　  测试配置目录
```
其中我们主要关心 pom.xml 文件和 main 下的 Java 文件夹。pom.xml 文件主要用于依赖和打包配置， Java 文件夹下放置您的源代码。

### 添加 Hadoop 依赖和样例代码
首先在 pom.xml 文件中添加 Maven 依赖：
```
<dependencies>
　　　    <dependency>
　　　        <groupId>org.apache.spark</groupId>
　　　        <artifactId>spark-core_2.11</artifactId>
　　　        <version>2.0.2</version>
　　　    </dependency>
　　　    <!--spark sql-->
　　　    <dependency>
　　　        <groupId>org.apache.spark</groupId>
　　　        <artifactId>spark-sql_2.11</artifactId>
　　　        <version>2.0.2</version>
　　　    </dependency>
</dependencies>
```
继续在 pom.xml 文件中添加打包和编译插件：
```
<build>
<plugins>
  <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
      <source>1.8</source>
      <target>1.8</target>
      <encoding>utf-8</encoding>
    </configuration>
  </plugin>
  <plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <configuration>
      <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
      </descriptorRefs>
    </configuration>
    <executions>
      <execution>
        <id>make-assembly</id>
        <phase>package</phase>
        <goals>
          <goal>single</goal>
        </goals>
      </execution>
    </executions>
  </plugin>
</plugins>
</build>
```
完整的 pom.xml 文件如下所示：
```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>$yourgroupID </groupId>
    <artifactId>$yourartifactID </artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.0.2</version>
        </dependency>
        <!--spark sql-->
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>2.0.2</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>utf-8</encoding>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```
>!修改其中的 $yourgroupID 和 $yourartifactID 为您自己的设置。

接下来添加样例代码，在 main>Java 文件夹下新建一个 Java Class 取名为 Demo.java，并将以下代码加入其中：
```
import org.apache.spark.rdd.RDD;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

/**
 * Created by tencent on 2018/6/28.
 */
public class Demo {
    public static void main(String[] args){
        SparkSession spark = SparkSession
                .builder()
                .appName("Java Spark Hive Example")
                .enableHiveSupport()
                .getOrCreate();

        Dataset<Row> df = spark.read().json(args[0]);

        RDD<Row> test = df.rdd();
        
        test.saveAsTextFile(args[1]);
    }
}
```

### 编译代码并打包上传
使用本地命令行进入工程目录，执行以下指令对工程进行编译打包：
```
mvn package
```
在显示 build success 表示操作成功，在工程目录下的 target 文件夹中能够看到打包好的文件。
使用 scp 或者 sftp 工具把打包好的文件上传到 EMR 集群。在本地命令行模式下运行：
```
scp $localfile root@公网IP地址:$remotefolder
```
其中，$localfile 是您的本地文件的路径加名称，root 为 CVM 服务器用户名，公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看。$remotefolder 是您想存放文件的 CVM 服务器路径。上传完成后，在 EMR 集群命令行中即可查看对应文件夹下是否有相应文件。

## 4. 准备数据并运行样例
使用 sparkSQL 来操作存放在 HDFS 上的数据。首先将数据上传到 HDFS 中，这里我们使用自带的文件 people.json，存放在路径 `/usr/local/service/spark/examples/src/main/resources/` 下，使用如下指令把该文件上传到 HDFS 中：
```
[hadoop@10 hadoop]$ hadoop fs -put /usr/local/service/spark/examples/src/main/resources/people.json 
/user/hadoop
```
测试文件用户也可以另选，这里 `/user/hadoop/` 是 HDFS 下的文件夹，如果没有用户可以自己创建。

**执行样例**，首先请登录 EMR 集群的 master 节点，并且切换到 Hadoop 用户如使用 SparkSQL 交互式控制台中所示，使用以下命令执行样例：
```
[hadoop@10spark]$ bin/spark-submit --class Demo --master yarn-client $yourjarpackage /  
/user/hadoop/people.json  /user/hadoop/$output
```
其中 --class 参数表示要执行的入口类，在本例子中即为 Demo，即在添加 Hadoop 依赖和样例代码中创建的 Java Class 的名字，--master 为集群主要的 URL，$yourjarpackage 是您打包后的包名，$output 为结果输出文件夹（**$output 为一个未创建的文件夹，如果执行指令前该文件夹已经存在，会导致程序运行失败**）。

成功运行后，可以在 `/user/hadoop/$output` 查看结果：
```
[hadoop@172 spark]$ hadoop fs -cat /user/hadoop/$output/part-00000
[null,Michael]
[30,Andy]
[19,Justin]
```
spark-submit 的更多参数，在命令行输入以下命令进行查看，或者请参考 [官方文档](https://spark.apache.org/docs/latest/submitting-applications.html)。
```
[hadoop@10spark]$ spark-submit -h
```
