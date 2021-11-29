本文为您详细介绍如何使用腾讯云服务器（CVM）执行持续集成构建任务。

## 前提条件

使用 CODING 持续集成的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见  [开通服务](https://cloud.tencent.com/document/product/1115/37268)。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 单击菜单栏左侧**持续集成** > **构建节点**。

## 功能介绍

CODING 中提供了内置云服务器用来执行持续集成（CI）中的构建计划，能够胜任大部分构建任务。但如果碰上了大型项目的构建，或者需要在本地服务器生成构建成果，单个计算资源就显得捉襟见肘了。针对这一部分需求，CODING 现已支持接入第三方计算资源作为构建节点，甚至可以接入多个服务器共同作为构建节点池，打造专属的计算集群。

下面将会以腾讯云 CVM 为例，演示如何在 CODING 持续集成中接入自己的计算资源。

## 开通安全组

在购买了 [腾讯云 CVM ](https://buy.cloud.tencent.com/cvm?tab=lite&regionId=1&projectId=-1) 后，第一件要做的事情就是开放相应的 [安全组策略](https://cloud.tencent.com/document/product/213/34601)，入站和出站规则都需要设置。
![](https://qcloudimg.tencent-cloud.cn/raw/0155ee0e2b8a7a92af6182049083b592.png)

## 登录服务器

在操作栏中单击**登录**，按照提示输入 root 密码。如果忘记密码可以在**更多** > **密码/密钥**中单击**重置密码**后再次输入即可。
![](https://qcloudimg.tencent-cloud.cn/raw/746fb31f6b23e6ad5f11a490c50dab59.png)
做完上述操作并成功登录服务器后，可以选择 Docker 或 cci-agent 两种方式将服务器接入至构建节点池。如果想使用与 CODING 官方提供的运行节点一致的环境，请选择使用 Docker 运行构建节点。如果想使用节点上自带的环境，譬如需要使用 MacOS 上的 Xcode 编译 iOS 应用，请选择 cci-agent 方式进行接入。

## 接入构建节点池

### 使用 Docker（推荐）

使用 Docker 的前提是服务器上已经安装了 Docker。需要注意的是，部分 openVZ 虚拟化的服务器因内核较低，无法成功安装 Docker，当然我们的腾讯云 CVM 是没有这个问题的。下面使用 `curl` 命令安装 Docker。

```curl
curl -fsSL https://get.docker.com/ | sh
```

如果提示 curl: command not found，那是因为服务还没有安装`curl`，相应的安装命令：

- 在 Fedora/Centos 上用 yum 安装：$ yum install curl
- 在 Ubuntu/Debian 上用 apt 安装：$ apt install curl

待 Docker 安装完成后，前往 CODING 进入**项目** > **持续集成** > **构建节点**，在构建节点页复制配置命令。
![](https://main.qcloudimg.com/raw/5d1168f061bd1f37cad89f86abfddfd2.png)
等待一小会，等镜像构建完成后便会提示构建成功。
![](https://qcloudimg.tencent-cloud.cn/raw/b821d036c1e9ab9203b7bd282cb90b6a.png)
在 CODING 构建节点页也可以看到新注册上线的服务器。
![](https://main.qcloudimg.com/raw/92ee62f7a5c076f445e151a49b1bf1aa.png)

### 手动接入 cci-agent
在 CODING 的构建节点页一键生成初始化命令，并在服务器中运行该命令。
![](https://main.qcloudimg.com/raw/1ac3342107d23ec4d87e7f701edea878.png)
执行 cci-agent 启动命令。
```cci-agent
./cci-agent up -d
```

等待配置运行安装完成。
![](https://qcloudimg.tencent-cloud.cn/raw/d275fdf77aafb3b477be7a071f46581c.png)
配置完成后会出现在节点池中。
![](https://main.qcloudimg.com/raw/8c0653db3bd8058e630afc71928a7f6c.png)
在安装过程中，节点状态会不断变化。关于节点的状态说明：

- 闲置：构建节点此时空闲。
- 占用：构建节点已被分配到构建任务中使用。
- 准备中：构建节点正在准备构建环境。
- 开启：只有处于开启状态的节点才能被分配使用，如果关闭节点不会影响正在运行的构建任务。
- 删除：节点将会脱离 CODING 持续集成服务，但只会删除工作空间和相关的配置信息，之前产生的全局缓存文件仍会保留。

### 使用自定义节点

计算资源接入成功后，在**构建计划** > **设置**中选择使用自定义节点。
![](https://main.qcloudimg.com/raw/443caae878e65202b89c821ee31d6f3e.png)
保存修改后，触发构建任务后就可以在自己的计算资源集群中执行持续集成任务了。使用自定义节点不会占用 CODING 团队配额，不受并行上限限制。并且服务器集群规模越大，构建大型项目的速度也会越快。



