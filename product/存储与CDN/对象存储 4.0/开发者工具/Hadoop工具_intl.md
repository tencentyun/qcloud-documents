## Feature Description
The Hadoop cosn plugin is used to execute high-layer computing tasks on file systems that use Tencent Cloud Object Storage (COS) as underlying storage. You can use Hadoop engines for big data processing, such as MapReduce, Hive, Spark, Tez, to process data stored on Tencent COS.  

## Operating Environment
### System Environment
Linux/Windows system

### Software Dependencies
Hadoop-2.7.2 or later
#### Installation and Configuration
For more information on how to install and configure Hadoop, please see [Install and Test Hadoop](/doc/product/436/10867).
## How to Use
### Install Maven
- **Linux:**
```
sudo apt-get install maven
```
- **Windows:**
Download link: [Maven](http://maven.apache.org/download.html)
For more information on how to install and configure Maven, please see [Install Maven and Configure Environment Variables on Windows](http://www.cnblogs.com/liuhongfeng/p/5057827.html) 

### Obtain cos-java-sdk
Download link: [cos-java-sdk](https://github.com/tencentyun/cos-java-sdk-hadoop-v4)

Execute the following command in the download path to compile to obtain cos_api-4.2.jar which is located in the target directory:
```
mvn clean package -Dmaven.test.skip=true
```
### Obtain hadoop-cos Plugin
Download link: [hadoop-cos plugin](https://github.com/tencentyun/hadoop-cosn-v4)

As cosn relies on SDK, copy the cos_api-4.2.jar compiled in the previous step to `src/main/resources` and execute the following command to compile, to obtain the hadoop-cos-2.7.2.jar under the target directory:
```
mvn clean package -Dmaven.test.skip=true
```
### Plugin Installation
#### Modify hadoop_env.sh
Enter hadoop_env.sh under `$HADOOP_HOME/etc/hadoop` directory. Add the following content and add the cosn related jar packages to Hadoop environment variable:
```
for f in $HADOOP_HOME/share/hadoop/tools/lib/*.jar; do
  if [ "$HADOOP_CLASSPATH" ]; then
    export HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$f
  else
    export HADOOP_CLASSPATH=$f
  fi
done
```
Copy the obtained cos_api-4.2.jar and hadoop-cos-2.7.2.jar to `$HADOOP_HOME/share/hadoop/tools/lib`, and copy json-20140107.jar under `/org/json/json/20140107` in local Maven warehouse and httpmime-4.2.5.jar under `/org/apache/httpcomponents/httpmime/4.2.5` to the directory.
Generally, the local Maven warehouse is under `${user.home}/.m2/repository`, and is controlled by the localRepository variable in ${MAVEN_HOME}/conf/settings.xml.
#### Modify Configuration File to Use the Plugin
Modify $HADOOP_HOME/etc/hadoop/core-site.xml, and add COS related users and implementation class information. For example:
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

> <font color="#0000cc">**Note:** </font>
The configuration file contains the following attributes of COS:
- fs.cos.userinfo.appid: Enter the APPID of your Tencent Cloud account, which can be seen at [Console -> Account Info](https://console.cloud.tencent.com/developer).
- fs.cos.userinfo.secretId/secretKey: Enter the API key information of your account, which can be seen at [Cloud API Key Console](https://console.cloud.tencent.com/capi).
- fs.cosn.impl is the implementation class of cosn. It is always org.apache.hadoop.fs.cosnative.NativeCosFileSystem.
- fs.cos.buffer.dir: Configure a directory that actually exists. Temporary files generated in the running process will be stored here.
- fs.cos.userinfo.region: Enter your region. Enumerated values are region abbreviations in the [List of Regions for Historical Versions](https://cloud.tencent.com/document/product/436/7777), such as sh, gz, sgp.

### Use of Software (Take Linux as an example)
#### Use hadoop fs Common Commands
Command format: `hadoop fs- -ls cosn://Bucket path`. Take the Bucket named "example" as an example. You can add a specific path after the Bucket.
```
hadoop fs -ls  cosn://example/
Found 7 items
-rw-rw-rw-   1 example example       3669 2016-10-25 21:23 cosn://example/b.txt
drwxrwxrwx   - example example          0 1970-01-01 08:00 cosn://example/dir1
drwxrwxrwx   - example example         0 1970-01-01 08:00 cosn://example/mr
-rw-rw-rw-   1 example example      16952 2016-10-25 21:37 cosn://example/qcloud_sign.proto
-rw-rw-rw-   1 example example       2048 2016-10-25 21:48 cosn://example/test2K.txt
-rw-rw-rw-   1 example example   52428800 2016-10-27 16:40 cosn://example/test50MB.txt
drwxrwxrwx   - example example          0 1970-01-01 08:00 cosn://example/xx1
```
#### Run the wordcount provided in MapReduce
> <font color="#0000cc">**Note:** </font>
hadoop-mapreduce-examples-2.7.2 in the following command is only available to Version 2.7.2. For other versions, change it to the appropriate version number.

```
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount cosn://example/mr/input cosn://example/mr/output3
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

