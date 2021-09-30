## 操作场景
该任务指导您通过 CAM 控制台，给子账号（子用户/协作者）分配财务账单只读、账单读写权限，实现子账号账单权限的精细化管理。


## 操作步骤

### 创建子用户/协作者
具体操作请参见 CAM 文档中的 [新建子用户](https://cloud.tencent.com/document/product/598/13674) / [新建协作者](https://cloud.tencent.com/document/product/598/36618)。

### 为子用户/协作者分配预设策略

1. 在 [CAM 用户列表](https://console.cloud.tencent.com/cam) 页面，找到需要授权的子用户/协作者，单击操作列的**授权**。
![](https://main.qcloudimg.com/raw/4ebbec079bc19c25e5e2f1008e5e77ca.jpg)

2. 在关联策略页面，勾选 [账单相关的预设策略](#1)（如 “QcloudFinanceBillReadOnlyAccess”），并单击**确定**。
![](https://main.qcloudimg.com/raw/b7b4565679689521ca987000409b95c5.jpg)

更多详细操作指引，请参见 CAM 文档中的 [CAM 授权管理](https://cloud.tencent.com/document/product/598/10602)。


## 账单相关的预设策略[](id:1)

| 策略名                          | 描述             | 介绍                                                         |
| ------------------------------- | ---------------- | ------------------------------------------------------------ |
| QcloudFinanceBillReadOnlyAccess | 计费账单只读权限 | 子用户/协作者只有主 uin 财务账单的只读权限，没有“存储账单数据”、“确认账单”、“申请盖章”、“设置/取消分账标签”权限。<br><br>**说明：**<li>此策略目前支持子用户/协作者对主账号的只读权限，不支持对主账号的成员账号的访问。</li><li>如果子用户/协作者原先关联过 QCloudResourceFullAccess 策略，需先解除再重新绑定 QCloudResourceFullAccess 策略。否则此策略会默认拒绝所有财务权限。</li> |
| QcloudFinanceBillFullAccess     | 计费账单读写权限 | 子用户/协作者拥有主uin财务账单读写权限。<br><br>**说明：**<li>此策略目前支持子用户/协作者对主账号的读写权限，不支持对主账号的成员账号的访问。</li><li>如果子用户/协作者原先关联过 QCloudResourceFullAccess 策略，需先解除再重新绑定 QCloudResourceFullAccess 策略。否则此策略会默认拒绝所有财务权限。</li> |
| QCloudFinanceFullAccess         | 全局财务权限     | 子用户/协作者拥有计费财务相关权限，包括主 uin 及主 uin 的成员账号的财务权限，例如：付款、开票。 |
| AdministratorAccess             | 管理员权限       | 子用户/协作者拥有主账户内所有用户及其权限、财务相关的信息、资源权限。 |
