Spark 作为 Apache 高级的开源项目，是一个快速、通用的大规模数据处理引擎，与 Hadoop 的 MapReduce 计算框架类似，但是相对于 MapReduce，Spark 凭借其可伸缩、基于内存计算等特点以及可以直接读写 Hadoop 上任何格式数据的优势，进行批处理时更加高效，并有更低的延迟。实际上，Spark 已经成为轻量级大数据快速处理的统一平台，各种不同的应用，如实时流处理、机器学习、交互式查询等，都可以通过 Spark 建立在不同的存储和运行系统上。

Spark 是基于内存计算的大数据并行计算框架。Spark 基于内存计算，提高了在大数据环境下数据处理的实时性，同时保证了高容错性和高可伸缩性，允许用户将 Spark 部署在大量廉价硬件之上，形成集群。

本教程演示的是提交的任务为 wordcount 任务即统计单词个数，提前需要在集群中上传需要统计的文件。

## 1. 开发准备
- 因为任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建一个存储桶（Bucket）](https://cloud.tencent.com/document/product/436/13309)。
- 确认您已开通腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Spark 组件，并且在【实例信息】>【基础配置】中开启对象存储的授权。

## 2. 使用 Maven 创建工程
在本次演示中，不再采用系统自带的演示程序，而是自己建立工程编译打包之后上传到 EMR 集群运行。推荐您使用 Maven 来管理您的工程。Maven 是一个项目管理工具，能够帮助您方便的管理项目的依赖信息，即它可以通过 pom.xml 文件的配置获取 jar 包，而不用去手动添加。

首先下载并安装 Maven，配置 Maven 的环境变量。如果您使用 IDE，请在 IDE 中设置 Maven 相关配置。

### 新建一个 Maven 工程

在本地 shell 下进入您想要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：
```
mvn archetype:generate -DgroupId=$yourgroupID -DartifactId=$yourartifactID -DarchetypeArtifactId=maven-archetype-quickstart
```
其中 $yourgroupID 即为您的包名。$yourartifactID 为您的项目名称，而 maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。

创建成功后，在`D://mavenWorkplace`目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：
```
simple
	---pom.xml　　　　核心配置，项目根下
	---src
		---main　　　　　　
			---java　　　　  Java 源码目录
			---resources　  Java 配置文件目录
		---test
			 ---java　　　　  测试源码目录
			 ---resources　  测试配置目录
```
其中我们主要关心 pom.xml 文件和 main 下的 Java 文件夹。pom.xml 文件主要用于依赖和打包配置，Java 文件夹下放置您的源代码。

首先在 pom.xml 中添加 Maven 依赖：
```
<dependencies>
    <dependency>
        <groupId>org.apache.spark</groupId>
        <artifactId>spark-core_2.11</artifactId>
        <version>2.0.2</version>
    </dependency>
</dependencies>
```
继续在 pom.xml 中添加打包和编译插件：
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
在 src>main>Java 下右键新建一个Java Class，输入您的 Class 名，这里使用 WordCountOnCos，在 Class 添加样例代码：
```
import java.util.Arrays;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

/**
 * Created by tencent on 2018/6/28.
 */
public class WordCountOnCos {
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
如果您的 Maven 配置正确并且成功的导入了依赖包，那么整个工程应该没有错误可以直接编译。在本地命令行模式下进入工程目录，执行下面的命令对整个工程进行打包：
```
mvn package
```
运行过程中可能还需要下载一些文件，直到出现 build success 表示打包成功。然后您可以在工程目录下的 target 文件夹中看到打好的 jar 包。

### 数据准备
首先需要把压缩好的 jar 包上传到 EMR 集群中，使用 scp 或者 sftp 工具来进行上传。在本地命令行模式下运行：
```
scp $localfile root@公网IP地址:$remotefolder
```
其中，$localfile 是您的本地文件的路径加名称；root 为 CVM 服务器用户名；公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看；$remotefolder 是您想存放文件的 CVM 服务器路径。上传完成后，在 EMR 命令行中即可查看对应文件夹下是否有相应文件。

需要处理的文件需要事先上传到 COS 中。如果文件在本地则可以通过 [COS 控制台直接上传](https://cloud.tencent.com/document/product/436/13321)。如果文件在 EMR 集群上，可以使用 Hadoop 命令上传。指令如下：
```
[hadoop@10 hadoop]$ hadoop fs -put $testfile cosn://$bucketname/
```
其中 $testfile 为要统计的文件的完整路径加名字，$bucketname 为您的存储桶名。上传完成后可以在 COS 控制台中查看文件是否已经在 COS 中。

### 运行样例
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户：
```
[root@172 ~]# su hadoop
```
然后进入您存放 jar 包的文件夹下，执行以下指令：
```
[hadoop@10spark]$ spark-submit    --class    $WordCountOnCOS    --master 
yarn-cluster $packagename.jar cosn:// $bucketname /$testfile cosn:// $bucketname 
/output
```
其中 $WordCountOnCOS 为您的 Java Class 名字，$packagename 为您新建 Maven 工程中生成的 jar 包名字，$bucketname 为您的存储桶名和路径，$testfile 为您要统计的文件名。最后输出的文件在 output 这个文件夹中，**这个文件夹事先不能被创建，不然运行会失败**。

运行成功后，在指定的存储桶和文件夹下可以看到 wordcount 的结果。
```
[hadoop@172 /]$ hadoop fs -ls cosn:// $bucketname /output
Found 3 items
-rw-rw-rw- 1 hadoop Hadoop  0 2018-06-28 19:20 cosn:// $bucketname /output/_SUCCESS
-rw-rw-rw- 1 hadoop Hadoop 681 2018-06-28 19:20 cosn:// $bucketname /output/part-00000
-rw-rw-rw- 1 hadoop Hadoop 893 2018-06-28 19:20 cosn:// $bucketname /output/part-00001

[hadoop@172 demo]$ hadoop fs -cat cosn://$bucketname/output/part-00000
18/07/05 17:35:01 INFO cosnative.NativeCosFileSystem: Opening 'cosn:// $bucketname/output/part-00000' for reading
(under,1)
(this,3)
(distribution,2)
(Technology,1)
(country,1)
(is,1)
(Jetty,1)
(currently,1)
(permitted.,1)
(Security,1)
(have,1)
(check,1)
```
