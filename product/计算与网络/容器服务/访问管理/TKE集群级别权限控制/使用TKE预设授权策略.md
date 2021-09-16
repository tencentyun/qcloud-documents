本文介绍腾讯云容器服务 TKE 的预设策略，及如何将子账号关联预设策略，授予子账号特定权限。您可参考文本并根据实际业务诉求进行配置。

## TKE 预设策略
您可以使用以下预设策略为您的子账号授予相关权限：

| 策略 | 描述 |
|------- |--------|
|`QcloudTKEFullAccess` | TKE 全读写访问权限，包括 TKE 及相关云服务器、负载均衡、私有网络、监控及用户组权限。 |
|`QcloudTKEInnerFullAccess`| TKE 全部访问权限， TKE 涉及较多产品，建议您配置 `QcloudTKEFullAccess` 权限。 |
|`QcloudTKEReadOnlyAccess` |TKE 只读访问权限。|

以下预设策略是在您使用 TKE 服务时，授予 TKE 服务本身的权限。不建议为子账号关联以下预设策略：

| 策略 | 描述 |
|------- |--------|
|`QcloudAccessForCODINGRoleInAccessTKE` |授予 Coding 服务 TKE 相关权限。|
|`QcloudAccessForIPAMDofTKERole` |授予 TKE 服务弹性网卡相关权限。|
|`QcloudAccessForIPAMDRoleInQcloudAllocateEIP` |授予 TKE 服务弹性公网 IP 相关权限。|
|`QcloudAccessForTKERole` | 授予 TKE 服务云服务器、标签、负载均衡、日志服务相关权限。|
|`QcloudAccessForTKERoleInCreatingCFSStorageclass`|授予 TKE 服务文件存储相关权限。|
|`QcloudAccessForTKERoleInOpsManagement` |该策略关联 TKE 服务角色（TKE_QCSRole），用于 TKE 访问其他云服务资源，包含日志服务等相关操作权限。|


## 子账号关联预设策略
您可在创建子账号的“设置用户权限”步骤中，通过 [直接关联](#direct) 或 [随组关联](#byGroup) 方式，为该子账户关联预设策略。



### 直接关联[](id:direct)

您可以直接为子账号关联策略以获取策略包含的权限。

1. 登录访问管理控制台，选择左侧导航栏中的**用户** > **[用户列表](https://console.cloud.tencent.com/cam)**。
2. 在“用户列表”管理页面，选择需要设置权限的子账号所在行右侧的**授权**。
3. 在弹出的“关联策略”窗口中，勾选需授权的策略。
4. 单击**确定**即可。


### 随组关联[](id:byGroup)

您可以将子账号添加至用户组，该子账号将自动获取该用户组所关联策略的权限。如需解除随组关联策略，仅需将子账号移出相应用户组即可。

1. 登录访问管理控制台，选择左侧导航栏中的**用户** > **[用户列表](https://console.cloud.tencent.com/cam)**。
2. 在“用户列表”管理页面，选择需要设置权限的子账号所在行右侧的**更多操作** > **添加到组**。
3. 在弹出的“添加到组”窗口中，勾选需加入的用户组。
4. 单击**确定**即可。


### 登录子账号验证

登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，验证可使用所授权策略对应功能，则表示子账号授权成功。





