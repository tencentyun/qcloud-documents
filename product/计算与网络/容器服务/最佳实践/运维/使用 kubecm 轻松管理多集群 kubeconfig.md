## 背景

Kubernetes 提供了 kubectl 命令行工具来操作集群，使用 kubeconfig 作为配置文件，默认路径是 `~/.kube/config`，如果想使用 kubectl 对多个集群进行管理和操作，就在 kubeconfig 中配置多个集群的信息即可。

如果使用 TKE 或 EKS 集群，并且希望使用 kubectl 来管理和操作集群，只需要在集群基本信息页开启 APIServer 的外网访问或内网访问即可得到 kubeconfig (集群访问凭证)，但如果要用 kubectl 管理多个集群，通常做法是提取 kubeconfig 中各个字段的内容，然后将其人肉合并到 kubectl 所在机器的 kubeconfig 文件中，比较麻烦而且容易出错。

如何更简单高效的将集群的访问凭证合并添加到 kubeconfig 中呢 ？我们可以借助 `kubecm` 这个工具，本文将介绍如何利用 `kubecm` 来实现多集群的 kubeconfig 高效管理。

## 前提条件

使用前请先确认是否满足以下条件:

* 已创建有 TKE 或 EKS 集群。
* 在需要管理多集群的机器上已安装 kubectl 命令

## 操作步骤

### 安装 kubecm

首先需要在管理多集群的机器上安装 `kubecm`，安装方法参考官方文档: https://kubecm.cloud/#/en-us/install

### 获取集群访问凭证

当新建了 TKE 集群后，开启外网或内网访问后即可下载或复制 kubeconfig 文件内容:

![](https://main.qcloudimg.com/raw/e969bd3bcabe41957caedc5054745924.png)

对于 EKS 集群，同样也是这样:

![](https://main.qcloudimg.com/raw/8bf28b8eabadee6bda988a259b5082a5.png)

### 使用 kubecm 添加访问凭证到 kubeconfig

获取到集群访问凭证后，假设文件名为 `cls-l6whmzi3-config`，使用 `kubecm` 将其添加到 kubeconfig 中 (`-n` 可指定 context 名称):

``` bash
kubecm add -f cls-l6whmzi3-config -n cd -c
```

### 查看集群列表

通过 `kubecm` 添加了要管理和操作的集群后，通过 `kubecm ls` 可查看 kubeconfig 中的集群列表 (星号标识的是当前操作的集群):

``` bash
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

当想要切换到其它集群操作时，可使用 `kubecm switch` 进行交互式切换:

![](https://main.qcloudimg.com/raw/3eea3d35d3a19f93906eabf60a423a0b.png)

### 移除集群

如果想要移除某个集群，可以用 `kubecm delete`:

``` bash
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

## 参考资料

* kubecm 开源地址: https://github.com/sunny0826/kubecm
* kubecm 官方文档: https://kubecm.cloud