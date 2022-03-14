支持将 EIP 从 [IP 带宽包](https://cloud.tencent.com/document/product/684/15245) 内移除，移除后，计费模式将统一变更为按流量计费。

## 前提条件
- 目前共享带宽包处于内测阶段，使用前，请确保您的 [内测申请](https://cloud.tencent.com/apply/p/8o8lmsr5nj8) 已通过 。
- 请确保您的账户类型为：标准账户类型，若您无法确定账户类型，请参见 [判断账户类型](https://cloud.tencent.com/document/product/1199/49090#judge)。

## 限制说明
1. EIP 中仅支持将按流量和按小时带宽计费的常规 IP 手动加入或移除 IP 带宽包，包月带宽的常规 IP 不支持加入或移除 IP 带宽包。
2. EIP 中的加速 IP 和静态单线 IP 不支持手动加入或移除 IP 带宽包。新建加速 IP 时，后台会自动创建 Anycast 加速带宽包（这里可视为 IP 带宽包）。新建静态单线 IP 时，后台会自动创建相应的移动、联通或电信带宽包（这里可视为 IP 带宽包）。删除加速 IP 或静态单线 IP 时，后台会自动将该 IP 移除相应带宽包。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，单击左侧导航的**共享带宽包**。
2. 选择地域，在列表中找到目标 IP 带宽包实例，单击实例 ID 进入详情页。
3. 在详情页的“带宽包资源”模块，选择您要移出 IP 带宽包的 EIP，单击**移除资源**，并确认操作即可。
![](https://main.qcloudimg.com/raw/de3527f3f7648f8a6e3c374090a5c649.png)
