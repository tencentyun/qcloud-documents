## 命令行模式
### 1. 连接  Sqoop Server
#### 运行 Client Shell
```
    ./sqoop.sh client
    Sqoop home directory: /usr/local/service/sqoop
    Mar 09, 2017 5:11:06 PM java.util.prefs.FileSystemPreferences$1 run
    INFO: Created user preferences directory.
    Sqoop Shell: Type 'help' or '\h' f or help.

    sqoop:000>
```
#### Server
```
    --host (sqoop server 地址)
    --port (sqoop server 服务端口)
    -webapp sqoop (服务名称)
    sqoop:000> set server --host 10.0.1.182 --port 11000 --webapp sqoop
    Server is set successfully
```
Server 的端口信息可在 sqoop-sys.sh 中查看：
   ` export SQOOP\_HTTP_PORT=11000 // 服务端口`

#### 查看 Server 信息
连接成功后，执行`show version -all`命令，Server version 会显示服务端的版本，API 版本等相关信息。
```
    sqoop:000> show version -all
    client version:
      Sqoop 1.99.5-cdh5.10.0 source revision bbb5e2eeed75bf80cdfd3122fe6b05da4175dcc6
      Compiled by jenkins on Fri Jan 20 11:58:45 PST 2017
    0 [main] WARN org.apache.hadoop.util.NativeCodeLoader -
      Unable to load native-hadoop library for your platform...
      using builtin-java classes where applicable
    server version: # 服务器版本信息
      Sqoop 1.99.5-cdh5.10.0 source revision bbb5e2eeed75bf80cdfd3122fe6b05da4175dcc6
      Compiled by jenkins on Fri Jan 20 11:58:45 PST 2017
    API versions:
      [v1]
```
### 2. connector
执行 `show connector` 可以看到支持的 connector：
```
    sqoop:000> show connector
    ---------------------------------------------------------------------------------
    Name                        Class
    ---------------------------------------------------------------------------------
    generic-jdbc-connector      org.apache.sqoop.connector.jdbc.GenericJdbcConnector
    kite-connector              org.apache.sqoop.connector.kite.KiteConnector
    hdfs-connector              org.apache.sqoop.connector.hdfs.HdfsConnector
    kafka-connector             org.apache.sqoop.connector.kafka.KafkaConnector
    ---------------------------------------------------------------------------------
```
### 3. link
link 表示一个数据通道，`from link1 to link2` 意味着将 link1 的数据导入到 link2 中。

