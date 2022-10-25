## 操作场景
轻量应用服务器支持使用 Docker 基础镜像创建实例，您可选择在创建实例时创建容器，也可在实例创建成功后通过控制台直接创建容器。您可使用该功能快速部署容器化应用，并直接通过控制台便捷管理 Docker 容器。

本文介绍如何通过轻量应用服务器控制台，进行创建、重建容器等容器管理操作。
 



## 操作步骤

### 创建容器
您可结合实际情况，选择以下方式创建容器：
<dx-tabs>
::: 购买实例时创建容器[](id:createBeforeExisting)
在 [轻量应用服务器购买页面](https://buy.cloud.tencent.com/lighthouse?buy_from=lh-doc)，选择所需配置完成轻量应用服务器购买。
其中，“镜像”及“容器配置”请参考以下信息进行配置，其他参数可参考 [购买方式](https://cloud.tencent.com/document/product/1207/44580) 进行选择。

#### 镜像
根据操作系统版本按需选择 **Docker基础镜像**。

#### 容器配置[](id:containerConfiguration)


<dx-alert infotype="explain" title="">
您可在创建实例时添加容器，实例创建成功后将自动按照配置创建 Docker 容器（相当于 `docker run`）。若您仅需在实例创建成功后再创建容器，请参考 [已有实例创建容器](#createAfterExisting)。
</dx-alert>


1. 单击**添加容器**后，参考以下信息进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/3d0c21bef9a032c9afb0be19c59cd2b9.png)
 - **容器名称**：自定义容器名称，不填写则默认使用 Docker 分配的随机名称。
 - **Docker镜像**：
    - **镜像仓库地址**：单击**选择镜像**，在弹出的“选择镜像”窗口中，选择所需镜像仓库地址。
<dx-alert infotype="notice" title="">
- 仅支持选择 [腾讯云容器镜像服务（TCR）个人版](https://console.cloud.tencent.com/tke2/registry/user?rid=1) 中的“我的镜像（公有类型）”。
- 建议选择与当前轻量应用服务器实例处于相同地域的镜像仓库，访问不同地域的镜像仓库将消耗公网流量，并受到公网网络出入带宽的影响。
</dx-alert>
      - **镜像版本**：单击**选择版本**，在弹出的“选择镜像版本”窗口中，选择所需镜像版本，不选则默认使用 `latest` 版本。
 - **启动命令**：可输入输入启动命令（Command）和参数（Arg），例如 `/run.sh`。
2. 单击**高级设置**后，参考以下信息配置容器端口、环境变量及挂载存储卷设置。如下图所示：
![](https://main.qcloudimg.com/raw/25324d7806767670b70bd6f5c3b605d6.png)
 - **绑定端口**：单击**添加**后，输入服务器端口、容器端口，并选择协议（支持 TCP、UDP 及 SCTP 协议）。
    相当于 `docker run` 命令中的 `-p` 参数。若服务器端口仅输入数字（例如80），则代表对应绑定的容器端口可被外部访问。若服务器端口输入 `127.0.0.1:数字`，则代表将对应的容器端口绑定至 localhost。
 - **环境变量**：单击**添加**后，输入变量名及变量值。
    相当于 `docker run` 命令中的 `-e` 参数。您可以在 Docker 容器中设置环境变量，或者覆盖您所使用的 Docker 镜像对应的 Dockerfile 中定义的环境变量。
 - **挂载存储卷**：单击**添加**后，输入服务器目录及容器目录。
   相当于 `docker run` 命令中的 `-v` 参数。您可将轻量应用服务器操作系统中的目录挂载至 Docker 容器中的目录，以实现容器内数据的持久化存储。若您输入的服务器目录当前在操作系统中并不存在，则将自动为您在服务器操作系统中创建该目录。
:::
::: 已有实例创建容器[](id:createAfterExisting)


<dx-alert infotype="explain" title="">
使用 Docker 基础镜像创建的实例，可通过控制台直接创建容器。若您的实例未使用 Docker 镜像，可通过 [重装系统](https://cloud.tencent.com/document/product/1207/44576) 进行重装。
</dx-alert>


1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签，并单击**新建容器**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/fb82f08317fa55519688aeee5755fe18.png)
3. 在弹出的“新建容器”窗口中，参考 [容器配置](#containerConfiguration) 信息进行配置。
4. 单击**确定**即可创建容器。
:::
</dx-tabs>


### 重建容器
您可通过控制台重建容器，相当于删除容器后再使用新配置重新创建容器。重建容器支持重新设置容器的启动命令、绑定端口、环境变量和挂载存储卷。


<dx-alert infotype="explain" title="">
重建容器操作将会导致容器内的非持久化数据丢失，以及一段时间的对外服务中断。
</dx-alert>


1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签。
3. 选择需重建容器所在行右侧的**更多** > **重建**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cfc40e59a0eabc7d7c503f2f1f1f5699.png)
4. 在弹出的“重建窗口”中，您可选择容器的各项配置为“保持当前配置”或“使用新配置”。如下图所示：
![](https://main.qcloudimg.com/raw/952dac3be57129b147b5a411231080f6.png)
 - 若选择“保持当前配置”，则可通过 [查看容器详情](#containerDetails) 获取容器现有配置信息。
 - 若选择“使用新配置”，则可参考 [容器配置](#containerConfiguration) 进行配置。
5. 单击**确定**即可开始重建。


### 删除容器
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签。
3. 按需进行单个或批量容器删除：
 - **删除单个容器**：选择需删除容器所在行右侧的**更多** > **删除**，并在弹出的“删除容器”窗口中单击**确定**。
 - **批量删除容器**：勾选需删除容器，单击列表上方的**删除**，并在弹出的“删除容器”窗口中单击**确定**。


## 相关操作

### 其他容器操作
您可通过控制台进行容器的启动、停止及重启操作。步骤如下：
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签。
 - **重启**：选择需重建容器所在行右侧的**重启**，并在弹出的“重启容器”窗口中单击**确定**。
 - **启动**：选择需启动容器所在行右侧的**更多** > **启动**，并在弹出的“启动容器”窗口中单击**确定**。
 - **停止**：选择需停止容器所在行右侧的**更多** > **停止**，并在弹出的“停止容器”窗口中单击**确定**。

### 查看容器详情[](id:containerDetails)
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签。
3. 单击容器所在行前的 <img src="https://main.qcloudimg.com/raw/7d67a3ff2ace65d914dd98855d3794b2.png" style="margin:-3px 0px">，即可查看容器详细信息。如下图所示：
![](https://main.qcloudimg.com/raw/65b8929be9ace8204cb48e7cfc472061.png)
4. 单击**查看更多**，可在弹出窗口中查看容器 docker inspect 详细信息。

### 查看容器操作事件
您可通过以下两种方式，查看容器操作事件。
- 在实例详情页中，选择**容器管理**页签。即可在页面右侧查看“最近操作事件”，支持查看5条最近容器操作事件概要信息。
- 在实例详情页中，选择**容器操作事件**页签。即可在页面查看并按需筛选容器操作事件。


### 修改容器名称
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)，选择实例。
2. 在实例详情页中，选择**容器管理**页签。
3. 单击容器名称右侧的 <img src="https://main.qcloudimg.com/raw/65111c95fa9fdba487b81bda72e156a3.png" style="margin:-3px 0px">，在弹出的“修改容器名称”窗口中输入新名称。
4. 单击**确定**即可完成修改。
