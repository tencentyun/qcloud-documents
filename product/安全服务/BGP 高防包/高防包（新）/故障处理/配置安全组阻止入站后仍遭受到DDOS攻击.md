
## 现象描述
配置了安全组规则阻止入站后，业务仍遭受到 DDoS 攻击。

## 可能原因
常见 DDoS 攻击方法包括：攻击网络和带宽资源、攻击系统资源、攻击应用资源等方式。
常见攻击流程如下图所示：
![](https://main.qcloudimg.com/raw/f47438cfa5dfa34da164027d05c84cb1.png)
1. 控制端通过僵尸网络等方式控制大量主机，通过放大、反射等方式构造大量 DDoS 流量攻击服务器。
2. 云业务服务提供商会提供一定攻击流量稀释与清洗的 [基础防护](https://cloud.tencent.com/document/product/1020)。
3. 用户进行安全组的入站策略等配置，只能达到基于 IP 和端口的防护，此时经过基础防护若不能完全将攻击流量进行稀释与清洗，攻击者仍可以达到利用 DDoS 攻击流量占用网络和带宽资源等目的。

## 解决思路
购买 DDoS 高防包或 DDoS 高防 IP，获得更强的防护能力，抵御大流量 DDoS 攻击。

## 处理步骤
- DDoS 高防包购买方法请参见 [购买指引](https://cloud.tencent.com/document/product/1021/43894)。
- DDoS 高防 IP 购买方法请参见 [购买指引](https://cloud.tencent.com/document/product/1014/44082)。

>?
>- 防护对象：
>  - DDoS 高防包只针对腾讯云内的服务提升 DDoS 防护能力。
>  - DDoS 高防 IP 面向云内外用户，支持网站域名和业务端口接入防护。
>- 接入：
>  - DDoS 高防包的接入配置更加便捷，无需变更公网 IP 地址。
>  - DDoS 高防 IP 需修改 DNS 解析或修改业务 IP 后才能接入防护。

详情请参见 [DDoS 防护解决方案对比](https://cloud.tencent.com/document/product/1021/44463)。