#### 创建 MySQL 的 link
```
    // 创建一个link，-c connetorid（connector 的Id，show connector 可以查到）
    sqoop:000> create link -c 1
    Creating link for connector with id 1
    Please fill following values to create new link object
    Name: mysql-link #link 的名称

    Link configuration

    JDBC Driver Class: com.mysql.jdbc.Driver //jdbc 的driver
    JDBC Connection String: jdbc:mysql://10.0.1.71:3306/sqoop_test //jdbc 连接string
    Username: root //mysql 实例用户名
    Password: ********** //mysql 实例连接密码
    JDBC Connection Properties:
    There are currently 0 values in the map:
    entry# protocol=tcp // 连接协议
    There are currently 1 values in the map:
    protocol = tcp
    entry#
    New link was successfully created with validation status OK and persistent id 1
```
#### 创建一个 HDFS 的 link：
```
    sqoop:000> create link -c 3
    Creating link for connector with id 3
    Please fill following values to create new link object
    Name: hdfs-link

    Link configuration

    HDFS URI: hdfs://10.0.1.182:4007 #hdfs URI
    New link was successfully created with validation status OK and persistent id 2
```
#### 查看创建的 link
执行`show link`命令，查看创建的 link，结果如下：
```
sqoop:000> show link
--------------------------------------------------------------------
Id   Name         Connector Id    Connector Name          Enabled
--------------------------------------------------------------------
1    mysql-link   1               generic-jdbc-connector  true
2    hdfs-link    3               hdfs-connector          true
--------------------------------------------------------------------
```
### 4. job
#### 把 MySQL 的数据导入到 hdfs
参数： -f linkId (from-link Id) ，-t linkId (to-link Id)。
```
    sqoop:000> create job -f 1 -t 2 // 创建一个job
    Creating job for links with from id 1 and to id 2
    Please fill following values to create new job object
    Name: mysql-hdfs //job 名称
    
    From database configuration

    Schema name: sqoop_test //mysql 数据库名
    Table name: test //mysql 导出表名
    Table SQL statement:（optional）// 导出sql 语句
    Table column names: （optional）
    Partition column name: // 用于partition 的colume name
    Null value allowed for the partition column: (optional)
    Boundary query: (optional)

    ToJob configuration

    Override null value: (optional)
    Null value: (optional)
    Output format:
    0 : TEXT_FILE
    1 : SEQUENCE_FILE
    Choose: 0 // 选择输出的文件格式
    Compression format:
    0 : NONE
    1 : DEFAULT
    2 : DEFLATE
    3 : GZIP
    4 : BZIP2
    5 : LZO
    6 : LZ4
    7 : SNAPPY
    8 : CUSTOM
    Choose: 0 // 选择压缩格式
    Custom compression format: (optional) // 自定义的压缩格式
    Output directory: /sqoop_test/mysql-sqoop // hdfs 输出文件目录
 
    Throttling resources

    Extractors: 100 // map 个数
    Loaders: 10 // reduce 个数
    New job was successfully created with validation status OK and persistent id 1
```
#### 查看 job
执行`show job`命令，查看job：
```
sqoop:000> show job
------------------------------------------------------------
Id  Name         From Connector   To Connector    Enabled
------------------------------------------------------------
1   mysql-hdfs   1                3               true
------------------------------------------------------------
```
#### 启动 job
```
    sqoop:000> start job -j 1 //-j jobid
    Submission details
    Job ID: 1
    Server URL: http://10.0.1.182:11000/sqoop/
    Created by: root
    Creation date: 2017-03-09 19:06:27 CST
    Lastly updated by: root
    External ID: job_1489050296063_0036
        http://10.0.1.182:5004/proxy/application_1489050296063_0036/
    2017-03-09 19:06:27 CST: BOOTING - Progress is not available
```
#### 查看 job 进度
```
    sqoop:000> status job -j 1 #-j jobid
    Submission details
    Job ID: 1
    Server URL: http://10.0.1.182:11000/sqoop/
    Created by: root
    Creation date: 2017-03-09 19:06:27 CST
    Lastly updated by: root
    External ID: job_1489050296063_0036
        http://10.0.1.182:5004/proxy/application_1489050296063_0036/
    2017-03-09 19:08:04 CST: RUNNING - 11.50 %
```
#### 终止 job
```
    sqoop:000> stop job -j 1 //-j jobid
    Submission details
    Job ID: 1
    Server URL: http://10.0.1.182:11000/sqoop/
    Created by: root
    Creation date: 2017-03-09 19:24:13 CST
    Lastly updated by: root
    External ID: job_1489050296063_0041
        http://10.0.1.182:5004/proxy/application_1489050296063_0041/
    2017-03-09 19:24:55 CST: SUCCEEDED
```
#### 根据 SQL 语句导出 MySQL 数据的 job 参数
```
    sqoop:000> show job -all
    1 job(s) to show:
    Job with id 1 and name mysql-hdfs (Enabled: true,
      Created by root at 3/9/17 6:48 PM, Updated by root at 3/9/17 7:24 PM)
    Using link id 1 and Connector id 1
      From database configuration
        Schema name: // 不填
        Table name: // 不填
        Table SQL statement:
         select a,b from sqoop_test.test where a>1 and a<1 and ${CONDITIONS} #sql 语句
        Table column names:
        Partition column name: a // 分区的column
        Null value allowed for the partition column:
        Boundary query:
      Throttling resources
        Extractors: 100
        Loaders: 10
      ToJob configuration
        Override null value:
        Null value:
        Output format: TEXT_FILE
        Compression format: NONE
        Custom compression format:
        Output directory: /sqoop_test/mysql-sqoop
```
## 基于 Hue 的 Sqoop 数据传输
### 1. link
#### 创建 link
【Data Browsers】 > 【Sqoop Transfer】 > 【Manager links】
![](//mc.qcloudimg.com/static/img/6588cdd6245e108ff93e1df00812bbbe/image.png)
在这里可以看到已经创建好的 link，新建 link 的话，单击【New link】。
![](//mc.qcloudimg.com/static/img/d5d00304ff277a8d3fb7e818de347d8c/image.png)
#### 创建 MySQL link
这里我们创建一个 MySQL 的 link 。
![](//mc.qcloudimg.com/static/img/9fa643e7ba18c00760898d99931d37f0/image.png)
保存后，可以看到创建的 mysql-link。
![](//mc.qcloudimg.com/static/img/cdc5de8c64a6aa106030bdfc88c05374/image.png)
单击 【mysql-link】，可以看到 link 的详细信息，并可以修改。
![](//mc.qcloudimg.com/static/img/703816355a90c7db83d73ba53d3075a1/image.png)
#### 创建 HDFS link
创建一个 HDFS link，请注意，HDFS URI内容需要填对应 HDFS 集群的 fs.defaultFS 名称。
![](//mc.qcloudimg.com/static/img/9eb85396a15da82c815da90b4597840f/image.png)
保存后，检查一下是否正确。
![](//mc.qcloudimg.com/static/img/d2a282409b5ecd668c5bd0fafa4a83e2/image.png)
### 2. job
#### 创建 job
【Data Browsers】 > 【Sqoop Transfer】 > 【New job】 选择创建好的 link。From link 表示源数据。To link 表示目标数据。我们这里是将数据从 MySQL 导入到 HDFS。
![](//mc.qcloudimg.com/static/img/2e002a74e6a0b012bd69a97ff2d9ec4e/image.png)
“Next”后，填写 from link 的 源数据相关信息，我们这里是 MySQL 数据、需要填导出的数据库名、表名、导出的 SQL 语句、分区的字段值、map 个数、reduce 个数等信息。
![](//mc.qcloudimg.com/static/img/61346dafb51d3da8fd702593c2f5c1be/image.png)
“Next” 后，填写 to link 的目的数据相关信息，我们这里是导出到 HDFS，需要填写导出的文件格式、文件压缩方式、导出到 HDFS 上的文件路径等信息。
![](//mc.qcloudimg.com/static/img/eab360c624968210af3145c3ad845072/image.png)
#### 执行 job
选择创建 job，单击 “run” 执行。
![](//mc.qcloudimg.com/static/img/bed6bc1ccbe45fb76cf9664425c23717/image.png)
job 提交后，可以看到 job 的执行相关信息。
![](//mc.qcloudimg.com/static/img/6eaaeb6e6f65deaadafd525f62862dec/image.png)
![](//mc.qcloudimg.com/static/img/bc1e8f987f5dec6acd3e989cfffd8bdd/image.png)
在 HDFS 的导出目录中，可以看到导出的数据文件。
![](//mc.qcloudimg.com/static/img/07be510f0733e91fa3b95c4f00486663/image.png)
