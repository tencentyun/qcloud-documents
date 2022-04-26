## 操作场景

Topic（主题）是某一种分类的名字，消息在 Topic 中可以被存储和发布。CKafka 对外使用 Topic 的概念，生产者往 Topic 中写消息，消费者从 Topic 中读消息。为了做到水平扩展，一个 Topic 实际是由多个 [Partition（分区）](https://cloud.tencent.com/document/product/597/32544#F)组成，遇到瓶颈时，可以通过增加 Partition 的数量进行横向扩容。

该任务指导您通过 CKafka 控制台，在已有实例下 Topic 进行管理。

## 操作步骤

### 创建 Topic

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在**实例列表**页，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击页面顶部的 **Topic 管理**，单击**新建**。
4. 在编辑 Topic 窗口中，选择分区数和副本数等信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/aff8d05db54da28566279205e65f0d66.png)
   - 名称：Topic 名称，输入后无法更改，名称只能包含字母、数字、下划线、“-”和“.”。
   - 分区数：一个物理上分区的概念，一个 Topic 可以包含一个或者多个 partition，CKafka 以 partition 作为分配单位。
   - 副本数：partition 的副本个数，用于保障 partition 的高可用，为保障数据可靠性，当前不支持创建单副本 Topic，默认开启2副本。
     副本数也算分区个数，例如客户创建了1个 Topic、6个分区、2个副本，那么分区额度一共用了1 * 6 * 2 = 12个。
   - 标签：设置资源标签，关于标签的详细介绍请参见 [标签管理](https://cloud.tencent.com/document/product/597/33355)。
   - 预设 ACL 策略：勾选提前设置好的 ACL 策略，关于 ACL 策略详情请参见 [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)。
5. 单击**提交**完成 Topic 创建。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1bcfbf5591a841ca7140aeb12b9956cd.png)

### 查看 Topic 详情

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击 **topic 管理**标签页，查看 Topic 信息，进入 Topic 列表页。
4. 在 Topic 列表页，单击 Topic 名称左侧右三角符号，查看 Topic 详情。
   ![](https://main.qcloudimg.com/raw/b26248c628d7b3bd80f005f8cea4422d.png)

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



### 发送消息

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页，在操作栏单击**发送消息**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1f0c4e65ded79440077b0ddb9f8b843a.png)
   - 消息内容：填写发送消息内容，必填。
   - 消息Key：填写发送 Key，选填。
   - 发送到指定分区：支持将消息发送到指定分区，默认关闭。
3. 单击**确认**，发送消息。在消息发送成功弹窗中单击**消息查询**可以查看刚刚发送的消息。



### 查看生产端连接关系

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页，在操作栏单击**生产端连接关系**，查看与 Topic 连接的生产者列表信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/5964448721f3c3a94d4deced5ec2ba88.png)



### 删除 Topic

> !
>
> - 删除 Topic 的同时，存储在此 Topic 中的消息也将被删除，请谨慎操作。
> - Topic 删除是异步操作，配置删除成功后，ZooKeeper 配置将会在1分钟后生效。若此期间创建同名 Topic，系统会提示错误码 [4000]10011，届时请您稍后重试。

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页，在操作栏单击**删除**。
3. 在弹出窗口单击**确认**，Topic 将被删除。



### 配置 Topic 高级参数

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页。
3. 单击操作列的**编辑** > **展示高级配置**，设置如下参数：
   ![](https://qcloudimg.tencent-cloud.cn/raw/e2dc1ba0b2e14379a57e991327da451e.png)

参数说明如下：

<table>
    <thead>
    <tr>
        <th style='text-align:left;'>参数名</th>
        <th style='text-align:left;'>默认值</th>
        <th style='text-align:left;'>参数范围</th>
        <th style='text-align:left;'>说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style='text-align:left;'>cleanup.policy</td>
        <td style='text-align:left;'>delete</td>
        <td style='text-align:left;'>delete/compact</td>
        <td style='text-align:left;'>支持日志按保存时间删除，或者日志按 key 压缩（Kafka Connect 时需要使用 compact 模式）。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>min.insync.replicas</td>
        <td style='text-align:left;'>1</td>
        <td style='text-align:left;'>-</td>
        <td style='text-align:left;'>当 producer 设置 request.required.acks 为1时，min.insync.replicas 指定 replicas 的最小数目。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>unclean.leader.election.enable</td>
        <td style='text-align:left;'>true</td>
        <td style='text-align:left;'>true/false</td>
        <td style='text-align:left;'>指定是否能够设置不在 ISR 中 replicas 作为 leader。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>segment.ms</td>
        <td style='text-align:left;'>-</td>
        <td style='text-align:left;'>1day - 90days</td>
        <td style='text-align:left;'>Segment 分片滚动的时长，单位为 ms，最小值为86400000ms。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>retention.ms</td>
        <td style='text-align:left;'>默认为实例的消息保留时间</td>
        <td style='text-align:left;'>60000ms - 90days</td>
        <td style='text-align:left;'>Topic 维度的消息保留时间。</td>
    </tr>
    <tr>
        <td style='text-align:left;'>retention.bytes</td>
        <td style='text-align:left;'>默认为实例的消息保留大小</td>
        <td style='text-align:left;'>1GB - 1024GB</td>
        <td style='text-align:left;'>Topic 维度的消息保留大小。对于一个 Topic，如果同时设置了消息保留时间和消息保留大小，实际保留消息时会以先达到的阈值为准</td>
    </tr>
    <tr>
        <td style='text-align:left;'>max.message.bytes</td>
        <td style='text-align:left;'>-</td>
        <td style='text-align:left;'>1KB - 12MB</td>
        <td style='text-align:left;'>Topic 维度的最大消息大小。不填写则默认实例维度消息大小为1MB。</td>
    </tr>
    </tbody>
</table>




### 设置 Topic 限流规则

您可以针对 Topic 进行限流，避免单个 Topic 流量过大而影响其他 Topic。

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击 **topic 管理**标签页。
3. 单击操作列的**编辑** > **限流**，设置限流阈值。
![](https://qcloudimg.tencent-cloud.cn/raw/3963798dd53c757c0a4f72f24e66d34b.png)
   - topic 最大生产流量：不含副本流量，取值范围为1MB/s到该实例购买的最大带宽/该 Topic 副本数。
   - topic 最大消费流量：取值范围为1MB/s到该实例购买的最大带宽。
> ?
>
> - 底层针对 broker 进行限流，实际限流值（等于 broker 数量的整数倍）可能会与设置的限流值略有区别。
> - 关于软限流机制说明请参见 [限流说明](https://cloud.tencent.com/document/product/597/55803)。


