## 操作场景
腾讯云容器镜像服务（Tencent Container Registry，TCR）兼容 OCI 标准，支持托管包含 Docker Image 在内的多种云原生制品（Artifacts），满足进阶用户对 Helm Chart，CNAB 及自定义的 OCI Artifacts 托管，分发的需求。

目前仅企业版及个人版实例均支持托管 OCI 制品，可直接推送 OCI 制品至镜像仓库内，并查看制品类型，或取拉取指令。

如需了解 OCI 制品及使用方式，请参考 GitHub 上官方项目 [opencontainers/artifacts](https://github.com/opencontainers/artifacts)。

## 前提条件
在上传并管理 TCR 实例内的 OCI 制品前，您需要完成以下准备工作：
- 已成功 [购买企业版实例](https://cloud.tencent.com/document/product/1141/51110)，或初始化个人版。
- 如使用子账号进行操作，请参考 [企业版授权方案示例](https://cloud.tencent.com/document/product/1141/41417) 提前为子账号授予对应实例的操作权限。

## 操作步骤
### 使用控制台管理 OCI 制品
1. 登录 [容器镜像服务](https://console.cloud.tencent.com/tcr) 控制台，选择左侧导航栏中的**镜像仓库**。
2. 在 “镜像仓库” 页面即可查看当前实例内的镜像仓库列表，默认支持托管 OCI 制品。您可使用 OCI 制品专用的客户端工具构建 OCI 制品，并推送至镜像仓库内。
3. 单击指定镜像仓库名称，进入该仓库详情页，查看仓库内已有 OCI 制品。
![](https://qcloudimg.tencent-cloud.cn/raw/23a78f323252e08d5f37b314c8b0936b.png)

## 相关文档
### Helm Chart 管理

如您需要使用 Helm Chart，可选择将 Helm Chart 作为 OCI 制品推送至镜像仓库内进行统一管理，此管理方式需要使用 Helm V3 工具。您也可以直接使用企业版实例基于 Chart Museum 开源项目提供的 Helm Chart 托管功能，详情请参考：[托管 Helm Chart](https://cloud.tencent.com/document/product/1141/41944)。