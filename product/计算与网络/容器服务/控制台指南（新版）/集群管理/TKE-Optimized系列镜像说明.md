


[TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel) 由腾讯云团队维护定制内核。[Tencent Linux](https://cloud.tencent.com/document/product/457/50124) 是腾讯云包含该内核版本的公共镜像，容器服务 TKE 目前已经支持该镜像并作为缺省选项。

在 Tencent Linux 公共镜像上线之前，为了提升镜像稳定性，并提供更多特性，容器服务 TKE 团队制作并维护 TKE-Optimized 系列镜像。目前控制台已不支持新建集群选择 TKE-Optimized 镜像。


<dx-alert infotype="notice" title="注意：">
- 仍在使用 TKE-Optimized 镜像的集群不受影响，可继续使用。建议您切换至到 Tencent Linux 2.4，新增节点使用 Tencent Linux 2.4，存量节点不受影响可继续使用。
- Centos7.6 TKE Optimized 镜像与使用 Tencent Linux 2.4镜像完全兼容。
- Ubuntu 18.04 TKE Optimized 镜像用户空间工具与 Tencent Linux 并不完全兼容，已对节点做配置变更的脚本需您自行适配新版本。
</dx-alert>


<style>
ul{
margin-bottom:0px !important;
}
</style>
