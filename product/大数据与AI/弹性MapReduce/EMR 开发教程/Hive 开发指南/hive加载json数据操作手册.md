### 1. 连接 Hive
登录 EMR 集群的 Master 节点，切换到 hadoop 用户并且进入 hive 目录：

```
[root@10 ~]# su hadoop
[hadoop@10 root]$ cd /usr/local/service/hive
```

### 2. 准备数据
创建数据文件（JSON 格式），编译以下内容并保存：
```
vim test.data
{"name":"Mary","age":12,"course":[{"name":"math","location":"b208"},{"name":"english","location":"b702"}],"grade":[99,98,95]}
{"name":"Bob","age":20,"course":[{"name":"music","location":"b108"},{"name":"history","location":"b711"}],"grade":[91,92,93]}
```

将数据文件存储在 hdfs 上：
```
hadoop fs -put ./test.data /
```

### 3. 创建表格
连接 Hive：
```
[hadoop@10 hive]$ hive
```
    
根据映射关系创建表格：
```
hive> CREATE TABLE test ( name string, age int, course array<map<string,string>>, grade array<int>) ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe' STORED AS TEXTFILE;
```
### 4. 导入数据
```
hive>LOAD DATA INPATH '/test.data' into table test;
```
### 5. 检查数据是否导入成功
查询所有数据：
```
hive> select * from test;
OK
Mary	12	[{"name":"math","location":"b208"},{"name":"english","location":"b702"}]    [99,98,95]
Bob	20	[{"name":"music","location":"b108"},{"name":"history","location":"b711"}]   [91,92,93]
Time taken: 0.153 seconds, Fetched: 2 row(s)
```
查询每条记录的第一个得分：
```
hive> select grade[0] from test;
OK
99
91
Time taken: 0.374 seconds, Fetched: 2 row(s)
```
查询每条记录的第一个课程的名称和地点：
```
hive> select course[0]['name'], course[0]['location'] from test;
OK
math	b208
music	b108
Time taken: 0.162 seconds, Fetched: 2 row(s)
```
