## 操作场景
基于容器镜像服务 TCR 的 [容器化持续部署](https://cloud.tencent.com/document/product/1141/39280#.E5.AE.B9.E5.99.A8.E5.8C.96.E6.8C.81.E7.BB.AD.E9.83.A8.E7.BD.B2)，本文介绍如何通过交付流水线功能，实现代码变更自动触发镜像构建，并更新容器服务 TKE 集群内应用。

## 前提条件
- 已开通 [CODING DevOps](https://cloud.tencent.com/document/product/1115/37268) 服务。
- 如使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。
- 如使用已有 TKE 集群，请确认操作子账号具有集群相关权限，请参考 [TKE 集群权限管理](https://cloud.tencent.com/document/product/457/11542)。


## 操作步骤
### 准备环境
#### 创建 TKE 标准集群
>?如已有 TKE 集群，可跳过此步骤。
>
前往 [容器服务控制台](https://console.cloud.tencent.com/tke2)，新建 TKE 标准集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/32189)。创建成功即如下图所示：
![](https://main.qcloudimg.com/raw/f34a5ac4c6d7b57677d204d5cec452ed.png)
#### 创建 TCR 企业版实例
>?如在 TKE 集群所在地域内已有 TCR 实例，可跳过此步骤，否则请在同一地域内新建企业版实例。
>
前往实例列表页面，新建企业版实例，详情请参见 [创建企业版实例](https://cloud.tencent.com/document/product/1141/40716)。创建成功即如下图所示：
![](https://main.qcloudimg.com/raw/fea3ea042359338b98cbe701797f08b4.png)
### 部署容器应用
当前容器服务 TKE 已支持在控制台内选择容器镜像服务 TCR 企业版镜像创建工作负载。同时，TKE 标准集群可安装 TCR 专属插件，实现内网及免密拉取 TCR 企业版内镜像，详情请参见 [使用 TCR 企业版实例内容器镜像创建工作负载](https://cloud.tencent.com/document/product/457/45624)。创建成功即如下图所示：
![](https://main.qcloudimg.com/raw/8c0234e04912fed506a8baf85f30bcc5.png)

### 配置交付流水线
>! 交付流水线功能依赖于 CODING DevOps 服务，请首先开通该服务并创建企业。
>
1. 登录容器镜像服务 TCR 控制台，选择左侧导航栏中的【[交付流水线](https://console.cloud.tencent.com/tcr/pipeline)】。
2. 在“交付流水线”页面中，单击【新建】。
3. 在“基本信息”步骤中，配置以下参数，单击【下一步：镜像配置】。如下图所示：
![](https://main.qcloudimg.com/raw/6453a4d336ff25fcb1576d7e4f6f40dd.png)
  - **流水线名称**：交付流水线名称，长度2-64个字符，只能包含小写字母、数字及分隔符(".", "_", "-")，且不能以分隔符开头、结尾或连续。
  - **流水线描述**：描述信息，支持中文，创建后可修改。
4. 在“镜像配置”步骤中，配置以下参数，单击【下一步：应用部署】。如下图所示：
![](https://main.qcloudimg.com/raw/da95168880fe1d5a2aaaa720d00a4d0d.png)
  - **镜像仓库**：交付流水线关联的镜像仓库，将自动配置镜像构建及推送，用于托管应用部署所需要的镜像，本文以 demo/getting-started 仓库为例。
  - **构建配置**：配置镜像构建相关信息，详情请参见 [配置镜像构建](https://cloud.tencent.com/document/product/1141/45762)。
5. 在“应用部署”步骤中，配置以下参数，单击【完成】。如下图所示：
![](https://main.qcloudimg.com/raw/328890bd7027a72553f2c078cd30a4d2.png)
  - **部署平台**：交付流水线同时支持容器服务 TKE，弹性容器服务 EKS 及边缘容器服务 ECK。本文以容器服务 TKE 为例。
  - **部署地域**：目标集群所在地域。选择已创建的 TKE 标准集群所在地域。
  - **部署集群**：目标集群。选择已创建的 TKE 标准集群。
  - **部署方式**：当前仅支持 “更新已有工作负载”。
  - **命名空间**：已部署应用所在的命名空间。
  - **工作负载**：已部署应用的关联工作负载。
  - **Pod容器**：已部署应用的工作负载内的 Pod 容器，该容器内使用了上步骤中关联镜像仓库内的镜像。

完成以上配置后，可在“交付流水线” 列表页查看新建的流水线。如下图所示：
![](https://main.qcloudimg.com/raw/8e58507817f255d125ee2f0084024675.png)


### 更新容器应用
完成以上配置后，即可在更新应用代码后，自动触发镜像构建，推送及应用更新。
1. 更新源代码
在本地编辑源代码，并提交至远端代码仓库。如下图所示：
![](https://main.qcloudimg.com/raw/5088ad6dab0a50164cca6bdddb1d848f.png)
2. 执行流水线
源代码推送完成后，如符合镜像配置中镜像构建的触发条件，将触发流水线执行。可点击流水线查看该流水线执行记录，并查看具体步骤进度。如下图所示：
![](https://main.qcloudimg.com/raw/81830a9d909b106f3774c9a87e69a661.png)
  - **Checkout**：检出代码。
  - **Docker Build**：基于镜像构建配置进行镜像构建，并为生成的镜像打上指定规则的Tag，如 getting-started-{tag}-{date}-{commit}。
  - **Docker Push**：推送镜像，自动推送至关联镜像仓库内。
  - **Deploy To TKE**：使用最新推送的镜像更新关联工作负载及Pod 内同名镜像。
3. 查看应用更新状态
前往容器服务 TKE 控制台，进入上述集群及工作负载详情页，并选择修订历史，可查看应用更新状态。如下图所示：
![](https://main.qcloudimg.com/raw/054ef802d1ea87cebeb46cb736124ba7.png)
也可直接访问该应用服务，查看是否已更新。本文以 Nginx 服务为例，并通过 Servce 暴露公网服务，查看结果。如下图所示：
![](https://main.qcloudimg.com/raw/1a69976b7cb13bc60652c20ff245d72e.png)

