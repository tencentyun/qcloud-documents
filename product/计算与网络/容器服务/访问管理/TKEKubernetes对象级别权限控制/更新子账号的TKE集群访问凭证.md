## 访问凭证功能
腾讯云容器服务 TKE 基于 x509 证书认证实现了以下功能：
- 每个子账号均单独具备客户端证书，用于访问 Kubernetes APIServer。
- 在 TKE 新授权模式下，不同子账号在获取集群访问凭证时，即访问集群基本信息页面或调用云 API 接口 DescribeClusterKubeconfig 时，将会获取到子账户独有的 x509 客户端证书，该证书是使用每个集群的自签名 CA 进行签发的。
- 当子账号在控制台访问 Kubernetes 资源时，后台默认使用该子账号的客户端证书去访问用户 Kubernetes APIServer。
- 支持子账号更新独有的客户端证书，防止凭证泄露。
- 支持主账号或使用集群 `tke:admin` 权限的账号进行查看、更新其他子账号的证书。

## 操作步骤
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 在“集群管理”页面中，选择需目标集群 ID。
3. 在集群详情页面中，选择左侧的**基本信息**，在“集群APIServer信息”模块中单击**Kubeconfig权限管理**。
4. 在弹出的 “Kubeconfig权限管理” 窗口中，按需勾选认证账号并单击**更新**即可。如下图所示：
![](https://main.qcloudimg.com/raw/b8c2a30a36d96946cf2f134f49bc2114.png)

