## 简介

### 组件介绍
TCR Addon 是容器镜像服务 TCR 推出的容器镜像内网免密拉取的官方插件。在容器服务 TKE 集群中安装该插件后，集群节点可通过内网拉取企业版实例内容器镜像，且无需在集群资源 YAML 中显式配置 ImagePullSecret。可提高 TKE 集群内镜像拉取速度，简化镜像配置流程。
>?
>- TKE 集群需为 v1.10.x 及以上版本。建议在v1.12.x 及以上版本中使用本插件。
- Kubernetes 的 `controller manager` 组件的启动参数需要包含 `authentication-kubeconfig` 和 `authorization-kubeconfig`（TKE v.12.x 默认启用）。


### 部署在集群内的 Kubernetes 对象

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
组件将自动创建 DaemonSet 工作负载 host-updater，用于更新集群节点的Host配置，解析当前关联实例域名至已建立的内网访问链路专用内网 IP 上。请注意，本配置仅用于测试场景配置，建议直接使用 TCR 提供的内网链路自动解析功能，或直接使用 PrivateDNS 产品进行私有域解柝配置，也可使用自建 DNS 服务自行管理解析。

## 限制条件
**针对免密拉取镜像使用场景**：
 - 用户需要具有指定的 TCR 企业版实例的获取访问凭证的权限，即 CreateInstanceToken 接口调用权限。建议具有 TCR 管理员权限的用户进行此插件的配置。
 - 安装插件并生效后，请避免在资源 YAML 中重复指定 ImagePullSecret，从而造成节点使用错误的镜像拉取访问凭证，引起拉取失败。

