本文为您详细介绍 CODING 里 Kubernetes 云账号的最小权限要求。

## 前提条件

使用 CODING 持续部署的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1159/44859)。 

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击工作台首页左侧的 <img src ="https://main.qcloudimg.com/raw/12230547b45d5eae85ad1c4fa86fba68.png" style ="margin:0" data-nonescope="true">，进入持续部署控制台。

### 功能说明

若希望在 Kubernetes 场景下（K8s 云账号）完成应用发布，CODING 持续部署需要调用相关的 Kubernetes APIs。CODING 团队不推荐您将 Kubernetes 集群所有权限皆授予 CODING CD；得益于 Kubernetes 的 RBAC（Role Based Access Control）机制，您可以给 CODING CD 配置应用发布所需的最小权限。下文是配置最小权限的指引。

### Role

CODING 推荐您在需要开放权限的命名空间中创建`Role`，并将`ServiceAccount`和`Role`进行绑定。

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: coding-cd-role
rules:
- apiGroups: [""]
  resources: ["namespaces", "configmaps", "events", "replicationcontrollers", "serviceaccounts", "pods/logs"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["pods", "pods/portforward", "services", "services/proxy", "secrets"]
  verbs: ["*"]
- apiGroups: ["autoscaling"]
  resources: ["horizontalpodautoscalers"]
  verbs: ["list", "get"]
- apiGroups: ["apps"]
  resources: ["controllerrevisions", "statefulsets"]
  verbs: ["list"]
- apiGroups: ["extensions", "app", "apps"]
  resources: ["deployments", "replicasets", "ingresses", "daemonsets"]
  verbs: ["*"]
```

### Service Account

下一步是为 CODING CD 创建一个`Service Account`，持续部署控制台将会用此`Service Account`与 Kubernetes 集群交互。您可以使用如下的 manifest 创建`Service Account`。

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
 name: coding-cd-service-account
 namespace: default
```

### Role Binding

最后，创建一个`RoleBinding`将上述的`coding-cd-role`与`coding-cd-service-account`进行绑定。

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: coding-cd-role-binding
 namespace: webapp
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: Role
 name: coding-cd-role
subjects:
- namespace: default
 kind: ServiceAccount
 name: coding-cd-service-account
```

