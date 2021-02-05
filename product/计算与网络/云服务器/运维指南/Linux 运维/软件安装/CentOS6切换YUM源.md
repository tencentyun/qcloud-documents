## 背景信息
CentOS 6操作系统版本生命周期（EOL）于2020年11月30日结束，Linux 社区不再维护该操作系统版本。按照社区规则，CentOS 6的源地址 `http://mirror.centos.org/centos-6/` 内容已移除，且目前第三方的镜像站中均已移除 CentOS 6的源。腾讯云的源 `http://mirrors.cloud.tencent.com/和http://mirrors.tencentyun.com/` 也无法同步到 CentOS 6的源，当您在腾讯云上继续使用默认配置的 CentOS 6的源会发生报错。

<dx-alert infotype="explain" title="">
建议您升级操作系统至 CentOS 7及以上，如果您的业务过渡期仍需要使用 CentOS 6操作系统中的一些安装包，请根据本文提供的信息切换 CentOS 6的源。
</dx-alert>


## 调整详情
请参考以下信息，在 CentOS 6操作系统的云服务器实例中，根据实际网络环境将 YUM 源配置进行以下切换。您可参考 [内网服务](https://cloud.tencent.com/document/product/213/5225) 及 [公网服务](https://cloud.tencent.com/document/product/213/5224) 进行判断。
- 内网访问需切换为：`http://mirrors.tencentyun.com/centos-vault/6.9/` 源。
- 公网访问需切换为：`https://mirrors.cloud.tencent.com/centos-vault/6.9/` 源。
