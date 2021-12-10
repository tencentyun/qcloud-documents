## 简介

DBbrain为方便 Mongo  DBA的日常运维，为您提供了Tencent MongoDB Top工具，此工具与mongodb官方工具类似，可实时查看节点维度top表监控情况。

#### 节点维度 MongoDB Top使用步骤：

1.   登录[DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/slow-sql)，在左侧导航选择【诊断优化】，在上方选择【性能趋势】页。
2.  点击【mongod节点】-->【MongoTop】
3.  通过下拉列表，选择一个您要查看的节点即可。
4.  右上方有暂停按钮，可以暂停后观看数据情况。

![](https://qcloudimg.tencent-cloud.cn/raw/d7f0d9c4e8f7b988868b69cfd1f1a54c.png)

## MongoTop表监控字段说明

mongotop，字段说明如下：

- **Time：**

​       当前状态的db时间。

- **ns：**

  包含数据库命名空间，后者结合了数据库名称和集合。

- **total：**

  mongod在这个命令空间上花费的总时间。

- **read：**

  在这个命令空间上mongod执行读操作花费的时间。

- **write：**

  在这个命名空间上mongod进行写操作花费的时间。

  
