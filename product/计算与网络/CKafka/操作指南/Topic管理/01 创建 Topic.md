## 操作场景

Topic（主题）是某一种分类的名字，消息在 Topic 中可以被存储和发布。CKafka 对外使用 Topic 的概念，生产者往 Topic 中写消息，消费者从 Topic 中读消息。为了做到水平扩展，一个 Topic 实际是由多个 [Partition（分区）](https://cloud.tencent.com/document/product/597/32544#F)组成，遇到瓶颈时，可以通过增加 Partition 的数量进行横向扩容。

本文介绍在 CKafka 控制台创建一个 Topic 的操作步骤。

## 前提条件

[已创建实例](https://cloud.tencent.com/document/product/597/53207)。

## 操作步骤

### 步骤1：创建 Topic

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在**实例列表**页，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击页面顶部的 **Topic 管理**，单击**新建**。
4. 在编辑 Topic 窗口中，选择分区数和副本数等信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c71e1e73fb7a503b4e517e10d6256f87.png)
   - 名称：Topic 名称，输入后无法更改，名称只能包含字母、数字、下划线、“-”和“.”。
   - 分区数：一个物理上分区的概念，一个 Topic 可以包含一个或者多个 partition，CKafka 以 partition 作为分配单位。
   - 副本数：Partition 的副本个数，用于保障 Partition 的高可用。为保障数据可靠性，默认开启2副本。副本数也算分区个数，例如客户创建了1个 Topic、6个分区、2个副本，那么分区额度一共用了1 × 6 × 2 = 12个。
> !设置为单副本会导致可用性无法保证，请谨慎操作。
   - 标签：设置资源标签，关于标签的详细介绍请参见 [标签管理](https://cloud.tencent.com/document/product/597/33355)。
   - 预设 ACL 策略：勾选提前设置好的 ACL 策略，关于 ACL 策略详情请参见 [配置 ACL 策略](https://cloud.tencent.com/document/product/597/31528)。
5. 单击**提交**，完成 Topic 创建。



### 步骤2：配置 Topic 高级参数

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
        <td style='text-align:left;'>5mins - 90days</td>
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
