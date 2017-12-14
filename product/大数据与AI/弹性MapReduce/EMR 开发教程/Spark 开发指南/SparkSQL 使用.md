在使用 SparkSQL 之前请登录 EMR 集群的 master 节点并以 Hadoop 身份进入到如下目录：/usr/local/service/spark，通过如下命令您可以进入 SparkSQL 的交互式控制台

<pre>
bin/spark-sql --master yarn --num-executors 64 --executor-memory 2g
</pre>

以上参数可以根据您的实际情况作出修改, 当然您也可以通过 sbin/start-thriftserver.sh 或者 sbin/stop-thriftserver.sh 来启动或者停止一个  SparkSQLthriftserver, 命令行参数使用教程请参考 [社区文档](http://spark.apache.org/docs/latest/sql-programming-guide.html)

通过 API 使用 SparkSQL：

- 添加 maven 依赖  

    ``` XML
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
    ```  
 
    添加 maven 打包插件请参考第一部分

- 样例代码

    ``` c++
    public class Demo {
      public static void main(String[] args){
      SparkSession spark = SparkSession
                            .builder()
                            .appName("Java Spark Hive Example")
                            .enableHiveSupport()
                            .getOrCreate();
      spark.sql("use hivewithhdfs");
      spark.sql("select * from record").write().saveAsTable("sparksql_hive_test");
      }
    }
    ```

    说明：如果要使用到 Hive 的数据表请确保 hive-site.xml 在您的工程的 classpath 下

- 提交执行   

  在提交执行前您需要通过 mvn package 进行打包，然后将编译的 jar 传输到服务器。

    <pre>
    spark-submit --class me.minusli.learning.hive.Demo --master yarn-client sparkstreaming-1.0-SNAPSHOT-jar-with-dependencies.jar
    </pre>
