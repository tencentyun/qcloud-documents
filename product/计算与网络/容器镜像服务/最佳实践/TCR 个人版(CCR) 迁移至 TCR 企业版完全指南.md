## 操作场景
当前容器镜像服务 TCR 同时提供个人版服务和企业版服务。个人版服务面向个人开发者，仅提供容器镜像存储分发的基础功能。企业版服务可为企业客户提供安全、独享的高性能云原生应用制品托管分发服务。个人版与企业版服务区别可参见 [规格说明](https://cloud.tencent.com/document/product/1141/40540#.E8.A7.84.E6.A0.BC.E8.AF.B4.E6.98.8E)。

本文主要介绍企业客户如何将容器镜像数据及业务配置从个人版迁移至企业版，实现业务的平滑迁移。

## 前提条件

从个人版服务迁移至企业版，您需要确认并完成以下准备工作：
- 已开通并使用个人版服务，且迁移操作账号具有拉取个人版镜像仓库内所有镜像的权限，请参考 [个人版授权方案示例](https://cloud.tencent.com/document/product/1141/41409) 提前为子账号授予个人版的全部管理权限。
- 已 [购买企业版实例](https://cloud.tencent.com/document/product/1141/51110)，且迁移操作账号具有向该企业版实例内推送镜像的权限，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的容器镜像、Helm Chart 推送权限，建议将容器镜像服务全读写权限授予配置同步的子账号。
- 已设置迁移工具运行的运行环境。建议在私有网络 VPC 内执行该迁移任务，以提升迁移速度，并避免公网流量成本。
  - 在私有网络 VPC 内运行迁移工具：在目标企业版实例的内网访问中添加迁移工具运行服务器所在的私有网络。详情可参见 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)。
  - 在公网环境内运行迁移工具：开启目标企业版实例的公网访问入口，并放通访问来源。详情可参见 [公网访问控制](https://cloud.tencent.com/document/product/1141/41837)。

## 数据迁移

### 准备基础运行环境

1. 在实际容器业务的主要部署地域购买企业版实例。
2. 在同地域内准备一台用于镜像迁移的云服务器 CVM，并尽量选择 CPU/内存配置高、内网带宽高的机型。云服务器启动后，安装最新 Docker 客户端，或选择已安装 Docker 的操作系统。
3. 将 CVM 所在 VPC 接入至该企业版实例，并开启自动内网解析，详情可参见 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)。
4. 获取该实例的访问凭证，并在迁移专用 CVM 上执行 `Docker Login`，确认在该 CVM 上可通过内网正常访问该实例并登录成功。

### 准备迁移配置信息

1. 获取镜像仓库访问凭证
   - 个人版镜像仓库访问凭证：用户名为需迁移镜像所属腾讯云账号 UIN，密码为初始化个人版服务时所设置密码。如忘记密码，可前往 **[容器镜像服务控制台](https://console.cloud.tencent.com/tcr/instance?rid=1)** > **实例列表**，选择个人版实例，进入更多中单击**重置登录密码**来重置密码。
   - 企业版镜像仓库访问凭证：可前往 **[容器镜像服务控制台](https://console.cloud.tencent.com/tcr/instance?rid=1)** > **访问凭证**，选择已创建的企业版实例，单击**新建**，生成迁移专用的长期访问凭证，已包含用户名及密码。请注意，生成该访问凭证用户需具备该实例的全读写权限。
2. 获取 API 调用凭证
   迁移镜像过程中将自动在企业版实例内新建命名空间及镜像仓库，需调用腾讯云 API 完成该操作。您可前往**[访问管理控制台](https://console.cloud.tencent.com/cam/capi)** > **访问密钥** > **API密钥管理** 新建密钥或查看已有密钥。请谨慎保管该密钥信息。

### 下载并执行迁移工具

执行如下命令，下载迁移专用容器镜像：

```bash
docker pull ccr.ccs.tencentyun.com/tcrimages/image-transfer:ccr2tcr
```

执行如下命令，查看该工具使用说明：

```bash
docker run --network=host --rm ccr.ccs.tencentyun.com/tcrimages/image-transfer:ccr2tcr /run --help
```

执行如下命令，修改配置信息，并正式执行迁移任务：

```bash
docker run --network=host --rm ccr.ccs.tencentyun.com/tcrimages/image-transfer:ccr2tcr /run --tcrName image-transfer --ccrRegionName ap-guangzhou --tcrRegionName ap-shanghai --ccrAuth username:password --tcrAuth username:password --ccrSecretId sid- example --ccrSecretKey skey-example --tcrSecretId sid-example --tcrSecretKey skey-example --tagNum 50
```

#### 参数说明
| 参数 | 参数说明 |
|---------|---------|
| tcrName | 目标迁移企业版实例的名称 |
| ccrRegionName、ccrRegionName | 实例地域，ccr 国内默认为 ap-guangzhou, tcr 需按照实际地域填写，例如 ap-shanghai |
| ccrAuth、tcrAuth | 镜像仓库访问凭证，格式：username:password |
| ccrSecretId、ccrSecretKey、tcrSecretId、tcrSecretKey | 腾讯云 API 调用密钥，如果是同账号下迁移，ccr 及 tcr 调用密钥相同 |
| tagNum | 指定仅迁移镜像仓库内最新 N 个版本镜像 |

### 查看及确认运行结果

因个人版迁移至企业版默认使用全量迁移模式，迁移时间直接与当前个人版内镜像仓库数量及大小有关，请耐心等待。
若运行后展示如下代码，即表示全量迁移成功。否则请重新运行该迁移工具进行重试。您可以通过 [在线咨询](https://cloud.tencent.com/online-service?from=doc_1141) 申请协助。

```bash
################# Finished, 0 transfer jobs failed, 0 normal urlPair generate failed, 0 jobs generate failed #################
```

## 业务迁移

### 集群镜像仓库配置切换

#### 访问地址切换

进入集群或弹性集群的详情页，选择左侧的“工作负载”，并选择新建/更新工作负载，在“实例内容器”中选择/填写镜像地址，或直接修改 YAML 中 **image** 参数。如下图所示：
![](https://main.qcloudimg.com/raw/d061990930dd2fa64ef22e32e523309e.png)
- 个人版地址：默认为 `ccr.ccs.tencentyun.com/namespace/repo:tag`，默认地域服务覆盖除中国香港以外的其他国内可用地域，如北京、上海、广州等，中国香港前缀域名为 hkccr。不支持多级路径。
- 企业版地址：可自定义实例名 `user-define`，例如 `user-define.tencentcloudcr.com/namespace/repo:tag`。支持自定义域名，例如 `xxx-company.com/namespace/repo:tag`。支持多级路径，镜像地址可为 `xxx-company.com/ns/sub01/sub02/repo:tag`。

#### 访问凭证切换
进入集群或弹性集群的详情页，选择左侧的“工作负载”，并选择新建/更新工作负载，在“镜像访问凭证“中切换访问凭证，或直接修改 YAML 中 **imagePullSecret** 参数。如下图所示：
![](https://main.qcloudimg.com/raw/709e7c6eae63262e252dd74fce504ddf.png)
- 个人版访问凭证：新建命名空间默认会下发个人版访问凭证，即 **qcloudregistrykey**，选择该凭证即可。
- 企业版访问凭证：
  - 推荐方案：使用 TCR 企业版专用插件自动下发并配置访问凭证，实现免密拉取。此方案无需配置镜像访问凭证，请将此参数已有值删除，保持为空。（仅支持 TKE）
  - 手动配置：可在 TCR 企业版实例内创建长期访问凭证，并下发至命名空间内，或在创 建工作负载时新建镜像访问凭证。

#### 网络环境切换

容器镜像服务个人版无网络访问控制功能，国内地域内服务器默认均可内网访问该服务。容器镜像服务企业版支持网络访问控制，需将集群所在 VPC 接入实例内，允许内网访问。

- 个人版网络配置：无需配置，默认所有网络环境均可访问该服务，上传/下载镜像。
- 企业版网络配置：
  - 内网访问（推荐）：主动将集群或弹性集群所在 VPC 接入目标实例，并开启 VPC 内自动解析或自行管理 DNS 解析，详情可参见 [内网访问控制](https://cloud.tencent.com/document/product/1141/41838)。
  - 公网访问：不建议开启，建议仅在测试时，或有面向外部团队分发镜像时开放，且配置访问白名单。

### 企业版入门最佳实践

本文档仅面向个人版迁移至企业版场景提供部分最佳实践说明。

#### 多实例规划

可根据实际业务需要，在多个地域内创建一个或多个实例，并配置同步复制策略，并使用自定义域名统一管理实例访问地址。详情可参见 [TCR 企业版实例同步](https://cloud.tencent.com/document/product/1141/41945)， [TCR 企业版实例复制](https://cloud.tencent.com/document/product/1141/52095)，[从自建 Harbor 同步镜像到 TCR 企业版](https://cloud.tencent.com/document/product/1141/44970)。

#### 安全合规

- 操作合规
   - 建议为使用企业版的子账号授予最小权限。支持仓库级权限配置，及指定某个子账号仅能拉取/管理指定镜像仓库，或更细粒度的 API 调用权限。操作详情可参见 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417)。
   - 针对不同使用场景，可创建专用的长期访问凭证，单个账号创建的所有长期访问凭证均与只用于登录，权限与该账号在 CAM 侧配置的权限一致。
   - 临时访问实例建议使用临时访问凭证（1小时有效），操作详情可参见 [获取临时登录指令](https://cloud.tencent.com/document/product/1141/41829#.E8.8E.B7.E5.8F.96.E4.B8.B4.E6.97.B6.E7.99.BB.E5.BD.95.E6.8C.87.E4.BB.A4)。

- 网络安全
   - 请避免开通公网访问入口，避免外部非授权对象访问实例，或是自身业务通过公网下载镜像，产生公网访问费用。
   - 可选为实例绑定自定义域名，并管理该域名的公网及 VPC 内解析。

#### 镜像管理

- 仓库规划
   - 建议使用命名空间来隔离业务、团队等，方便后期权限管理及配置同步规则。
   - 支持多级路径，可根据需要创建多层级仓库，避免创建过多命名空间。
   - 支持推送镜像自动创建仓库，可在命名空间层级配置公开/私有等默认属性。
   - **请注意**：命名空间，镜像仓库等均是路径标记，后端数据存储无隔离。

- 版本命名
   - 请避免在生产环境内使用 latest 更新镜像版本，可能影响服务更新及回滚。
   - 建议使用 CI 工具为镜像进行自动化命名，便于后续版本管理及镜像同步等。
   - **请注意**：删除指定版本镜像时，相同 digest 镜像将会同时被删除。

#### CI/CD

- 使用企业版自带服务
   - 企业版 CI/CD 能力完全基于腾讯云 CODING DevOps 产品，需开通该产品，并完成基础配置。详情请参见 [CODING DevOps](https://cloud.tencent.com/product/coding)。
   - 支持镜像构建，代码源可选 Github、Gitlab、工蜂、码云、CODING 等。
   - 支持交付流水线，可自动部署镜像至集群、弹性集群及边缘集群。

- 对接外部服务
   - 可使用触发器（webhook）功能对接已有 CI/CD 系统，推送镜像自动触发 webhook 通知，消息体包含镜像基础信息。详情可参见 [管理触发器](https://cloud.tencent.com/document/product/1141/44369)。
   - 可直接使用 CODING DevOps 完整服务，已内置容器镜像服务 TCR 相关模板。
