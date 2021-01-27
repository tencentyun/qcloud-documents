## 简介

### 组件介绍
TCR Addon 是容器镜像服务 TCR 推出的容器镜像内网免密拉取的官方插件。在容器服务 TKE 集群中安装该插件后，集群节点可通过内网拉取企业版实例内容器镜像，且无需在集群资源 YAML 中显式配置 ImagePullSecret。可提高 TKE 集群内镜像拉取速度，简化镜像配置流程。
>?
>- TKE 集群需为 v1.10.x 及以上版本。建议在v1.12.x 及以上版本中使用本插件。
- Kubernetes 的 `controller manager` 组件的启动参数需要包含 `authentication-kubeconfig` 和 `authorization-kubeconfig`（TKE v.12.x 默认启用）。


### 在 Kubernetes 集群创建的资源

| 名称                                           | 类型                           | 资源量                 | Namespace            |
| ---------------------------------------------- | ------------------------------ | ---------------------- | -------------------- |
| tcr-assistant-system                           | Namespace                      | 1                      |-                    |
| tcr-assistant-manager-role                     | ClusterRole                    | 1                      | -                    |
| tcr-assistant-manager-rolebinding              | ClusterRoleBinding             | 1                      | -                    |
| tcr-assistant-leader-election-role             | Role                           | 1                      | tcr-assistant-system |
| tcr-assistant-leader-election-rolebinding      | RoleBinding                    | 1                      | tcr-assistant-system |
| tcr-assistant-webhook-server-cert              | Secret                         | 1                      | tcr-assistant-system |
| tcr-assistant-webhook-service                  | Service                        | 1                      | tcr-assistant-system |
| tcr-assistant-validating-webhook-configuration | ValidatingWebhookConfiguration | 1                      | tcr-assistant-system |
| imagepullsecrets.tcr.tencentcloudcr.com        | CustomResourceDefinition       | 1                      | tcr-assistant-system |
| tcr.ips*                                      | ImagePullSecret CRD            | (2-3)                  | tcr-assistant-system |
| tcr.ips*                                      | Secret                         | (2-3)*{Namespace No.} | tcr-assistant-system |
| tcr-assistant-controller-manager               | Deployment                     | 1                      | tcr-assistant-system |
| updater-config                                 | ConfigMap                      | 1                      | tcr-assistant-system |
| hosts-updater                                  | DaemonSet                      | {Node No.}             | tcr-assistant-system |

### 组件资源用量

| 组件                             | 资源用量                | 实例数量   |
| -------------------------------- | ----------------------- | ---------- |
| tcr-assistant-controller-manager | CPU：100m memory：30Mi  | 1          |
| hosts-updater                    | CPU：100m memory：100Mi | 工作节点数 |


## 使用场景

### 免密拉取镜像

Kubernetes 集群拉取私有镜像需要创建访问凭证 Secret 资源，并配置资源 YAML 中的 ImagePullSecret 属性，显式指定已创建的 Secret。整体配置流程较为繁琐，且会因未配置 ImagePullSecret 或指定错误 Secret 而造成镜像拉取失败。
为解决以上问题，可集群中安装 TCR 插件，插件将自动获取指定的 TCR 企业版实例的访问凭证，并下发至 TKE 集群指定命名空间内。在使用 YAML 创建或更新资源时，无需配置 ImagePullSecret，集群会将自动使用已下发的访问凭证拉取 TCR 企业版内镜像。

### 内网拉取镜像

Kubernetes 集群拉取镜像时将通过节点网络访问 TCR，当通过公网镜像进行访问时将产生公网流量费用，且拉取速度较慢，存在网络安全风险。当前 TCR 同时支持公网及内网访问，可在 TCR 控制台接入需要进行内网访问的私有网络，配置完成后私有网络内 TKE 集群即可通过内网访问 TCR 内私有仓库。为确保集群节点上可将 TCR 独享实例域名正常解析至内网访问地址，还需在节点上配置 Host 或使用自建 DNS 服务。
为简化内网解析配置，可在集群中安装 TCR 插件，插件将自动为集群节点配置指定的 TCR 企业版实例的域名的内网解析，同时支持使用默认域名、专属内网域名及自定义域名。

