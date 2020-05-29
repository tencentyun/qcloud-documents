## 操作场景
腾讯云容器镜像服务（Tencent Container Registry，TCR）支持托管 Helm Chart，满足用户对云原生应用托管分发的需要。用户可在同个命名空间内同时管理容器镜像及 Helm Chart，实现在业务项目内同时使用容器镜像和 Helm Chart 云原生交付物。

目前仅企业版实例支持托管 Helm Chart，支持使用 Helm 客户端实现 Chart 的上传及下载。Helm Chart 仓库继承其所属的命名空间的公开及私有属性，无需额外配置。在权限管理上，Helm Chart 与容器镜像共用 **repository** 资源类型，即<b> qcs::tcr:$region:$account:repository/tcr-xxxxxx/project-a/*</b> 资源描述将包含命名空间 project-a 内全部镜像仓库及 Helm Chart，用户可在进行资源权限管理时灵活使用。 


## 前提条件
在上传并管理 TCR 企业版实例内的 Helm Chart 前，您需要完成以下准备工作：
- 已成功 [创建企业版实例](https://cloud.tencent.com/document/product/1141/40716)。
- 如使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。

## 操作步骤
### 安装并配置 Helm 客户端
1. 登录节点，并从 Helm 官方项目中下载指定的 [Helm 客户端](https://github.com/helm/helm/releases)。
>?
>- 若您当前希望在容器服务 TKE 中使用 Helm，请选择 Helm v2.10.0 版本。可执行 `helm version -c` 命令查看已安装的客户端版本。
>- 本文以在 Linux  操作系统的节点上安装为例，如在其他平台安装请下载对应安装包。 
>
3. 在节点上依次执行以下命令，解压安装包并移动至指定位置。
```shell
tar -zxvf helm-v2.10.0-linux-amd64.tgz
```
```shell
mv linux-amd64/helm /usr/local/bin/helm
```
3. 请对应实际情形执行以下命令，初始化 Helm。
 - 在容器集群节点上进行初始化，默认已经开通 Helm 并安装完成 tiller。
```
helm init --client-only --skip-refresh
```
 - 在自建的 kubernetes 集群上，尚未安装 tiller。
```
helm init --skip-refresh   
```
4. 执行以命令下安装 Helm 插件。
>!Helm 上传 Chart 需要提前安装 git 并安装上传插件，请确保您使用的机器上已安装 git。
>
```
helm plugin install https://github.com/chartmuseum/helm-push
```

				
				
### 添加 Helm 仓库
1. 登录 [容器镜像服务控制台](https://console.cloud.tencent.com/tcr)，在“实例列表”页面选择实例名称，进入实例详情页。
2. <span id="Step2"></span>参考 [获取实例访问凭证](https://cloud.tencent.com/document/product/1141/41829) 获取用户名及登录密码。
3. 在节点上执行以下命令，添加希望用于托管 Helm Chart 的命名空间至本地 Helm 仓库。
>!执行命令的机器需确保已在对应实例的公网白名单中，详情请参见 [公网访问控制](https://cloud.tencent.com/document/product/1141/41837)。
>
```
helm repo add $instance-$namespace https://$instance.tencentcloudcr.com/chartrepo/$namesapce --username $username --password $instance-token
```
 - `$instance-$namespace`：为 helm repo 名称，建议使用**实例名称+命名空间名称**组合的方式命名，以便于区分各个实例及命名空间。
 - `https://$instance.tencentcloudcr.com/chartrepo/$namesapce`：为 helm repo 的远端地址。
    - `$username`：为 [步骤2](#Step2) 中已获取的用户名。
    - `$instance-token`：为 [步骤2](#Step2) 中已获取的登录密码。
如添加成功将提示以下信息。
```
"$instance-$namespace" has been added to your repositories
```

### 推送 Helm Chart
已安装的 Helm-push 插件支持使用 `helm push` 指令推送 helm chart 至指定 repo，支持上传目录及压缩包。此步骤以将 tcr-chart-demo 1.0.0 版本上传至已添加的仓库为例。
1. 在节点上执行以下命令，创建一个 Chart。
```
helm create tcr-chart-demo
```
2. 执行以下命令，推送至 Chart 目录。
```
helm push tcr-chart-demo $instance-$namespace
```
其中 `$instance-$namespace` 为已添加的本地仓库名称。
3. 执行以下命令，将已创建的 Chart 压缩。
```shell
tar zcvf tcr-chart-demo-1.0.0.tgz tcr-chart-demo/
```
3. 执行以下命令，推送 Chart 压缩包。
```
helm push tcr-chart-demo-1.0.0.tgz $instance-$namespace
```
其中 `$instance-$namespace` 为已添加的本地仓库名称。


### 拉取 Helm Chart
1. 在节点上执行以下命令，获取最新的 Chart 信息。
```
helm repo update
```
2. 执行以下命令，拉取指定版本 Helm Chart。
```
helm fetch <本地仓库名称>/<Chart 名称> --version <Chart 版本>
```
以从企业版实例 tcr-demo 中拉取命名空间 project-a 内 tcr-chart-demo 1.0.0 版本为例：
```
helm fetch tcr-demo-project-a/tcr-chart-demo --version 1.0.0
```

### 控制台管理 Helm Chart
1. 登录 [容器镜像服务](https://console.cloud.tencent.com/tcr) 控制台，选择左侧导航栏中的【Helm Chart】。
2. 在 “Helm Chart” 页面即可查看当前实例内的 Helm Chart 列表。如需切换实例，请在页面上方的“实例名称”下拉列表中进行选择。
   实例列表包含以下信息及操作：
   - **名称**：Helm Chart 名称，单击可进入 Chart 详情页，可查看并管理 Chart 各个版本，并可在【基本信息】页签内查看各个版本 Chart 包内的文件详情。
   - **命名空间**：Helm Chart 所属命名空间。
   - **创建时间**：Helm 首次推送至仓库的时间。
   - **操作**：单击【删除】以删除当前仓库。
