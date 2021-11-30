HBase 是一个高可靠性、高性能、面向列、可伸缩的分布式存储系统，是 Google BigTable 的开源实现。HBase 利用 Hadoop HDFS 作为其文件存储系统；Hadoop MapReduce 来处理 HBase 中的海量数据；Zookeeper 来做协同服务。

Hbase 主要由 Zookeeper、HMaster 和 HRegionServer 组成。其中：
- ZooKeeper 可避免 Hmaster 的单点故障，其 Master 选举机制可保证一个 Master 提供服务。
- Hmaster 管理用户对表的增删改查操作，管理 HRegionServer 的负载均衡。并可调整 Region 的分布，在 HRegionServer 退出时迁移其内的 HRegion 到其他 HRegionServer 上。
- HRegionServer 是 Hbase 中最核心的模块，其主要负责响应用户的 I/O 请求，向 HDFS 文件系统中读写数据。HRegionServer 内部管理了一系列 HRegion 对象，每个 HRegion 对应一个 Region，HRegion 中由多个 Store 组成。每个 Store 对应了 Column Family 的存储。

本开发指南将从技术人员的角度帮助用户使用 EMR 集群开发。考虑用户数据安全，EMR 中当前只支持 VPC 网络访问。

## 1. 开发准备
确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择了 Hbase 组件和 Zookeeper 组件。

## 2. 使用 Hbase Shell
在使用 Hbase Shell 之前请登录 EMR 集群的 Master 节点。登录 EMR 的方式可参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里可以选择使用 WebShell 登录。单击对应云服务器右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入 EMR 命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入目录 `/usr/local/service/hbase`：
```
[root@172 ~]# su hadoop
[hadoop@10root]$ cd /usr/local/service/hbase
```
通过如下命令您可以进入 Hbase Shell ：
```
[hadoop@10hbase]$ bin/hbase shell
```
在 hbase shell 下输入 help 可以查看基本的使用信息和示例的指令。接下来我们使用以下指令建立一个新表：
```
hbase(main):001:0> create 'test', 'cf'
```
表格建立后，可以使用 `list` 指令来查看您建立的表是否已经存在。
```
hbase(main):002:0> list 'test'
TABLE                                                                             
test                                                                               
1 row(s) in 0.0030 seconds

=> ["test"]
```
使用`put`指令来为您创建的表加入元素：
```
hbase(main):003:0> put 'test', 'row1', 'cf:a', 'value1'
0 row(s) in 0.0850 seconds

hbase(main):004:0> put 'test', 'row2', 'cf:b', 'value2'
0 row(s) in 0.0110 seconds

hbase(main):005:0> put 'test', 'row3', 'cf:c', 'value3'
0 row(s) in 0.0100 seconds
```
我们在创建的表中加入了三个值，第一次在“row1”行“cf:a”列插入了一个值“value1”，以此类推。

使用`scan`指令来遍历整个表：
```
hbase(main):006:0> scan 'test'
ROW  COLUMN+CELL                                                                   
row1   column=cf:a, timestamp=1530276759697, value=value1                         
row2   column=cf:b, timestamp=1530276777806, value=value2                         
row3   column=cf:c, timestamp=1530276792839, value=value3                         
3 row(s) in 0.2110 seconds
```
使用`get`指令来取得表中指定行的值：
```
hbase(main):007:0> get 'test', 'row1'
COLUMN  CELL                                                                       
 cf:a       timestamp=1530276759697, value=value                                   
1 row(s) in 0.0790 seconds
```
使用`drop`指令来删除一个表，在删除表之前需要先使用`disable`指令来禁用一个表：
```
hbase(main):010:0> disable 'test'
hbase(main):011:0> drop 'test'
```
最后可以使用`quit`指令来关闭 hbase shell。

