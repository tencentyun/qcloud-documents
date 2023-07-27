Flink 擅长处理无界和有界数据集精确的时间控制和状态化使得 Flink 的运行（runtime）能够运行任何处理无界流的应用。有界流则由一些专为固定大小数据集特殊设计的算法和数据结构进行内部处理，产生了出色的性能。
以下针对于在对象存储上的有界或者无界数据集的数据进行演示操作，这里为了更好地观察作业的运行情况使用 yarn-session 模式来提交任务。Flink On Yarn 支持 Session Mode 和 Application Mode 两种形式，具体可参考 [社区文档](https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/deployment/resource-providers/yarn/)。
本教程演示的是提交的任务为 wordcount 任务即统计单词个数，提前需要在集群中上传需要统计的文件。
## 开发准备
1. 由于任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 确认您已开通腾讯云，且已创建一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Flink 组件，并且在**集群>集群信息**页面开启对象存储的授权。
3. 集群购买完成后，可以使用 HDFS 访问对象存储确保其基础功能可用。具体命令如下：
```
[hadoop@10 ~]$ hdfs dfs -ls cosn://$BUCKET_NAME/path
Found 1 items
-rw-rw-rw-   1 hadoop hadoop      27040 2022-10-28 15:08 cosn://$BUCKET_NAME/path/LICENSE
```
其中，$BUCKET_NAME/path 为您的存储桶名及路径。

## 示例
```
# -n 表示申请1个容器，这里指的就是多少个taskmanager
# -tm 表示每个TaskManager的内存大小
# -s 表示每个TaskManager的slots数量
# -d 表示以后台程序方式运行，后面接的session名字
[hadoop@10 ~]$ yarn-session.sh -jm 1024 -tm 1024 -n 1 -s 1 -nm wordcount-example -d
```
```
/usr/local/service/flink/bin/flink run -m yarn-cluster /usr/local/service/flink/examples/batch/WordCount.jar --input cosn://$BUCKET_NAME/path/LICENSE -output cosn://$BUCKET_NAME/path/wdp_test
[hadoop@10 ~]$ hdfs dfs -ls cosn://$BUCKET_NAME/path/wdp_test
-rw-rw-rw-   1 hadoop hadoop       7484 2022-11-04 00:47 cosn://$BUCKET_NAME/path/wdp_test
```


## Maven 工程示例
在本次演示中，不再采用系统自带的演示程序，而是自己建立工程编译打包之后上传到 EMR 集群运行。推荐您使用 Maven 来管理您的工程。Maven 是一个项目管理工具，能够帮助您方便的管理项目的依赖信息，即它可以通过 pom.xml 文件的配置获取 jar 包，而不用去手动添加。
1. 首先 [下载并安装 Maven](https://maven.apache.org/download.cgi)，配置 Maven 的环境变量。如果您使用 IDE，请在 IDE 中设置 Maven 相关配置。
2. 在本地 shell 下进入您想要新建工程的目录，例如 D://mavenWorkplace 中，输入如下命令新建一个 Maven 工程：
```
mvn archetype:generate -DgroupId=$yourgroupID -DartifactId=$yourartifactID -DarchetypeArtifactId=maven-archetype-quickstart
```
其中 yourgroupID 即为您的包名。yourartifactID 为您的项目名称，而 maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。
创建成功后，在 D://mavenWorkplace 目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：
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
<properties>
    <scala.version>2.12</scala.version>
    <flink.version>1.14.3</flink.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-java</artifactId>
        <version>1.14.3</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-streaming-scala_${scala.version}</artifactId>
        <version>${flink.version}</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-clients_${scala.version}</artifactId>
        <version>${flink.version}</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```
>? scala.version 和 flink.version 请根据自身使用 EMR 版本中的组件版本保持一致。

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
其中，是您的本地文件的路径加名称；为服务器用户名；公网可以在控制台的节点信息中或者在云服务器控制台查看；localfile 是您的本地文件的路径加名称；root 为 CVM 服务器用户名；公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看；remotefolder 是您想存放文件的 CVM 服务器路径。上传完成后，在 EMR 命令行中即可查看对应文件夹下是否有相应文件。
需要处理的文件需要事先上传到 COS 中。如果文件在本地则可以通过 [COS 控制台直接上传](https://cloud.tencent.com/document/product/436/13321)。如果文件在 EMR 集群上，可以使用 Hadoop 命令上传。指令如下：
```
[hadoop@10 hadoop]$ hadoop fs -put $testfile cosn://BUCKET_NAME/
```

### 运行样例
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考登录 [Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。
在 EMR 命令行先使用以下指令切换到 Hadoop 用户：
```
[root@172 ~]# su hadoop
[hadoop@172 ~]$ flink  run  -m yarn-cluster -c com.tencent.flink.CosWordcount ./flink-example-1.0-SNAPSHOT.jar cosn://$BUCKET_NAME/test/data.txt cosn://$BUCKET_NAME/test/result
[hadoop@172 ~]$ hdfs dfs -cat cosn://becklong-cos/test/result
(Flink,8)
(Hadoop,3)
(Spark,7)
(Hbase,3)
```





