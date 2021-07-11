本文介绍在业务迁移过程中，有混访需求时的配置示例。


### 混访示例
假设用户基础网络业务使用如下产品：
+ CVM 客户端访问内网 CLB。
+ 内网 CLB 绑定了两台云服务器 CVM1 和 CVM2 作为后端服务器。
+ CVM1 和 CVM2 上部署了应用服务，应用服务会访问后端的云数据库服务 MySQL。

迁移过程中的业务混访要求：
+ 将基础网络的服务资源迁移至私有网络。
+ 要求私有网络客户端可以优先访问基础网络内网 CLB 服务。
+ 基础网络客户端在网络切换后还能继续访问业务一个月。

### 操作流程
<dx-steps>
-准备私有网络环境
-切换云数据库网络
-配置终端连接
-创建内网 CLB 并配置后端服务
-配置基础网络互通
-释放基础网络资源
</dx-steps>


### 迁移步骤
1. 参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515) 创建 VPC 网络。
2. 参见 [更换 MySQL 的网络](https://cloud.tencent.com/document/product/236/35671) 切换云数据库网络。
    >?云数据库在网络切换时连接不中断，且切换后同时保持原基础网络和私有网络 IP，可确保迁移过程中不停服。
    >
![](https://main.qcloudimg.com/raw/7f51057acb0d56e40351217bad32993c.png)
3. 配置 [终端连接 ]()服务，使得 VPC 内 CVM 客户端可以访问基础网络内网 CLB 服务。
     ![](https://main.qcloudimg.com/raw/cf97a576438ee48dc5ee9aac08c33d91.png)
4. 在私有网络内创建内网 CLB 以及后端 CVM，并配置相关业务。
   ![](https://main.qcloudimg.com/raw/458118bf68d8761883fff89a2a74cc2d.png)
5. 配置基础网络互通，使得基础网络内 CVM 客户端可以访问 VPC 内网 CLB，并验证私有网络业务提供是否正常。
    ![](https://main.qcloudimg.com/raw/05db818c7fad5d91bad7f31086b2a686.png)
6. 待私有网络业务验证正常后，私有网络 CVM 客户端开始访问私有网络内内网 CLB 业务，删除终端连接，继续保持基础网络互通，释放基础网络服务资源。
    ![](https://main.qcloudimg.com/raw/0abdb8141743e23985f3adc200e6da24.png)
    
 

