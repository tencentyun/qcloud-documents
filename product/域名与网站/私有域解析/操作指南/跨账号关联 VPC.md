## 操作场景
若您需使用账号 A 绑定账号 B 的 VPC 资源，您需要先对账号 A 进行角色授权。本文将指导您如何跨账号关联 VPC。

## 前提条件
在账号 A 中已创建私有域，如未创建，请参考 [创建私有域](https://cloud.tencent.com/document/product/1338/50532)。

## 操作指南
### 步骤1：B 账号给 A 账号进行角色授权
1. 使用 B 账号登录腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/role)，进行 “角色” 管理页面，并单击**新建角色**。如下图所示：
![](https://main.qcloudimg.com/raw/1211f0e6bab235117faeb89c3e3c19d5.png)
2. 在弹出的 “选择角色载体 ”窗口中，单击**腾讯云账户**。如下图所示：
![](https://main.qcloudimg.com/raw/194aacbc920fbe9d39469ea0fc89dd00.png)
3. 在 “新建自定义角色” 页面，填写相关信息并单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/6a6c61d5038119965c4c930fd48a3936.png)
 - **云账号类型**：勾选**其他主账号**。
 - **账号 ID**：请输入 A 账号的账号 ID。账号 ID 获取可参考 [账号基本信息](https://cloud.tencent.com/document/product/378/11245)。
 - **外部 ID**：默认不勾选。
 - **控制台访问**：默认不勾选。
4. 进入 “配置角色策略” 步骤，查找并勾选 `QcloudVPCReadOnlyAccess` 策略，单击**下一步**。如下图所示：
![](https://main.qcloudimg.com/raw/c5d09ad1df000b33c68bd29773271104.png)
5. 进入 “审阅” 步骤，填写相关信息。如下图所示：
![](https://main.qcloudimg.com/raw/fc977bb5dddf69f257cbae94dc2f23c1.png)
 - **角色名称**：请输入 `PRIVATEDNS_ACCOUNT_被授权 UIN`。例如 `PRIVATEDNS_ACCOUNT_88888888`。
 - **角色描述**：请输入相关描述。
6. 单击**完成**，即可完成角色授权操作。

### 步骤2：A 账号添加 B 账号为关联账号
1. 使用 A 账号登录 [私有域解析 Private DNS 控制台](https://console.cloud.tencent.com/privatedns/domains)，进入 “私有域列表” 管理页面。
2. 在 “私有域列表” 管理页面，选择需要授权的私有域，单击**关联 VPC**。如下图所示：
![](https://main.qcloudimg.com/raw/e7f693f0cc73a844b075a32195c47ac8.png)
3. 在弹出的 “修改关联 VPC” 窗口中，单击**添加账号**。如下图所示：
![](https://main.qcloudimg.com/raw/b6757bdc378ed43927339e70091c3100.png)
4. 在弹出的 “添加账号” 窗口中，输入 B 账号的账号 ID 并单击**确定**。如下图所示：
>?账号 ID 获取可参考 [账号基本信息](https://cloud.tencent.com/document/product/378/11245)。
>
![](https://main.qcloudimg.com/raw/c29bdf2da3bffd072d26e5041fdc93ce.png)
5. 关联成功后，即可对本账号 VPC 或关联账号的 VPC 进行关联或修改等操作。




