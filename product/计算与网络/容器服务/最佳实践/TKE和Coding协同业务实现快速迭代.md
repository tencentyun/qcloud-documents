## 操作场景
在互联网行业，敏捷开发、DevOps 理念被越来越多的企业采纳，敏捷开发和 DevOps 本质上都是一种协作文化，都是着眼于打破壁垒以增加成员共同责任感。其中，DevOps 和 Agile 减少了交接，提高了向客户交付的速度。DevOps 在企业中的落地不仅是一些流程化的工具（例如 CI，CD，容器等技术），更是一整套整体的开发流程和团队协作的改造。对于中小企业，选择 CICD 工具尤其重要，使用成熟的工具和现在流出的容器技术不仅为企业节省成本，并向企业提供快速迭代和快速应对业务变化的能力。  
CI/CD 与敏捷开发、DevOps 的关系如下图所示：
![cicd.png](https://main.qcloudimg.com/raw/c22036387fd9ade9a6c827f3613555e6/1.png)

## 基本概念

### CI (Continuous Integration)

持续集成（Continuous Integration）简称 CI。在 CI 环境中，当开发者频繁地对代码进行更改合并，系统就会自动构建应用并运行不同级别的自动化测试来验证更改，以确保更改内容不会对应用造成破坏。测试内容涵盖了从类和函数到构成整个应用的不同模块。如果自动化测试发现新代码和现有代码之间存在冲突，CI 可以轻松且快速地修复错误。如下图所示：
![ci.jpg](https://main.qcloudimg.com/raw/affb69c501ba39c196eedd5f24ad853c/2.png)

### CD (Continuous Delivery 和 Continuous Deployment)

- 持续交付（Continuous Delivery）简称 CD。在完成 CI 的流程后，持续交付可以支持以下操作：
  - 自动将已经验证的代码发布到存储库。
  - 预生产环境部署。
  - 交付给质量团队或用户。

  具体流程如下图所示：
![cd.jpg](https://main.qcloudimg.com/raw/bea8b96fe8cd01995bcd9aa6e6101198/3.png)

- 持续部署（Continuous Deployment）简称 CD，是 CICD 的最后一个阶段。持续部署即持续交付在内的所有变更都会被自动部署到生产环境。一般情况下，出于业务考虑，可以选择不部署，如需部署必须先实施持续交付。具体流程如下图所示：
![cd2.png](https://main.qcloudimg.com/raw/a1ba3567b9a9045e2b2d8c9326311940/4.png)

> ? 持续交付与持续部署的区别：持续交付是一种能力，持续部署是一种方式。


### CI/CD 工具<span id="CICD"></span>

目前存在以下两种类型的 CI/CD 工具：
- **On-Premise**：需要用户搭建服务器来运行 CI/CD 工具。
- **Hosted 工具类 SaaS 服务**：无需用户搭建服务器。Hosted 的优势如下：
  - **维护成本低**：运行环境由服务托管，维护成本为零，相比 On-Premise 工具，使用者需要花大量时间部署和维护服务器。
  - **干净的运行环境**：使用 Python 作为项目的开发语言时，需要对不同的 Python 版本（2.7，3.6，3.7）进行持续集成，Hosted CI/CD 每次可创建一个新的运行环境，可随时调整版本。
  - **预装软件和运行时**：项目在做持续集成时，需要依赖不同的运行时和工具链，Hosted CI/CD Service 已预装大量常用的软件和运行时，缩减了搭建环境的时间。

### Coding
Coding 是实现 CICD 流程的工具。Coding 提供整套的研发流程管理系统（包含完整的 CICD 流程）。从需求提交到产品迭代，从产品设计到代码管理，自动化测试、持续集成，构建物管理直至最终持续部署，整套流程均在 Coding 完成。使用 Coding 可以实现流水线标准化作业，自动化版本记录，从而降低企业研发管理难度，提升研发效率。
- Coding 同时支持 Hosted 模式和 On-Premise 模式（支持私有化部署）的 [CICD 工具](#CICD)。
- Coding 支持 Jenkins、代码管理（也同时支持 github，gitlab）、敏捷开发管理以及支持 Kubernetes 容器化部署，无缝支持容器服务 TKE。
- 中小企业可使用 [Hosted 模式](#CICD) 来快速应对产品交付，实现业务快速迭代。

## 操作步骤

腾讯云容器服务（TKE）基于原生 Kubernetes 提供以容器为核心的解决方案，解决用户开发、测试及运维过程的环境问题，帮助用户降低成本，提高效率。
实践 DevOps 理念需要用到许多工具与底层服务，但若要完成闭环链路需要长期的投入、搭建复杂工具链体系。这导致了团队整体时间、资源投入很大，甚至有可能因此影响研发能效与交付能效、耽误业务的发展时机。而 CODING 与云端优势相结合，提供了统一协作平台及研发工具链。

在 CODING 一体化研发效能平台上运行工作流，这些宝贵的数据将会演化为项目实施过程中所积累的团队知识，沉淀为集体经验，帮助您的团队不断自我迭代更新。不仅如此，使用 CODING 还能够实施软件研发全生命周期管理，摆脱复杂的基础设施运维托管。

Coding 目前无缝对接 TKE 服务，这次给初步介绍下在 Coding 中如何实现 CICD，并将服务部署到 TKE 集群中。

### 准备工作：开通 DevOps 服务

> ! 该部分步骤以初次使用 DevOps 服务的主账号用户为例，如已开通可忽略。

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。

2. 单击左侧导航栏中【DevOps】，前往“容器 DevOps”界面，如下所示：

   ![](https://main.qcloudimg.com/raw/ea075b0ae5bca065c092ea20d029779f.png)
   
3. 单击【开通服务】>【前往访问管理】，进入如下“角色管理”界面：

   ![](https://main.qcloudimg.com/raw/ed82a514b85c63f9ac26554f8d27bbbb.png)
   
4. 单击【同意授权】，授权成功即跳转至“完善团队信息”页面，如下所示：

   ![](https://main.qcloudimg.com/raw/e8c6f297a755bf151ef8ea0d91ed60cb.png)
5. 设置完成，点击【确定】即可。

### 创建项目并创建代码仓库

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。

2. 单击左侧导航栏中【DevOps】，前往“容器 DevOps”界面。

3. 单击【立即使用】，跳转至 Coding DevOps 界面。

4. 选择【项目】，单击【+ 创建项目】，如下图所示：

![createproject.png](https://main.qcloudimg.com/raw/5e2184075d3ce2380f1a9124f03b4596/5.png)

5. 在项目模板页面选择“DevOps 项目模板”，自定义设置项目基本信息，单击【完成创建】即可。

    > ? 本次创建项目名称以 coding-test 为例。

![devops-test1.png](https://main.qcloudimg.com/raw/2263ffd37e6d8fdcc8b2a10e63fa5abd/6.2%20fs2z9hhsau.png)
6. 使用 DevOps 项目模板成功创建项目之后，系统将会自动创建一个属于同名代码仓库，如下所示：
![git.png](https://main.qcloudimg.com/raw/fbfd9e041d60a5750873549c5157bf28/7%20nj89f8dagt.png)

### 创建制品库

##### 什么是制品库  

软件制品是指由源码编译打包生成的二进制文件，不同的开发语言对应着不同格式的二进制文件，这些二进制通常可以直接运行在服务器上。

##### 创建流程

1. 在 Coding DevOps 控制界面，选择【项目】并单击需要创建制品库的项目 ID，进入该项目详情页。
2. 依次选择【制品库】>新建制品库模块处【创建仓库】，如下图所示：

![zhipin1.png](https://main.qcloudimg.com/raw/5536f4ed912f23c83341de47bbf70137/8.png)

3. 在“新建仓库”页面，根据实际需求进行关键信息自定义设置，如下所示：
![zhipin2.png](https://main.qcloudimg.com/raw/b828c928b86e4bee47d011c4c09a279a/9.png)

4. 单击【确定】，仓库创建完成即可跳转至如下仓库详情页。
![zhipin3.png](https://main.qcloudimg.com/raw/1d6db1200fb902d927b7a9b2876f09bb/10.png)

5. 单击【使用访问令牌生成配置】，身份验证通过之后进行配置。
> ! 在设置好访问令牌后，需要记下这个访问令牌，用于后续 TKE 拉取镜像。

### 持续集成

1. 在 Coding DevOps 控制界面，选择【项目】并单击需要创建制品库的项目 ID，进入该项目详情页。

2. 依次选择【持续集成】>【构建计划】> 新建构建计划配置，如下图所示：

   ![](https://main.qcloudimg.com/raw/7e93acc1debf6314b835642d85529fac.png)

2. 根据实际情况选择构建计划模板，并确认模板默认设置信息，单击【确认】即可。

> ! 在执行构建计划前，需要在 TKE 集群中把 Coding 的 docker registry 账号添加到集群中用来作为 pull 镜像授权，执行命令如下：
>
> `kubectl  create secret docker-registry coding --docker-server=coding的registry地址 --docker-username=用户名 --docker-password=密码 --docker-email=邮箱地址`

本次以选择 Golang+Gin+Docker 模板为例，进行 go 项目演示。具体的操作步骤将在下面的短视频中给大家展示：

> ![视频内容](https://cloud.tencent.com/edu/learning/course-2962-55143)

### 持续部署<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2963-55144?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

该部分主要为您展示持续部署操作流程：持续部署 --> kubernetes --> 配置云账号 --> 配置应用和流程 --> 关联项目和应用 --> 开始部署。操作步骤如下：

1. 在 Coding DevOps 控制界面，选择【项目】并单击需要创建制品库的项目 ID，进入该项目详情页。

2. 依次选择【持续部署】>【Kubernetes 】> 【配置云账号：立即配置】，如下图所示：

   ![](https://main.qcloudimg.com/raw/56e23db59118408abd1709ef875192f5.png)

3. 自定义选择需要配置的云账号类型即可继续进行剩余步骤。

此处以配置“腾讯云 TKE”类型账号为例。具体的操作步骤将在下面的短视频中给大家展示:

> <div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2963-55144?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

#### 总结

在本篇文章中给大家展示了CODING 基于 TKE 实现的 CICD，本次只是简单的介绍了下基本使用，更加详细的内容可以参考 [CODING 官网文档](https://help.coding.net/?_ga=2.41805154.1108335780.1596510033-936626996.1595315264)。