更多的 Hbase shell 指令请查看 [官方文档](http://hbase.apache.org/book.html)。

## 3. 通过 API 使用 Hbase
首先 [下载并安装 Maven](http://maven.apache.org/download.cgi)，配置 Maven 的环境变量，如果您使用 IDE，请在 IDE 中设置 Maven 相关配置。

### 新建一个 Maven 工程
在命令行下进入您想要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：
```
mvn      archetype:generate      -DgroupId=$yourgroupID       -DartifactId=$yourartifactID 
-DarchetypeArtifactId=maven-archetype-quickstart
```
其中 $yourgroupID 即为您的包名。$yourartifactID 为您的项目名称，而 maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。

创建成功后，在 `D://mavenWorkplace` 目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：
```
simple
　　　---pom.xml　　　　核心配置，项目根下
　　　---src
　　　　　---main　　　　　　
　　　　　　　---java　　　　Java 源码目录
　　      　---resources　  Java 配置文件目录
　　　　---test
　　　　　　---java　　　　测试源码目录
　　　　　　---resources　  测试配置目录
```
其中我们主要关心 pom.xml 文件和 main 下的 Java 文件夹。pom.xml 文件主要用于依赖和打包配置，Java 文件夹下放置您的源代码。

### 添加 Hadoop 依赖和样例代码
首先在 pom.xml 文件中添加 Maven 依赖：
```
<dependencies>
	 <dependency>
		 <groupId>org.apache.hbase</groupId>
		 <artifactId>hbase-client</artifactId>
		 <version>1.2.4</version>
	</dependency>
</dependencies>
```
然后在 pom.xml 文件中添加打包和编译插件：
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
在添加样例代码之前，需要用户获取 Hbase 集群的 zookeeper 地址。登录 EMR 任意一台 Master 节点或者 Core 节点，进入 `/usr/local/service/hbase/conf` 目录，查看 hbase-site.xml 的 hbase.zookeeper.quorum 配置获得 zookeeper 的 IP 地址 $quorum，hbase.zookeeper.property.clientPort 配置获得 zookeeper 的端口号 $clientPort。

接下来添加样例代码，在 main>java 文件夹下新建一个 Java Class 取名为 PutExample.java，并将以下代码加入其中：
```
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.*;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.hbase.io.compress.Compression.Algorithm;

import java.io.IOException;

/**
 * Created by tencent on 2018/6/30.
 */
public class PutExample {
    public static void main(String[] args) throws IOException {
        Configuration conf = HBaseConfiguration.create();
        conf.set("hbase.zookeeper.quorum","$quorum");
        conf.set("hbase.zookeeper.property.clientPort","$clientPort");

        Connection connection = ConnectionFactory.createConnection(conf);
        Admin admin = connection.getAdmin();

        HTableDescriptor table = new HTableDescriptor(TableName.valueOf("test1"));
        table.addFamily(new HColumnDescriptor("cf").setCompressionType(Algorithm.NONE));

        System.out.print("Creating table. ");
        if (admin.tableExists(table.getTableName())) {
            admin.disableTable(table.getTableName());
            admin.deleteTable(table.getTableName());
        }
        admin.createTable(table);

        Table table1 = connection.getTable(TableName.valueOf("test1"));
        Put put1 = new Put(Bytes.toBytes("row1"));
        put1.addColumn(Bytes.toBytes("cf"), Bytes.toBytes("a"),
                Bytes.toBytes("value1"));
        table1.put(put1);
        Put put2 = new Put(Bytes.toBytes("row2"));
        put2.addColumn(Bytes.toBytes("cf"), Bytes.toBytes("b"),
                Bytes.toBytes("value2"));
        table1.put(put2);
        Put put3 = new Put(Bytes.toBytes("row3"));
        put3.addColumn(Bytes.toBytes("cf"), Bytes.toBytes("c"),
                Bytes.toBytes("value3"));
        table1.put(put3);

        System.out.println(" Done.");
    }
}
```

### 编译代码并打包上传
使用本地命令行进入工程目录，执行以下指令对工程进行编译打包：
```
mvn package
```
显示 build success 表示操作成功，在工程目录下的 target 文件夹中能够看到打包好的文件。

使用 scp 或者 sftp 工具把打包好的文件上传到 EMR 集群。**这里一定要上传把依赖一起进行打包的 jar 包**。在本地命令行模式下运行：
```
scp $localfile root@公网IP地址:$remotefolder
```
其中，$localfile 是您的本地文件的路径加名称，root 为 CVM 服务器用户名，公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看。$remotefolder 是您想存放文件的 CVM 服务器路径。上传完成后，在 EMR 集群命令行中即可查看对应文件夹下是否有相应文件。

## 4. 运行样例
登录 EMR 集群的 Master 节点，并且切换到 hadoop 用户。使用如下命令执行样例：
```
[hadoop@10 hadoop]$ java –jar $package.jar
```
在控制台输出“Done”后，说明所有的操作已完成。可切换到 hbase shell 中使用`list`命令来查看使用 API 创建的 Hbase 表是否成功。如果成功可使用`scan`命令来查看表的具体内容。
```
[hadoop@10hbase]$ bin/hbase shell
hbase(main):002:0> list 'test1'
TABLE                                                                                           
Test1                                                                                           
1 row(s) in 0.0030 seconds

=> ["test1"]
hbase(main):006:0> scan 'test1'
ROW  COLUMN+CELL                                                                                 
row1   column=cf:a, timestamp=1530276759697, value=value1                                       
row2   column=cf:b, timestamp=1530276777806, value=value2                                       
row3   column=cf:c, timestamp=1530276792839, value=value3                                       
3 row(s) in 0.2110 seconds
```

更多的 API 使用说明请参见 [官方文档](http://hbase.apache.org/book.html)。
