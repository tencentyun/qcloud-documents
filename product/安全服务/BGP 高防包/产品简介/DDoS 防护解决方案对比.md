DDoS 防护基于腾讯社交、游戏、资讯、金融等领域累积的多年安全攻防和实战经验，提供了丰富和全面的安全解决方案，满足您不同业务场景应对的各类 DDoS 攻击安全防护需求。

本文将介绍不同 DDoS 防护解决方案的基本信息和适用场景。
>?
>- 若您需要定制专属的安全解决方案，您可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行咨询。
>- DDoS 防护（包含 DDoS 基础防护、DDoS 高防包和 DDoS 高防 IP）不会对访问量小于50QPS的流量进行防护。

| 产品名称 | 适用用户 | 防护对象 |接入方式 | 计费方式 | 防护能力 |配置特点 |
|---------|---------|---------|---------|---------|---------|---------|
| [DDoS 基础防护](https://cloud.tencent.com/document/product/1020/31625) | 仅限腾讯云内用户 | 适用于腾讯云产品（如 CVM、CLB 等），普通用户可享受2Gbps防护，[VIP 用户](https://cloud.tencent.com/act/event/service-plan) 可享受10Gbps防护。 |无需配置。| 免费 | <ul><li>主要为遭受攻击概率不大，攻击流量不超过免费的基础防护能力的云上用户业务提供防护。如需更高防护能力，推荐选择[ DDoS 高防包服务](https://cloud.tencent.com/document/product/1021/43890)。<li>普通客户默认享受2Gbps的 DDoS 防护能力，VIP 客户默认享受10Gbps的 DDoS 防护能力。但当客户业务遭受到频繁的攻击时，腾讯云会根据客户的历史攻击情况调整其基础 DDoS 防护能力，以保障腾讯云平台的整体稳定。</ul> | 无需配置，自动为云内产品 IP 开启防护。|
| DDoS 高防包 | 仅限腾讯云北京，上海，广州区域的用户 | 适用于腾讯云产品，包括 CVM、CLB、WAF、黑石物理服务器、黑石负载均衡、NAT IP、EIP、GAAP IP 等，同时也适用于有大量云产品 IP 需要防护的用户 。| 在 DDoS 防护控制台上绑定防护 IP 后生效，详情可参见 [快速入门](https://cloud.tencent.com/document/product/1021/43898) 。| 采用“防护次数+防护资源数”组合方式计费 | <ul><li>在用户购买的防护次数范围内，腾讯云提供不低于30Gbps的 DDoS 防护能力， 最高防护能力根据各个区域的实际网络情况动态调整。<li>支持HTTP CC防护。</ul> |无需变更业务，购买后绑定需要防护的云内产品 IP，即刻拥有更高 DDoS 防护能力。 |
|[ DDoS 高防 IP](https://cloud.tencent.com/document/product/1014/44078)<br>（中国大陆）| 面向业务是部署在中国大陆地区的所有互联网用户 | 支持 TCP，UDP，HTTP 和 HTTPS 业务（默认支持 websocket）。| 通过高防 IP 进行代理后，转发至后端源站 IP，详情可参见 [网站业务接入](https://cloud.tencent.com/document/product/1014/44087) 及 [非网站业务接入](https://cloud.tencent.com/document/product/1014/44088)。| 采用“保底防护+弹性防护+转发带宽+转发规则数”组合方式计费 | 支持 HTTP/HTTPS CC 防护。<br>防护线路分为 BGP 线路和三网线路两种：<ul><li>BGP 线路最高提供 300Gbps 的防护能力。<li>三网线路最高可提供 1Tbps 的防护能力。</ul> |通过配置转发规则接入，使用高防 IP 作为源站的对外服务地址，隐藏用户源站。 |
| [DDoS 高防 IP](https://cloud.tencent.com/document/product/1014/44078)<br>（境外） | 面向业务是部署在非中国大陆地区所有互联网用户 | 支持 TCP，UDP，HTTP 和 HTTPS 业务（默认支持 websocket）| 通过高防 IP 进行代理后，转发至后端源站 IP，详情可参见 [网站业务接入](https://cloud.tencent.com/document/product/1014/44087) 及 [非网站业务接入](https://cloud.tencent.com/document/product/1014/44088)。|采用“保底防护+弹性防护+转发带宽+转发规则数”组合方式计费 |  <ul><li>当前最高可提供400Gbps的防护能力。<li>支持 HTTP/HTTPS CC 防护。<li>清洗中心部署在中国香港，中国台湾，新加坡，首尔，东京，弗吉尼亚、硅谷、法兰克福等。  |通过配置转发规则接入，使用高防 IP 作为源站的对外服务地址，隐藏用户源站。 |




