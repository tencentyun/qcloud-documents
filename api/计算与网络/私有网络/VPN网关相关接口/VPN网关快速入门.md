简单搭建一个 VPN，一般需要以下几步：
1. 创建 VPN 网关
您可以使用 [购买 VPN 网关](https://cloud.tencent.com/doc/api/245/5106) 接口购买一个 VPN 网关实例，该接口会返回一个订单号，您可以使用 [查询 VPN 网关列表](https://cloud.tencent.com/doc/api/245/5108) 接口查询购买的 VPN 网关信息。

2. 创建对端网关 
创建 VPN 网关后，您可以使用 [创建对端网关](https://cloud.tencent.com/doc/api/245/5116) 接口创建一个对端网关，您需要指定对端网关的IP地址。

3. 创建通道
对端网关也创建好了，您可以使用 [创建 VPN 通道](https://cloud.tencent.com/doc/api/245/5110) 接口创建一个 VPN 通道，您需要填写通道的本段 VPN 网关和对端网关，设置一个预共享密钥后和名称后，通道创建成功。

4. 修改路由表
通道创建好后，您可以使用 [修改路由表](https://cloud.tencent.com/doc/api/245/1417) 接口修改路由表策略，新增一条路由策略，将需要访问对端网关网段的下一跳指向 VPN 网关。

5. 修改子网关联路由表
路由策略配置完成后，您可以使用 [修改子网关联的路由表](https://cloud.tencent.com/doc/api/245/1416) 接口将需要通过 VPN 网关访问 IDC 的子网指向上述路由表。
