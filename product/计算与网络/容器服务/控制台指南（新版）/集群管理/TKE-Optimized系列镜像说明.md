


[TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel) 由腾讯云团队维护定制内核。[Tencent Linux](https://cloud.tencent.com/document/product/457/50124) 是腾讯云包含该内核版本的公共镜像，容器服务 TKE 目前已经支持该镜像并作为缺省选项。

在 Tencent Linux 公共镜像上线之前，为了提升镜像稳定性，并提供更多特性，容器服务 TKE 团队制作并维护 TKE-Optimized 系列镜像。目前控制台已不再提供新建集群选择 TKE-Optimized 镜像的选项。

>! 
- 仍在使用 TKE-Optimized 镜像的集群不受影响，可继续使用。建议您切换至到 Tencent Linux 2.4，新增节点使用 Tencent Linux 2.4，存量节点不受影响可继续使用。
- Centos7.6 TKE Optimized 镜像与 Tencent Linux 2.4完全兼容。
- Ubuntu 18.04 TKE Optimized 镜像基于 Centos 7，用户对节点做配置变更的脚本需自行适配新版本。
