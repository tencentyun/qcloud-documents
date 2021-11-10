## 操作场景

**标签**是腾讯云提供的用于标识云上资源的标记，是一个键-值对（Key-Value）。标签可以帮助您从各种维度（例如业务，用途，负责人等）方便的对 TDMQ RabbitMQ 版资源进行分类管理。
>?腾讯云不会使用您设定的标签，标签仅用于您对 TDMQ RabbitMQ 版资源的管理。

## 使用限制

使用标签时，需注意以下限制条件：

| 限制类型 | 限制说明 | 
|---------|---------|
| 数量限制 |每个云资源允许的最大标签数是50。|
| 标签键限制 | <li>`qcloud`、`tencent`、`project` 开头为系统预留标签键，禁止创建。</li><li> 只能为`数字`、`字母`、`+=.@-`，且标签键长度最大为255个字符。</li>|
| 标签值限制 |只能为`空字符串或数字`、`字母`、`+=.@-`，且标签值最大长度为127个字符。|


## 操作方法及案例

### 案例描述

案例：某公司在腾讯云上拥有6个 TDMQ RabbitMQ 版集群，这6个集群的使用部门、业务范围以及负责人的信息如下:

| 队列 ID           | 使用部门 | 业务范围 | 负责人 |
| ----------------- | -------- | -------- | ------ |
| amqp-78383dp8p8w1 | 电商     | 营销活动 | 张三   |
| amqp-78383dp8p8w2 | 电商     | 营销活动 | 王五   |
| amqp-78383dp8p8w3 | 游戏     | 游戏 A   | 李四   |
| amqp-78383dp8p8w4 | 游戏     | 游戏 B   | 王五   |
| amqp-78383dp8p8w5 | 文娱     | 后期制作 | 王五   |
| amqp-78383dp8p8w6 | 文娱     | 后期制作 | 张三   |

以 amqp-78383dp8p8w1为例，我们可以给该实例添加以下三组标签 ：

<table id="table02">
	<tr><th>标签键</th><th>标签值</th></tr>
	<tr><td>dept</td><td>ecommerce</td></tr>
	<tr><td>business</td><td>mkt</td></tr>
	<tr><td>owner</td><td>zhangsan</td></tr>
</table>


类似的，其他队列资源也可以根据其使用部门、业务范围和负责人的不同设置其对应的标签。

### 在 TDMQ RabbitMQ 版控制台设置标签

以上文场景为例，当您完成标签键和标签值的设计后，可以登录 TDMQ RabbitMQ 版控制台进行标签的设置。

1. 登录 [TDMQ RabbitMQ 版控制台](https://console.cloud.tencent.com/tdmq/rabbit-cluster)。
2. 在集群管理列表页面，选择好地域后，勾选需要编辑标签的集群，单击页面上方的**编辑资源标签**。
   ![](https://main.qcloudimg.com/raw/2579fb5e9729b03adcdc57f78cf832bf.png)
3. 在弹出的 “编辑标签” 窗口中设置标签。
   例如：为 amqp-78383dp8p8w1 集群添加三组标签。
   ![](https://main.qcloudimg.com/raw/11381698a0bbbc24f9f3ec7e4e8701e5.png)
>?如现有标签不符合您的要求，请前往 [标签管理](https://console.cloud.tencent.com/tag/taglist) 新建标签。
4. 单击**确定**，系统出现修改成功提示，在集群的资源标签栏可查看与之绑定的标签。
  ![](https://main.qcloudimg.com/raw/47247075b0d2a13aa989853df36b7129.png)


### 通过标签键筛选资源

当您希望筛选出绑定了相应标签的集群时，可通过以下操作进行筛选。

1. 在页面右上方搜索框中，选择**标签**。
2. 在**标签：**后弹出的窗口中选择您要搜索的标签，单击**确定**进行搜索。
   例如：选择 `标签：owner:zhangsan` 可筛选出绑定了标签键 `owner:zhangsan` 的集群。
   ![](https://main.qcloudimg.com/raw/b90b02dcdb4be7171cacab02a218d992.png)
