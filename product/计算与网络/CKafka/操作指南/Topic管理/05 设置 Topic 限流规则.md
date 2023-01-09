## 操作场景

您可以针对 Topic 设置限流规则，避免单个 Topic 流量过大而影响其他 Topic。

<dx-alert infotype="explain" title="">
只有 broker 版本为1.1.1和 2.4.x 才支持 topic 设置限流规则。
</dx-alert>

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击 **topic 管理**标签页。
4. 单击操作列的**更多** > **限流**，设置限流阈值。
  ![](https://qcloudimg.tencent-cloud.cn/raw/3963798dd53c757c0a4f72f24e66d34b.png)
  - topic 最大生产流量：不含副本流量，取值范围为1MB/s到该实例购买的最大带宽/该 Topic 副本数。
  - topic 最大消费流量：取值范围为1MB/s到该实例购买的最大带宽。

> ?
> 
> - 底层针对 broker 进行限流，实际限流值（等于 broker 数量的整数倍）可能会与设置的限流值略有区别。
> - 关于软限流机制说明请参见 [限流说明](https://cloud.tencent.com/document/product/597/55803)。
