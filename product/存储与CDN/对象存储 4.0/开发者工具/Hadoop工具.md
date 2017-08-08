## 功能说明
Hadoop cosn 插件实现了以腾讯云 COS 作为底层存储文件系统运行上层计算任务的功能，使用 Hadoop 大数据处理引擎，如 MapReduce，Hive、Spark、Tez 等，可以处理存储在腾讯云对象存储 COS 上的数据。  

## 使用限制
只适用于 COS V4 版本

## 使用环境
### 系统环境
Linux 或 Windows 系统

### 软件依赖
Hadoop-2.7.2 及以上版本

#### 安装及配置
- **Linux （以 CentOS 为例）：**
 1. 必须具有 JavaTM1.5.x 以上版本，SSH 必须安装并且保证 sshd 一直运行，以便用 Hadoop 脚本管理远端 Hadoop 守护进程。
 2. 下载：为了获取 Hadoop 的发行版，从  [Apache 官网](http://hadoop.apache.org/core/releases.html) 下载最新的稳定发行版。
 3. 运行 Hadoop 集群的准备工作：解压所下载的 Hadoop 发行版。编辑 conf/hadoop-env.sh 文件，至少需要将 JAVA_HOME 设置为 Java 安装根路径。
 4. 输入`$ bin/hadoop` ，将会显示 Hadoop 脚本的使用文档。
 5. 您可以通过选择单机模式、伪分布式模式和完全分布式模式中的一种启动 Hadoop 集群。

详细过程请参考 Apache 官网 [Hadoop 快速入门](https://hadoop.apache.org/docs/r1.0.4/cn/quickstart.html)。

- **Windows：**
 1. 到 [Apache 官网](http://hadoop.apache.org/releases.html) 选择 2.7.3 版本的 tar.gz 包下载。
 2. 确保操作系统是 64 位，已安装 `.netframework`（一般都自带）。
 3. 配置 Java 环境，请参考 [本地同步工具](https://cloud.tencent.com/document/product/436/7133) 中的配置方法。
 4. 下载 Windows 下运行的链接库，点击 [下载地址](http://download.csdn.NET/detail/kokjuis/9706480) 下载。
 5. 解压下载好的 hadoop-2.7.3.tar.gz  到某个盘下，注意路径里不要带空格，否则可能会无法正确识别。
 6. 解压 hadooponwindows-master.zip，直接覆盖到 hadoop-2.7.3 根目录。
 7. 配置 Hadoop 环境变量（与配置 Java 类似），创建 HADOOP_HOME：
![Hadoop工具1](//mc.qcloudimg.com/static/img/68dce2c58c989fe5de2e774f506731d9/image.png)
   另外在 Path 下添加 `%HADOOP_HOME%\bin`。
 8. 到 Hadoop 根目录，新建 data 文件夹，然后在 data 下分别创建 datanode、namenode 两个文件夹。
 9. 用记事本打开 `\hadoop-2.7.3\etc\hadoop\hadoop-env.cmd`文件，修改 JAVA_HOME 为你自己 JDK 路径。
>   <font color="#0000cc">**注意：** </font>
	 如果你的 JDK 安装在 Program Files 目录下，名称建议用 \PROGRA~1\Java ，否则空格可能会识别失败。<br>
 10. 最后，点击命令提示符（管理员）运行命令提示符，切换到 Hadoop 的安装目录。进行以下操作：
     1）切换到 `etc/hadoop` 目录，运行`hadoop-env.cmd`；
  2）格式化 HDFS 文件系统，切换到 bin 目录然后执行命令：`hdfs namenode -format`；
3）输入：`hadoop version`，可以查看版本：
![Hadoop工具2](//mc.qcloudimg.com/static/img/4830e7422665394160bda8145ef39608/image.png)
 11. 启动：切换到 sbin 目录 执行：`start-dfs.cmd` 。

## 使用方法
### 安装 Maven
- **Linux ：**
```
sudo apt-get install maven
```
- **Windows：**
下载链接：[Maven](http://maven.apache.org/download.html)
安装与配置请参考：[Windows 环境下 Maven 安装与环境变量配置](http://www.cnblogs.com/liuhongfeng/p/5057827.html) 

### 获取 cos-java-sdk
下载地址：[cos-java-sdk](https://github.com/tencentyun/cos-java-sdk-hadoop-v4)

进入存放路径，运行以下命令进行编译，获取 target 目录下的 cos_api-4.2.jar：
```
mvn clean package -Dmaven.test.skip=true
```
### 获取 hadoop-cos 插件
下载地址：[hadoop-cos 插件](https://github.com/tencentyun/hadoop-cosn-v4)

因为 cosn 依赖 SDK，请将上一步编译的 cos_api-4.2.jar 拷贝到 `src/main/resources` 下，然后运行以下命令进行编译，获取 target 目录下的 hadoop-cos-2.7.2.jar：
```
mvn clean package -Dmaven.test.skip=true
```
### 插件安装方法
#### 修改 hadoop_env.sh
在 `$HADOOP_HOME/etc/hadoop`目录下，进入 hadoop_env.sh，增加如下内容，将 cosn 相关 jar 包加入 Hadoop 环境变量：
```
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```
将获取的 cos_api-4.2.jar 和 hadoop-cos-2.7.2.jar 拷贝到 `$HADOOP_HOME/share/hadoop/tools/lib`下，同时将本地 `Maven/maven-Repository/org/json/json/20140107`目录下的 json-20140107.jar 和 `Maven/maven-Repository/org/apache/httpcomponents/httpmime/4.2.5`目录下的 httpmime-4.2.5.jar 拷贝到该目录。

#### 修改配置文件使用插件
修改 $HADOOP_HOME/etc/hadoop/core-site.xml，增加 COS 相关用户和实现类信息，例如：
```
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/data/rabbitliu/work/hadoop/hadoop_test</value>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property> 
        <name>dfs.name.dir</name>           
        <value>/data/rabbitliu/work/hadoop/hadoop_test/name</value> 
    </property>
    <property> 
        <name>fs.cos.userinfo.appid</name>           
        <value>1252448703</value> 
    </property>
    <property> 
        <name>fs.cos.userinfo.secretId</name>           
        <value>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</value> 
    </property>
    <property> 
        <name>fs.cos.userinfo.secretKey</name>           
        <value>xxxxxxxxxxxxxxxxxxxxxxxx</value> 
    </property>
    <property>
        <name>fs.cosn.impl</name>
        <value>org.apache.hadoop.fs.cosnative.NativeCosFileSystem</value>
    </property>
    <property>
        <name>fs.cos.buffer.dir</name>
        <value>/data/rabbitliu/work/hadoop/hadoop_test/cos_buf</value>
    </property>
    <property>
        <name>fs.cos.userinfo.region</name>
        <value>tj</value>
    </property>
</configuration>
```

> <font color="#0000cc">**注意：** </font>
配置文件中含有 COS 的几个属性：
- fs.cos.userinfo.appid 属性： 填写您使用的 腾讯云账户的 APPID。可通过 [控制台-账号信息](https://console.qcloud.com/developer) 查看。
- fs.cos.userinfo.secretId/secretKey 属性：填写您账户的API 密钥信息。可通过 [云 API 密钥 控制台](https://console.qcloud.com/capi) 查看。
- fs.cosn.impl 为 cosn 的实现类，固定为 org.apache.hadoop.fs.cosnative.NativeCosFileSystem。
- fs.cos.buffer.dir 请设置一个实际存在的目录，运行过程中产生的临时文件会暂时放于此处。
- fs.cos.userinfo.region 请填写你的地域信息，tj(天津)，sh(上海)，gz(广州)。请参考 [可用地域](https://www.qcloud.com/document/product/436/6224)。

### 使用软件（以 Linux 为例）
#### 使用 hadoop fs 常用命令
```
[rabbitliu@VM_83_1_centos bin]$ hadoop fs -ls  cosn://rabbitliu/
Found 7 items
-rw-rw-rw-   1 rabbitliu rabbitliu       3669 2016-10-25 21:23 cosn://rabbitliu/b.txt
drwxrwxrwx   - rabbitliu rabbitliu          0 1970-01-01 08:00 cosn://rabbitliu/dir1
drwxrwxrwx   - rabbitliu rabbitliu          0 1970-01-01 08:00 cosn://rabbitliu/mr
-rw-rw-rw-   1 rabbitliu rabbitliu      16952 2016-10-25 21:37 cosn://rabbitliu/qcloud_sign.proto
-rw-rw-rw-   1 rabbitliu rabbitliu       2048 2016-10-25 21:48 cosn://rabbitliu/rabbit_test2K.txt
-rw-rw-rw-   1 rabbitliu rabbitliu   52428800 2016-10-27 16:40 cosn://rabbitliu/rabbit_test50MB.txt
drwxrwxrwx   - rabbitliu rabbitliu          0 1970-01-01 08:00 cosn://rabbitliu/xx1

```

#### 运行 MapReduce 自带的 wordcount
```
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://rabbitliu/mr/input cosn://rabbitliu/mr/output3
```

执行成功会返回统计信息，示例如下：
```
File System Counters
        COSN: Number of bytes read=72
        COSN: Number of bytes written=40
        COSN: Number of read operations=0
        COSN: Number of large read operations=0
        COSN: Number of write operations=0
        FILE: Number of bytes read=547350
        FILE: Number of bytes written=1155616
        FILE: Number of read operations=0
        FILE: Number of large read operations=0
        FILE: Number of write operations=0
        HDFS: Number of bytes read=0
        HDFS: Number of bytes written=0
        HDFS: Number of read operations=0
        HDFS: Number of large read operations=0
        HDFS: Number of write operations=0
    Map-Reduce Framework
        Map input records=5
        Map output records=7
        Map output bytes=59
        Map output materialized bytes=70
        Input split bytes=99
        Combine input records=7
        Combine output records=6
        Reduce input groups=6
        Reduce shuffle bytes=70
        Reduce input records=6
        Reduce output records=6
        Spilled Records=12
        Shuffled Maps =1
        Failed Shuffles=0
        Merged Map outputs=1
        GC time elapsed (ms)=0
        Total committed heap usage (bytes)=653262848
    Shuffle Errors
        BAD_ID=0
        CONNECTION=0
        IO_ERROR=0
        WRONG_LENGTH=0
        WRONG_MAP=0
        WRONG_REDUCE=0
    File Input Format Counters 
        Bytes Read=36
    File Output Format Counters 
        Bytes Written=40
```
