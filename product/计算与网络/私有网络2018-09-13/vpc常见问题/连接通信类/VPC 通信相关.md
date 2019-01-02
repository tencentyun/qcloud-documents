### 同一 VPC 不同子网的云服务器、云数据库等可以实现内网互通吗？
同一 VPC 下的所有资源（云服务器、云数据库等），无论是否在一个子网中，都默认内网互通。您可在每个路由表中都看到一条 [Local，Local，Local] 的路由规则，即表示该 VPC 内所有子网资源内网互通。且一个私有网络下，不同子网所在可用区的不同（如广州一区、广州二区），也不会影响此特性。
例如，您的一个 VPC 属于广州地域，包含三个子网，分别是广州一区、广州二区、广州三区，每个子网内都有云服务器或云数据库等资源默认内网互通。

### 如何实现不同 VPC 间云服务器、云数据库等资源内网互通？
每个 VPC，无论属于同一账号还是不同账号，都是一个逻辑隔离的网络空间，默认无法互通。
您可以使用 [对等连接](https://cloud.tencent.com/document/product/553) 或 [云联网](https://cloud.tencent.com/document/product/877) 来实现 VPC 间的通信，但需要互通的 VPC 网段（即 CIDR ）不能重叠。
对等连接和云联网的收费方式，详情请参考 [对等连接计费详情](https://cloud.tencent.com/document/product/553/18833)、[云联网计费详情](https://cloud.tencent.com/document/product/877/18676)。
- 同账号互通示例：您有两个 VPC，分别包含云服务器或云数据库等资源，需要这些资源实现内网互通，可以建立 [同账号对等连接](https://cloud.tencent.com/document/product/553/18836)。
- 跨账号互通示例：您有一个 VPC A，需要与另一个账号的 VPC B 中的资源（云服务器、云数据库等）实现内网互通，无论两个 VPC 是否在同一个地域，您都可以建立 [跨账号对等连接](https://cloud.tencent.com/document/product/553/18837)。
- 错误示例：不同 VPC 下的资源，即使内网 IP 在同一网段内甚至完全相同，都无法实现互通。

>**注意：**
如果您的两个 VPC 网段已经重叠，您可以参考 [网段重叠解决方法](https://cloud.tencent.com/document/product/215/30101#.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.E5.9B.A0-vpc-.E7.BD.91.E6.AE.B5.E5.86.B2.E7.AA.81.E8.80.8C.E6.97.A0.E6.B3.95.E5.BB.BA.E7.AB.8B.E5.AF.B9.E7.AD.89.E8.BF.9E.E6.8E.A5.E7.9A.84.E9.97.AE.E9.A2.98.EF.BC.9F)。

### 如何处理因 VPC 网段冲突而无法建立对等连接的问题？
建立对等连接时，要求两端 VPC 的 CIDR 不可以重叠，否则无法建立对等连接。

- 如果您两端 VPC 中，需要通信的子网网段不重叠，可以使用 [云联网](https://cloud.tencent.com/product/ccn) 来实现通信。云联网可以将 VPC 通信时的网段限制缩小到子网层面。
例如，您需要通信的两个 VPC 网段均为 `10.0.0.0/16`，但子网分别为 `10.0.0.1/24` 和 `10.0.0.2/24`，则可以通过云联网实现通信。详情请参考 [云联网产品文档](https://cloud.tencent.com/document/product/877)。
- 如果云联网仍不能满足您的需求，则需要将重叠子网内的资源进行迁移。
    - 云服务器更换子网，详情请参考 [操作指南](https://cloud.tencent.com/document/product/213/16565)。
    - VPC 间迁移，详情请参考 [云服务器切换私有网络](https://cloud.tencent.com/document/product/213/20278#.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B9.8B.E9.97.B4.E5.88.87.E6.8D.A2)。
    
 >**注意：**
>在进行迁移前，请仔细阅读相关文档。

### 若 VPC1 分别和 VPC2、VPC3 建立了对等连接，那 VPC2 和 VPC3 能互通吗？
不能，对等连接能使 VPC 两两建立互联，但是这种互通关系不发生传递。即当 VPC1 与 VPC2 建立了对等连接，VPC1 和 VPC3 也建立了对等连接时，由于对等连接的不传递性，VPC2 和 VPC3 的流量不能互通。

