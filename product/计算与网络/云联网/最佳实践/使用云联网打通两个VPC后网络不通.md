## 现象描述
通过云联网打通两个 VPC 网络后，发现网络 ping 不通。
>? 
>+ 测试网络连通性可使用如下方式之一：
>  + ping 命令： 用于测试源主机与目标主机网络是否连通，使用方式：ping  **对端 IP**。
>   + telnet 命令： 用于测试指定目标主机的端口是否可达，使用方式：telnet **对端 IP地址** **对端端口号**。
>+ 腾讯云数据库、CFS/ES 集群等默认禁 ping，建议使用 telnet 检测连通性。
>+ 内网负载均衡的 IP 仅支持来自本 VPC 的客户端 ping，因此使用云联网打通的网络，不能通过网络 ping 对端网络的内网负载均衡的 VIP 来测试网络连通性，可以使用 ping 对端 CVM，或 telnet CLB 服务端口。


## 可能原因
- 云服务器内部安装了 docker 容器，存在容器路由
- 通信子网间网段冲突，导致路由失效
- 安全组规则未放通
- 子网 ACL 规则未放通
- 云服务器内部开启了防火墙


## 处理步骤

### 步骤一：检查通信两端云服务器是否存在 docker 路由
1. 进入[ 云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=16)，单击云服务器右侧的**登录**，按照界面提示输入密码或密钥，以 [标准方式登录云服务器](https://cloud.tencent.com/document/product/213/5436)，并执行 route 查看系统内部路由表。
2. 查看系统内是否存在 docker 容器网段路由，且与对端云服务器所在子网网段相同。
  + 如存在容器网段路由，且容器网段与对端子网网段重叠，容器网段路由与 VPC 互通路由将发生冲突，此时系统将优先选择容器路由，从而导致与对端访问不通。请更换为其他网段的通信子网，或修改容器网段，处理后请再次尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查 [步骤二](#step2) 。
  + 如不存在，请继续排查 [步骤二](#step2)。
 ![](https://qcloudimg.tencent-cloud.cn/raw/d539f8bd7364e7bd6edd0b0521be3a00.png)

### 步骤二：判断两个 VPC 子网网段是否冲突导致路由失效[](id:step2)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/ccn)，单击**云联网**，进入云联网控制台。
2. 单击云联网实例 ID，进入详情页面。
3. 单击**路由表**页签，查看是否有如下图所示的**失效**路由。
  + 如存在**失效**路由，即如下图所示存在两条到相同目的端的路由条目，从而导致[ 路由冲突 ](https://cloud.tencent.com/document/product/877/18679#.E8.B7.AF.E7.94.B1.E9.99.90.E5.88.B6)失效，请根据实际情况删除/禁用冲突网段的路由，启用需要通信的路由，然后再尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查 [步骤三](#step3) 。
  + 如不存在失效路由，请继续排查 [步骤三](#step3)。
    ![](https://qcloudimg.tencent-cloud.cn/raw/0fb0729a942e7d8adcc208a71b807d7e.png)

### 步骤三：检查通信两端云服务器的安全组规则是否放通[](id:step3)
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 单击云服务器实例 ID，进入实例详情界面。
3. 单击**安全组**页签，查看是否有放通 ICMP 协议，及对应来源 IP/目的 IP 的出入站安全组规则。
 + 如无对应协议规则，或规则为**拒绝**，请单击**编辑**修改对应协议的安全组规则，然后尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查 [步骤四](#step4) 。
 + 如安全组出入站规则均正确，请继续排查 [步骤四](#step4) 。
	**异常示例**：
	![](https://qcloudimg.tencent-cloud.cn/raw/2c7a3bf9c7f88d6f1f96f56ffcf62fc2.png)
	**正常示例**：
	![](https://qcloudimg.tencent-cloud.cn/raw/d591b7590bdeb9c88cd290dd1b3f5bdc.png)

### 步骤四：检查通信两端子网关联的 ACL 规则是否放通[](id:step4)
1. 在云服务器详情页，单击该云服务器所属子网 ID 进入子网详情界面。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c3f6292eb5cc2a55e1d237936f5307df.png" width="60%">
2. 单击 **ACL 规则**页签，查看子网是否绑定了网络 ACL，且 ACL 出入站规则中，是否有拒绝 ICMP 协议，及来源/目标 IP 的规则。
  +  如未绑定 ACL，请继续排查 [步骤五](#step5)。
  + 如绑定了 ACL，且 ACL 规则已允许相应协议及 IP，则继续排查 [步骤五](#step5)。
  + 如绑定了 ACL，但 ICMP 规则为**拒绝**，或 ACL 中无 ICMP 规则，请单击 ACL ID，进入 ACL 界面，修改使得对应协议及来源/目标 IP 的规则为**允许**，然后尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查 [步骤五](#step5) 。
>?如确认不需要使用 ACL 规则对子网流量进行控制，也可以解绑 ACL，该操作需谨慎评估影响后再执行。
>
 ![](https://qcloudimg.tencent-cloud.cn/raw/dff28d3b2825b35655084d21c7f03bd7.png)
	 

### 步骤五：请检查通信两端云服务器是否开启了防火墙[](id:step5)
请自行确认云服务器是否开启防火墙，如开启请确保防火墙不会对通信流量进行拦截，否则需要放通防火墙的限制。
>?
>- 清除防火墙的操作方法请参见 [如何清除防火墙](https://cloud.tencent.com/document/product/213/17403#.E5.A6.82.E4.BD.95.E6.B8.85.E9.99.A4.E9.98.B2.E7.81.AB.E5.A2.99.EF.BC.9F)。
>- 如已完成上述所有问题排查但问题依然存在，请做好问题记录，并联系 [售后在线支持](https://cloud.tencent.com/online-service)。
>
