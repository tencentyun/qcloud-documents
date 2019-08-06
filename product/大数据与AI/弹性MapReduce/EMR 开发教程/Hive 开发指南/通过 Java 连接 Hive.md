Hive 中集成了 Thrift 服务。Thrift 是 Facebook 开发的一个软件框架，它用来进行可扩展且跨语言的服务的开发。Hive 的 HiveServer2 就是基于 Thrift 的，所以能让不同的语言如 Java、Python 来调用 Hive 的接口。对于 Java，Hive 提供了 jdbc 驱动，用户可以使用 Java 代码来连接 Hive 并进行一系列操作。
本节将演示如何使用 Java 代码来连接 HiveServer2。
## 1. 开发准备
- 确认您已经开通了腾讯云，并且创建了一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Hive 组件。 
- Hive 等相关软件安装在路径 EMR 云服务器的`/usr/local/service/`路径下。

## 2. 使用 Maven 来创建您的工程
### 查看参数
首先需要登录 EMR 集群中的任意机器，最好是登录到 Master 节点。登录 EMR 的方式请参考 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。这里我们可以选择使用 WebShell 登录。单击对应云服务器机右侧的登录，进入登录界面，用户名默认为 root，密码为创建 EMR 时用户自己输入的密码。输入正确后，即可进入命令行界面。

在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Hive 安装文件夹：

```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/hive/
[hadoop@172 hive]$

```
查看在程序中需要使用的参数：

```
[hadoop@172 hive]$ vim conf/hive-site.xml

<property>
        <name>hive.server2.thrift.bind.host</name>
        <value>$hs2host</value>
</property>
<property>
        <name>hive.server2.thrift.port</name>
        <value>$hs2port</value>
</property>

```
其中 $hs2host 为您的 HiveServer2 的 hostID，$hs2port 为您的 HiveServer2 的端口号。

### 新建一个 Maven 工程
推荐使用 Maven 来管理您的工程。Maven 是一个项目管理工具，能够帮助您方便的管理项目的依赖信息，即它可以通过 pom.xml 文件的配置获取 jar 包，而不用去手动添加。

首先在本地下载并安装 Maven，配置好 Maven 的环境变量，如果您使用 IDE，请在 IDE 中设置好 Maven 相关配置。
在本地 shell 下进入要新建工程的目录，例如`D://mavenWorkplace`中，输入如下命令新建一个 Maven 工程：

```
mvn archetype:generate -DgroupId=$yourgroupID -DartifactId=$yourartifactID -DarchetypeArtifactId=maven-archetype-quickstart
```
其中 $yourgroupID 即为您的包名；$yourartifactID 为您的项目名称；maven-archetype-quickstart 表示创建一个 Maven Java 项目。工程创建过程中需要下载一些文件，请保持网络通畅。
创建成功之后，在`D://mavenWorkplace`目录下就会生成一个名为 $yourartifactID 的工程文件夹。其中的文件结构如下所示：

```
simple
	---pom.xml　　　　 核心配置，项目根下
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
            <groupId>org.apache.hive</groupId>
            <artifactId>hive-jdbc</artifactId>
            <version>2.1.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>2.7.3</version>
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
在 src>mai>Java 下右键新建一个 Java Class，输入您的 Class 名，这里使用 HiveTest.java，在 Class 添加样例代码：

```
import java.sql.*;

/**
 * Created by tencent on 2018/7/6.
*/
public class HiveTest {
    private static String driverName =
            "org.apache.hive.jdbc.HiveDriver";

    public static void main(String[] args)
            throws SQLException {
        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }

        Connection con = DriverManager.getConnection(
                "jdbc:hive2://$hs2host:$hs2port/default", "hadoop", "");
        Statement stmt = con.createStatement();
        String tableName = "HiveTestByJava";
        stmt.execute("drop table if exists " + tableName);
        stmt.execute("create table " + tableName +
                " (key int, value string)");
        System.out.println("Create table success!");
        // show tables
        String sql = "show tables '" + tableName + "'";
        System.out.println("Running: " + sql);
        ResultSet res = stmt.executeQuery(sql);
        if (res.next()) {
            System.out.println(res.getString(1));
        }

        // describe table
        sql = "describe " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(res.getString(1) + "\t" + res.getString(2));
        }

        sql = "insert into " + tableName + " values (42,\"hello\"),(48,\"world\")";
        stmt.execute(sql);

        sql = "select * from " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(String.valueOf(res.getInt(1)) + "\t"
                    + res.getString(2));
        }

        sql = "select count(1) from " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(res.getString(1));
        }
    }
}

```
>!将程序中的参数 $hs2host 和 $hs2port 分别修改为您查到的 HiveServer2 的 hostID 和端口号的值。

整个程序会先连接 HiveServer2 服务，然后在 default 数据库中建立一个名为 HiveTestByJave 的表。然后插入两个元素到该表中，并最后输出整个表的内容。
如果您的 Maven 配置正确并且成功的导入了依赖包，那么整个工程应该没有错误可以直接编译。在本地 shell 下进入工程目录，执行下面的命令对整个工程进行打包：

```
mvn package
```
运行过程中可能还需要下载一些文件，直到出现 build success 表示打包成功。然后您可以在工程目录下的 target 文件夹中看到打好的 jar 包。

## 3. 上传并运行程序
首先需要把压缩好的 jar 包上传到 EMR 集群中，使用 scp 或者 sftp 工具来进行上传。在本地 shell 下运行：

```
scp $localfile root@公网IP地址:/usr/local/service/hive
```
其中，$localfile 是您的本地文件的路径加名称，root 为 CVM 服务器用户名，公网 IP 可以在 EMR 控制台的节点信息中或者在云服务器控制台查看。将打好的 jar 包上传到 EMR 集群的`/usr/local/service/hive`目录下。上传完成后，在 EMR 命令行中即可查看对应文件夹下是否有相应文件。**一定要上传具有依赖的 jar 包**。

登录 EMR 集群切换到 Hadoop 用户并且进入目录`/usr/local/service/hive`。接下来可以执行程序：
```
[hadoop@172 hive]$ yarn jar $package.jar HiveTest
```
其中 $package.jar 为您的 jar 包的路径加名字，HiveTest 为之前的 Java Class 的名字。运行结果如下：

```
Create table success!
Running: show tables 'HiveTestByJava'
hivetestbyjava
Running: describe HiveTestByJava
key	int
value	string
Running: select * from HiveTestByJava
42	hello
48	world
Running: select count(1) from HiveTestByJava
2

```










