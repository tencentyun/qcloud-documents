Flink 擅长处理无界和有界数据集 精确的时间控制和状态化使得 Flink 的运行（runtime）能够运行任何处理无界流的应用。有界流则由一些专为固定大小数据集特殊设计的算法和数据结构进行内部处理，产生了出色的性能。
以下针对于在对象存储上的有界或者无界数据集的数据集进行演示操作，这里为了更好的观察作业的运行情况使用 yarn-session 模式来提交任务。Flink On Yarn 支持 Session Mode 和 Application Mode 两种形式，具体可参考 [社区文档](https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/deployment/resource-providers/yarn/)。
本教程演示的是提交的任务为 wordcount 任务即统计单词个数，提前需要在集群中上传需要统计的文件。
## 开发准备
1. 由于任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中先 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
2. 确认您已开通腾讯云，且已创建一个 EMR 集群。在创建 EMR 集群的时候需要在软件配置界面选择 Flink 组件，并且在基础配置页面开启对象存储的授权。
3. 集群购买完成后，可以使用 HDFS 访问对象存储确保其基础功能可用。具体命令如：
```
[hadoop@10 ~]$ hdfs dfs -ls cosn://$BUCKET_NAME/path
Found 1 items
-rw-rw-rw-   1 hadoop hadoop      27040 2022-10-28 15:08 cosn://$BUCKET_NAME/path/LICENSE
```


## 示例
```
# -n 表示申请1个容器，这里指的就是多少个taskmanager
# -tm 表示每个TaskManager的内存大小
# -s 表示每个TaskManager的slots数量
# -d 表示以后台程序方式运行，后面接的session名字
[hadoop@10 ~]$ yarn-session.sh -jm 1024 -tm 1024 -n 1 -s 1 -nm wordcount-example -d
```
```
/usr/local/service/flink/bin/flink run -m yarn-cluster /usr/local/service/flink/examples/batch/WordCount.jar --input cosn://$BUCKET_NAME/path/LICENSE -output cosn://$BUCKET_NAME/path/wdp_test
[hadoop@10 ~]$ hdfs dfs -ls cosn://$BUCKET_NAME/path/wdp_test
-rw-rw-rw-   1 hadoop hadoop       7484 2022-11-04 00:47 cosn://$BUCKET_NAME/path/wdp_test

```