## 使用方法
1. 选择关联实例：选择当前登录账户下已有的 TCR 企业版实例，并确认当前登录用户具有创建实例长期访问凭证的权限。如果需要新建企业版实例，请在当前集群所在地域内新建。
2. 配置免密拉取（默认启用）：可选自动下发当前操作用户的访问凭证，或指定用户名及密码，可选配置免密拉取生效的命名空间及 ServiceAccount，具体配置请参见 [参数说明](#ParameterDescription)。建议均使用默认配置，避免新建命名空间后无法使用该功能。
3. 配置内网解析（高级功能）：确认集群与关联 TCR 实例已建立内网访问链路，并启用内网解析功能。请注意，本配置仅用于测试场景配置，建议直接使用TCR提供的内网链路自动解析功能，或直接使用 PrivateDNS 产品进行私有域解柝配置，也可使用自建DNS服务自行管理解析。
4. 创建插件完成后，如需修改插件相关配置，请删除插件并重新配置及安装。
>! 删除插件将不会同时删除自动创建的专属访问凭证，可前往 TCR 控制台手动禁用或删除。

## 原理说明
### 概述
TCR Assistant 用于帮助用户自动部署 k8s `imagePullSecret` 到任意 `Namespace`，并关联到该空间下的 `ServiceAccount`。在用户创建的工作负载当中**没有明确指定** `imagePullSecret` 和 `serviceAccount` 的情况下，k8s 会尝试从当前命名空间下名为 `default` 的 `ServiceAccount` 资源中查找、匹配合适的 `imagePullSecret`。

### 术语表

| Name            | 别名      | 描述                                                                                                   |
| :-------------- | :-------- | :----------------------------------------------------------------------------------------------------- |
| ImagePullSecret | ips, ipss | TCR Assistant 定义的 CRD。用于存储镜像仓库用户名与密钥，分发目标 `Namespace` 和目标 `ServiceAccount`。 |


### 实现原理

![](https://qcloudimg.tencent-cloud.cn/raw/0d699c0f710b3dee883773d4dc0749b5.png)

TCR Assistant 是一个典型的 k8s Operator。在部署 TCR Assistant 时，我们会在目标 k8s 集群当中创建 CRD 对象：`imagepullsecrets.tcr.tencentcloudcr.com`。该 CRD 的 kind 为 `ImagePullSecret`，版本是 `tcr.tencentcloudcr.com/v1`，缩写为 `ips` 或者 `ipss`。

TCR Assistant 通过持续观察（watch） k8s 集群的 `Namespace` 和 `ServiceAccount` 资源，并在这些资源发生变更的时候，检查资源变化是否匹配 `ImagePullSecret` 中设定的规则来自动的为用户部署拉取**私有镜像仓库**所需要的 Secret 资源。程序通常部署在 k8s 集群内，使用 `in cluster` 模式访问 k8s master API。

#### 创建 CRD 资源
程序部署完成后，不会在目标 k8s 集群部署任何的 TCR 镜像拉取密钥。此时，需要我们使用 kubectl 或者通过 Client Go 新建 `ImagePullSecret` 资源。

```bash
# 新建 ImagePullSecret 资源
$ kubectl create -f allinone/imagepullsecret-sample.yaml

imagepullsecret.tcr.tencentcloudcr.com/imagepullsecret-sample created
```

`ImagePullSecret` 资源示例文件（allinone/imagepullsecret-sample.yaml）：
```yaml
apiVersion: tcr.tencentcloudcr.com/v1
kind: ImagePullSecret
metadata:
  name: imagepullsecret-sample
spec:
  namespaces: "*"
  serviceAccounts: "*"
  docker:
    username: "100012345678"
    password: tcr.jwt.token
    server: fanjiankong-bj.tencentcloudcr.com
```

`ImagePullSecret` spec 字段解释如下表：

| 字段            | 作用                       | 注释  |
| --------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| namespaces      | `NameSpace` 匹配规则       | `*` 或者空字符表示匹配任意；要匹配任意多个 `NameSpace` 则使用 `,` 分隔多个资源名称，**注意**：不支持任何表达式，需要明确填写资源名称。      |
| serviceAccounts | `serviceAccounts` 匹配规则 | `*` 或者空字符表示匹配任意；要匹配任意多个 `ServiceAccount` 则使用 `,` 分隔多个资源名称，**注意**：不支持任何表达式，需要明确填写资源名称。 |
| docker.server   | 镜像仓库域名               | 仅填写仓库域名                                                                                                                              |
| docker.username | 镜像仓库用户名             | 请确保用户在镜像仓库拥有足够的访问权限                                                                                                      |
| docker.password | 镜像仓库用户名所对应的密码 |


创建完成后，我们可以使用下列命令观察 TCR Assistant 执行结果：
```bash
# 列出 ImagePullSecret 信息
$ kubectl get ipss
NAME                     NAMESPACES   SERVICE-ACCOUNTS   SECRETS-DESIRED   SECRETS-SUCCESS
imagepullsecret-sample   *            *                  10                10

# 查看详细信息
$  kubectl describe ipss
Name:         imagepullsecret-sample
Namespace:
Labels:       <none>
Annotations:  <none>
API Version:  tcr.tencentcloudcr.com/v1
Kind:         ImagePullSecret
Metadata:
  Creation Timestamp:  2021-12-01T06:47:34Z
  Generation:          1
    Manager:      kubectl-client-side-apply
    Operation:    Update
    Time:         2021-12-01T06:47:34Z
    API Version:  tcr.tencentcloudcr.com/v1
    Manager:         manager
    Operation:       Update
    Time:            2021-12-01T06:47:38Z
  Resource Version:  30389349
  UID:               2109f384-240b-405c-9ce8-73ce938a7c2f
Spec:
  Docker:
    Password:        tcr.jwt.token
    Server:          fanjiankong-bj.tencentcloudcr.com
    Username:        100012345678
  Namespaces:        *
  Service Accounts:  *
Status:
  S As Desired:  47
  S As Success:  1
  Secret Update Successful:
    Namespaced Name:  kube-public/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  devtools/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  demo/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  kube-system/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  tcr-assistant-system/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  kube-node-lease/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  cert-manager/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  default/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:36Z
    Namespaced Name:  afm/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:37Z
    Namespaced Name:  lens-metrics/tcr.ipsimagepullsecret-sample
    Updated At:       2021-12-01T06:47:37Z
  Secrets Desired:    10
  Secrets Success:    10
  Service Accounts Modify Successful:
    Namespaced Name:  default/default
    Updated At:       2021-12-01T06:47:38Z
Events:               <none>

```

>! 如果需要更新 TCR Assistant 部署的 `Secret` 资源，无需删除重建 `ImagePullSecret` 资源，只需要编辑其中 `docker.username` 和 `docker.password` 字段即可生效。例如：
```bash
$ kubectl edit ipss imagepullsecret-sample
```
>


#### Namespace 变更
TCR Assistant 在观察到有新的 k8s `Namespace` 资源创建后，会首先检查名称是否和 `ImagePullSecret` 资源中的 `namespaces` 字段匹配。如果资源名称**不匹配**跳过后续流程；资源名称匹配的情况下，会调用 k8s API 创建 `Secret` 资源，并添加 `Secret` 资源名称到 `ServiceAccount` 资源的 `imagePullSecrets` 字段当中。示例如下：

```
# 查看 newns 下自动部署的 Secret
$ kubectl get secrets -n newns
NAME                            TYPE                                  DATA   AGE
tcr.ipsimagepullsecret-sample   kubernetes.io/dockerconfigjson        1      7m2s
default-token-nb5vw             kubernetes.io/service-account-token   3      7m2s

# 查看 newns 下自动关联到 ServiceAccount 资源 default 中的 Secret
$ kubectl get serviceaccounts default -o yaml -n newns
apiVersion: v1
imagePullSecrets:
- name: tcr.ipsimagepullsecret-sample
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-12-01T07:09:56Z"
  name: default
  namespace: newns
  resourceVersion: "30392461"
  uid: 7bc67144-3685-4666-ba41-b1447bbbaa38
secrets:
- name: default-token-nb5vw

```

#### ServiceAccount 变更
TCR Assistant 在观察到有新的 k8s `ServiceAccount` 资源创建后，会首先检查名称是否和 `ImagePullSecret` 资源中的 `serviceAccounts` 字段匹配。如果资源名称**不匹配**跳过后续流程；资源名称匹配的情况下，会调用 k8s API 创建或更新 `Secret` 资源，并添加 `Secret` 资源名称到 `ServiceAccount` 资源的 `imagePullSecrets` 字段当中。示例如下：

```bash
# 在 newns 新建 ServiceAccount 资源
$ kubectl create sa kung -n newns
serviceaccount/kung created

# 查看 newns 下自动关联到新建 ServiceAccount 资源 kung 中的 Secret
$ kubectl get serviceaccounts kung -o yaml -n newns
apiVersion: v1
imagePullSecrets:
- name: tcr.ipsimagepullsecret-sample
kind: ServiceAccount
metadata:
  creationTimestamp: "2021-12-01T07:19:12Z"
  name: kung
  namespace: newns
  resourceVersion: "30393760"
  uid: e236829e-d88e-4feb-9e80-5e4a40f2aea2
secrets:
- name: kung-token-fljt8
```



