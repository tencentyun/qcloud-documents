## 操作场景

**标签**是腾讯云提供的用于标识云上资源的标记，是一个键-值对（Key-Value）。标签可以帮助您从各种维度（例如业务、用途、负责人等）方便地对 TDMQ CMQ 版资源进行分类管理。
>?腾讯云不会使用您设定的标签，标签仅用于您对 TDMQ CMQ 版资源的管理。

## 使用限制

使用标签时，需注意以下限制条件：

| 限制类型 | 限制说明 | 
|---------|---------|
| 数量限制 |每个云资源允许的最大标签数是50。|
| 标签键限制 | <li>`qcloud`、`tencent`、`project` 开头为系统预留标签键，禁止创建。</li><li> 只能为`数字`、`字母`、`+=.@-`，且标签键长度最大为255个字符。</li>|
| 标签值限制 |只能为`空字符串或数字`、`字母`、`+=.@-`，且标签值最大长度为127个字符。|

## 操作方法及案例

### 案例描述

案例：某公司在腾讯云上拥有6个 TDMQ CMQ 版队列服务，这6个队列的使用部门、业务范围以及负责人的信息如下：

| 队列 ID           | 使用部门 | 业务范围 | 负责人 |
| ----------------- | -------- | -------- | ------ |
| cmqq-372ovdpw8ob1 | 电商     | 营销活动 | 张三   |
| cmqq-372ovdpw8ob2 | 电商     | 营销活动 | 王五   |
| cmqq-372ovdpw8ob3 | 游戏     | 游戏 A   | 李四   |
| cmqq-372ovdpw8ob4 | 游戏     | 游戏 B   | 王五   |
| cmqq-372ovdpw8ob5 | 文娱     | 后期制作 | 王五   |
| cmqq-372ovdpw8ob6 | 文娱     | 后期制作 | 张三   |

以 cmqq-372ovdpw8ob1 为例，我们可以给该实例添加以下三组标签 ：

<table id="table02">
	<tr><th>标签键</th><th>标签值</th></tr>
	<tr><td>dept</td><td>ecommerce</td></tr>
	<tr><td>business</td><td>mkt</td></tr>
	<tr><td>owner</td><td>zhangsan</td></tr>
</table>


类似的，其他队列资源也可以根据其使用部门、业务范围和负责人的不同设置其对应的标签。

### 在 TDMQ CMQ 版控制台设置标签

以上文场景为例，当您完成标签键和标签值的设计后，可以登录 TDMQ CMQ 版控制台进行标签的设置。

1. 登录 [TDMQ CMQ 版控制台](https://console.cloud.tencent.com/tdmq/cmq-queue)。
2. 在队列服务列表页面，选择好地域后，勾选需要编辑标签的队列，单击页面上方的**编辑资源标签**。
   ![](https://main.qcloudimg.com/raw/98091abb3b806a2fc0a3656b949c1470.png)
3. 在弹出的 “编辑标签” 窗口中设置标签。
   例如：为 cmqq-372ovdpw8ob1 的队列添加三组标签。
   ![](https://main.qcloudimg.com/raw/11381698a0bbbc24f9f3ec7e4e8701e5.png)
>?如现有标签不符合您的要求，请前往 [标签管理](https://console.cloud.tencent.com/tag/taglist) 新建标签。
4. 单击**确定**，系统出现修改成功提示，在队列的资源标签栏可查看与之绑定的标签。
 ![](https://main.qcloudimg.com/raw/cd1a0daca2d94503ec9062030e1075e5.png)


### 通过标签键筛选资源

当您希望筛选出绑定了相应标签的队列时，可通过以下操作进行筛选。

1. 在 [队列服务](https://console.cloud.tencent.com/tdmq/cmq-queue?rid=1) 页面右上方搜索框中，选择**标签**。
2. 在**标签：**后弹出的窗口中选择您要搜索的标签，单击**确定**进行搜索。
   例如：选择`标签：owner:zhangsan`可筛选出绑定了标签键 `owner:zhangsan` 的队列。
   ![](https://main.qcloudimg.com/raw/75fa474269963006d44710f07e3b8ecf.png)
