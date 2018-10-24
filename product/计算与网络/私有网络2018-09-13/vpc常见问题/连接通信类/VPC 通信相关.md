### 不同 VPC 间如何通信？
您可以使用 [对等连接](https://cloud.tencent.com/document/product/553) 或 [云联网](https://cloud.tencent.com/document/product/877) 来实现 VPC 间的通信。
- 对等连接用于建立 VPC 间的一对一连接，要求建立连接的两个 VPC 的 CIDR（网段）不能重叠。成功建立对等连接后，还需在两端的 VPC 配置路由策略，方能实现 VPC 间的通信。更多信息，请参考 [对等连接产品文档](https://cloud.tencent.com/document/product/553)
- 云联网用于多个 VPC 间、VPC 与 IDC 间通信，VPC 与云联网关联后，会自动下发到与云联网关联的其它所有 VPC 的路由，CIDR 的限制缩小到子网层面，更加灵活。更多信息，请参考 [云联网产品文档](https://cloud.tencent.com/document/product/877)。

### 如何处理因 VPC 网段冲突而无法建立对等连接的问题？
建立对等连接时，要求两端 VPC 的 CIDR 不可以重叠，否则无法建立对等连接。
- 如果您两端 VPC 中，需要通信的子网网段不重叠，可以使用 [云联网](https://cloud.tencent.com/product/ccn) 来实现通信。云联网可以将 VPC 通信时的网段限制缩小到子网层面。
例如，您需要通信的两个 VPC 网段均为`10.0.0.0/16`，但子网分别为`10.0.0.1/24`和`10.0.0.2/24`，则可以通过云联网实现通信。更多信息，请参考 [云联网产品文档](https://cloud.tencent.com/document/product/877)。
- 如果云联网仍不能满足您的需求，则需要将重叠子网内的资源进行迁移。
    - 云服务器更换子网，请参考 [操作指南](https://cloud.tencent.com/document/product/213/16565)。
    - VPC 间迁移，请参考 [云服务器切换私有网络](https://cloud.tencent.com/document/product/213/20278#.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B9.8B.E9.97.B4.E5.88.87.E6.8D.A2)。
    
 >**注意：**
>在进行迁移前，请仔细阅读相关文档。

### 若 VPC1 分别和 VPC2、VPC3 建立了对等连接，那 VPC2 和 VPC3 能互通吗？
不能，对等连接能使 VPC 两两建立互联，但是这种互通关系不发生传递。即当 VPC1 与 VPC2 建立了对等连接，VPC1 和 VPC3 也建立了对等连接时，由于对等连接的不传递性，VPC2 和 VPC3 的流量不能互通。

### 对等连接、云联网能否和其他账号的VPC通信？
可以，对等连接和云联网均支持与其他账号 VPC 通信。如果需要建立对等连接，则连接的两个 VPC 网段不能重叠，更多信息，请参考 [对等连接产品文档](https://cloud.tencent.com/document/product/553)。

