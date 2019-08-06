
## 操作场景
当企业需要管理 AWS 资源时，管理员可以在 IDaaS 控制台的“应用管理”模块添加 AWS 控制台应用。本文将介绍 AWS 控制台的配置方法及相关注意事项。配置成功后，您的企业用户即可以角色身份登录 AWS 控制台，管理 AWS 资源。 （AWS 角色描述请参见 [角色术语和概念](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_roles_terms-and-concepts.html)）

## 前提条件
- 您的腾讯云账号已开通 IDaaS 服务。详情请参见 [开通服务](https://cloud.tencent.com/document/product/1106/36332)。
- 您已有 AWS 账号，并有权限管理 IAM。

## 操作步骤
### 创建 AWS 控制台应用
1. 管理员登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)。
2. 在左侧导航栏中，单击【应用管理】，进入应用管理页面。
3. 单击【新建应用】，选择【库应用程序】>【Amazon Web Service】，并填写应用名称和应用详情。单击【提交】，完成 AWS 控制台应用的创建。
4. 单击【下载】，下载元数据文件。
![](https://main.qcloudimg.com/raw/d2c8d59fc3475645a45409293d995246.png)

### 配置身份提供商和角色
1. 登录 AWS，前往 [IAM 控制台](https://console.aws.amazon.com/iam/home)。在左侧导航栏中，单击【身份提供商】，进入身份提供商页面。
2. 单击【新建提供商】，填写提供商基本信息，在元数据文档处上传已下载的元数据文件。单击【下一步】，确认信息并单击【完成】。
![](https://main.qcloudimg.com/raw/0ee841f7a6cc6d208b655a1c3c9d71c1.png)
3. 在左侧导航栏中，单击【角色】，进入角色页面。单击【创建角色】，选择【SAML2.0 身份联合】。
4. 选择第2步创建的身份提供商，并勾选【允许编程访问和AWS管理控制台访问】。您可以根据实际需要添加使用条件。
![](https://main.qcloudimg.com/raw/257fbb8df777c6351573c32971999a4a.png)
5. 单击【下一步】，为角色设置预设策略。
6. 单击【下一步】，添加标签（可选）。
7. 单击【下一步】，设置角色名称，并完成创建。

### 配置腾讯云应用属性值
1. 返回 AWS 应用配置页面，配置属性。腾讯云 IDaaS 已基本预设好属性和属性值，您只需补充如下图中红框部分的内容：
![](https://main.qcloudimg.com/raw/7164950e4e522f8e7a9341f18f7b94ac.png)
2. 替换`https://aws.amazon.com/SAML/Attributes/Role`属性的值，替换规则如下：
	- `<AccountID>`替换为 AWS 账号 ID，可前往 [IAM 控制台](https://console.aws.amazon.com/iam/home)  查看。
	- `<RoleName>`替换为您在角色页面创建的角色名，可前往 [角色控制台](https://console.aws.amazon.com/iam/home#/roles) 查看。
	- `<ProviderName>`替换为您在身份提供商页面创建的角色名，可前往 [身份提供商控制台](https://console.aws.amazon.com/iam/home#/providers) 查看。
	
	
### 测试并分配权限
1. 为应用关联一个用于测试的用户，详情请参见 [管理应用权限](https://cloud.tencent.com/document/product/1106/36361)。
2. 测试用户登录 IDaaS 企业门户，尝试访问 AWS 应用。
3. 若访问成功即可关联其他用户，设置应用访问权限。
>?如果访问不成功，请检查您是否按照文档步骤填写正确的信息。
