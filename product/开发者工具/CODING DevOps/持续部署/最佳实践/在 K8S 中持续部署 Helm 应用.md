本文为您详细介绍如何在 K8S 中持续部署 Helm 应用。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

Helm 是 Kubernetes 的包管理器，也是一个强大的 yaml 模版引擎。在真实的部署场景中，往往需要部署至多个环境，比如说可能先部署到测试环境再部署到生产环境，它们的 `yaml` 文件基本是相同的，但某些地方又会有一些微小的差异，我们可以在部署前通过 Helm 和一些自定义参数非常灵活的渲染出来当前环境所需的 `yaml` 文件，现在 CODING 的持续部署已经支持部署 `Helm`（不需要 Tiller），本文将介绍如何使用 CODING 来部署一个 Helm 制品。

## 基本原理

CODING 的服务器会下载 Helm 的 pkg 文件，使用 helm2 客户端的命令 `helm template --set --values` 生成 `yaml` 文件，最后部署这个生成的 `yaml` 文件，整个过程完全不需要 Tiller。

## 主要部署流程

整个流程非常简单，一共就 3 步。

1.  [准备阶段](#准备阶段)，配置 Helm 的仓库地址和版本。
2.  [配置部署流程](#配置部署流程)，目的是对 Helm 中需要修改的值进行配置，生成最终的 yaml 文件。
3.  [部署](#部署阶段)部署上述步骤所生成的 yaml 文件。

## 准备阶段

### 创建 Helm 仓库

需要在 CODING 制品库新建 Helm 仓库，然后将 Helm 包文件上传到仓库，将在后续步骤中部署 `tomcat 0.4.1`。

![](https://help-assets.codehub.cn/enterprise/20200728103604.png)

### 创建持续部署云账号

用 [kubeconfig](https://kubernetes.io/zh/docs/concepts/configuration/organize-cluster-access-kubeconfig) 创建一个[云账号](/docs/cd/cloudaccount.html)

## 配置部署流程

创建一个名为 `helm` 和部署流程

![](https://help-assets.codehub.cn/enterprise/20200728104105.png)

### 配置 helm 仓库地址和版本

添加 Heml 制品并设置制品别名为 `helm-pkg`，后面阶段会引用这个别名。

![](https://help-assets.codehub.cn/enterprise/20200728104130.png)

### 添加 Bake 阶段

添加一个类型为 `Bake (Manifest)` 的阶段，Expected Artifact 选项中选择 `helm-pkg`，Overrides 可以配置需要修改的参数，“Add value artifact" 对应了 Helm 客户端命令行的 `--values` 参数，”Key Value“ 对应了 `--set` 参数

![](https://help-assets.codehub.cn/enterprise/20200728104159.png)

生成的 `yaml` 我们需要传给后面的阶段使用，所以需要配置生成制品，选择 `Base64`，这个配置会将生成的 `yaml` 文件编码为 `Base64` 格式，生成一个名叫 `helm-yaml` 的新制品。

![](https://help-assets.codehub.cn/enterprise/20200728104214.png)

## 部署阶段

-   添加一个类型为 `部署 (Manifest)` 的阶段，并选择上一阶段生成的制品 `helm-yaml` 和之前配置的云账号，配置完成后，点击右下角的保存就完成了配置。

![](https://help-assets.codehub.cn/enterprise/20200728104232.png)

要执行配置好的部署流程，新建发布单，选择刚才配置的部署流程 `helm`，并选择需要部署的制品版本 `0.4.1`，几分钟之后就部署成功了。

![](https://help-assets.codehub.cn/enterprise/20200728104247.png)

![](https://help-assets.codehub.cn/enterprise/20200728104304.png)

## 总结

本文主要介绍如何使用 CODING 来部署一个 Helm 制品，其核心就是 Bake 的配置，初看起好像很简单，用脚本也能达到同样的效果，但实际上在部署流程中，Bake 是可以同其它阶段相互配合， 创建非常复杂的部署流程的。