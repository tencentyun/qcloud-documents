## 操作场景

Kubernetes 提供 Kubectl 命令行工具用于操作集群，Kubectl 使用 Kubeconfig 作为配置文件（默认路径为 `~/.kube/config`），通过其配置多个集群的信息，并管理和操作多个集群。


通过 Kubectl 管理和操作容器服务 TKE 或 EKS 集群，需要在集群基本信息页面开启 APIServer 的外网访问或内网访问，获取 Kubeconfig （集群访问凭证）。如果需要使用 Kubectl 管理多个集群，通常做法是提取 Kubeconfig 中各个字段的内容，将其合并到 Kubectl 所在设备的 Kubeconfig 文件中，但该方式操作繁琐且容易出错。

借助 kubecm 工具，可以更简单高效的将多个集群访问凭证合并添加到 kubeconfig 中。本文将介绍如何利用 kubecm 实现多集群的 kubeconfig 高效管理。



## 前提条件


- 已创建 [TKE](https://cloud.tencent.com/document/product/457/32189) 或 [EKS](https://cloud.tencent.com/document/product/457/39813) 集群。
- 已在需要管理多集群的设备上安装 [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) 命令行工具。


## 操作步骤

### 安装 kubecm

在管理多集群的设备上安装 [Kubecm](https://kubecm.cloud/#/en-us/install)。


### 获取集群访问凭证

创建 TKE 或 EKS 集群后，请按照以下 [TKE](#tke) 或 [EKS](#eks) 获取集群访问凭证步骤获取访问凭证：


[](id:tke)

#### TKE 集群获取集群访问凭证

1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 在左侧菜单栏中选择**基本信息**，进入“基本信息”页面。
4. 在“基本信息”页面找到**集群APIServer信息**配置项，开启**外网访问**和**内网访问**。
![](https://main.qcloudimg.com/raw/eaefe0e780bf0ef303619a6f054f583a.jpg)
5. 单击右侧的**下载**，下载 Kubeconfig。


[](id:eks)

#### EKS 集群获取集群访问凭证

1. 登录容器服务控制台，选择左侧导航栏中的 **[弹性集群](https://console.cloud.tencent.com/tke2/ecluster)**。
2. 单击需要获取集群访问凭证的集群 ID/名称，进入该集群的管理页面。
3. 在左侧菜单栏中选择**基本信息**，进入“基本信息”页面。
4. 在“基本信息”页面找到**集群APIServer信息**配置项，开启**外网访问**和**内网访问**。
![](https://main.qcloudimg.com/raw/f8884ee3527e3eaf63ad3e114d8a431b.jpg)
5. 单击**下载**，下载 Kubeconfig。




### 使用 Kubecm 添加访问凭证到 Kubeconfig

本文以集群访问凭证文件名 `cls-l6whmzi3-config` 为例，执行以下命令，使用 Kubecm 将访问凭证添加到 Kubeconfig 中（`-n` 可指定 context 名称）。示例如下：
```plaintext
kubecm add -f cls-l6whmzi3-config -n cd -c
```

### 查看集群列表

执行以下 `kubecm ls` 命令查看 kubeconfig 中的集群列表（星号标识的是当前操作的集群）。示例如下：

```plaintext
$ kubecm ls
+------------+------------+-----------------------+--------------------+-----------------------------------+-------------------+
|   CURRENT  |    NAME    |        CLUSTER        |        USER        |               SERVER              |     Namespace     |
+============+============+=======================+====================+===================================+===================+
|      *     |     cd     |   cluster-chh6kgf9d9  |   user-chh6kgf9d9  |   https://cls-l6whmzi3.ccs.tence  |      default      |
|            |            |                       |                    |            nt-cloud.com           |                   |
+------------+------------+-----------------------+--------------------+-----------------------------------+-------------------+
|            |     bj     |   cluster-6qaua96n    |   user-6qaua96n    |   https://cls-6qaua96n.ccs.tence  |    kube-system    |
|            |            |                       |                    |            nt-cloud.com           |                   |
+------------+------------+-----------------------+--------------------+-----------------------------------+-------------------+
```

### 切换集群


执行以下 `kubecm switch` 命令可以交互式切换到其他集群。如下图所示：

![](https://main.qcloudimg.com/raw/3eea3d35d3a19f93906eabf60a423a0b.png)

### 移除集群

执行以下 `kubecm delete` 命令可以移除某个集群。示例如下：

```plaintext
$ kubecm delete bj
Context Delete:「bj」
「/Users/roc/.kube/config」 write successful!
+------------+---------+-----------------------+--------------------+-----------------------------------+--------------+
|   CURRENT  |   NAME  |        CLUSTER        |        USER        |               SERVER              |   Namespace  |
+============+=========+=======================+====================+===================================+==============+
|            |    cd   |   cluster-chh6kgf9d9  |   user-chh6kgf9d9  |   https://cls-l6whmzi3.ccs.tence  |    default   |
|            |         |                       |                    |            nt-cloud.com           |              |
+------------+---------+-----------------------+--------------------+-----------------------------------+--------------+
```

## 参考文档

- [kubecm 开源地址](https://github.com/sunny0826/kubecm)
- [kubecm 官方文档](https://kubecm.cloud)
