没有外网 IP 的云服务器，可通过位于不同子网的公网网关访问 Internet。公网网关主机将对公网流量进行源地址转换，其他所有主机访问外网的流量经过公网网关后，IP 都被转换为公网网关主机的 IP 地址，如下图所示：
![](https://main.qcloudimg.com/raw/db435a5ad2c8f4bf631574bfe6851e5b.png)
实现 VPC 内无外网 IP 主机通过公网网关访问外网，需要完成以下4个步骤：
- 步骤1：[创建网关子网](https://cloud.tencent.com/document/product/215/20136)。
- 步骤2：[购买公网网关](https://cloud.tencent.com/document/product/215/20137)。
- 步骤3：[创建网关子网路由表](https://cloud.tencent.com/document/product/215/20138)，网关所在的子网需单独一张路由表控制（在无其它路由诉求的情况，无需添加路由策略）。
- 步骤4：[配置普通子网路由表](https://cloud.tencent.com/document/product/215/20139)，新增路由策略：目的端为公网，下一跳指向公网网关。
