## Feature Description

You can use Hadoop big data processing engines (such as MapReduce, Hive) to process data that is stored on Tencent Cloud Object Storage (COS). **Only applicable to COS 4.0**

**Implementation mechanism**: The Hadoop cosn plugin is used to execute high-layer computing tasks (such as MapReduce, Hive, Spark, Tez) on file systems that use Tencent COS as underlying storage. With cosn, Hadoop is able to process data that has been uploaded to COS using any method.

## Operating Environment

### System Environment

Linux/Windows system

### Required Software

Hadoop-2.7.2 or above

## How to Use

### Acquire cos-java-sdk

Download link: https://github.com/tencentyun/cos-java-sdk-hadoop-v4

Execute the following command from the download path and compile to acquire cos_api-4.2.jar which is located in the target directory

```
mvn clean package -Dmaven.test.skip=true
```

### Acquire hadoop-cos Plugin

Download link: https://github.com/tencentyun/hadoop-cosn-v4

As cosn relies on SDK, please copy the cos_api-4.2.jar which was compiled in the previous step to src/main/resources and execute the following command to compile, to acquire the hadoop-cos-2.7.2.jar under the target directory

```
mvn clean package -Dmaven.test.skip=true
```

### Plugin Installation

#### Modify hadoop_env.sh

Add the following content and add the cosn relevant jar packages to Hadoop environment variable

```
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```

Copy cos_api-4.2.jar and hadoop-cos-2.7.2.jar (acquired in the previous two steps) to $HADOOP_HOME/share/hadoop/tools/lib, and copy json-20140107.jar and httpmime-4.2.5.jar (required by SDK. You can find these two JAR packages in the local maven repository) to this directory.

#### Modify Configuration File to Use the Plugin

Modify $HADOOP_HOME/etc/hadoop/core-site.xml, add COS relevant user and implementation class information. For example:

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
</configuration>
```

Note the attributes with "COS" in them:

- fs.cos.userinfo.appid: Enter the APPID of the COS account you use
- fs.cos.userinfo.secretId/secretKey: Enter the private key information of your account
- fs.cosn.impl is the implementation class of cosn, it is always org.apache.hadoop.fs.cosnative.NativeCosFileSystem
- fs.cos.buffer.dir: Please configure a directory that actually exists. Temporary files generated during operations will be stored here

## Use the Software

### Use hadoop fs Common Commands

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

### Use MapReduce's wordcount Application

```
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://rabbitliu/mr/input cosn://rabbitliu/mr/output3
```

When successfully executed, it will return the following statistical information:

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



