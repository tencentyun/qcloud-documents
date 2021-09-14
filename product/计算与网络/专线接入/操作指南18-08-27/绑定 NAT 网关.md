创建专线网关完成后如果您业务需要通过 NAT 网关方式进行公网访问，那么您需要为专线网关绑定 NAT 网关。本文将介绍如何为专线网关绑定 NAT 网关。

## 前提条件
- 已[ 创建 VPC 网络](https://cloud.tencent.com/document/product/215/36515)。
- 已 [创建 VPC 型专线网关](https://cloud.tencent.com/document/product/216/19256)。
- 已[ 创建 NAT 网关](https://cloud.tencent.com/document/product/552/18186#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.88.9B.E5.BB.BA-nat-.E7.BD.91.E5.85.B3)。

## 绑定 NAT 网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中，单击**专线网关**，进入管理页面。
3. 在专线网关列表中单击需要绑定 NAT 网关的专线网关名称，进入详情页面。
4. 在**基本信息**页面选择需要绑定的 NAT 网关。
![](https://main.qcloudimg.com/raw/cc408812274ac0ab9fb5257dcb727c2d.png)

## 解绑 NAT 网关
如果您不再需要专线网关上绑定的 NAT 网关，您可以进入专线网关详情页面的**基本信息**页签解绑。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中，单击**专线网关**，进入管理页面。
3. 在专线网关列表中单击需要解绑 NAT 网关的专线网关名称，进入详情页面。
4. 在**基本信息**页面**绑定 NAT 网关**所在行单击**解绑**，并在弹出的对话框中单击**确定**。
![](https://main.qcloudimg.com/raw/0e62068c6ef5c455f5f59c2e6d794f15.png)
