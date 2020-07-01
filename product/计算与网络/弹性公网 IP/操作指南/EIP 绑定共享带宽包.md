IP 带宽包是共享带宽包的其中一种类型，[创建 IP 带宽包](https://cloud.tencent.com/document/product/684/39942) 实例后，您需要将使用该 IP 带宽包的 EIP 添加到 IP 带宽包实例中。

## 前提条件
- 目前共享带宽包处于内测阶段，使用前，请确保您的 [内测申请](https://cloud.tencent.com/apply/p/8o8lmsr5nj8) 已通过 。
- 请确保您的账户类型为：带宽上移账户，若您无法确定账户类型，请参见 [账户类型区分](https://cloud.tencent.com/document/product/1199/41692#judge)。

## 限制说明
1. 仅支持按流量计费和按小时带宽计费的 EIP 加入 IP 带宽包，包年包月的 EIP 不支持加入 IP 带宽包。
2. 添加 EIP 到 IP 带宽包后，EIP 原本的计费模式将变更为共享带宽包模式，不额外收取公网网络费，但正常收取 IP 资源费。
3. EIP 的 IP 资源费与是否加入 IP 带宽包无关，当 EIP 绑定云资源时，免除 IP 资源费。
4. 单个 IP 带宽包最多可添加100个 EIP。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，单击左侧导航的【共享带宽包】。
2. 选择地域，在列表中找到目标 IP 带宽包实例，单击实例 ID 进入详情页。
3. 在详情页的“带宽包资源”模块，单击【+添加资源】。
4. 在弹出的“绑定资源”窗口中，选择【弹性公网IP/普通公网IP】为资源类型，并选择需添加到 IP 带宽包的 EIP，单击【确定】即可。
![](https://main.qcloudimg.com/raw/935a60911d409c65a3f4ec200b027bcc.png)
