

## 操作背景
用户在使用数据接入平台（DIP）访问 CLS、COS 等服务时，需要授权 DIP 访问用户账号下 CLS、COS 等服务的权限。如果使用 DIP 的子账号具备访问管理的策略权限（QcloudCamRoleFullAccess），在创建 DIP 任务时勾选 **角色授权 **，DIP将自动为您完成授权。否则，需要拥有管理员权限（AdministratorAccess）的用户进行相应的授权后，再使用子账号创建 DIP 任务。

![](https://qcloudimg.tencent-cloud.cn/raw/581c3db0a13a097594a697ae462d50ee.png)

## 需授权服务列表

| 需授权的服务 | 关联的角色 | 需要的策略权限 |
| --- | --- | --- |
| 日志服务（CLS） | Datahub_QcsRole | QcloudCLSFullAccess |
| 对象存储（COS） | Datahub_QcsRole | QcloudCOSFullAccess |

## 授权步骤

如果您创建 DIP 任务的子账号不具备访问管理的策略权限（QcloudCamRoleFullAccess），可能会遇到缺少 CreateRole 或 AttachRolePolicy 权限的提示。如果您的账号下还没有 Datahub_QcsRole 角色，参见 [**创建角色**](#CreateRole) 进行授权。如果账号已经拥有 Datahub_QcsRole 角色，可参见 [**授权角色**](#AttachRolePolicy) 进行授权。

[](id:CreateRole)
### 创建角色

1. 如果提示缺少 CreateRole 策略权限，需要有管理员权限（AdministratorAccess）的用户进入 **[访问管理](https://console.cloud.tencent.com/cam/role)** 控制台，角色页面，单击 **新建角色**。
![](https://qcloudimg.tencent-cloud.cn/raw/843ee5f3b7231cd4d998d9755c4d92ba.png)
2. 在**选择角色载体**页面选择腾讯云产品服务：
![](https://qcloudimg.tencent-cloud.cn/raw/d8559b28dde2a3ec3e7268e215830f6e.png)
3. 进入**输入角色载体信息**步骤，选择**消息服务（ckafka）**：
![](https://qcloudimg.tencent-cloud.cn/raw/b7e319300d48fb30834627625a4e27dc.png)
4. 在**配置角色策略**步骤，选择需要 DIP 任务访问的服务对应的策略，此处选择了 CLS、COS 对应的策略：
![](https://qcloudimg.tencent-cloud.cn/raw/ab63aa3db80d2afd07d0d20b8a9459b9.png)
5. 在**配置角色标签**步骤可以给角色配置相应的标签，此处忽略。
6. 在**审阅**步骤，将角色名称命名为 **Datahub_QcsRole**：
![](https://qcloudimg.tencent-cloud.cn/raw/f9d4c8fcb03d87973d0891de06870174.png)
创建角色成功后，子账号即可进行相应的 DIP 任务创建。

[](id:AttachRolePolicy)
### 授权角色

1. 如果提示缺少 AttachRolePolicy 策略权限，需要有管理员权限（AdministratorAccess）的用户进入 **[访问管理](https://console.cloud.tencent.com/cam/role)** 控制台，角色页面，找到服务对应的角色，此处以 Datahub_QcsRole 角色为例。
![](https://qcloudimg.tencent-cloud.cn/raw/8cb46590c4a889b0da91b439c7bcb14c.png)
2. 单击角色名称，进入角色管理详情页面，在 **权限** 一栏单击 **关联策略**：
![](https://qcloudimg.tencent-cloud.cn/raw/ff25bac71afbf31e53b342fdcf5a9e42.png)
3. 找到您需要授权的服务相关的策略，此处以 CLS 服务为例，单击**确定**完成授权：
![](https://qcloudimg.tencent-cloud.cn/raw/d15a05e14be15753ec92b3a0d296c52e.png)
4. 当该角色拥有访问相应服务的权限后，子账号就可以成功创建相应的 DIP 任务。
