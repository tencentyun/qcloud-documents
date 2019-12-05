## 1. VPC 和子网中可以使用哪些 IP 地址范围？
- 私有网络支持三个网段的内网IP：`10.a.0.0/8`（a属于0至255）、`172.b.0.0/16`（b属于0至31）、`192.168.0.0/16` 。私有网络的 CIDR 可以为以上三个网段，或者是网段中的一部分。
- 网络块包括的 IP 数 =` 2^(32-掩码)`，因而 `10.1.0.0/16` 网络块最多包含 65536 个 IP 地址。

## 2. 什么是 CIDR，分配私有网络的 CIDR 需要注意什么？
CIDR（无类别域间路由，Classless Inter-Domain Routing）是由用户指定的独立网络空间地址块，通过 IP 和掩码结合，实现对网络的整体划分。点击查看 <a href="https://cloud.tencent.com/doc/product/215/4927#cidr" target="_blank">分配私有网络的 CIDR 需要注意的内容</a>。

## 3. 路由表配置了某子网内通过 NAT 网关访问公网，但是该子网内的云主机又配置了弹性 IP，这些云主机是通过 NAT 网关还是弹性 IP 访问公网？
NAT 网关，点击查看 <a href="https://cloud.tencent.com/doc/product/215/4954#.E8.B7.AF.E7.94.B1.E8.A7.84.E5.88.99.E4.BC.98.E5.85.88.E7.BA.A7" target="_blank">路由规则优先级说明</a>。

## 4. 如何修改云主机内网 IP？
云主机主网卡的主内网 IP 支持修改，辅助网卡的主内网 IP 不支持修改，操作步骤如下：
（1）进入 <a href="https://console.cloud.tencent.com/cvm/" target="_blank">云服务器控制台</a>，点击左导航栏的云主机，进入云主机列表页。
（2）点击云主机 ID，进入云主机详情页，点击上方 tab：弹性网卡。
（3）点击修改主 IP。
（4）填入新的 IP，并保存即可。
<div style="text-align:center">
![](https://mc.qcloudimg.com/static/img/9c08d3a7ead4707abd6315e2a092184b/A%7D%257Q%25R3C5QDOR%24JM%25I3U%28D.png)

</div>
您也可以在弹性网卡详情页修改主内网 IP，点击查看<a href="https://cloud.tencent.com/doc/product/215/6513#.E4.BF.AE.E6.94.B9.E4.B8.BB.E5.86.85.E7.BD.91ip" target="_blank">操作详情。</a>