
## 相关概念
#### 角色
[角色（Role）](https://cloud.tencent.com/document/product/598/19420)是腾讯云 [访问管理（Cloud Access Management，CAM）](https://cloud.tencent.com/document/product/598/10583)提供的拥有一组权限的虚拟身份，角色也可被授予策略，主要用于对 [角色载体](https://cloud.tencent.com/document/product/598/19421#.E8.A7.92.E8.89.B2.E8.BD.BD.E4.BD.93) 授予腾讯云中服务、操作和资源的访问权限，这些权限附加到角色后，通过将角色赋予腾讯云的服务，允许服务代替用户完成对授权资源的操作。腾讯云云函数 SCF 的角色分为**配置角色**和**运行角色**，您可以通过使用配置角色使 SCF 在服务配置流程中访问用户资源；也可以通过使用运行角色，为运行代码申请临时授权，便于代码通过角色的授权机制实现权限打通和资源访问。

#### 策略
[策略](https://cloud.tencent.com/document/product/598/10601) 是定义和描述一条或多条权限的语法规范。CAM 支持两种类型的策略，预设策略和自定义策略。预设策略是由腾讯云创建和管理的一些常见的权限集合，如超级管理员、云资源管理员等，这类策略只读不可写。自定义策略是由用户创建的更精细化的描述对资源管理的权限集合。预设策略不能具体描述某个资源，粒度较粗，而自定义策略可以灵活的满足用户的差异化权限管理需求。

#### 权限
[权限](https://cloud.tencent.com/document/product/598/10600) 是描述在某些条件下允许或拒绝执行某些操作访问某些资源。默认情况下，主账号是资源的拥有者，拥有其名下所有资源的访问权限。子账号没有任何资源的访问权限。资源创建者不自动拥有所创建资源的访问权限，需要资源拥有者进行授权。

## 操作场景
您在创建云函数 SCF 时，可能会操作部分 SCF 以外的云产品，不同的操作可能需要不同的权限，例如 COS 触发器创建和删除所需的 COS 权限、API 网关触发器创建和删除所需的 API 网关权限、COS 代码文件的 zip 包读取权限等，通过角色的配置和选择可以实现授权。

## 配置角色
配置角色用于提供 SCF 配置对接其他云上资源的相关权限，在已关联策略的权限范围内访问您的其他云服务资源，包括但不限于代码文件访问、触发器配置。配置角色的预设策略可支持函数执行基本操作，基本覆盖了 SCF 常用场景所需要的权限。

### 角色详情
SCF 默认的配置角色为 `SCF_QcsRole`，其角色详情如下：
- 角色名：`SCF_QcsRole` 
- 角色载体：`产品服务-scf.qcloud.com`
- 角色描述：SCF 默认配置角色。该服务角色用于提供 SCF 配置对接其他云上资源的权限，包括但不限于代码文件访问、触发器配置。配置角色的预设策略可支持函数执行的基本操作。
- 角色已关联策略：此角色所拥有 `QcloudAccessForScfRole` 策略，具备以下功能：
 - 配置 COS 对象存储触发器时向 Bucket 配置中写入触发配置信息。 
 - 读取 COS 对象存储 Bucket 中的触发器配置信息。 
 - 在使用 COS 对象存储更新代码时，从 Bucket 完成代码 zip 包的读取操作。 
 - 配置 API 网关触发器时，完成 API 网关的服务、API 创建，以及服务发布等操作。 
 - 配置和使用日志服务 CLS 的读写访问等操作。
 - 配置和使用消息队列 CMQ 的读写访问等操作。
 - 配置和使用消息队列 Ckafka 的创建、列表等操作。

>!用户可前往 [CAM 控制台](https://console.cloud.tencent.com/cam/overview) 查看并修改当前配置角色 `SCF_QcsRole` 所关联的策略，但修改角色的关联策略可能会造成 SCF 无法正常执行等问题，故不建议修改。
>

### 服务授权
1. 如果您是首次使用 SCF，打开 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=1) 时会提示您进行服务授权。如下图所示：
![](https://main.qcloudimg.com/raw/e2c9a7755b2f1f1671a6cc12f47bdef6.png)

2. 选择**前往访问管理**进入“角色管理”页面，单击**同意授权**确认授权。如下图所示：
![](https://main.qcloudimg.com/raw/59611885715e48011cc4e7de393efa1c.png)

3. 确认授权后，将会为您自动创建角色 `SCF_QcsRole`。可在 [角色](https://console.cloud.tencent.com/cam/role) 中查看。如下图所示：
![](https://main.qcloudimg.com/raw/9702d15f8ade526bf55cb836be360ef7.png)

## 运行角色
运行角色服务于用户代码，角色载体为`产品服务-scf.qcloud.com`。用户为函数添加对应的运行角色后，SCF 在运行角色已关联策略的权限范围内为用户的运行代码申请临时授权，便于代码通过角色的授权机制实现权限打通和其他云上资源访问。
以 `SCF_QcsRole` 为例，用户也可以选择 `SCF_QcsRole` 作为函数的运行角色，这意味着将 `SCF_QcsRole` 关联策略对应的权限授权给 SCF，使 SCF 获得为用户代码申请访问其他云上资源的权利。

### 创建运行角色
1. 登录 SCF 控制台，选择左侧导航栏中的 **[函数服务](https://console.cloud.tencent.com/scf)**。
2. 在“函数服务”列表页面，单击需创建运行角色的函数名，进入函数配置页。
3. 选择函数配置页右上角的**编辑**。
4. 勾选“运行角色”中的**启用**，并单击**新建运行角色**。如下图所示：
![](https://main.qcloudimg.com/raw/c8d4e42e246ae3bab15db83c9f7e44df.png)
5. 在“输入角色载体信息”步骤中勾选**云函数（scf）**，并单击**下一步**。
![](https://main.qcloudimg.com/raw/61f45843b7a52b8edb1432c17618ff3c.png)
6. 在“配置角色策略”步骤中，选择函数所需策略并单击**下一步**。如下图所示：
>? 本文以选择 `QcloudCOSFullAccess` 对象存储（COS）全读写访问权限为例，请根据实际需求进行选择。
>
![](https://main.qcloudimg.com/raw/f4b2f40ca703f033e61f8a1911e7991e.png)
7. 在“审阅”步骤中填写“角色名称”，并单击**完成**。本文以 `scf_cos_full_access` 角色名称为例。 
8. 返回函数配置页，单击“运行角色”右侧的<img src="https://main.qcloudimg.com/raw/b32932fe6f9afabb88280c38bb287887.png" style="margin:-3px 0px">，即可在下拉列表中选择刚创建的运行角色。如下图所示：
![](https://main.qcloudimg.com/raw/f891ccabd030dfafd3119d10f28b42ea.png)
>! 在为运行角色添加策略时，除了选择预置策略外，还可以通过自定义策略的方式做更细粒度的权限划分，SCF 的策略语法遵循 CAM 的 [语法结构](https://cloud.tencent.com/document/product/598/10604) 和 [资源描述方式](https://cloud.tencent.com/document/product/598/10606)，策略语法以 JSON 格式为基础，具体可参考 [SCF 策略语法](https://cloud.tencent.com/document/product/583/47934)。
>

### 使用运行角色获取环境变量
在函数运行时，SCF 服务将会使用选定的运行角色完成临时 SecretId、SecretKey、SesstionToken 的申请，并以环境变量的形式将相关内容传递到运行环境中。如下图所示：
![](https://main.qcloudimg.com/raw/04d1d326e4a383d44c4d019a2207ba6e.png)
以 Python 为例，您可以通过如下代码将上述信息传递到函数运行环境中，并以环境变量的方式获取。
```python
secret_id = os.environ.get('TENCENTCLOUD_SECRETID')
secret_key = os.environ.get('TENCENTCLOUD_SECRETKEY')
token= os.environ.get('TENCENTCLOUD_SESSIONTOKEN')
```
