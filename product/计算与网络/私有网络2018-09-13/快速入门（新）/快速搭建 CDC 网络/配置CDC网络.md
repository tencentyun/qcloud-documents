本文指导您配置本地专用集群（CDC）的网络。

## 前提条件
[已完成 CDC 集群部署](https://cloud.tencent.com/document/product/1346/49917)
## 操作步骤

### 步骤1：创建 VPC 并确认可用区
在主Region地域创建一个 CDC 集群待关联的 VPC 网络，具体操作请参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515)。同时，请提前确认好 CDC 集群所在的可用区信息。

### 步骤2：在 VPC 中创建一个专线网关
在已创建的 VPC 中，创建一个专线网关，其中【关联网络】选择【私有网络】，【所在网络】选择已创建的 VPC ID，【网关类型】选择【标准型】，具体操作请参见 [创建专线网关](https://cloud.tencent.com/document/product/216/19256).

### 步骤3：创建 CDC 集群
创建 CDC，关联至已创建的 VPC，及专线网关，具体操作请联系腾讯云技术支持人员。

### 步骤4：创建 CDC 子网
1. 登录本地专用集群控制台。
2. 选择 CDC 子网，单击创建 CDC 子网。
3. 在弹出的对话框中，选择已创建的 CDC 集群，以及集群关联的主 Region VPC、可用区等信息，路由表默认是 VPC 主路由表，如需创建多个子网请单击【添加子网】。
	![](https://main.qcloudimg.com/raw/d81e2e02af5afc641fd9024ca078fdc0.png)
4. 在配置完 CDC 子网后，单击【确定】完成操作。
	![](https://main.qcloudimg.com/raw/8fd183549092a70809252c4bd29ed6e7.png)
5. （可选）如需更换路由表，可单击【更多】>【更换路由表】，为 CDC 子网更换路由表。
	![](https://main.qcloudimg.com/raw/a039849dd23858734727d868bc702c4a.png)

### 步骤5：在 CDC 子网创建云服务器
CDC 子网创建后，即可在子网中创建云服务器实例。

### 步骤6：创建 CDC 本地网关
1. 登录本地专用集群控制台。
2. 选择 CDC 本地网关。
3. 在弹出的“创建 CDC 本地网关”界面，填写网关名称，选择所属 CDC 集群和所属 VPC 网络。
 ![](https://main.qcloudimg.com/raw/81f47315a7347d62df99652c8e22ff22.png)
4. 单击【确定】，CDC 本地网关展示在列表中，目前1个 CDC 集群仅支持创建1个 CDC 本地网关。
   ![](https://main.qcloudimg.com/raw/b56d0a48e0d13dc6d9df87b3cbce3f27.png)

### 步骤7：创建路由策略
当 CDC 子网需要访问 IDC 网段时，可配置目标到本地网关的路由策略。CDC 默认关联主 Region 下 VPC 主路由表，可在路由表中增加路由策略，也可以[ 创建自定义路由表 ](https://cloud.tencent.com/document/product/215/36682)并增加路由策略。如下为增加路由策略的配置指导：
1. 登录 [路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)。
2. 选择 CDC 子网关联的路由表，单击路由表 ID 进入路由表详情界面。
3. 单击【新增路由】，当 CDC 子网需要访问 IDC 网段，可配置路由策略：目的端为 IDC 网段，下一跳类型为 CDC 本地网关，下一跳为具体 CDC 网关实例。
    ![](https://main.qcloudimg.com/raw/9cfa0556cdbdc801a30b6252bbdcd913.png)
4. 单击【创建】完成路由策略的配置，路由表详情如下图所示。
    ![](https://main.qcloudimg.com/raw/7c5e837eb481b2db93499dfdf7193e66.png)
		
### 步骤8：（可选）绑定弹性 IP
如果 CDC 子网中云服务器实例有公网通信的需求，需要先为云服务器绑定一个 CDC 本地弹性 IP，然后该弹性 IP 经由用户 IDC 本地交换机进行 NAT 转换为公网 IP，最终实现与公网的交互。
>!
>+ 仅支持 [标准账户](https://cloud.tencent.com/document/product/1199/49090#judge)
>+ 此处弹性 IP 为内网 IP，弹性 IP 地址池需由用户分配1个内网地址段（不能够和 IDC Underlay 其他已经使用网段重叠），且网段 CIDR 掩码要求大于等于/29。
>+ 如需进行公网访问，请在安全组和网络 ACL 中放通通信的公网 IP。
>+ 主 Region 资源不能绑定 CDC 本地弹性IP。
>+ 弹性 IP 暂不收取 IP 资源费和公网网络费用，且暂不支持监控。

1. 在本地专用集群控制台，选择专有集群弹性 IP。
2. 单击申请弹性 IP。
3. 单击【更多】>【绑定】，绑定 CDC 子网中的云服务器实例。
4. 其他操作：如不再需要弹性 IP，可在更多中执行解绑、释放等操作。

### 步骤9：（可选）为 CDC 内云服务器关联安全组
如需控制 CDC 内云服务器的进出流量，请为云服务器关联安全组，具体操作和普通子网中的云服务器无差别，请参见 [安全组](https://cloud.tencent.com/document/product/215/37888)。

### 步骤10：（可选）为 CDC 子网关联网络 ACL   
如需控制 CDC 子网的进出流量，请为 CDC 子网关联网络 ACL，具体操作与普通子网无差别，请参见 [网络 ACL](https://cloud.tencent.com/document/product/215/20160) 。



