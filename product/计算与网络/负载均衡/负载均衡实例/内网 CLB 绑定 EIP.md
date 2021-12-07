内网负载均衡用于分发来自腾讯云内网的请求，没有公网 IP 且不能与公网互通。若您需要使用内网负载均衡并与公网互通，则可选择内网负载均衡绑定弹性公网 IP，通过弹性公网 IP 访问公网。

>?内网 CLB 绑定弹性公网 IP 功能处于内测阶段，如需使用，请提交 [内测申请](https://cloud.tencent.com/apply/p/4kxj7picqci)。

## 使用限制
- 仅标准账户类型支持，传统账户类型不支持。
- 仅负载均衡实例类型支持，传统型负载均衡不支持。
- 仅 VPC 的内网 CLB 支持，基础网络的内网 CLB 不支持。
- 济南、杭州、福州、石家庄、武汉、长沙地域没有内网 CLB，因此不支持此功能。
- 内网 CLB 绑定 EIP 后，CLB 上的安全组对来自 EIP 的流量不生效，对来自内网 CLB 的流量生效。开启安全组默认放通后，对二者的流量均生效。
- 目前内网 CLB 不支持端口段。
- 内网 CLB 仅能绑定同地域且未被其他资源绑定的 EIP。
- 每个内网 CLB 仅能与一个 EIP 互相绑定。
- 内网 CLB 绑定 EIP 后，功能类似于公网 CLB，但公网 CLB 无法拆分为内网 CLB 和 EIP。


## 操作步骤

<dx-accordion>
::: 方式一：购买\sCLB\s时选择\sEIP
1. 登录腾讯云 [负载均衡购买页](https://buy.cloud.tencent.com/lb)。
2. 按需选择以下负载均衡相关配置，其余配置详情请参见 [购买方式](https://cloud.tencent.com/document/product/214/8849)。
<table>
<thead>
<tr>
<th width="18%">参数</th>
<th width="82%">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight:bold">计费模式</span></td>
<td>
选择“按量计费”模式。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">地域</span></td>
<td>
选择所属地域。CLB 支持的地域详情请参见 <a href="https://cloud.tencent.com/document/product/214/30670#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8">地域列表</a>。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">实例类型</span></td>
<td>
仅支持负载均衡实例类型。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">网络类型</span></td>
<td>选择“公网”网络类型。
</td>
</tr>
<tr>
<td><span style="font-weight:bold">弹性公网 IP</span></td>
<td>选择弹性公网 IP，腾讯云将为您分配一个弹性公网 IP 和一个内网 CLB。弹性公网 IP 的类型支持：常规 IP、加速 IP、静态单线 IP。
</td>
</tr>
</tbody></table>
:::
::: 方式二：内网\sCLB\s绑定\sEIP
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，单击左侧导航栏的**实例管理**。
2. 在“实例管理”页面左上角选择地域，在实例列表中选择目标内网 CLB 实例，在右侧“操作”列选择**更多** > **绑定弹性公网 IP**。
3. 在弹出的“绑定弹性公网 IP”对话框中，选择需绑定的 EIP，单击**提交**即可为内网 CLB 绑定 EIP。
<img src="https://qcloudimg.tencent-cloud.cn/raw/201e56b830bc8e165070b8963fe72cb3.png" width="60%">
4. （可选）在实例列表中选择目标内网 CLB 实例，在右侧“操作”列选择**更多** > **解绑弹性公网 IP**即可为内网 CLB 解绑 EIP。
:::
</dx-accordion>


## 相关文档
- [绑定弹性公网 IP API 文档](https://cloud.tencent.com/document/product/215/16700)
- [购买方式](https://cloud.tencent.com/document/product/214/8849)
- [产品属性选择](https://cloud.tencent.com/document/product/214/33415)
