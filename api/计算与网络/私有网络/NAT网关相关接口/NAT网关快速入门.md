创建一个 NAT 网关可以让 VPC 内只具有内网 IP 的云服务器可以快速访问 Internet。一般需要以下几步：
1. 创建 NAT 网关
您可以使用 [创建 NAT 网关](/doc/api/245/4094)接口购买一个 NAT 网关，该接口会返回一个订单号，您可以使用 [查询 NAT 网关的操作状态](https://cloud.tencent.com/doc/api/245/4089)接口查询购买的 NAT 网关信息。
2. 修改路由表
NAT 网关创建好后，您可以使用 [修改路由表](https://cloud.tencent.com/doc/api/245/1417) 接口修改路由表策略。新增一条路由策略，将需要通过 NAT 网关访问 Internet 的下一跳指向 NAT 网关。
3. 修改子网关联路由表
路由策略配置完成后，您可以使用 [修改子网关联的路由表](https://cloud.tencent.com/doc/api/245/1416) 接口将需要通过 NAT 网关访问 Internet 的子网指向上述路由表。

NAT 网关具体使用场景，请参见 <a href="https://cloud.tencent.com/document/product/552/12953" title="NAT网关">NAT 网关-应用场景</a>。
