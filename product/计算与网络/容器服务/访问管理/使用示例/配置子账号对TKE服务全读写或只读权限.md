## 操作场景

您可以通过使用访问管理（Cloud Access Management，CAM）策略让用户拥有在容器服务（Tencent Kubernetes Engine，TKE）控制台中查看和使用特定资源的权限。本文档中的示例指导您在控制台中配置部分权限的策略。

## 操作步骤

### 配置全读写权限

1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧导航栏中，单击 [策略](https://console.cloud.tencent.com/cam/policy)，进入策略管理页面。
3. 在策略管理页面中，单击 **QcloudCCSFullAccess** 策略行的【关联用户/组】。如下图所示：
![QcloudCCSFullAccess策略](https://main.qcloudimg.com/raw/c695ca64920265a99815814d9c89de48.png)
4. 在弹出的 “关联用户/用户组” 窗口中，勾选需对 TKE 服务拥有全读写权限的账号，单击【确定】，即可完成子账号对 TKE 服务全读写权限的配置。
5. 在策略管理页面中，单击 **QcloudCCRFullAccess** 策略行的【关联用户/组】。如下图所示：
![QcloudCCRFullAccess策略](https://main.qcloudimg.com/raw/00a475b724671615217205c57bdcff63.png)
6. 在弹出的 “关联用户/用户组” 窗口中，勾选需对镜像仓库拥有全读写权限的账号，单击【确定】，即可完成子账号对镜像仓库全读写权限的配置。
>? 如果您需要使用镜像仓库的触发器和自动构建功能，还需额外配置容器服务-持续集成（CCB）的相关权限。

### 配置只读权限

1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在左侧导航栏中，单击 [策略](https://console.cloud.tencent.com/cam/policy)，进入策略管理页面。
3. 在策略管理页面中，单击 **QcloudCCSReadOnlyAccess** 策略行的【关联用户/组】。如下图所示：
![QcloudCCSReadOnlyAccess策略](https://main.qcloudimg.com/raw/9e08736c48dd13bfb96c70abf36300f3.png)
4. 在弹出的 “关联用户/用户组” 窗口中，勾选需对 TKE 服务拥有只读权限的账号，单击【确定】，即可完成子账号对 TKE 服务只读权限的配置。
5. 在策略管理页面中，单击 **QcloudCCRReadOnlyAccess** 策略行的【关联用户/组】。如下图所示：
![QcloudCCRReadOnlyAccess策略](https://main.qcloudimg.com/raw/fe1dabaac6b5b812072222860b9b86e3.png)
6. 在弹出的 “关联用户/用户组” 窗口中，勾选需对镜像仓库拥有只读权限的账号，单击【确定】，即可完成子账号对镜像仓库只读权限的配置。
>? 如果您需要使用镜像仓库的触发器和自动构建功能，还需额外配置容器服务-持续集成（CCB）的相关权限。

