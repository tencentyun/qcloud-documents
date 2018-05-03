您可以通过子帐号实现不同的人管理不同的服务。默认情况下，子帐号在使用 TSF 的部分功能时会受限，因为 TSF 会访问其他产品（如 CVM 等）的资源，因此需要主帐号授权子帐号可以传递指定角色（Pass Role）到 TSF。

关于腾讯云访问管理及用户身份的说明请参考 [腾讯云访问管理](https://cloud.tencent.com/document/product/598) 和 [腾讯云用户管理介绍](https://cloud.tencent.com/document/product/598/13665)。

## 子账号使用 TSF 的准备工作

当主账号希望授权子账号（或协作者）使用 TSF 时，需要将下面的策略关联到子账号（或协作者）。步骤如下：

### 1. 新建 tsf_PassRole 策略
1.1 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。
1.2 单击左侧导航栏的 **策略管理**。
![](https://main.qcloudimg.com/raw/26fc2bc64a06e312d9c567a4738e331a.png)
1.3 单击【新建自定义策略】。
![](https://main.qcloudimg.com/raw/9e50eb9b644c1e4b560e786ad36c697d.png)
1.4 单击【按策略语法创建】。
![](https://main.qcloudimg.com/raw/e26002f8c16eca54a76edaf4e50aaf1b.png)
1.5 选择【空白模板】，单击下一步。
![](https://main.qcloudimg.com/raw/da7849eb16acf32e084beef40784e1dc.png)
1.6 填写策略名（ 如 tsf_PassRole ），填写策略内容如下，其中 `${roleOwnerUin}` 使用主账号的账号 ID。

```
{
	"version": "2.0",
	"statement": [
			{
					"effect": "allow",
					"action": "cam:PassRole",
					"resource": "qcs::cam::uin/${roleOwnerUin}:roleName/TSF_QCSRole"
			}
	]
}
```
![](https://main.qcloudimg.com/raw/c573361bd5d497c5fa2b5aadd733c146.png)
### 2. 将  tsf_PassRole 策略绑定到子账号

2.1 单击左侧导航栏 **用户管理**。
![](https://main.qcloudimg.com/raw/f56790ed7836fd4ae255f342125c09f3.png)
2.2 选择要授予 TSF 使用权限的用户。
![](https://main.qcloudimg.com/raw/f56790ed7836fd4ae255f342125c09f3.png)
2.3 单击【关联策略】。
![](https://main.qcloudimg.com/raw/e8c8994b8655db02dcfeeb89638b7c5e.png)
2.4 从策略列表中筛选出步骤 1.6 中的创建的策略（ 如 `tsf_PassRole`） 。
![](https://main.qcloudimg.com/raw/bada6e84ee25c9fb8a67785476341f5d.png)
2.5 绑定策略后，策略显示在用户的策略列表中。
![](https://main.qcloudimg.com/raw/325a4006966f715aec2861357668c3a1.png)

## 其他资源访问授权

TSF 产品需要获取用户的 VPC 、CVM 、Ckafka 等信息，需要主账号将相关的资源权限授权给子账号。

当子账号使用 TSF 时，弹出如下提示框时，表示 TSF 需要调用其他产品的云 API 获取信息。例如下图显示 TSF 依赖 CKafka 的 ListInstance 接口。

![](https://main.qcloudimg.com/raw/a653f0e7b2df62ba16c9e7be31adb895.png)

此时需要 **主账号** 用户去腾讯云 [访问管理](https://console.cloud.tencent.com/cam) 控制台给子账号添加对应服务的权限。具体指引可参考 [访问管理](https://cloud.tencent.com/document/product/598) 产品文档。


