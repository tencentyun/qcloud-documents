 


## 组件介绍
Ceberus 组件支持对签名镜像进行可信验证，确保在 TKE 集群中只部署可信授权方签名的容器镜像，降低在容器环境中的镜像安全风险。


### 部署在集群内的 Kubernetes 对象
| Kubernetes 对象名称 | 类型       | 请求资源                     | 所属 Namespace |
| :----------------- | ---------- | ---------------------------- | -------------- |
| cerberus-webhook | Deployment | 每个实例 CPU 0.5C，Memory 0.5G，共1个实例 | tcr-verification |
| cerberus-webhook | Service    | -                            | tcr-verification |
| cerberus-webhook | Configmap  | -                            | tcr-verification |
| cerberus-webhook | Secret | - | tcr-verification |
| cerberus-webhook | validatingwebhookconfigurations | - | -  |
| cerberus-rolebinding | ClusterRoleBinding | - | -  |
| cerberus-role | ClusterRole | - |  - |
| cerberus-controller | ServiceAccount | - | -  |


## 限制条件
- TKE 集群版本 = 1.18。
- 开通并使用 TCR 高级版 [容器镜像签名](https://cloud.tencent.com/document/product/1141/80862) 功能后，才可在 TKE 集群中为已加签的镜像进行验签。
- 验签需要提前授权容器服务角色拥有使用 TCR 接口的权限。


## 使用方法
### 授权容器服务使用 TCR 查询接口
为让 TKE 服务可以读取到您账号下的签名信息，需要在您的账号配置如下策略。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)。
2. 在“角色”页面，单击**TCR_QCSRole**。
3. 在 TCR_QCSRole 角色详情页，关联预设策略 **QcloudTCRReadOnlyAccess**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7e61d49e56078f0ffca1997c50afbc72.png)


### 安装组件并配置验签策略
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**组件管理**，进入“组件列表”页面。
4. 在“组件列表”页面中选择**新建**，并在“新建组件”页面中勾选 Ceberus 组件并进行签名验证策略的参数配置，说明如下：
![](https://qcloudimg.tencent-cloud.cn/raw/a16bf97bcebd5bb2c3351836a217d5cd.png)
	- **策略名称**：请为验签策略设置合理名称。
	- **命名空间**：请选择当前验签策略生效的 Kubernetes 命名空间，每个验签策略仅对一个命名空间生效。
	- **证明者**：证明者将定位到镜像加签时所采用的 KMS 密钥，可通过该字段确保镜像签名来源的可信性。
		- **地域**：选择 TCR 镜像仓库实例所在的地域，和 TKE 集群所造地域无强制关联性。
		- **TCR 实例**：选择 TCR 镜像仓库实例。
		- **签名策略**：选择已经创建的签名策略。签名策略和镜像签名时使用的 KMS 密钥相对应，支持选择多个签名策略。
5. 单击**确定**完成组件创建。
>? 
>- 组件创建时则验签策略生效，未通过签名验证的镜像将部署失败。为保障 TKE 基础服务的正常运行，请不要为 TKE 系统组件所在的命名空间（如 kube-system）设置验签策略。
>- 若您需要为集群中相同 Kubernetes 命名空间绑定不同 TCR 仓库实例下的签名策略，可在当前验签策略中**新增证明者**；若您需要为集群的多个 kubernetes 命名空间都设置镜像签名验证，可直接**添加策略**。
>

### 镜像签名验证
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面单击目标集群 ID，进入集群详情页。
3. 选择左侧菜单栏中的**工作负载**，单击**新建**。
4. 在新建工作负载页，配置**实例内容器 > 镜像**时，选择待部署的已经加签的容器镜像及镜像版本（Tag），同时勾选**摘要（SHA256）**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c15e50d4e2239aa394ee6d7e2fd0a55d.png)
5. 单击**完成**创建工作负载部署。若签名验证通过，则 Pod 将正常部署；若签名验证不通过，则 Pod 部署将被阻断，相关 event 信息展示如下图所示：
	- 若拉取镜像所在 TCR 仓库实例下未开启镜像签名特性，则报错如下：
	![](https://qcloudimg.tencent-cloud.cn/raw/c28630dd9e6cd578d1fc850537e151d0.png)
	- 若拉取镜像没有签名信息，则报错如下：
	![](https://qcloudimg.tencent-cloud.cn/raw/fd1b8bb3e49a4aebc757e9317bff13c6.png)
	- 若拉取镜像的签名信息验证不通过，则报错如下：
	![](https://qcloudimg.tencent-cloud.cn/raw/94d4cf0013d981e8139153afb1ab75a6.png)
>? 镜像签名验证目前只支持使用 digest 格式的镜像，否则会验证不通过。
>

