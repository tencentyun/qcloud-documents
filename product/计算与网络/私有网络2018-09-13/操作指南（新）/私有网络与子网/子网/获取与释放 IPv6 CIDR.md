当您的私有网络有 IPv6 业务通信需求时，您需要先为网络环境配置 IPv6 网段，然后才能在 VPC 内的资源分配 IPv6 地址，从而进行 IPv6 通信业务。大致顺序为：获取 VPC IPv6 CIDR > 获取子网 IPv6 CIDR  > 云资源实例分配 IPv6 地址。本章节为您介绍子网 IPv6 CIDR 的获取与释放。
>?目前 IPv6/IPv4 双栈 VPC 功能处于内测中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/a9k0gialqhj)。
>
## 获取 IPv6 CIDR

### 前提条件
子网所属的 [VPC 已获取 IPv6 CIDR](https://cloud.tencent.com/document/product/215/53425#31)。

### 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 在左侧目录中单击【子网】，在子网列表上方，选择【地域】和【私有网络】，将会展示所属地域和私有网络下的所有子网信息。
3. 选择一个子网，单击操作列的【更多】>【获取 IPv6 CIDR】。 
![](https://main.qcloudimg.com/raw/2284268112758fe68b367cf13bf11e14.png)
4. 填写如下 IP 段，范围为0～255，请确认不能与其他子网的 IPv6 CIDR 网段重叠，单击【确认】系统将为该子网分配1个`/64`的 IPv6 CIDR。
    ![](https://main.qcloudimg.com/raw/c6702e17f4ad4cd172af2ef95dad93cd.png)

### 相关文档
[搭建 IPv6 私有网络](https://cloud.tencent.com/document/product/215/47557)

## 释放IPv6 CIDR
1.  登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2.  在左侧目录中单击【子网】，在子网列表上方，选择【地域】和【私有网络】，将会展示所属地域和私有网络下的所有子网信息。
3. 选择一个已获取到 IPv6 CIDR 的子网，【更多】>【释放 IPv6 CIDR】。
![](https://main.qcloudimg.com/raw/b1bcc6be3cda4c578053fd31cbc6d74a.png)
4. 在弹出的确认框中，单击【确定】，系统将回收该子网的 IPv6 CIDR。
![](https://main.qcloudimg.com/raw/99dd050f1e03d4a2bad75a9d14980aab.png)

