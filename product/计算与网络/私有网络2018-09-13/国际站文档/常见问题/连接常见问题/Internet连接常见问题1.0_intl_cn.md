## 1. 没有公有 IP 地址的实例（云主机、数据库）如何访问 Internet？
可以通过 NAT 网关/  公网网关访问 Internet。
- <a href="https://cloud.tencent.com/doc/product/215/4975" target="_blank">NAT 网关</a>，通过创建 NAT 网关和配置相关子网所关联的路由表，那么子网内的实例即可访问 Internet，<a href="https://cloud.tencent.com/doc/product/215/4975#.E4.BD.BF.E7.94.A8-nat-.E7.BD.91.E5.85.B3.E8.AE.BF.E9.97.AE-internet" target="_blank">点击查看操作步骤详情</a>。
- <a href="https://cloud.tencent.com/doc/product/215/4972" target="_blank">公网网关</a>，没有外网 IP 但需要进行 Internet 访问的云服务器可通过位于不同子网的公网网关来访问 Internet，<a href="https://cloud.tencent.com/doc/product/215/4972#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97" target="_blank">点击查看操作指南</a>。

## 2. 公网网关与云主机带有公网 IP 有什么区别？
云主机自带公网 IP 相当于多加一个公网网卡，主机可以自由访问 Internet。

## 3. 为什么子网配置好路由策略，并指向公网网关后无法实现策略转发？
通过公网网关访问公网的云主机与公网网关处于同一子网时，转发功能失效，请将两者布置在不同的子网，<a href="https://cloud.tencent.com/doc/product/215/4972#.E6.93.8D.E4.BD.9C.E6.8C.87.E5.8D.97" target="_blank">点击查看操作指南</a>。

## 4.路由表配置了某子网内通过 NAT 网关访问公网，但是该子网内的云主机又配置了弹性 IP，这些云主机是通过 NAT 网关还是弹性 IP 访问公网？
**NAT 网关**，<a href="https://cloud.tencent.com/doc/product/215/4954#.E8.B7.AF.E7.94.B1.E8.A7.84.E5.88.99.E4.BC.98.E5.85.88.E7.BA.A7" target="_blank">点击查看路由规则优先级说明</a>。