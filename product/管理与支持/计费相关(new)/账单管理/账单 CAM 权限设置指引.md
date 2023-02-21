## 操作场景
该任务指导您通过访问管理（Cloud Access Management，CAM）控制台，给子账号（子用户/协作者）授予计费相关读写权限，实现子账号权限的精细化管理。


## 计费相关策略[](id:1)
<table>
<thead>
<tr>
<th><strong>策略名</strong></th>
<th width="15%"><strong>描述</strong></th>
<th><strong>介绍</strong></th>
<th><a href="https://cloud.tencent.com/document/product/598/10600">策略类型</a></th>
</tr>
</thead>
<tbody><tr>
<td>QcloudFinanceBillReadOnlyAccess</td>
<td>财务账单只读访问权限</td>
<td>子用户/协作者只有主 UIN 及主 UIN 的成员账号的财务账单只读权限，没有“存储账单数据”、“确认账单”、“申请盖章”、“设置/取消分账标签”权限。<br><strong>说明：</strong><br>如果子用户/协作者在2021-07-29前关联过 QCloudResourceFullAccess 策略，需先解除再重新绑定 QCloudResourceFullAccess 策略，否则此策略会默认拒绝所有财务权限。</td>
<td>预设策略</td>
</tr>
<tr>
<td>QcloudFinanceBillFullAccess</td>
<td>财务账单全读写访问权限</td>
<td>子用户/协作者拥有主 UIN 及主 UIN 的成员账号的财务账单读写权限。<br><strong>说明：</strong><br>1. 如果子用户/协作者在2021-07-29前关联过 QCloudResourceFullAccess 策略，需先解除再重新绑定 QCloudResourceFullAccess 策略，否则此策略会默认拒绝所有财务权限。<br>2. 如果要允许子用户/协作者设置“存储账单数据”权限，还需同时赋予子用户/协作者以下权限策略：<br>QcloudCOSGetServiceAccess（访问 COS 桶列表权限）<br>QcloudCamSubaccountsAuthorizeRoleFullAccess（获取 CAM 服务角色授权）</td>
<td>预设策略</td>
</tr>
<tr>
<td>QCloudFinanceFullAccess</td>
<td>全局财务权限</td>
<td>子用户/协作者拥有计费财务相关权限，包括主 UIN 及主 UIN 的成员账号的财务权限，例如：付款、开票。</td>
<td>预设策略</td>
</tr>
<tr>
<td>AdministratorAccess</td>
<td>管理员权限</td>
<td>子用户/协作者拥有主账户内所有用户及其权限、财务相关的信息、资源权限。</td>
<td>预设策略</td>
</tr>
<tr>
<td>DescribeAccountBalance</td>
<td>计费账户余额只读权限</td>
<td>子用户/协作者只有主 UIN 及主 UIN 的成员账号的账户余额只读权限，没有付款、开票等其他财务权限。</td>
<td>自定义策略</td>
</tr>
<tr>
<td>DescribeIncomeExpensesList</td>
<td>查看收支明细</td>
<td>子用户/协作者只有主 UIN 及主 UIN 的成员账号的收支明细只读权限，没有其他财务权限。</td>
<td>自定义策略</td>
</tr>
<tr>
<td>DescribeVoucherList</td>
<td>获取代金券列表</td>
<td>子用户/协作者只有主 UIN 的代金券只读权限，没有其他财务权限。</td>
<td>自定义策略</td>
</tr>
</tbody></table>



## 操作步骤

<dx-alert infotype="explain" title="">
 - 通过用户/用户组关联策略，者通过策略关联用户/用户组，两种方式仅操作入口有区别，实现的功能无区别。
- 更多详细操作指引，请参见 CAM 文档中的 [CAM 授权管理](https://cloud.tencent.com/document/product/598/10602)。
</dx-alert>


<dx-tabs>
::: 通过用户/用户组关联策略

### 创建子用户/协作者

具体操作请参见 CAM 文档中的 [新建子用户](https://cloud.tencent.com/document/product/598/13674) / [新建协作者](https://cloud.tencent.com/document/product/598/36618)。

### 关联策略

1. 在 [CAM 用户列表](https://console.cloud.tencent.com/cam) 页面，找到需要授权的子用户/协作者，单击操作列的**授权**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9ac33093de0d0365ba7259605c43fd66.png)
2. 在“关联策略”窗口中，输入“财务账单”后搜索，在结果中勾选 [计费相关策略](#1)（如 “QcloudFinanceBillReadOnlyAccess”），并单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/40296a964e5d0342804bb492fd693b68.png)

:::
::: 通过策略关联用户/用户组

1. 登录访问管理控制台，选择左侧导航栏中的 **[策略](https://console.cloud.tencent.com/cam/policy)**。
2. 在“策略”页面选择**新建自定义策略**，并在弹出的“选择创建策略方式”窗口中选择**按策略生成器创建**。
3. 在“按策略生成器创建”页面中，参考以下信息新建策略：
  1. 在“编辑策略”步骤中，主要参数配置如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/620a7bc6b5b5838b53fba6b25cf831eb.png)
     - **效果（Effect）**：选择**允许**。
     - **服务（Service）**：选择**财务（finance）**。
     - **操作（Action）**：搜索并选择相关策略。本文以“读操作”中的 DescribeAccountBalance 获取账户余额策略为例，其他策略可参考  [计费相关策略](#1)。
     - **资源（Resource）**：选择**全部资源**。
  2. 单击**下一步**。
  3. 在“关联用户/用户组/角色”步骤中，单击**选择用户**或**选择用户组**，在弹出窗口中选择对应用户/用户组后，单击**确定**。
  4. 单击**完成**，即可完成策略设置。


:::
</dx-tabs>




