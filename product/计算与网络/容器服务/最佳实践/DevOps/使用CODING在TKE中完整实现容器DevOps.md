## 敏捷开发及 DevOps
在互联网行业，敏捷开发及 DevOps 理念被越来越多的企业采纳，其本质作为一种协作文化，均为打破壁垒并增加成员共同责任感，同时还减少了交接，提高向客户交付的速度。
DevOps 在企业中不仅落地了流程化的工具（例如 CI，CD及容器），还整体改造了开发及团队协作的流程。对于中小企业来说，选择 CICD 工具尤其重要，使用成熟的工具及容器技术，不仅为企业节省成本，并获取了快速迭代和快速应对业务变化的能力。
CI/CD 与敏捷开发、DevOps 的关系如下图所示：
![cicd.png](https://main.qcloudimg.com/raw/c22036387fd9ade9a6c827f3613555e6/1.png)

## 操作场景
腾讯云容器服务（TKE）基于原生 Kubernetes 提供以容器为核心的解决方案，解决用户开发、测试及运维过程的环境问题，帮助用户降低成本，提高效率。实践 DevOps 理念需要用到许多工具与底层服务，且完成闭环链路需要长期投入及搭建复杂工具链体系，会消耗巨量时间和资源，甚至影响研发能效与交付能效、耽误业务的发展时机。而 Coding 与云端优势相结合，提供了统一协作平台及研发工具链。在 Coding 一体化研发效能平台上运行工作流，数据将会演化为项目实施过程中所积累的团队知识，沉淀为集体经验，帮助团队不断自我迭代更新。使用 Coding 还能够实施软件研发全生命周期管理，摆脱复杂的基础设施运维托管。
Coding 目前无缝对接 TKE 服务，本文档介绍在 Coding 中如何实现 CICD，并将服务部署到 TKE 集群中。


## 基本概念

### CI（Continuous Integration）

持续集成（Continuous Integration）简称 CI。在 CI 环境中，当开发者频繁地对代码进行更改合并，系统就会自动构建应用并运行不同级别的自动化测试来验证更改，以确保更改内容不会对应用造成破坏。测试内容涵盖了从类和函数到构成整个应用的不同模块。如果自动化测试发现新代码和现有代码之间存在冲突，CI 可以轻松且快速地修复错误。如下图所示：
![](https://main.qcloudimg.com/raw/645f2a056fa79574dd9efb424f483785.png)


### CD（Continuous Delivery 和 Continuous Deployment）
> ? 持续交付与持续部署的区别：持续交付是一种能力，持续部署是一种方式。

- 持续交付（Continuous Delivery）简称 CD。在完成 CI 的流程后，持续交付支持以下操作：
  - 自动将已经验证的代码发布到存储库。
  - 预生产环境部署。
  - 交付给质量团队或用户。

  具体流程如下图所示：
![](https://main.qcloudimg.com/raw/c9e69c621bd787d93d17d103cf0b902e.png)
- 持续部署（Continuous Deployment）简称 CD，是 CICD 的最后一个阶段。持续部署将持续交付在内的所有变更自动部署到生产环境。一般情况下，出于业务考虑可以选择不部署，如需部署必须先实施持续交付。具体流程如下图所示：
![](https://main.qcloudimg.com/raw/597edfd80f9a23ebb223e7ecd54d7714.png)



### CI/CD 工具[](id:CICD)

目前存在以下两种类型的 CI/CD 工具：
- **On-Premise**：需要用户搭建服务器来运行 CI/CD 工具。
- **Hosted 工具类 SaaS 服务**：无需用户搭建服务器。Hosted 的优势如下：
  - **维护成本低**：运行环境由服务托管，维护成本为零。而使用 On-Premise 工具，会花大量时间部署和维护服务器。
  - **干净的运行环境**：使用 Python 作为项目的开发语言时，需要对不同的 Python 版本（2.7、3.6、3.7）进行持续集成，Hosted CI/CD 每次可创建一个新的运行环境，可随时调整版本。
  - **预装软件和运行时**：项目在做持续集成时，需要依赖不同的运行时和工具链，Hosted CI/CD Service 已预装大量常用的软件和运行时，缩减了搭建环境的时间。

### Coding
Coding 是实现 CICD 流程的工具。Coding 提供整套的研发流程管理系统（包含完整的 CICD 流程）。从需求提交到产品迭代，产品设计、代码管理、自动化测试、持续集成、构建物管理及持续部署，整套流程均在 Coding 完成。使用 Coding 可以实现流水线标准化作业及自动化版本记录，从而降低企业研发管理难度，提升研发效率。
- Coding 同时支持 Hosted 模式和 On-Premise 模式（支持私有化部署）的 [CICD 工具](#CICD)。
- Coding 支持 Jenkins、代码管理（也同时支持 github，gitlab）、敏捷开发管理以及支持 Kubernetes 容器化部署，无缝支持容器服务 TKE。
- 中小企业可使用 [Hosted 模式](#CICD) 来快速应对产品交付，实现业务快速迭代。

## 操作步骤
### 开通 DevOps 服务
> ! 该步骤以初次使用 DevOps 服务的主账号用户为例，如已开通服务则可跳过此步骤，进行 [创建项目并创建代码仓库](#createProduct)。

1. 登录容器服务控制台，选择左侧导航栏中的 **[DevOps](https://console.cloud.tencent.com/coding/container-devops)**。
2. 进入“容器 DevOps”页面。如下图所示：
![](https://main.qcloudimg.com/raw/6f1e13d45996ec30637a0c8d3db9348b.png)
3. 选择**开通服务** > **前往访问管理**，进入“角色管理”页面。如下图所示：
![](https://main.qcloudimg.com/raw/ed82a514b85c63f9ac26554f8d27bbbb.png)   
4. 单击**同意授权**，授权成功即跳转至**开通服务**页面。如下图所示：
![](https://main.qcloudimg.com/raw/e8c6f297a755bf151ef8ea0d91ed60cb.png)
5. 完善团队信息后单击**确定**，即可开通 DevOps 服务。

### 创建项目并创建代码仓库[](id:createProduct)
1. 登录容器服务控制台，选择左侧导航栏中的 **[DevOps](https://console.cloud.tencent.com/coding/container-devops)**。
2. 进入“容器 DevOps”页面。如下图所示：
![](https://main.qcloudimg.com/raw/8c30f351eb48428dfaef9ef7afa3f252.png)
3. 单击**立即使用**，跳转至**Coding DevOps**页面。
4. 在左侧导航中选择**项目**，进入项目详情页。
5. 在项目详情页，单击页面右上角**+创建项目**。如下图所示：
![](https://main.qcloudimg.com/raw/ee0f237acf7d50d9a4d2ed78f95769f0.png)
6. 在“选择项目模板”步骤中，单击 “DevOps 项目”进入下一页。
7. 在“填写项目基本信息”步骤中，自定义设置项目基本信息。本次创建项目名称以 coding-test 为例。如下图所示：
![](https://main.qcloudimg.com/raw/e4838a93eb724a1dc865ef408db55e9a.png)
8. 单击**完成创建**即可创建项目，项目创建完成即跳转至该项目概览页。
9. 单击该概览页左侧导航栏中**代码仓库**，进入代码仓库详情页。如下图所示：
![](https://main.qcloudimg.com/raw/67d2b83d9ab4e8400505b8d1dc22d8bc.png)
10. 单击**新建代码仓库**，自定义设置仓库基本信息。本次创建代码仓库名称以 coding-test 为例。如下图所示：
![](https://main.qcloudimg.com/raw/2fc4fee7e595b8c88def7a66c9ee7678.png)
11. 单击**确定**即可完成创建代码仓库。

### 创建制品库
软件制品是指由源码编译打包生成的二进制文件，不同的开发语言对应着不同格式的二进制文件，通常可以直接在服务器运行。

#### 创建流程
1. 登录 Coding DevOps，选择左侧导航中的 **[项目](https://tencent-test.coding.net/user/projects)**，进入项目管理页。
2. 在“项目管理页”中，单击需要创建制品库的项目名称，进入该项目详情页。
3. 在左侧导航栏中选择**制品库** > **创建仓库**，进入**新建仓库**页面。如下图所示：
![zhipin1.png](https://main.qcloudimg.com/raw/5536f4ed912f23c83341de47bbf70137/8.png)
4. 在“新建仓库”页面，根据实际需求进行关键信息自定义设置。如下图所示：
![](https://main.qcloudimg.com/raw/3542899f0b0790ca5929be907bd92887.png)
5. 单击**确认**即可完成仓库创建，并自动跳转至仓库详情页。如下图所示：
6. 单击**使用访问令牌生成配置**，身份验证通过之后进行配置。
> ! 在设置好访问令牌后，需自行记录访问令牌，用于后续 TKE 拉取镜像。
> 
![](https://main.qcloudimg.com/raw/115292dfd2ab72317c0a22e00b7e7c76.png)


### 持续集成
> ! 在执行构建计划前，需要执行以下命令，在 TKE 集群中把 Coding 的 docker registry 账号添加到集群中用来作为 pull 镜像授权。
```
kubectl  create secret docker-registry coding --docker-server=coding的registry地址 --docker-username=用户名 --docker-password=密码 --docker-email=邮箱地址
```

1. 登录 Coding DevOps ，选择左侧导航中的 **[项目](https://tencent-test.coding.net/user/projects)**，进入项目管理页。
2. 在“项目管理页”中，单击需要创建制品库的项目名称，进入该项目详情页。
3. 在左侧导航栏中选择**持续集成** > **构建计划** > **创建构建计划**，进入**选择构建计划模版**页面。如下图所示：
![](https://main.qcloudimg.com/raw/82dd4540bab7095f50c4eb78805899d2.png)
4. 根据实际情况选择构建计划模板，并确认模板默认设置信息，单击**确认**即可完成。
本文以选择 Golang+Gin+Docker 模板为例，进行 go 项目演示。以下视频将为您介绍具体的操作步骤：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2962-55143?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


### 持续部署

1. 登录 Coding DevOps ，选择左侧导航中的 **[项目](https://tencent-test.coding.net/user/projects)**，进入项目管理页。
2. 在“项目管理页”中，单击需要创建制品库的项目名称，进入该项目详情页。
3. 在左侧导航栏中选择**持续部署** > **Kubernetes**，单击**立即配置**。如下图所示：
![](https://main.qcloudimg.com/raw/56e23db59118408abd1709ef875192f5.png)
4. 在“部署控制台”页面，自定义选择需要配置的云账号类型即可继续进行配置应用和流程、关联项目和应用及开始部署等后续步骤。
本文以配置“腾讯云 TKE”类型账号为例，以下视频将为您介绍具体的操作步骤：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2963-55144?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>


## 更多信息
本文简单介绍了 Coding 基于 TKE 实现 CICD 的基本使用，详细内容请参阅 [Coding 官网文档](https://help.coding.net/)。

