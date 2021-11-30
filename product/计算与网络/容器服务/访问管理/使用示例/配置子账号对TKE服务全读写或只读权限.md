## 操作场景

您可以通过使用访问管理（Cloud Access Management，CAM）策略让用户拥有在容器服务（Tencent Kubernetes Engine，TKE）控制台中查看和使用特定资源的权限。本文档中的示例指导您在控制台中配置部分权限的策略。

## 操作步骤

### 配置全读写权限
1. 登录访问管理控制台，选择左侧导航栏中的 **[策略](https://console.cloud.tencent.com/cam/policy)**。
2. 在“策略”管理页面，选择 **QcloudTKEFullAccess** 策略行的**关联用户/组**。如下图所示：
![](https://main.qcloudimg.com/raw/7cde595023f9fda17ae3e1e2ae02bc65.png)
3. 在弹出的“关联用户/用户组”窗口中，勾选需对 TKE 服务拥有全读写权限的账号，单击**确定**，即可完成子账号对 TKE 服务全读写权限的配置。
5. 在策略管理页面中，单击 **QcloudTKEFullAccess** 策略行的**关联用户/组**。
6. 在弹出的“关联用户/用户组”窗口中，勾选需对镜像仓库拥有全读写权限的账号，并单击**确定**，即可完成子账号对镜像仓库全读写权限的配置。
>? 如果您需要使用镜像仓库的触发器和自动构建功能，还需额外配置容器服务-持续集成（CCB）的相关权限。

### 配置只读权限
1. 登录访问管理控制台，选择左侧导航栏中的 **[策略](https://console.cloud.tencent.com/cam/policy)**。
2. 在“策略”管理页面，选择 **QcloudTKEReadOnlyAccess** 策略行的**关联用户/组**。如下图所示：
![](https://main.qcloudimg.com/raw/f2c2a0b9282f0e3d0c40be313801c1fc.png)
4. 在弹出的“关联用户/用户组”窗口中，勾选需对 TKE 服务拥有只读权限的账号，并单击**确定**，即可完成子账号对 TKE 服务只读权限的配置。
5. 在策略管理页面中，单击 **QcloudCCRReadOnlyAccess** 策略行的**关联用户/组**。如下图所示：
![](https://main.qcloudimg.com/raw/18dd6bf93dea77deb9919274edab2e8e.png)
6. 在弹出的“关联用户/用户组”窗口中，勾选需对镜像仓库拥有只读权限的账号，并单击**确定**，即可完成子账号对镜像仓库只读权限的配置。
>? 如果您需要使用镜像仓库的触发器和自动构建功能，还需额外配置容器服务-持续集成（CCB）的相关权限。




