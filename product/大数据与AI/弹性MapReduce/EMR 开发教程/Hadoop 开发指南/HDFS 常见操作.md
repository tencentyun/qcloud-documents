腾讯云 EMR 的 Hadoop 集成了腾讯云对象存储，如果您在购买的时候勾选了支持 COS，那么您也可以通过常见的 hadoop 命令操作 COS 上的数据。可通过如下命令操作集群中的数据。
``` shell
#cat 数据
hadoop fs -cat /usr/hive/warehouse/hivewithhdfs.db/record/data.txt
#修改目录或者文件权限
hadoop fs -chmod -R 777 /usr
#改变文件或者目录 owner
hadoop fs -chown -R root:root /usr
#创建文件夹
hadoop fs -mkdir <paths>
#本地文件发送到 HDFS 上
hadoop fs -put <localsrc> ... <dst>
#拷贝本地文件到 HDFS 上
hadoop fs -copyFromLocal <localsrc> URI
#查看文件或者目录的存储使用量
hadoop fs -du URI [URI …]
#删除文件
hadoop fs -rm URI [URI …]
#设置目录或者文件的拷贝数
hadoop fs–setrep [-R] [-w] REP PATH [PATH …]
#检查集群文件坏块
hadoop fsck <path> [-move | -delete | -openforwrite] [-files [-blocks [-locations | -racks]]]
```

更多 HDFS 命令请参考 [社区文档](http://hadoop.apache.org/docs/r2.7.3/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html)，此外如果您的集群是 HA 集群（双 namenode），您可以通过如下命名查看哪个 namenode 是 active 的。
``` shell
#nn1 是 namenode 的 ID，一般为 nn1 和 nn2
hdfs haadmin -getServiceState nn1
#查看当前集群报告
hdfs dfsadmin -report
#namenode 离开安全模式
hdfs dfsadmin -safemode leave
```

