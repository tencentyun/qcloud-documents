腾讯云 EMR 已经无缝集成了腾讯云对象存储，可以直接在 EMR 集群中对 COS 中的数据进行运算。如果需要使用对象存储，在创建 EMR 集群的时候填写 COS 的相关信息即可。

在 Hadoop 中访问 COS 上的文件可以通过命令进行：`bin/hadoop fs -ls cosn://emrtest/data/`
运行结果如下：
```
	[hadoop@10 hadoop]$ bin/hadoop fs -ls cosn://emrtest/data/
	Found 4 items
	-rw-rw-rw- 1 hadoop hadoop 5262 2017-03-10 10:21 cosn://emrtest/data/201408_station_data.csv
	-rw-rw-rw- 1 hadoop hadoop 653037596 2017-03-10 10:43 cosn://emrtest/data/201408_status_data.csv
	-rw-rw-rw- 1 hadoop hadoop 80320 2017-03-10 10:28 cosn://emrtest/data/201408_weather_data.csv
	drwxrwxrwx - hadoop hadoop 0 1970-01-01 08:00 cosn://emrtest/data/hive
```
* 上述命令中`cosn://`为协议名称
* emrtest 为 Bucket 名称
* `/data/`为 Bucket 下的路径

>**注意：**
>在 EMR 环境中使用对象存储，需保证对象存储版本在 V4 或以上。
