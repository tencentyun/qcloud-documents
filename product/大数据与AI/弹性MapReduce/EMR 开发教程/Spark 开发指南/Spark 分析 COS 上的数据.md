Spark 要分析 COS 上的数据前提是您购买的 EMR 集群在创建的时候已经勾选支持 COS，如果没有勾选而想使用 COS 请联系腾讯云客服。本教程演示的是 wordcount，请提前准备好数据, 并确保 core-site.xml 在您的应用的 classpath 下。

- 工程代码添加 maven 依赖

  ``` xml
  <dependency>
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-core_2.11</artifactId>
      <version>2.0.2</version>
  </dependency>
  ```

- 打包和编译插件

  ``` xml
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

- 样例代码

  ``` C++
  public class WordCountOnCOS {
    public static void main(String[] args){
      SparkConf sc = new SparkConf().setAppName("spark on cos");
      JavaSparkContext context = new JavaSparkContext(sc);
      JavaRDD<String> lines = context.textFile(args[0]);

      lines.flatMap(x -> Arrays.asList(x.split(" ")).iterator())
        .mapToPair(x -> new Tuple2<String, Integer>(x, 1))
        .reduceByKey((x, y) -> x+y)
        .saveAsTextFile(args[1]);
    }
  }
  ```

- 打包项目(mvn package)并上传到 EMR 集群中(sftp，scp 等文件传输工具)

- 提交任务
  
  <pre>
  park-submit --class me.minusli.learning.spark.WordCountOnCOS --master
  yarn-cluster sparkstreaming-1.0-SNAPSHOT-jar-with-dependencies.jar
  cosn://huadong/logs/yarn/yarn.log cosn://huadong/logs/spark-on-cos-result
  </pre>
