# 在 TKE 中实践 DevOps



## 概述

DevOps 理念被越来越多的企业采纳，DevOps 是 Development 和 Operations 的组合词，代表着重视「软件开发人员(Dev)」和「IT 运维技术人员(Ops)」之间沟通合作的文化；旨在透过自动化「软件交付」和「架构变更」的流程，使得构建、 测试、发布软件的过程能够更加地快捷、频繁和可靠。在云原生时代，我们更需要 Devops 思维来实现敏捷开发， 本文将介绍和实践专为云原生打造的 TKE 容器 DevOps 服务，实现从代码提交时触发镜像的自动构建，再到镜像构建成功时触发自动部署流程将应用部署、更新到 TKE 集群中的一整套无缝衔接的 Devops 流水线。



## TKE 容器 DevOps 简介

TKE 容器 DevOps 是 [容器服务 TKE](https://cloud.tencent.com/document/product/457/)、[容器镜像服务 TCR](https://cloud.tencent.com/document/product/1141/39278) 和 [CODING DevOps](https://cloud.tencent.com/product/coding) 三个服务紧密结合，面向容器业务场景，具备自动化代码编译、容器镜像构建、镜像推送及应用部署等功能，为客户提供强大的一站式云原生 DevOps 服务。容器 DevOps 快速入门请参考 [TKE 和 Coding 协同业务实现快速迭代](https://cloud.tencent.com/document/product/457/47834) 最佳实践文档。



## TKE 容器 DevOps 业务流程

TKE 容器 DevOps 服务贯穿了整个应用开发和部署流程的全生命周期管理，实现了从更新代码到应用部署、更新的自动化，如下图所示：

![process](https://main.qcloudimg.com/raw/19a60b1a7ee79e58188676085808d535.svg)



## 如何使用 TKE 容器 DevOps

### 操作场景

TKE 容器 Devops 功能提供了强大的云原生 Devops服务，下面将按照上述 TKE 容器 Devops 业务流程图来实现从源码更新到业务发布的整套自动化流程。

### 前提条件

- 创建 TKE 测试集群

  关于如何创建可参考文档 [部署容器服务TKE](https://cloud.tencent.com/document/product/457/11741)。

- 开通 [容器镜像服务 TCR](https://cloud.tencent.com/document/product/1141/39278) 服务

  已创建可访问的 TCR 测试实例和生成测试实例访问凭证。 TCR 需要开通企业标准版或高级版支持云原生交付工作流，详情请参考 [容器镜像服务购买指南](https://cloud.tencent.com/document/product/1141/40540)，目前 TCR 支持区域请参考 [支持地域](https://cloud.tencent.com/document/product/1141/40540)。

- 开通 [CODING DevOps](https://cloud.tencent.com/document/product/1115/37268) 服务

  已创建和完善了 Coding Devops 团队。如使用子账号进行操作，请使用主账号在 [CODING DevOps](https://console.cloud.tencent.com/coding/container-devops) 控制台快速创建拥有权限的子用户或参考 [子用户权限设置](https://cloud.tencent.com/document/product/598/10594) 提前为子账号授予对应实例的操作权限。

### 操作步骤

#### TKE 容器 Devops 访问入口

在 TKE 控制台左侧功能菜单栏点击【Devops】功能链接即可进入【容器 Devops】介绍界面，如下图所示：

![image-20201027152508060](https://main.qcloudimg.com/raw/52ca9b502289c85aa5b358e69a129fc8.png)

点击 【立即使用】即可跳转到所属团队的 Coding 主页面使用相关 DevOps 功能。

#### 配置代码托管

在 Coding 团队主页面创建一个测试项目和测试代码仓库，关于 Coding 代码托管介绍请参考 [代码托管介绍](https://help.coding.net/docs/host/introduce.html ) 。创建步骤如下：

步骤 1：在 Coding 团队主页面【 项目】中创建测试项目，如下图所示：

![image-20201027154142270](https://main.qcloudimg.com/raw/a3d7667b654b2391ad01b6846b0345ec.png)

步骤 2：点击已创建的测试项目 “test-jokey” 进入项目主页面，在【代码仓库】菜单中新建测试代码仓库，如下图所示：

![image-20201027153950849](https://main.qcloudimg.com/raw/bb420e9c94b4030918f63bdc283ecf47.png)

#### 创建构建计划

在测试项目 “test-jokey” 主页面左侧菜单【持续集成】的子菜单 【构建计划】中创建一个构建计划，构建计划是持续集成的基本单元，可以通过选择构建计划模版快速创建一个构建计划，详情请参考文档 [快速开始持续集成](https://help.coding.net/docs/ci/start.html)。

步骤 1：选择 “构建镜像并推送到 TCR 企业版” 模版快速创建一个构件计划，创建示例如下：

![image-20201027205220167](https://main.qcloudimg.com/raw/35e16328dbc48c1c521a276ec2d67828.png)

步骤 2：根据构建计划模版选择要检出的代码源和配置 TCR 访问凭证相关环境变量， 右边可以看到模版生成的 Jenkinsfile 预览，如下图：

> 提示：Coding devops 和 TCR 实例之间内网互通，镜像 push 默认使用内网传输，无需另外配置。

![image-20201027210052362](https://main.qcloudimg.com/raw/05b1948809f31370d26405dce27aa628.png)

使用构建模版生成的构建项目，也可以通过点击构建项目的【设置】菜单再对构建详情进行自定义配置，构建计划配置页面的功能说明如下： 

![image-20201027155032737](https://main.qcloudimg.com/raw/5d1bc0409904065284650ccddccbf216.png)

【基础信息】

​	基础配置页面可选择代码源和节点池等基础配置，节点池相关说明请参考文档 [构建节点](https://help.coding.net/docs/ci/node/overview.html)。

【流程配置】

​	用来配置运行构建任务的环境，相关说明请参考 [构建环境](https://help.coding.net/docs/ci/ways.html)。

【触发规则】

​	用来配置构建计划的触发规则，可支持通过多种方式来触发构建计划，相关说明请参考 [触发规则](https://help.coding.net/docs/devops/ci/trigger.html)。

【变量与缓存】

​	环境变量与缓存配置，相关说明请参考 [环境变量](https://help.coding.net/docs/ci/env.html) 和 [缓存目录](https://help.coding.net/docs/ci/cache.html) 。

【通知提醒】

​	构建计划完成时可向指定的 Coding 团队成员发送通知提醒。

另外还可以在【项目配置 -> 开发者选项 -> WebHook】 中新建 WebHook 的方式将事件通知推送到企业微信等即时通信平台，详情请参考 [WebHook](https://help.coding.net/docs/project/open/webhook.html) 和 [绑定企业微信群机器人](https://help.coding.net/docs/project/open/wechat-robot.html)，配置示例如下图：

![image-20201029142314911](https://main.qcloudimg.com/raw/abe21b637c7cc88a0a969694286dc5d3.png)

想了解更多关于 Coding 持续集成的详细介绍请参考 [持续集成介绍](https://help.coding.net/docs/ci/index.html)。



#### 创建持续部署

在测试项目 “test-jokey” 主页面左侧菜单 【持续集成】的子菜单 【Kubernetes】中根据步骤引导创建持续部署流水线，如下图所示：

![image-20201028162532013](https://main.qcloudimg.com/raw/86962357bdba8d0cfffef2b8b03353b0.png)

##### 配置云账号

请参考 [云账号](https://help.coding.net/docs/cd/cloudaccount.html) 文档，添加配置部署云上资源的访问云账号信息，可以选择【腾讯云 TKE】或者【Kubernetes】 类型的云账号，输入相关认证配置添加云账号，这里选择了【Kubernetes】方式绑定。

![image-20201028153949177](https://main.qcloudimg.com/raw/6105020867677b0608177ef8e07c746e.png)



##### 配置应用和流程

关于 Coding 应用与项目相关说明请参考文档 [应用与项目](https://help.coding.net/docs/cd/app-project.html)和 [流程配置](https://help.coding.net/docs/cd/pipe/overview.html) ，这里仅简单说明下在配置应用和流程过程中的关键配置项。

在创建应用时，需要勾选【 Kubernetes(TKE) 部署】方式：

![image-20201028163103428](https://main.qcloudimg.com/raw/fb37c8e0ccd00b5ed65b2a1bf22d3d48.png)

在新建的应用中创建部署流程时，选择【Kubernetes】流程模版，再根据实际需要选择模版下的流程，这里选择了下图中第二个流程，部署 Deployment 和 Service 到 Kubernets 集群的流程：

![image-20201029110126926](https://main.qcloudimg.com/raw/f47ed856b705531f86a61b0cfd1e4c33.png)

在【部署流程】中配置部署流程时，【启动所需制品】选项关联之前的持续集成环节生成的 TCR 仓库镜像制品：

![image-20201028155758913](https://main.qcloudimg.com/raw/8a6f97977e97f1805ea99ad24b8d5d47.png)

使用【自动触发器】绑定 TCR 仓库镜像制品，这里是重点，作用是当有新版本镜像构建成功时，将自动触发部署流程，配置方式如下：

![image-20201028160108451](https://main.qcloudimg.com/raw/2a2d605dc6afa36432ff3d71d06420f7.png)

接下来就是配置【部署 Deployment】和【部署 Service】部署阶段，两个阶段的配置方式类似，选择之前添加的有部署权限的云账号和填写自定义的 Manifest，即自定义部署 YAML 模版。

![image-20201028165509592](https://main.qcloudimg.com/raw/5f34df7762ab3457b8464a31a245e3b4.png)

自定义 Deployment YAML 示例如下：

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

其中， 对于 `spec.template.spec.containers.*.image` 的镜像地址字段 Coding 会有一个转换匹配规则， 关于转换匹配规则的说明请参考文档 [在 manifest 中绑定制品](https://help.coding.net/docs/cd/pipe/artifacts/in-kubernetes.html#%E5%9C%A8-manifest-%E4%B8%AD%E7%BB%91%E5%AE%9A%E5%88%B6%E5%93%81)。

关于 TKE 拉取 TCR 私有仓库镜像有两种方式：

- 在 TCR 支持区域内可配置 TKE 免密拉取 TCR 容器镜像，关于 TCR 支持区域请参考 [支持地域](https://cloud.tencent.com/document/product/1141/40540)，关于如何配置可参考文档 [TKE 集群使用 TCR 插件内网免密拉取容器镜像](https://cloud.tencent.com/document/product/1141/48184)。
- 手动配置 TKE 拉取 TCR 私有仓库镜像的访问凭证，配置方式可参考 [TKE 配置私有仓库访问示例](https://help.coding.net/docs/cd/question/private-repo.html#Kubernetes-%E4%BA%91%E8%B4%A6%E5%8F%B7%EF%BC%88TKE-%E9%9B%86%E7%BE%A4%EF%BC%89) 。

> 注意：上面的 Deployment YAML 示例使用了 “手动配置 TKE 拉取 TCR 私有仓库镜像的访问凭证” 的方式。
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

另外可以为部署流程的每个阶段配置自定义事件通知（可选），以便方便快捷的获知部署流程执行情况，这里配置了企业微信通知方式，获取企业微信 Webook 机器人链接的方法可参考 [创建企业微信群机器人](https://help.coding.net/docs/project/open/wechat-robot.html#%E5%88%9B%E5%BB%BA%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E7%BE%A4%E6%9C%BA%E5%99%A8%E4%BA%BA)。

![image-20201029142546113](https://main.qcloudimg.com/raw/b6b69f6ef2a564b9ef0a049c66bafab0.png)

##### 关联项目和应用

关联项目和应用配置请参考文档 [项目和应用关联](https://help.coding.net/docs/cd/app-project.html#%E5%BA%94%E7%94%A8%E4%B8%8E%E9%A1%B9%E7%9B%AE%E5%85%B3%E8%81%94)。

##### 提单发布

提单发布使用和配置请参考文档 [新建发布单](https://help.coding.net/docs/cd/app-project.html#%E6%96%B0%E5%BB%BA%E5%8F%91%E5%B8%83%E5%8D%95)。



想了解更多关于 Coding 持续部署的详细介绍请参考 [持续部署介绍](https://help.coding.net/docs/cd/overview.html)。



### 测试验证

在项目代码文件中修改添加如下所示的 v2 API 代码后提交 master 分支：

![image-20201028215536169](https://main.qcloudimg.com/raw/878df7f0f9fdb38b57805ab817f76a16.png)

由于【持续集成】中的构建计划使用了 “代码更新时自动执行” 的事件触发配置， 了解相关触发配置请参考 [触发规则](https://help.coding.net/docs/devops/ci/trigger.html)。当提交修改的代码时，会自动触发关联的构建计划执行：

![image-20201028211045329](https://main.qcloudimg.com/raw/5f369aa9ab3eb5f97ac9a78e015dc6cc.png)

如果为持续集成配置了企业微信 Webhook 通知，企业微信也会收到相应的即时通知消息，如下图所示：

![image-20201029170912443](https://main.qcloudimg.com/raw/0b22628dd8da488f1c982e00b42b78dd.png)

当构建计划生成 Docker 镜像制品时，又会自动触发关联的【持续部署】流程，将新的镜像应用更新到 TKE 集群中：

![image-20201028211358719](https://main.qcloudimg.com/raw/e4ecb43fec5cba253d5e20a16c7c8bed.png)

如果部署流程有配置企业微信通知的话，当部署流程任务完成时，会收到对应的企业微信部署完成通知，如下图所示：

![image-20201029171424492](https://main.qcloudimg.com/raw/a3e7d8b6b7da770c06b577e50fbdae1f.png)

此时，可以在 TKE 中看到已经成功更新了工作负载：

![image-20201028214913813](https://main.qcloudimg.com/raw/6ab74e1d81f6c1f44c302ffbaeb1babc.png)

从测试验证结果可以看出，我们在 TKE 中实现了从源码更新到业务发布的整套 DevOps 流程。
