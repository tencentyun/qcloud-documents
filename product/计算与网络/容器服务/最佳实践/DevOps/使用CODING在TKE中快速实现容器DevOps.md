



## 概述

DevOps 理念被越来越多的企业采纳，DevOps 是 Development 和 Operations 的组合词，代表着重视“软件开发人员（Dev）”和 “IT 运维技术人员（Ops）”之间沟通合作的文化，旨在透过自动化“软件交付”和“架构变更”的流程，使得构建、测试、发布软件的过程能够更加地快捷、频繁和可靠。在云原生时代，使用 Devops 思维可实现敏捷开发，本文将介绍和实践专为云原生打造的 TKE 容器 DevOps 服务，实现从代码提交时触发镜像自动构建，镜像构建成功时触发自动部署流程将应用部署、更新到 TKE 集群中的一整套无缝衔接的 Devops 流水线。



## TKE 容器 DevOps 
### 简介

TKE 容器 DevOps 是 [容器服务 TKE](https://cloud.tencent.com/document/product/457/)、[容器镜像服务 TCR](https://cloud.tencent.com/document/product/1141/39278) 和 [CODING DevOps](https://cloud.tencent.com/product/coding) 服务紧密结合，面向容器业务场景，具备自动化代码编译、容器镜像构建、镜像推送及应用部署等功能，为客户提供强大的一站式云原生 DevOps 服务。容器 DevOps 快速入门请参见 [TKE 和 Coding 协同业务实现快速迭代](https://cloud.tencent.com/document/product/457/47834)。



### 业务流程

TKE 容器 DevOps 服务贯穿了整个应用开发和部署流程的全生命周期管理，实现了从更新代码到应用部署、更新的自动化，业务流程如下图所示：
![process](https://main.qcloudimg.com/raw/19a60b1a7ee79e58188676085808d535.svg)


## 前提条件

- 已创建 TKE 测试集群，创建过程可参见 [部署容器服务 TKE](https://cloud.tencent.com/document/product/457/11741)。
- 开通 [TCR](https://cloud.tencent.com/document/product/1141/39278) 服务。并已创建可访问的 TCR 测试实例和生成测试实例访问凭证，TCR 需要开通企业标准版或高级版支持云原生交付工作流，详情请参见 [容器镜像服务购买指南](https://cloud.tencent.com/document/product/1141/40540)。目前 TCR 支持区域请参见 [支持地域](https://cloud.tencent.com/document/product/1141/40540)。
- 已开通 [CODING DevOps](https://cloud.tencent.com/document/product/1115/37268) 服务，并已创建和完善 Coding Devops 团队。如使用子账号进行操作，请使用主账号在 [CODING DevOps 控制台](https://console.cloud.tencent.com/coding/container-devops) 快速创建拥有权限的子用户或参考 [子用户权限设置](https://cloud.tencent.com/document/product/598/10594) 提前为子账号授予对应实例的操作权限。
	
	
## 操作步骤


TKE 容器 Devops 功能提供了强大的云原生 Devops 服务，本文将介绍 TKE 容器 Devops 如何实现从源码更新到业务发布的整套自动化流程。




### 访问容器 DevOps 
登录容器服务控制台，选择左侧导航栏中的 **[DevOps](https://console.cloud.tencent.com/coding/container-devops)**，单击**立即使用**。如下图所示：
![](https://main.qcloudimg.com/raw/2ace8e2476fea433581b712463b73a22.png)


### 配置代码托管[](id:step2)

在 Coding 团队主页面创建一个测试项目和测试代码仓库，创建步骤请参见 [创建项目并创建代码仓库](https://cloud.tencent.com/document/product/457/47834#.E5.88.9B.E5.BB.BA.E9.A1.B9.E7.9B.AE.E5.B9.B6.E5.88.9B.E5.BB.BA.E4.BB.A3.E7.A0.81.E4.BB.93.E5.BA.93.3Cspan-id.3D.22createproduct.22.3E.3C.2Fspan.3E)。关于 Coding 代码托管介绍请参见 [代码托管介绍](https://help.coding.net/docs/host/introduce.html )。

### 创建构建计划
1. 登录 Coding DevOps ，选择左侧导航中的 **[项目](https://tencent-test.coding.net/user/projects)**，进入项目管理页。
2. 在“项目管理页”中，单击已创建 [测试项目](#step2) 的名称，进入该项目详情页。
3. 在左侧导航栏中选择**持续集成** > **构建计划** > **创建构建计划**，进入**选择构建计划模版**页面。
>? 构建计划是持续集成的基本单元，可以通过选择构建计划模版快速创建一个构建计划，详情请参见 [快速开始持续集成](https://help.coding.net/docs/ci/start.html)。
>
4. 选择 “构建镜像并推送到 TCR 企业版” 模版快速创建一个构件计划，如下图所示：
![](https://main.qcloudimg.com/raw/dd99288dbf9a993199530f22ff789926.png)
 根据构建计划模版选择需要检出的代码源和配置 TCR 访问凭证相关环境变量，在右边可查看模版生成的 Jenkinsfile 预览，如下图所示：
 >? Coding DevOps 和 TCR 实例之间内网互通，镜像 push 默认使用内网传输，无需另外配置。
 > 
![](https://main.qcloudimg.com/raw/414a5b4d3dcb1faa2f1c794be8cc7493.png)
使用构建模版生成的构建项目，也可通过在构建计划详情页中选择项目名称，进入项目详情页后单击**设置**菜单对构建详情进行自定义配置，构建计划配置页面如下图所示： 
![](https://main.qcloudimg.com/raw/7bea5de5055144ec617d39aa1844e3fe.png)
 - **基础信息**基础配置页面可选择代码源和节点池等基础配置，节点池相关说明请参见 [构建节点](https://help.coding.net/docs/ci/node/overview.html)。
 - **流程配置**用来配置运行构建任务的环境，相关说明请参见 [构建环境](https://help.coding.net/docs/ci/ways.html)。
 - **触发规则**用来配置构建计划的触发规则，可支持通过多种方式来触发构建计划，相关说明请参见 [触发规则](https://help.coding.net/docs/devops/ci/trigger.html)。
 - **变量与缓存**环境变量与缓存配置，相关说明请参见 [环境变量](https://help.coding.net/docs/ci/env.html) 和 [缓存目录](https://help.coding.net/docs/ci/cache.html)。
 - **通知提醒**构建计划完成时可向指定的 Coding 团队成员发送通知提醒。
6. 单击**确认**即可完成创建构建计划。
7. （可选）在**项目配置** > **开发者选项** > **WebHook**中选择**新建 WebHook**，将事件通知推送到企业微信等即时通信平台，详情请参见 [WebHook](https://help.coding.net/docs/project/open/webhook.html) 和 [绑定企业微信群机器人](https://help.coding.net/docs/project/open/wechat-robot.html)。更多关于 Coding 持续集成的介绍请参见 [持续集成介绍](https://help.coding.net/docs/ci/index.html)。



### 创建持续部署
1. 登录 Coding DevOps，选择左侧导航中的 **[项目](https://tencent-test.coding.net/user/projects)**，进入项目管理页。
2. 在“项目管理页”中，单击已创建 [测试项目](#step2) 的名称，进入该项目详情页。
3. 在左侧导航栏中选择**持续部署** > **Kubernetes**，单击**立即配置**。如下图所示：
![](https://main.qcloudimg.com/raw/bd0f34e27589669f5fc01ed0e144e8ce.png)
4. 在“部署控制台”页面，自定义选择 [需要配置的云账号](#one) 类型即可继续进行 [配置应用和流程](#two)、[关联项目和应用](#three) 及 [开始部署](#four) 等后续步骤。

#### 配置云账号[](id:one)

如何选择云账号类型请参见 [云账号](https://help.coding.net/docs/cd/cloudaccount.html) 官方文档，添加配置部署云上资源的访问云账号信息，可以选择**腾讯云 TKE**或者**Kubernetes**类型的云账号，输入相关认证配置添加云账号，本文以选择**Kubernetes**为例介绍如何配置云账号。
1. 在“基于 Kubernetes 的持续部署”页面，单击**立即配置**。
2. 在“云账号管理”页面，单击右侧的**绑定云账号**。
3. 在“绑定云账号”页面，选择**Kubernetes**，其他内容按需选择。如下图所示：
![](https://main.qcloudimg.com/raw/21cedb65beee545294b7fc04ab4768b2.png)
4. 单击**确定**即可完成绑定云账号。




#### 配置应用和流程[](id:two)

关于 Coding 应用与项目相关说明请参见 [应用与项目](https://help.coding.net/docs/cd/app-project.html) 和 [流程配置](https://help.coding.net/docs/cd/pipe/overview.html)，本文将介绍配置应用和流程过程中的关键配置项。
1. 在创建应用时，需要勾选** Kubernetes(TKE) 部署**方式，如下图所示：
![](https://main.qcloudimg.com/raw/ed426b65010cebfea21a86dafe131939.png)
2. 在新建的应用中创建部署流程时，选择**Kubernetes**流程模版，再根据实际需要选择模版流程，本文以“部署 Deployment 和 Service 到 Kubernetes 集群”流程为例。如下图所示：
![](https://main.qcloudimg.com/raw/e9dc02a43375d9d26f12071377ab3514.png)
3. 在**部署流程**中配置部署流程时，**启动所需制品**选项关联之前的持续集成环节生成的 TCR 仓库镜像制品。如下图所示：
![](https://main.qcloudimg.com/raw/4f957dd0e30ad1701d62a66421ad836c.png)
4. 使用**自动触发器**绑定 TCR 仓库镜像制品，当有新版本镜像构建成功时，将自动触发部署流程。配置方式如下图所示：
![](https://main.qcloudimg.com/raw/ef7b2d48a7d5726f83f02c2d2c8c1e7b.png)
5. 配置**部署 Deployment**和**部署 Service**部署阶段，两个阶段的配置方式类似，选择添加有部署权限的 [云账号](#one) 和填写自定义的 Manifest，即自定义部署 YAML 模版。
![](https://main.qcloudimg.com/raw/8f389ec513011636f9c8a0fa84dc92a3.png)
本文将以“手动配置 TKE 拉取 TCR 私有仓库镜像的访问凭证” 的方式为例，自定义 Deployment YAML。示例如下：
>! 本示例仅使用简单的 Deployment YAML 部署到 Kubernetes 集群，使用了默认的滚动部署（RollingUpdate）更新策略。实际上，可以借助 Nginx-ingress / Istio 等工具配置更高级的更新策略，如蓝绿发布、金丝雀、A / B 测试等，具体使用方法可参见 [蓝绿发布](https://help.coding.net/docs/best-practices/cd/blue-green.html) 、[Nginx-ingress 实现自动化灰度发布](https://help.coding.net/docs/best-practices/cd/nginx-ingress.html)、[持续部署 + TKE Mesh 灰度发布实践](https://help.coding.net/docs/best-practices/cd/tke-mesh.html)。
>
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devops-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: devops-app
  template:
    metadata:
      labels:
        app: devops-app
    spec:
      containers:
        - image: xxx-test.tencentcloudcr.com/xxx-test/jokey-test  # 示例镜像地址
          name: devops-app
          ports:
            - containerPort: 5000
      imagePullSecrets:  # 私有仓库访问凭证配置 
        - name: tcr-secret # 访问凭证 secret
```
其中，`spec.template.spec.containers.*.image` 的镜像地址字段包含在 Coding 的转换匹配规则中，关于转换匹配规则的说明可参见 [在 manifest 中绑定制品](https://help.coding.net/docs/cd/pipe/artifacts/in-kubernetes.html#%E5%9C%A8-manifest-%E4%B8%AD%E7%BB%91%E5%AE%9A%E5%88%B6%E5%93%81)。
>? TKE 拉取 TCR 私有仓库镜像有两种方式：
>- 在 TCR 支持区域内可配置 TKE 免密拉取 TCR 容器镜像，关于 TCR 支持区域请参见 [支持地域](https://cloud.tencent.com/document/product/1141/40540)，关于如何配置可参见 [TKE 集群使用 TCR 插件内网免密拉取容器镜像](https://cloud.tencent.com/document/product/1141/48184)。
>- 手动配置 TKE 拉取 TCR 私有仓库镜像的访问凭证，配置方式可参见 [TKE 配置私有仓库访问示例](https://help.coding.net/docs/cd/question/private-repo.html#Kubernetes-%E4%BA%91%E8%B4%A6%E5%8F%B7%EF%BC%88TKE-%E9%9B%86%E7%BE%A4%EF%BC%89) 。
>
自定义的 Service Manifest YAML 示例：
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: devops-svc
  name: devops-svc
spec:
  ports:
    - port: 5000
      protocol: TCP
  selector:
    app: devops-app
```
6. （可选）为部署流程的每个阶段配置自定义事件通知，可方便快捷获知部署流程执行情况。本文以配置“企业微信”通知方式，获取企业微信 Webook 机器人链接的方法可参见 [创建企业微信群机器人](https://help.coding.net/docs/project/open/wechat-robot.html#%E5%88%9B%E5%BB%BA%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E7%BE%A4%E6%9C%BA%E5%99%A8%E4%BA%BA)。

#### 关联项目和应用[](id:three)

关联项目和应用配置可参见 [项目和应用关联](https://help.coding.net/docs/cd/app-project.html#%E5%BA%94%E7%94%A8%E4%B8%8E%E9%A1%B9%E7%9B%AE%E5%85%B3%E8%81%94)。

#### 开始部署[](id:four)
提单发布使用和配置请参见 [新建发布单](https://help.coding.net/docs/cd/app-project.html#%E6%96%B0%E5%BB%BA%E5%8F%91%E5%B8%83%E5%8D%95)。更多关于 Coding 持续部署的详细介绍请参见 [持续部署介绍](https://help.coding.net/docs/cd/overview.html)。



## 测试验证

在项目代码文件中修改添加如下图所示的 v2 API 代码后提交 master 分支：
![](https://main.qcloudimg.com/raw/edf184f16d1feaf6255a417947556242.png)
由于**持续集成**中的构建计划使用了 “代码更新时自动执行” 的事件触发配置，了解相关触发配置请参见 [触发规则](https://help.coding.net/docs/devops/ci/trigger.html)。当提交修改的代码时，会自动触发关联的构建计划执行，如下图所示：
![image-20201028211045329](https://main.qcloudimg.com/raw/5f369aa9ab3eb5f97ac9a78e015dc6cc.png)
如果为持续集成配置企业微信 Webhook 通知，企业微信也会收到相应的即时通知消息，如下图所示：
![](https://main.qcloudimg.com/raw/e84e986ffe004abaa9d6a601aca947b4.png)
当构建计划生成 Docker 镜像制品时，又会自动触发关联的**持续部署**流程，将新的镜像应用更新到 TKE 集群中，如下图所示：
![image-20201028211358719](https://main.qcloudimg.com/raw/e4ecb43fec5cba253d5e20a16c7c8bed.png)
如果部署流程有配置企业微信通知的话，当部署流程任务完成时，会收到对应的企业微信部署完成通知，如下图所示：
![](https://main.qcloudimg.com/raw/c393b7f3cb8ca6dd224a3ae7b9cf9229.png)
此时，可以在 TKE 中看到已经成功更新了工作负载，如下图所示：
![image-20201028214913813](https://main.qcloudimg.com/raw/6ab74e1d81f6c1f44c302ffbaeb1babc.png)
从测试验证结果可以看出，我们在 TKE 中实现了从源码更新到业务发布的整套 DevOps 流程。
