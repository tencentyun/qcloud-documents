本文为您详细介绍如何基于腾讯云弹性伸缩（AS）使用 CODING 持续部署。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

在当今各种强调云原生的背景下，似乎云主机已经逐渐被大众所抛弃。但是事实真的是这样么？能用腾讯云的云主机玩出 k8s 的效果吗？比如，将服务数量根据业务的状态，进行随心所欲的伸缩。其实答案是可以的，在国外这种技术早已兴起，可以说蔚然成风，但在国内却不温不火。让我们今天，以一个技术人对新鲜事物的探索视角，来看看如果使用云主机来玩出新的花样。

我们经过大量实践，编写了此简易用例。在力求保证准确性的前提下，介绍它的快速使用方法，以致力于让您看到一个不一样的云主机，从而窥探技术的前沿。

通过阅读此文章，您将主要有如下收获：

1.  如何使用云主机进行随心所欲的扩/缩容；
2.  其中所用的工具、概念的分享与介绍。

## 效果展示

此处分两部分，简单的整体介绍与演示。

## 简介

初始时，所有的请求通过负载均衡器进行转发，且每个服务组拥有一个实例。

![](https://help-assets.codehub.cn/enterprise/20200728140147.png)

请求示例

![](https://help-assets.codehub.cn/enterprise/20200728140202.png)

## 扩容

![](https://help-assets.codehub.cn/enterprise/20200728140300.gif)

结果为

![](https://help-assets.codehub.cn/enterprise/20200728140538.gif)

可以看见，module01 服务组中的实例已经增加 1 个，等实例启动完成，即变成为

![](https://help-assets.codehub.cn/enterprise/20200728141403.png)

此时的请求如下，可以明显注意到，服务器的 hostname 已经变成了两个

![](https://help-assets.codehub.cn/enterprise/20200728141434.png)

## 缩容

![](https://help-assets.codehub.cn/enterprise/20200728141523.gif)

缩容的结果，我们可以很清楚地从下面这张图中看到

![](https://help-assets.codehub.cn/enterprise/20200728141545.png)

以上便是扩/缩容部分的展示，除了上述显而易见的演示外，还有更多的功能隐藏在 CODING 持续部署中等待你的发掘。相信好奇心让你在内心深处产生了一个疑问：那么该如何下手？So, talk is cheap，show you the code!

## 动手实践

在动手实践开始之前，你所需的准备工作为：

-   腾讯云账号（提供云服务；提供 [CODING DevOps](https://console.cloud.tencent.com/coding)）

当然也可以在已有的 CODING 账号中，添加腾讯云的账号，进行后续的实践。

## 项目

[DEMO 项目](https://ci-cd.coding.net/public/tencent-asg/tencentcvm-java/git/files)中含有两个模块，即 module01 和 module02，这两个单独的服务，分别监听 9000、9001 这两个端口。另外该仓库中还包含后续所需要的 CI 配置文件，CD 配置文件，可以做一个参考。在开始前，先将此项目克隆到您的账号下。

### 开始主要配置前

在开始主要的配置（即 CI、CD）前，您需要先完成下述步骤，才能顺利地进行后面的配置。

1.  在 代码仓库 中新建一个代码仓库，让后将项目代码上传至该仓库中
2.  在 项目设置 - 功能开关 中打开 持续集成、持续部署 以及 制品库
3.  在 制品库 中新建一个名为 jar-repo 的 Generic 类型的仓库

## 构建计划

在持续集成中，依次选择：【构建计划】->【+】-> 模板选【自定义构建过程】

![](https://help-assets.codehub.cn/enterprise/20200728142850.png)

配置来源勾选 `使用代码库中的 Jenkinsfile`，确认即可。

![](https://help-assets.codehub.cn/enterprise/20200728142908.png)

配置完手动触发一次构建计划，让制品库中有编译好的 jar 包。

## 持续部署

1.  在部署设置中绑定腾讯云账号，名称为 tencent。

2.  在 部署控制台 中新增应用，名称为 tencent-cvm，勾选支持 `腾讯云服务器` 部署，并将应用与项目进行关联。

![](https://help-assets.codehub.cn/enterprise/20200728142930.png)

3.  新建一个负载均衡器，留作后面配置使用。如下图所示

![](https://help-assets.codehub.cn/enterprise/20200728142951.png)

4.  创建一个部署流程 java-sample，选择 `复制现有流程 - 空白模板` 或 选择 `腾讯云服务器 - 并行部署多个弹性伸缩组` 模板，并按如下方式添加/配置阶段。

> 如果使用模板，请注意模板中生成的阶段与本文描述中阶段的对应关系，建议修改阶段名称，与本文保持一致。

![](https://help-assets.codehub.cn/enterprise/20200728143626.png)

此流水线中包含两个并行的 bake + deploy 操作。以 module01 为例，

-   BakeModule01 阶段的类型是 bake，主要用做烧录镜像，类似于 docker 中的构建自己的镜像，核心工作是往镜像中加入我们的服务；

-   DeployModule01 阶段的类型是 deploy，主要是将含有我们服务的镜像资源启动起来，类似于 docker 中的 `docker run` ，核心工作是启动。

## 持续部署详细配置

先看部署流程中的 `配置`，它主要定义一些流水线启动所需的制品，也就是我们烧录镜像所需要的 jar 包，以及流水线的触发方式。

### 启动所需制品

可粗浅理解为，当此部署流程开始时，能获取到 module01、module02 的 jar 的下载方式。

#### module01

![](https://help-assets.codehub.cn/enterprise/20200728143831.png)

注意勾选 `使用默认制品`，因为前面只是一个制品匹配规则，在匹配失败的时候，会使用默认的制品。

#### module02

还需再添加一个制品，步骤与上面的类似，但是为 module02。同样注意勾选 `使用默认制品`。

### 自动触发器

点击添加触发器，类型选择 `Webhook触发` ，如下：

![](https://help-assets.codehub.cn/enterprise/20200728143850.png)

**拷贝该 Webhook 地址到前面构建计划中的触发持续部署中，以便于在构建计划中触发此流水线**，如下：

![](https://help-assets.codehub.cn/enterprise/20200728144131.png)

### bake

*此处以 **CentOS 系统** 为例，若选择 **Ubuntu 系统**，请务必注意下面脚本是否兼容或适用。*

先看 BakeModule01 的配置，如下图所示。此处有两处建议：
-   镜像名称留空
-   **在`云服务器配置`中，复用已存在的 VPC 和子网**

上述建议的原因是由于当前腾讯云的上述资源存在数量上的限制，具体可参考腾讯云文档相关内容。

![](https://help-assets.codehub.cn/enterprise/20200728144153.png)

点开高级配置，

-   在`预装软件-软件名称`栏填入我们服务依赖的软件 `java-1.8.0-openjdk-devel.x86_64`，即 java。
-   在`持久化文件`处，选择 module01 制品，并填写好将该制品复制到镜像中的位置 `/root/module_01-1.0-SNAPSHOT.jar`。
-   在`运行脚本`处，添加脚本，生成服务的自启动配置，如下：

```shell
echo '''#!bin/bash
java -jar /root/module_02-1.0-SNAPSHOT.jar 2>&1 > module_01.log &''' > /root/autostart.sh

chmod +x /root/autostart.sh

echo "begin to add systemd configuration..."

echo '''[Unit]
Description=TencentCVM Module 02
After=network.target

[Service]
Type=forking
ExecStart=/root/autostart.sh
User=root

[Install]
WantedBy=multi-user.target ''' > /usr/lib/systemd/system/tencentcvm.service

systemctl enable tencentcvm
```

![](https://help-assets.codehub.cn/enterprise/20200728144349.png)

对 BakeModule02 的配置，基本与 BakeModule01 类似，但是需要**注意高级设置部分，要改为 module02 的 jar 包，包括脚本、持久化文件**。为确保准确性，在此还是给出 module02 相关的 bake 高级配置信息，如下：

![](https://help-assets.codehub.cn/enterprise/20200728144417.png)

### deploy

先看 DeployModule01 的配置，如下：

![](https://help-assets.codehub.cn/enterprise/20200728144441.png)

具体的各项设置为：

![](https://help-assets.codehub.cn/enterprise/20200728144501.png)

![](https://help-assets.codehub.cn/enterprise/20200728144517.png)

要注意安全组所定义的内容中，是否含有我们所需的业务端口，即 9000 和 9001，如果没有，那么后面部署会出现问题。

![](https://help-assets.codehub.cn/enterprise/20200728144537.png)

对 DeployModule02 的配置，它与 DeployModule01 的区别在于集群的名称、lb 的配置

![](https://help-assets.codehub.cn/enterprise/20200728144554.png)

![](https://help-assets.codehub.cn/enterprise/20200728144641.png)

其余均类似。

## 跑起来

至此，bake 和 deploy 的配置都已完成。让我们开始吧！

在 `持续集成-构建计划` 中，手动触发一次构建计划，让整个流程先跑起来，如下：

构建计划的执行结果

![](https://help-assets.codehub.cn/enterprise/20200728144708.png)

部署流程的执行结果

![](https://help-assets.codehub.cn/enterprise/20200728144755.png)

执行完后的集群信息

![](https://help-assets.codehub.cn/enterprise/20200728144809.png)

通过负载均衡器的访问结果

![](https://help-assets.codehub.cn/enterprise/20200728144821.png)

## 结语

我们还可以通过代码仓库来触发构建计划，即可通过代码提交的方式，来触发构建计划。这样我们就能做到了，在代码提交后，后面的部署完全自动化，并且部署成功后，可以随时调整服务的数量、或者设定检测条件，如 CPU 占用率达到 50% 便进行扩容。最后值得一提的是，部署应用时，新旧服务的交替，还有策略可供选择，如红/黑等。还有更多值得发现的功能，尽在 CODING DevOps，等你来发现！