## 操作场景

本文档指导您通过本地 Helm 客户端连接集群。

## 操作步骤

### 下载 Helm 客户端

执行以下命令，下载 Helm 客户端。
```
 curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
 chmod 700 get_helm.sh
 ./get_helm.sh
```

更多查看[Installing Helm](https://helm.sh/docs/intro/install/)

### 配置 Helm Chart 仓库(可选)
1. 配置kubernetes官方仓库：
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
```
2. 配置腾讯云应用市场
```
helm repo add  tkemarket  https://market-tke.tencentcloudcr.com/chartrepo/opensource-stable
```
3. [配置TCR私有Helm 仓库](https://cloud.tencent.com/document/product/1141/41944#.E6.B7.BB.E5.8A.A0-helm-.E4.BB.93.E5.BA.93)


### 内网/外网通过 Helm 安装Chart包到指定的TKE集群 

Helm v3对比Helm v2 已移除Tiller组件，Helm 客户端直接连接集群的ApiServer， 应用相关的版本数据直接存储在Kunernetes中。  
![](https://main.qcloudimg.com/raw/a1c2fc3a632f3369b14c72498c573593.png)

方式1: Helm Client使用TKE生成的客户端证书访问集群
1. 通过TKE控制台或API[获取可用公网或内网访问的Kubeconfig](https://cloud.tencent.com/document/product/457/32191#.E9.85.8D.E7.BD.AE-kubeconfig)
2. 可通过配置Helm Client所在机器的kubectl config use-contest为上述获取的kubeconfig. helm install等命令即可连接目标集群。 
3. 可通过通过制定参数的形式访问目标集群
```
helm  install ....  --kubeconfig [kubeconfig所在路径]
```

