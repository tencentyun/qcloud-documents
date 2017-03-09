## 功能说明

可以使用 Hadoop 大数据处理引擎，如 MapReduce，Hive 处理存储在腾讯云对象存储 COS 上的数据。**只适用于COS 4.0**

**实现机制**：Hadoop cosn 插件实现了以腾讯云 COS 作为底层存储的文件系统运行上层的计算任务，如 MapReduce、Hive、Spark、Tez 等。cosn 支持以任意形式上传到 COS 上的数据被 Hadoop 处理。

## 使用环境

### 系统环境

Linux、Windows 系统

### 软件依赖

Hadoop-2.7.2 及以上

## 使用方法

### 获取 cos-java-sdk

下载地址：https://github.com/tencentyun/cos-java-sdk-hadoop-v4

在下载路径运行以下命令进行编译，获取 target 目录下的 cos_api-4.2.jar

```
mvn clean package -Dmaven.test.skip=true
```

### 获取 hadoop-cos 插件

下载地址：https://github.com/tencentyun/hadoop-cosn-v4

因为 cosn 依赖 SDK，请将上一步编译的 cos_api-4.2.jar 拷贝到 src/main/resources 下，然后运行以下命令进行编译,获取 target 目录下的 hadoop-cos-2.7.2.jar

```
mvn clean package -Dmaven.test.skip=true
```

### 插件安装方法

#### 修改 hadoop_env.sh

增加如下内容，将 cosn 相关 jar 包加入 Hadoop 环境变量

```
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```

将上两步获取的 cos_api-4.2.jar 和 hadoop-cos-2.7.2.jar 拷贝到 $HADOOP_HOME/share/hadoop/tools/lib 下，同时需要拷贝 SDK 依赖的 json-20140107.jar 和httpmime-4.2.5.jar 到该目录（这两个 JAR 包可在本地的 maven 仓库下找到）。

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

注意其中含有 COS 的几个属性：

- fs.cos.userinfo.appid 属性 填写您使用的 COS 账户 APPID
- fs.cos.userinfo.secretId/secretKey 属性 填写您账户的秘钥信息
- fs.cosn.impl 为 cosn 的实现类，固定为 org.apache.hadoop.fs.cosnative.NativeCosFileSystem
- fs.cos.buffer.dir 请设置一个实际存在的目录，运行过程中产生的临时文件会暂时放于此处
- fs.cos.userinfo.region 请填写你的地域信息，tj(天津)，sh(上海)，gz(广州)
## 使用软件

### 使用 hadoo fs 常用命令

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

### 运行 MapReduce 自带的 wordcount

```
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://rabbitliu/mr/input cosn://rabbitliu/mr/output3
```

执行成功会返回一些统计信息如下：

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


