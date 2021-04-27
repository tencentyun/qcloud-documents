## 操作场景

该任务指导您通过 CKafka 控制台在已创建好的实例下创建 Topic。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在【实例列表】页，单击 [步骤一](https://cloud.tencent.com/document/product/597/54839) 创建的实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击页面顶部的【Topic 管理】，单击【新建】。
4. 在编辑 Topic 窗口中，选择分区数和副本数等信息。
   ![](https://main.qcloudimg.com/raw/05f7dc495a90da08c2b1a5593b908c1f.png)
  - 名称：Topic 名称，输入后无法更改，名称只能包含字母、数字、下划线、“-”和“.”。
  - 分区数：一个物理上分区的概念，一个 Topic 可以包含一个或者多个 Partition，CKafka 以 Partition 作为分配单位。
  - 副本数：Partition 的副本个数，用于保障 Partition 的高可用，为保障数据可靠性，当前不支持创建单副本 Topic，默认开启2副本。
    副本数也算分区个数，例如客户创建了1个 Topic、6个分区、2个副本，那么分区额度一共用了1 * 6 * 2 = 12个。
  - 白名单： 开启白名单后，只有白名单中的 IP 才可访问该 Topic，有效保证数据安全（在新建 Topic 和编辑 Topic 页面均可以开启白名单）。
4. 单击【提交】完成 Topic 创建。
