##什么是DDoS高防IP？
DDoS高防IP是腾讯云面向所有互联网云服务器（含非腾讯云服务器）推出的防DDoS攻击的付费产品，能够有效应对大流量的DDoS攻击。目前支持电信、联通、移动、BGP四条线路防护，可直接购买单线路IP或套餐（多线路IP）防护。

##使用场景
DDoS高防IP，服务于腾讯云以及腾讯云以外的所有云服务器。

##防护原理
DDoS高防IP通过代理转发模式防护源站服务器，业务流量直接访问高防IP然后回源到源站服务器。如果发生DDoS攻击，攻击流量在经过高防IP时，防护系统则会进行过滤清洗，并将清洁业务流量转发回源到业务服务端，以保障业务在 DDoS 攻击场景下的可用性。

##为什么选择该产品？
- 隐藏真实源站 IP

DDoS高防IP将通过代理转发模式，将业务流量转发给源站IP，以此隐藏源IP，攻击流量被清洗，保护源站业务。

- 超大带宽防护

DDoS高防IP可针对云内外服务器提供T级防护，轻松抵御大流量 DDoS 、 CC 攻击。

注意：如需配置更高带宽防护，请联系客服咨询。

- 支持单IP、套餐购买

DDoS高防IP支持一次性购买一条或多条不同线路IP，灵活选购，适合各种业务场景使用。如果业务防护需求主要是某一个运营商，可以直接选购单IP线路防护。而套餐支持提供多线路防护，避免跨网访问，更划算。比如三网3IP 保底20Gbps 19500/月，相比单IP定价电信、联通、移动分别保底20Gbps，合计13600*3=40800/月实惠更多。详情可参考[DDoS高防IP单IP定价](https://cloud.tencent.com/document/product/685/15262)、[DDoS高防IP套餐定价](https://cloud.tencent.com/document/product/685/19025)

- 灵活计费

按月预付费的保底+按天后付费的弹性，按用户实际攻击量计费，为用户节约成本。详情可参考[计费说明](https://cloud.tencent.com/document/product/685/15263)

##使用时需要注意什么？
DDoS高防 IP 是通过将高防 IP 作为业务 IP 对外发布来隐藏源站 IP的方式实现防护目的，若用户源站曾被攻击过且源站 IP 已暴露，那么建议购买DDoS高防 IP 服务后更换源站 IP，以确保源站 IP 的隐秘性，让攻击者无法直接攻击源站。如果是腾讯云主机IP，可见[如何更换腾讯云主机IP地址](https://cloud.tencent.com/document/product/685/18802)

##如何配置DDoS高防IP？
用户登录[宙斯盾安全防护控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fgamesec)，立即购买，点击[购买DDoS高防IP](https://buy.cloud.tencent.com/gamesec)。如何操作见[DDoS高防IP](https://cloud.tencent.com/document/product/685/15264)