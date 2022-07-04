## 操作场景

本文介绍您在 CKafka 控制台创建 Topic 后，查看 Topic 详情和生产端连接关系的操作步骤。

## 操作步骤

### 步骤1：查看 Topic 详情

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击 **topic 管理**标签页，查看 Topic 信息，进入 Topic 列表页。
4. 在 Topic 列表页，单击 Topic 名称左侧右三角符号，查看 Topic 详情。
![](https://qcloudimg.tencent-cloud.cn/raw/bda6f0af5afdae2b51bbaa5ecf8d0faa.png)
<table>
    <thead>
    <tr>
        <th>项目</th>
        <th>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>分区名称</td>
        <td>partition 的名称</td>
    </tr>
    <tr>
        <td>leader</td>
        <td>leader 处理 partition 的所有读写请求，follower 会被动定期地去复制 leader 上的数据</td>
    </tr>
    <tr>
        <td>副本</td>
        <td>副本列表</td>
    </tr>
    <tr>
        <td>ISR</td>
        <td>已同步消息的副本</td>
    </tr>
    <tr>
        <td>起始 offset</td>
        <td>消息最后消费的位置</td>
    </tr>
    <tr>
        <td>末端 offset</td>
        <td>消息最后写入的位置</td>
    </tr>
    <tr>
        <td>消息数</td>
        <td>存储的消息数量</td>
    </tr>
    <tr>
        <td>未同步副本</td>
        <td>未同步的副本数量，支持筛选存在未同步副本的 partition</td>
    </tr>
    </tbody>
</table>




### 步骤2：查看生产端连接关系

> ?当前仅2.4版本及以上实例支持查看生产端连接关系。

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页，在操作栏单击**生产端连接关系**，查看与 Topic 连接的生产者列表信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5964448721f3c3a94d4deced5ec2ba88.png)
