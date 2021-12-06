## 操作场景

本文档会指导您如何授权 API 网关访问 TKE 集群的 API Server，并提供授权相关问题解决方案。最后通过 YAML文件描述 API 网关获取的权限列表。

## 前提条件

1. 已登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index)。
2. 已有容器服务 TKE 的集群，并且已获取集群 admin 角色。

## 操作步骤

- 在 API 网关的 TKE 通道配置中，如果是首次引用某个 TKE 集群，需授予 API 网关访问该 TKE 集群 API Server 的权限，并且需要保证 TKE集群已经开启了内网访问。

 授权操作，是在配置 TKE 通道时候，系统会自动识别集群是否已经授权，如果没有授权，API 网关会提示用户授权。
![](https://qcloudimg.tencent-cloud.cn/raw/2a5a13b6626f9975394c3a83b27d2d71.png)        

- 如果集群已经授权API网关访问，则会显示**已授权API网关**。每个集群只需要在 API 网关授权一次，后面使用不需要重复授权。                 
<img src="https://qcloudimg.tencent-cloud.cn/raw/51688fa680387191c838fcf6dbe0ba23.png" width="450px">      

## 原理说明

API 网关获取用户授权的流程如下：

1. 在命名空间 kube-system 下，通过创建名为 apigw-ingress 的 ServiceAccount 和名为 apigw-ingress-clusterrole 的 ClusterRole。

2. 把 apigw-ingress 和 apigw-ingress-clusterrole 通过 ClusterRoleBinding 绑定在一起。接着 apigw-ingress 这个 ServiceAccount 的权限就被 API 网关获取到，用来访问集群的 APIServer。

   其中名为 apigw-ingress 的 ServiceAccount 权限，是保存在以 apigw-ingress-token- 为前缀的 Secret 中。

如果您想了解 API 网关获取的权限明细和具体方式，可以查看我们创建相关资源的 YAML 文件。

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: apigw-ingress-clusterrole
rules:
  - apiGroups:
      - ""
    resources:
      - services
      - namespaces
      - endpoints
      - nodes
      - pods
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - apps
    resources:
      - deployments
      - replicasets
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - configmaps
      - secrets
    verbs:
      - "*"
  - apiGroups:
      - extensions
    resources:
      - ingresses
      - ingresses/status
    verbs:
      - "*"
  - apiGroups:
      - ""
    resources:
      - events
    verbs:
      - create
      - patch
      - list
      - update
  - apiGroups:
      - apiextensions.k8s.io
    resources:
      - customresourcedefinitions
    verbs:
      - "*"
  - apiGroups:
      - cloud.tencent.com
    resources:
      - tkeserviceconfigs
    verbs:
      - "*"
---
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: kube-system
  name: apigw-ingress
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: apigw-ingress-clusterrole-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: apigw-ingress-clusterrole
subjects:
  - kind: ServiceAccount
    name: apigw-ingress
    namespace: kube-system
```

## 注意事项

用户在成功授权 API 网关 TKE 集群的访问权限后，就不能修改 API 网关保留使用的资源，资源列表如下：

- kube-system 命名空间下，名为 apigw-ingress 的 ServiceAccount。
- kube-system 命名空间下，名为 apigw-ingress-clusterrole 的 ClusterRole。
- kube-system 命名空间下，名为 apigw-ingress-clusterrole-binding 的 ClusterRoleBinding。
- kube-system 命名空间下，以 apigw-ingress-token- 为前缀的 Secret。



## 常见问题

**问题描述**：授权时发现，TKE 集群没有开启内网访问功能。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5f87b05a0ceb35b43cb881634687ba55.png" width="450px">              

**解决方法**：主动 [开启 TKE 集群内网访问功能](https://cloud.tencent.com/document/product/628/64693#.E5.A6.82.E4.BD.95.E5.BC.80.E5.90.AF-tke-.E9.9B.86.E7.BE.A4.E5.86.85.E7.BD.91.E8.AE.BF.E9.97.AE.E5.8A.9F.E8.83.BD.EF.BC.9F)，然后点击重试。
