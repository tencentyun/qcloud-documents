## 简介
为方便数据库管理员的日常运维，DBbrain 为您提供了 Tencent MongoDB Top 工具，此工具与 MongoDB 官方工具类似，可实时查看节点维度 Top 表监控情况。

## 操作步骤
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/performance/monitor)，在左侧导航选择**诊断优化**，在上方选择**性能趋势**页。
2. 在上方选择对应 MongoDB 实例，然后选择 **mongod节点** > **MongoTop**。
3. 通过下拉列表，选择一个您要查看的节点即可。
4. 单击右上方暂停按钮，可以暂停后观看数据情况。
![](https://qcloudimg.tencent-cloud.cn/raw/61673e63da885f4678adcebb8133c7f3.png)

## MongoTop 表监控字段说明
MongoTop 字段说明如下：
- **Time：**
当前状态的 db 时间。

- **ns：**
包含数据库命名空间，后者结合了数据库名称和集合。

- **total：**
mongod 在这个命令空间上花费的总时间。

- **read：**
在这个命令空间上 mongod 执行读操作花费的时间。

- **write：**
在这个命名空间上 mongod 进行写操作花费的时间。

  
