
## 操作场景
很多企业客户会在企业内部构建 IT 系统来管理员工子账号申请的流程，当企业内有多个账号时，将集团账号和 CAM 结合使用能够大幅提升管理的效率和安全性。

假设存在以下条件：
- 公司已有账号 A，作为管理账号开通了集团账号管理产品。
- 在账号 A 下有 CAM 子用户 a，具有全部管理权限。
- 在公司内有游戏业务负责人小王，想要申请一个新的主账号来运行新发布的游戏，并为开发员工小李在该主账号申请一个具有开发权限的子用户，用于日常登录访问腾讯云。


## 流程说明
通过 CAM 子用户 a 的密钥来完成整个主账号创建以及子账号申请和授权的流程。

流程1：为新游戏申请主账号
![](https://qcloudimg.tencent-cloud.cn/raw/f6b21aa24a0e3b12634c0dbe299c14b8.png)

流程2：为开发员工小李创建 CAM 子账号并授权
![](https://qcloudimg.tencent-cloud.cn/raw/a82ec6172be6bea8e538d792f685551a.png)       


## 操作步骤
### 使用管理子用户 a 为新业务创建账号

1. 调用集团账号管理产品的 [CreateOrganizationMember ](https://cloud.tencent.com/document/product/850/63310) API，创建新的主账号。
>?
>- 创建的主账号为使用集团管理账号的实名信息，自动完成企业实名认证。
>- 创建的主账号，管理账号会自动具有管理权限。
>- 同时也可以为新创建的账号分配财务管理权限 ，当前支持五类权限：查看成员账号的账单、查看成员账号的消费、为成员账号划拨资金、为成员账号申请开具发票、合并出账。
>- 也可以为成员账号设置付费方式：自付费 + 优惠继承、代付费。
>- 成员财务管理说明请参考 [查看成员财务权限](https://cloud.tencent.com/document/product/850/58725)。
  

2. 通过集团账号管理 API 为集团管理子用户 a 授予管理新建的主账号的权限。
	1. 在管理账号 A 下创建对新建账号具有 admin 管理权限的策略：[CreateOrganizationMemberPolicy](https://cloud.tencent.com/document/api/850/74595)
	2. 将刚创建的策略授予管理子账号 a：[BindOrganizationMemberAuthAccount](https://cloud.tencent.com/document/api/850/63308)


3. 调用访问管理产品的 [CreatePolicy](https://cloud.tencent.com/document/product/598/34578) API，在创建的账号下，创建所需的自定义授权策略（按需执行）。
>?如使用预设策略可以满足授权需要，则可忽略该步骤。


至此，为新游戏创建账号流程已完成，如果需要同时开通多个账号，则可重复上述流程。




### 使用管理子用户 a 为员工创建 CAM 子账号
1. 调用访问管理产品的 [AddUser](https://cloud.tencent.com/document/product/598/34595) API，在创建的腾讯云账号下，创建子用户。
>?子用户的创建需要使用管理员身份，并扮演创建的成员的角色 OrganizationAccessControlRole，API 使用角色的调用可参考 [使用角色](https://cloud.tencent.com/document/product/598/19419) 文档。
2. 获取需要绑定策略的策略 ID。
 1. 在访问管理控制台的 [**策略**](https://console.cloud.tencent.com/cam/policy) 页面，通过搜索找到需要绑定的策略（以 TI-ONE 的全读写策略为例 ）。
![](https://qcloudimg.tencent-cloud.cn/raw/1f17f78add4874e5f2d218bf8b39ae96.png) 
 2. 单击策略名称，进入策略详情页，浏览器地址栏的如下位置即为策略 ID。
![](https://qcloudimg.tencent-cloud.cn/raw/9b587d8ad196392af8249b7f30c39e3b.png)    
3. 调用访问管理产品的 [AttachUserPolicy](https://cloud.tencent.com/document/product/598/34579) API，为创建的子用户授权。

