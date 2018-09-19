创建一个NAT网关可以让 VPC 内只具有内网 IP 的云服务器可以快速访问Internet。一般需要以下几步：

1) 创建NAT网关
您可以使用[创建NAT网关](/doc/api/245/4094)接口购买一个NAT网关，该接口会返回一个订单号，您可以使用[查询NAT网关的操作状态](https://cloud.tencent.com/doc/api/245/4089)接口查询购买的NAT网关信息。

2) 修改路由表
NAT网关创建好后，您可以使用[修改路由表](https://cloud.tencent.com/doc/api/245/1417)接口修改路由表策略。新增一条路由策略，将需要通过NAT网关访问Internet的下一跳指向NAT网关。

3) 修改子网关联路由表
路由策略配置完成后，您可以使用[修改子网关联的路由表](https://cloud.tencent.com/doc/api/245/1416)接口将需要通过NAT网关访问Internet的子网指向上述路由表。

NAT网关具体使用场景，详见<a href="https://cloud.tencent.com/doc/product/215/1682#2.-nat.E7.BD.91.E5.85.B3" title="NAT网关">NAT网关说明</a>