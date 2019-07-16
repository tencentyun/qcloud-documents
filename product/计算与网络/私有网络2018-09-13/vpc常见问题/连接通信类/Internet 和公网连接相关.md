### 如果云服务器在购买时没有分配公网 IP ，应该如何申请？
如果您在购买云服务器时没有分配公网 IP，那么无法为该云服务器再申请普通公网 IP，但可以通过 [弹性公网 IP](https://cloud.tencent.com/document/product/213/5733) 来实现相同功能。操作详情请参见 [申请弹性公网 IP](https://cloud.tencent.com/document/product/213/16586)。

弹性公网 IP 是公网 IP 的一种，是某地域下一个固定不变的公网 IP 地址。与普通公网 IP 不同的是，它是与您的账户绑定，即：您可以将一个弹性公网 IP 根据需要与不同的云服务器绑定、解绑（一次只能绑定一个）。

由于弹性 IP 的特殊性，如果您申请了弹性 IP 但并未绑定实例，需要收取一定的闲置费用，详情请参见 [弹性公网 IP 计费](https://cloud.tencent.com/document/product/213/17156)。

### 没有公网 IP 地址的实例（云服务器、数据库）如何访问 Internet？
没有公网 IP 的实例可以申请弹性公网 IP（请参见上一个问题），或者通过 NAT 网关 / 公网网关访问 Internet。

- [NAT 网关](https://cloud.tencent.com/document/product/552) 
通过创建 NAT 网关、配置相关子网所关联的路由表，子网内的实例即可访问 Internet。
- [公网网关](https://cloud.tencent.com/document/product/215/20078) 
没有外网 IP 的云服务器，可通过位于不同子网的公网网关来实现 Internet 的访问。

### 能否为云服务器更换公网 IP？
如果您的云服务器是在购买时分配的公网 IP，则无法直接更换为其他公网 IP，但您可以借助弹性公网 IP 实现需求。

您需要执行以下步骤：

1. 将需要更换公网 IP 的云服务器目前的公网 IP 转换成弹性公网 IP，操作详情请参见 [公网 IP 转弹性 IP](https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91-ip-.E8.BD.AC.E5.BC.B9.E6.80.A7-ip)。
2. 将转换成功的这个弹性 IP 与该云服务器解绑并释放，操作详情请参见 [解绑和释放弹性 IP](https://cloud.tencent.com/document/product/213/16586#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip-.E8.A7.A3.E7.BB.91.E4.BA.91.E4.BA.A7.E5.93.81)。
3. 重新申请一个弹性 IP ，并与该云服务器绑定，操作详情请参见 [申请和绑定弹性 IP](https://cloud.tencent.com/document/product/213/16586#.E7.94.B3.E8.AF.B7.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip)。

>!公网 IP 转换成弹性公网 IP 后，建议您立即释放，否则，未绑定实例的弹性 IP 将会收取一定 [资源占用费](https://cloud.tencent.com/document/product/213/17156)。 

### 能否找回之前使用的公网 IP？能否申请指定的弹性公网 IP？
非常抱歉，目前公网 IP 释放后无法再找回，也暂时不支持申请指定的弹性公网 IP。

### 弹性 IP 数量达到上限后能否申请增加配额？
非常抱歉，由于弹性 IP 资源的有限性，每个账号每个地域仅能申请20个，不能再增加。您可以使用 NAT 网关等方式实现无公网 IP 的云服务器访问 Internet 。

### 什么是公网网关？
公网网关是开启了转发功能的云服务器，无外网 IP 但需进行 Internet 访问的云服务器，可通过位于不同子网的公网网关来访问 Internet。详情请参见 [公网网关](https://cloud.tencent.com/document/product/215/11119#.E7.AE.80.E4.BB.8B)。
 >!公网网关子网和普通子网不能关联同一个路由表，需要新建一个独立的网关路由表来关联网关子网。详情请参见 [公网网关使用限制](https://cloud.tencent.com/document/product/215/20078#.E4.BD.BF.E7.94.A8.E9.99.90.E5.88.B6)。

### 如果云服务器有公网 IP/EIP，所在子网又关联了 NAT 网关，将如何实现 Internet 的访问?
如果一台云服务器有公网 IP/EIP（弹性公网 IP），同时，子网又关联了 NAT 网关（即路由表中设置了该子网访问 Internet 流量的下一跳是 NAT 网关），那么，默认该云服务器访问 Internet 的流量会全部通过 NAT 网关实现。

### 云服务器通过公网网关、NAT 网关访问 Internet，网络费用是否会收取双份？
不会，网络费用只收取一份。通过公网网关、NAT 网关访问 Internet，收取的是公网网关和 NAT 网关的网络费用。

