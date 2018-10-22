#VPC间通信
####不同VPC间如何通信？
您可以使用[对等连接](https://cloud.tencent.com/document/product/553)或[云联网](https://cloud.tencent.com/document/product/877)以实现VPC间的通信。
- 对等连接用于VPC建立一对一的连接，要求建立连接的两个VPC的CIDR（网段）不能重叠，否则无法建立连接。成功建立对等连接后您还需在两端VPC配置路由策略方能实现通信。更多信息请参考[对等连接产品文档](https://cloud.tencent.com/document/product/553)
- 云联网用于多个VPC间、VPC与IDC间通信，VPC与云联网关联后会自动下发到与云联网关联的其它所有VPC的路由，CIDR的限制缩小到子网层面，更加灵活。更多信息请参考[云联网产品文档](https://cloud.tencent.com/document/product/877)。

####因为VPC网段冲突而无法建立对等连接怎么办？
建立对等连接要求两端 VPC CIDR 不可以重叠，如果重叠则无法建立对等连接。

- 如果您两端VPC中需要通信的子网网段不重叠，可以使用[云联网](https://cloud.tencent.com/product/ccn)，云联网可以将VPC通信时对网段的限制缩小到子网层面。
    例如您需要通信的两个VPC网段均为10.0.0.0/16，但子网分别为10.0.0.1/24和10.0.0.2/24，则可以通过云联网实现通信。更多信息请参考[云联网产品文档](https://cloud.tencent.com/document/product/877)。
- 如果云联网仍不能满足您的需求，则您需要将重叠的子网内的资源进行迁移。
    - 云服务器更换子网请参考[操作指南](https://cloud.tencent.com/document/product/213/16565)
    - VPC间迁移请参考[云主机切换私有网络](https://cloud.tencent.com/document/product/213/20278#.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B9.8B.E9.97.B4.E5.88.87.E6.8D.A2)，请您在操作前仔细阅读文档。
####VPC1分别和VPC2、VPC3建立了对等连接，VPC2和VPC3会互通吗？
不会，对等连接能使VPC两两建立互联，但是这种互通关系不发生传递。
如果VPC 1 与 VPC 2 建立了对等连接，VPC 1 和 VPC 3 也建立了对等连接。然而由于对等连接的不传递性，VPC 2 和 VPC 3 的流量不能互通。
####能否和其他账号的VPC通信？
可以，对等连接和云联网均支持与其他账号VPC通信。如果需要建立对等连接，则连接的两个VPC网段不能重叠，更多信息请参考[产品文档](https://cloud.tencent.com/document/product/553) 和[建立跨账号对等连接](https://cloud.tencent.com/document/product/553/18837)。


