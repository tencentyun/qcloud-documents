## 应用场景
随着客户业务增长，出于安全考虑，客户希望云服务器内网 IP 不要暴露在公网，希望能实现云内 IP 地址的**双向隐藏**。

## 配置方案
基于如上需求，结合腾讯云产品能力，可通过 CLB + NAT 网关方式实现在隐藏云服务器内网 IP 情况下，安全地与公网互访：
+ CVM 主动访问外网：即云服务器主动访问外网，可以通过公网 NAT 网关实现。通过 NAT 网关的 SNAT 功能将云服务器的内网 IP 地址转换为 SNAT 后的公网 IP 地址，从而**隐藏**云服务器的内网 IP 地址。
+ 外网访问 CVM：当云服务器需要对外提供服务时，可通过公网负载均衡 VIP 统一对外提供服务，从而**隐藏**云服务器的内网 IP 地址，实现公网到云服务器的安全访问。
![](https://qcloudimg.tencent-cloud.cn/raw/f5a724d63c8fe50f5d47fd64daf17330.png)

## 配置流程
假设客户已创建了业务 VPC，并在 VPC 内云服务器上部署相关业务，可按照如下流程配置：
<dx-steps>
- [创建 NAT 网关并配置子网路由指向 NAT 网关](#step1)
- [创建公网负载均衡 CLB 实例并配置监听器规则](#step2)
- [配置安全策略](#step3)
- [操作验证](#step4)
</dx-steps>



## 操作步骤
<dx-accordion>
::: 创建 NAT 网关并配置子网路由指向 NAT 网关[](id:step1)
创建 NAT 网关并配置子网路由指向 NAT 网关，可以将子网流量引流到 NAT 网关，统一通过 NAT 网关上的公网 IP 来访问公网，从而隐藏内网 IP，实现安全的公网访问。详情请参见 [NAT 快速入门](https://cloud.tencent.com/document/product/552/18186)。

#### 步骤一：创建 NAT 网关
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)。
2. 单击左上角的**新建**，在弹出框中依次配置参数。
3. 参数配置完成后，按照界面提示完成购买即可。详情请参见 [创建 NAT 网关](https://cloud.tencent.com/document/product/552/83056)。

#### 步骤二：配置子网路由表指向 NAT 网关
1. 在 NAT 实例列表中，单击目标 NAT 实例所在行的私有网络 ID。
2. 在私有网络详细信息中，单击子网。
3. 在子网列表中，选择需要访问公网的子网所在行的路由表 ID。
4. 在路由表基本信息页面，单击**新增路由策略**。
5. 在**新增路由**弹框中，输入目的端（目的公网对应的 IP 地址段）、下一跳类型选择 NAT 网关、下一跳选择已创建的 NAT 网关 ID。
 ![](https://qcloudimg.tencent-cloud.cn/raw/f4cb2c636ec24571f127fdcd358be710.png)
6. 单击**创建**完成以上配置后，关联此路由表的子网内的云服务器访问公网的流量将指向该 NAT 网关，并通过 NAT 网关上的公网 IP 访问公网。

#### 步骤三：（可选）配置 SNAT 规则
NAT 支持绑定多个公网 IP，子网路由指向 NAT 网关时，默认子网下的云服务器均可通过 NAT 上的所有公网 IP 访问公网。如需指定云服务器通过 NAT 上指定的公网 IP 访问公网，则可以配置 SNAT 规则，详情请参见[ 创建 SNAT 规则](https://cloud.tencent.com/document/product/552/52323#.E5.88.9B.E5.BB.BA-snat-.E8.A7.84.E5.88.99.3Ca-id.3D.22cjgz.22.3E.3C.2Fa.3E)。

#### 步骤四：（可选）配置端口转发规则
NAT 网关默认提供主动内访外的能力，如需要对外提供服务，也可以通过配置端口转换规则来实现。
即可将 VPC 内云服务器的**内网 IP**，**协议**，**端口**映射成**外网 IP**，**协议**，**端口**，使得云服务器上的资源可一对一地被外网访问，详情请参见[ 配置端口转发规则](https://cloud.tencent.com/document/product/552/18176)。
>?NAT 网关的端口转换服务仅能提供一对一的对外访问服务，如需通过统一的 IP 地址对外提供服务，则参考如下步骤通过公网 CLB 来实现。
>
:::
::: 创建公网负载均衡 CLB 实例并配置监听器规则[](id:step2)
通过创建公网 CLB，并配置监听器规则，使得外部客户端可通过 CLB 的外网 VIP 访问后端的云服务器业务，通过公网 CLB 的流量将转发至后端云服务器上。详情请参见 [负载均衡快速入门](https://cloud.tencent.com/document/product/214/8975)。

#### 步骤一：购买负载均衡实例
1. 登录腾讯云[ 负载均衡服务购买页](https://buy.cloud.tencent.com/clb)。
2. 在负载均衡 CLB 购买页面，地域选择与云服务器相同的地域，实例类型选择**负载均衡**，网络类型选择**公网**。详情请参见 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。
3. 单击**立即购买**，完成付款。

#### 步骤二：配置负载均衡监听器
当客户端发起请求时，负载均衡会根据监听的前端协议与端口接收请求并向后端服务器转发请求，详情请参见 [配置 TCP 监听器](https://cloud.tencent.com/document/product/214/36386)。
1. 在负载均衡列表页，单击目标负载均衡实例右侧的**配置监听器**。
2. 在**监听器管理**页签对应协议区域下，单击**新建**。
3. 在**创建监听器**对话框中，逐步配置监听器健康检查，会话保持等相关参数，单击**提交**。
4. 在右侧监听器详情中，单击**绑定**，为 CLB 绑定后端云服务器，并配置云服务器端口和权重，完成后单击**确定**。
    ![](https://qcloudimg.tencent-cloud.cn/raw/73314c69869f929c67cd2afd4e6956d5.png)
:::
::: 配置安全策略[](id:step3)
1. 创建完负载均衡后，您可以配置负载均衡的安全组来隔离公网流量，详情请参考[ 配置 CLB 安全组](https://cloud.tencent.com/document/product/214/14733#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E9.85.8D.E7.BD.AE-clb-.E5.AE.89.E5.85.A8.E7.BB.84)。
2. 可以为云服务器绑定安全组，实现云服务器级别的流量控制，详情请参见[ 添加安全组规则](https://cloud.tencent.com/document/product/213/39740) 和 [关联实例至安全组](https://cloud.tencent.com/document/product/213/39751)。
3. 可以[ 配置 WAF 对负载均衡的监听域名进行 Web 安全防护](https://cloud.tencent.com/document/product/214/49031)。
4. 可以为 [NAT 网关绑定 DDoS 高防包](https://cloud.tencent.com/document/product/552/18185) 以抵御 DDoS 攻击。
:::
::: 操作验证[](id:step4)
1. 云服务器主动访问外网。
    ![](https://qcloudimg.tencent-cloud.cn/raw/1c390ab20ce53f39553e20ac81f37a23.png)
2. 外网通过公网 CLB 的 VIP 访问后端业务。
    ![](https://qcloudimg.tencent-cloud.cn/raw/72e21cf523e96235f0fec77c035cf8e9.png)
:::
</dx-accordion>


		
## 相关文档
+ 当一个子网关联了 NAT 网关，且子网内云服务器有公网 IP（或弹性 IP）时，会默认通过 NAT 网关访问 Internet（因为最精确路由的优先级高于公网 IP），但您可以设置路由策略，实现通过云服务器公网 IP 访问 Internet，详情请参见 [调整 NAT 网关和 EIP 的优先级](https://cloud.tencent.com/document/product/552/30012)。
+ 若您使用 CLB 转发业务流量到 CVM 上，为保障健康检查功能，在 CVM 的安全组上需做相应配置，详情请参见[ 后端云服务器的安全组配置](https://cloud.tencent.com/document/product/214/6157)。