## 限制条件
- **针对免密拉取镜像使用场景**：
 - 用户需要具有指定的 TCR 企业版实例的获取访问凭证的权限，即 CreateInstanceToken 接口调用权限。建议具有 TCR 管理员权限的用户进行此插件的配置。
 - 安装插件并生效后，请避免在资源 YAML 中重复指定 ImagePullSecret，从而造成节点使用错误的镜像拉取访问凭证，引起拉取失败。
- **针对内网拉取镜像使用场景**：
 - 请首先在 TCR 控制台内将集群所在私有网络 VPC 接入至指定的 TCR 实例，并确认内网访问链路正常后再安装及配置本插件。
 - 自定义域名仅支持使用 tencentcloudcr.com 根域名，且配置后在集群内无法通过公网访问指定的 TCR 实例。


## 使用方法
1. 选择关联实例：选择当前登录账户下已有的 TCR 企业版实例，并确认当前登录用户具有创建实例长期访问凭证的权限。如果需要新建企业版实例，请在当前集群所在地域内新建。
2. 配置免密拉取（默认启用）：配置免密拉取生效的命名空间及 ServiceAccount，具体配置请参见 [参数说明](#ParameterDescription)。建议均使用默认配置，避免新建命名空间后无法使用该功能。
3. 配置内网解析（可选功能）：确认集群与关联 TCR 实例已建立内网访问链路，并启用内网解析功能。如已通过手动修改集群节点 Host 或使用自建 DNS 服务实现内网解析，可不启用该功能。
>! 该功能启用后，内网访问域名将强制解析至关联的 TCR 实例提供的内网访问地址，无法用于公网访问。
4. 创建插件完成后，如需修改插件相关配置，请删除插件并重新配置及安装。
>! 删除插件将不会同时删除自动创建的专属访问凭证，可前往 TCR 控制台手动禁用或删除。





## 操作步骤
1. 登录[ 容器服务控制台 ](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的【集群】。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的【组件管理】，进入 “组件列表” 页面。
4. 在“组件列表”页面中选择【新建】，并在“新建组件”页面中勾选 TCR。
5. 选择“参数配置”，在弹出的“TCR组件参数设置”窗口中配置相关参数。如下图所示： 
![](https://main.qcloudimg.com/raw/2426d439484edd183585127700817624.png)
6. 单击【确定】即可创建插件。





## 相关信息
### 参数说明<span id="ParameterDescription"></span>

- **关联实例**：当前集群需要使用的 TCR 企业版实例，插件将自动为当前集群配置该 Registry 实例的访问凭证及内网域名解析。
- **免密拉取配置**：
  - **命名空间**：免密拉取功能生效的命名空间，可指定单个、多个命名空间，或直接使用 `*` 指定集群内全部命名空间（含新建的命名空间）。默认配置为 `*` ，即将在当前集群的全部命名空间内生效。插件安装完成后，可在生效的命名空间内查看插件自动创建的 Secret。
  - **ServiceAccount**：免密拉取功能生效的 ServiceAccount，可指定单个、多个 ServiceAccount，或直接使用 `_` 指定命名空间内全部 ServiceAccount（含新建的 ServiceAccount）。默认配置为 `_` ，即将在当前集群的指定命名空间内的全部 ServiceAccount 生效。
  - **访问凭证描述**：启用集群免密拉取功能，将在关联的企业版实例内自动创建该集群专用的长期访问凭证，此描述用于提示该访问凭证的使用场景，默认为：TKE 集群（cls-xxxxxxx）专用访问凭证，其中 cls-xxxxxxx 为当前集群的唯一 ID。
- **内网访问配置**：
  - **内网访问链路**：如需在集群内通过内网访问关联的 TCR 企业版实例，则需要在 TCR 控制台内将集群所在 VPC 接入至关联实例，建立两者的内网访问链路。该参数取值显示当前集群与所选关联实例是否已正常建立内网访问链路，如未建立，请前往 TCR 控制台 >【访问控制】>【内网访问】进行接入。
  - **启用内网解析**：可选功能。如已在当前集群及关联 TCR 实例创建了内网访问链路，可手动配置节点 Host 或使用自建 DNS 服务实现内网解析，也可选择启用本功能，插件将自动为集群内已有及新增节点配置关联 TCR 实例的域名内网解析。
  - **内网访问域名**：TCR 企业版实例提供专属的访问域名，在集群内可使用默认域名，内网专属域名或自定义域名，以上域名的内网解析配置仅在集群内生效。如使用自定义域域名，仅支持使用 tencentcloudcr.com 根域名。
