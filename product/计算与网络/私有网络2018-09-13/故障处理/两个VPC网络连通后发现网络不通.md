## 现象描述
通过云联网打通两个 VPC 网络后，发现网络无法 ping 通。

## 可能原因
- 两个 VPC 子网网段冲突，导致路由失效。
- 存在容器路由。

## 处理步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/ccn)，单击**云联网**，进入云联网控制台。
2. 单击云联网实例 ID，进入详情页面。
3. 单击**路由表**页签，查看是否有如下图所示的**失效**路由。
  + 如存在**失效**路由，则可以看出两个 VPC 存在相同 CIDR 的子网，导致云联网路由冲突，请删除相同 CIDR 的子网，更换其他网段的子网。
  + 如不存在失效路由，请继续排查 [步骤4](#step4)。
    ![](https://qcloudimg.tencent-cloud.cn/raw/0fb0729a942e7d8adcc208a71b807d7e.png)
4. <span id="step4">进入[云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=16)，单击云服务器右侧的**登录**，按照界面提示输入密码或密钥，以 [标准方式登录云服务器](https://cloud.tencent.com/document/product/213/5436)，并执行 route 查看系统内部路由表。
5. 查看系统内是否存在 docker 容器网段路由，且与对端云服务器所在子网网段相同。
  + 如存在容器网段路由，且容器网段与对端子网网段相同，容器网段路由与 VPC 互通路由将发生冲突，此时系统将优先选择容器路由，从而导致与对端访问不通。请更换为其他网段的通信子网，或修改容器网段来解决该问题。
  + 如不存在，请记录问题，并联系 [售后在线支持](https://cloud.tencent.com/online-service)。
>?当 VPC 内的云服务器使用了容器服务，容器网段与子网网段相同时，也可能会出现访问同 VPC 内的云服务器实例不通，也是因容器路由冲突所致，因此请提前规划好网段。
>
 ![](https://qcloudimg.tencent-cloud.cn/raw/d539f8bd7364e7bd6edd0b0521be3a00.png)
