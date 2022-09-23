
## 操作场景
TKE Serverless 集群支持通过 configmap 进行全局配置。在 TKE 弹超级节点场景以及纯 TKE Serverless 集群场景下，如果用户需要批量对每个超级节点或每个 Pod 设置 annotation，此时在超级节点维度或 Pod 维度进行配置会相对繁琐，对业务 yaml 的侵入性也较大，因此 TKE Serverless 集群提供全局配置的能力，用户可以通过 configmap 进行全局配置来实现对集群内每个 Pod 注入 Annotation 的能力。

## 操作步骤
1. 在 kube-system 下新建一个 eks-config 的 configmap。
2. 填入相应的参数设置，使其对所有 TKE Serverless 集群的 Pod 生效。
全局配置参考如下：
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: eks-config
  namespace: kube-system
data:
  pod.annotations: |
    eks.tke.cloud.tencent.com/resolv-conf: |
      nameserver 183.60.83.19 
    eks.tke.cloud.tencent.com/host-sysctls: "[{"name": "net.core.rmem_max","value": "26214400"}]"
```

## 配置优先级说明

全局配置的优先级最低，其次是超级节点维度的配置，优先级最高的为 Pod 本身的配置，若配置冲突时，按照优先级生效。
