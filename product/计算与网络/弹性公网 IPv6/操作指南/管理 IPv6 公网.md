>? 目前弹性公网 IPv6 处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/a9k0gialqhj)。

## 开通 IPv6 公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧导航栏选择 **IP 与网卡** > **弹性公网 IPv6**。
3. 在“弹性公网 IPv6”页面，选择需要开通 IPv6 公网的地域，如“华南地区（广州）”，单击**申请**。
4. 在“申请弹性公网 IPv6”页面，勾选需要开通 IPv6 公网的 IPv6 地址，选择目标带宽上限（传统账户类型还支持选择计费模式，下图以传统账户类型为例），单击**提交**。
>?
>- 当运营商类型为 BGP 时，弹性公网 IPv6 地址即为弹性网卡获取到的 IPv6 地址，所以请确保弹性网卡已经获取到 IPv6 地址。
>- 传统账户类型的每个地域的 IPv6 实例仅支持选择为按流量计费或按带宽包计费，不支持同时存在两种计费模式。
>- 单次操作可支持最多100个 IPv6 地址同时开通公网，如果超过100个 IPv6 地址需要开通公网，请分多次操作。
>
![](https://main.qcloudimg.com/raw/f342a6010de213cb43b321f13711ac7a.png)

## 关闭 IPv6 公网
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择 **IP 与网卡** > **弹性公网 IPv6**。
3. 在弹性公网 IPv6 列表页，勾选需要关闭公网的 IPv6 地址，并单击**释放**。
 ![](https://main.qcloudimg.com/raw/c327e00a6f68ae0e89bf18c4bbd5ac87.png)
4. 在弹窗中勾选**确定关闭以上 IP** 并单击**确定**，即可释放弹性公网 IPv6。释放弹性公网 IPv6 后，对应的 IPv6 地址将关闭公网访问。


## 调整 IPv6 公网带宽
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录下选择 **IP 与网卡** > **弹性公网 IPv6**。
3. 在单个弹性公网 IPv6 的操作栏下，单击**调整网络**。
![](https://main.qcloudimg.com/raw/37e9fae5f1afdc2b51ede5ec9d10c491.png)
4. 在弹窗中，修改该弹性公网 IPv6 的带宽上限，单击**调整**。
![](https://main.qcloudimg.com/raw/2edd77e622c0253a3884522a4c073f5c.png)
