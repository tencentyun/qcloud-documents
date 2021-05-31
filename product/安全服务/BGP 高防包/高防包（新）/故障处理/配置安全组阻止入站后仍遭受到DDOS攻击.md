
## 现象描述
配置了安全组规则阻止入站后，业务依然受到 DDoS 攻击。

## 可能原因
常见 DDoS 攻击方法包括：攻击网络和带宽资源、攻击系统资源、攻击应用资源等方式。
常见攻击流程如下图：
![](https://main.qcloudimg.com/raw/f47438cfa5dfa34da164027d05c84cb1.png)
- 控制端通过僵尸网络等方式控制大量主机，通过放大、反射等方式构造大量 DDoS 流量攻击服务器。
- 云业务服务提供商会提供一定攻击流量稀释与清洗的 [基础防护](https://cloud.tencent.com/document/product/1020)。
- 当用户进行安全组的入站策略等配置时，已经在 DDoS 攻击流量后方，此时经过基础防护如果不能完全将攻击流量进行稀释与清洗，就会出现 DDoS 攻击流量到达业务的情况。

## 解决思路
购买 DDoS 高防包或 DDoS 高防 IP，获得更强的防护能力，抵御大流量 DDoS 攻击。

## 处理步骤
- DDoS 高防包购买方法请参见 [购买指引](https://cloud.tencent.com/document/product/1021/43894)。
- DDoS 高防 IP 购买方法请参见 [购买指引](https://cloud.tencent.com/document/product/1014/44082)。

