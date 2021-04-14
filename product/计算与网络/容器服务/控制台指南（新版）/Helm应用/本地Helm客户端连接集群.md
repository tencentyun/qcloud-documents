## 操作场景

本文档指导您通过本地 Helm 客户端连接集群。

## 操作步骤

### 下载 Helm 客户端

依次执行以下命令，下载 Helm 客户端。关于安装 Helm 的更多信息，请参见 [Installing Helm](https://helm.sh/docs/intro/install/)。
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
```
```
chmod 700 get_helm.sh
```
```
./get_helm.sh
```


### 配置 Helm Chart 仓库（可选）
1. 执行以下命令，配置 kubernetes 官方仓库。
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
```
2. 执行以下命令，配置腾讯云应用市场。
```
helm repo add tkemarket https://market-tke.tencentcloudcr.com/chartrepo/opensource-stable
```
3. [配置 TCR 私有 Helm 仓库](https://cloud.tencent.com/document/product/1141/41944#.E6.B7.BB.E5.8A.A0-helm-.E4.BB.93.E5.BA.93)。


### 连接集群

Helm v3对比 Helm v2已移除 Tiller 组件，Helm 客户端可直接连接集群的 ApiServer，应用相关的版本数据直接存储在 Kubernetes 中。如下图所示：
![](https://main.qcloudimg.com/raw/a1c2fc3a632f3369b14c72498c573593.png)
Helm Client 使用 TKE 生成的客户端证书访问集群，具体操作步骤如下：
1. 通过 TKE 控制台或 API [获取可用公网或内网访问的 Kubeconfig](https://cloud.tencent.com/document/product/457/32191#.E9.85.8D.E7.BD.AE-kubeconfig)。
2. 连接目标集群可参考以下两种方式：
  -  使用上述获取的 kubeconfig，对 Helm Client 所在机器的 kubectl config use-contest 进行配置。 
  - 执行以下命令，通过指定参数的形式访问目标集群。
```
helm  install ....  --kubeconfig [kubeconfig所在路径]
```




