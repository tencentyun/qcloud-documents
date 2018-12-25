您可以通过子帐号实现不同的人管理不同的服务。默认情况下，子帐号在使用 TSF 的部分功能时会受限，因为 TSF 会访问其他产品（如 CVM 等）的资源，因此需要主帐号授权子帐号可以传递指定角色（Pass Role）到 TSF。
关于腾讯云访问管理及用户身份的说明请参考 [腾讯云访问管理](https://cloud.tencent.com/document/product/598) 和 [腾讯云用户管理介绍](https://cloud.tencent.com/document/product/598/13665)。

由于 TSF 需要访问其他云产品的 API（如 TKE 等），所以需要授权 TSF 创建服务角色。TSF 有两种方法创建服务角色：

- 主账号访问 [TSF 概览页 >> ](https://console.cloud.tencent.com/tsf?rid=1)  会自动创建 TSF 相关服务角色，角色名  `TSF_QCSRole`

- 具有 QcloudCamRoleFullAccess 策略的用户可以在 CAM 产品控制台创建 TSF 相关服务角色，角色名由用户自定义（不能是 TSF_QCSRole）

下面介绍在 CAM 产品页面创建 TSF 相关服务角色的步骤。

## <span id="des">创建 TSF 相关服务角色</span>

1. 登录 CAM 控制台，进入[角色界面](https://console.cloud.tencent.com/cam/role)。

2. 单击【新建角色】。

3. 选择 **腾讯云产品服务**，参考下图设置角色相关信息。

   - 选择【分布式服务治理平台】

   ![](https://main.qcloudimg.com/raw/f0e5c438beeedcdbc5ea8ea4538ef812/1.png)

   - 选择预设策略 QcloudAccessForTSFRole

     ![](https://main.qcloudimg.com/raw/939876b2ccb4cf7d26da3830aa1665a2/2.png)

   - 填写角色名称 TSF-DefaultRole

     ![](https://main.qcloudimg.com/raw/65252bbd43280f4d0e7599db93916f1b/3.png)



## 向协作者或子账号授予 PassRole 策略

协作者或者子账号使用 TSF 时，需要主账号授予 PassRole 策略，传递的角色（Role）就是上文中创建的角色。

> **注意：** 如果协作者或者子账号在不具备 **PassRole** 策略的情况下尝试使用 TSF 相关功能，会收到错误 role not exist。

要将角色（及其许可策略）传递至 TSF 服务，用户必须具有 **传递角色** 至服务的许可。这有助于管理员确保仅批准的用户可配置具有能够授予许可的角色的服务。


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
1.6 填写策略名（ 如 tsf_PassRole ），填写策略内容如下，其中 `<roleOwnerUin>` 使用主账号的账号 ID，`<roleName>` 根据角色创建的方式有所不同：

- 主账号单击 TSF 概览页自动创建，roleName 填写 TSF_QCSRole
- 在 CAM 控制台角色界面，手动创建角色，填写自定义角色名，参考上文  [创建 TSF 相关服务角色](#des) 中创建的角色 TSF-DefaultRole

```text
{
	"version": "2.0",
	"statement": [
			{
					"effect": "allow",
					"action": "cam:PassRole",
					"resource": "qcs::cam::uin/<roleOwnerUin>:roleName/<roleName>"
			}
	]
}
```
![](https://main.qcloudimg.com/raw/c573361bd5d497c5fa2b5aadd733c146.png)

### 2. 将  tsf_PassRole 策略绑定到用户

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

## 用户使用镜像相关功能
用户要使用镜像功能，需要被授予 CCR 相关权限。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。
2. 单击左侧导航栏 **用户管理**。
![](https://main.qcloudimg.com/raw/f56790ed7836fd4ae255f342125c09f3.png)
3. 选择要授予 TSF 使用权限的用户。
![](https://main.qcloudimg.com/raw/f56790ed7836fd4ae255f342125c09f3.png)
4. 单击【关联策略】。
![](https://main.qcloudimg.com/raw/e8c8994b8655db02dcfeeb89638b7c5e.png)
5. 从策略列表中选择 `QcloudCCRFullAccess` 策略。
![](https://main.qcloudimg.com/raw/d9c6a36f4cbc362f23d0d0a4fe8a8a4f.png)
6. 绑定策略后，策略显示在用户的策略列表中。
![](https://main.qcloudimg.com/raw/850ce1e93101cdd98899d66a1468fd60.png)

## 其他资源访问授权

TSF 产品需要获取用户的 VPC 、CVM 、Ckafka 等信息，需要主账号将相关的资源权限授权给用户。
当用户使用 TSF 时，弹出如下提示框时，表示 TSF 需要调用其他产品的云 API 获取信息。例如下图显示 TSF 依赖 CKafka 的 ListInstance 接口。
![](https://main.qcloudimg.com/raw/a653f0e7b2df62ba16c9e7be31adb895.png)
此时需要 **主账号** 用户去腾讯云 [访问管理](https://console.cloud.tencent.com/cam) 控制台给用户添加对应服务的权限。具体指引可参考 [访问管理](https://cloud.tencent.com/document/product/598) 产品文档。


### 访问镜像仓库
如果主账号未开通过镜像仓库，会提示如下图所示信息，此时需要主账号登录 TSF 控制台，开通镜像仓库。主账号开通镜像仓库后协作者/子账号才能继续使用镜像仓库。
![](https://main.qcloudimg.com/raw/245c87613aa7bb17c05f1955bd7de3c5.png)
