## 简介

本文介绍如何在不同 VPC 下访问云 HDFS（Cloud HDFS，CHDFS）的过程。

- **权限组**是 CHDFS 提供的访问控制白名单，用户可以自行创建权限组，以此实现对 CHDFS 的权限管理，权限组需要绑定且只能绑定一个 VPC 网络。
- 创建**挂载点**时候，需要将权限组绑定挂载点。

一个挂载点可以同时被多个权限组绑定，因此我们可以利用不同 VPC 的权限组绑定同一个挂载点来实现跨 VPC 访问 CHDFS。

本文以不同 VPC 下的 EMR 集群访问 CHDFS 为例。

## 前提条件

需要账户中已有 CHDFS 文件系统和EMR集群，并且 EMR 集群已配置好 CHDFS 环境，可参考下列创建指南。

- 已创建文件系统，详情请参考 [创建 CHDFS](https://cloud.tencent.com/document/product/1105/37234)。
- 已创建 [挂载点](https://cloud.tencent.com/document/product/1105/37237)。
- EMR 集群已配置 [CHDFS 环境](https://cloud.tencent.com/document/product/1105/36368)。

## 操作步骤

<span id="step1"></span>
### 步骤1：创建权限组和权限规则

1. 登录 [CHDFS 控制台](https://console.cloud.tencent.com/chdfs)。
2. 在左侧导航栏中，单击**权限组**，选择地域（例如广州），单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/806b6656ea1acc5add5d4a62a97a2160.jpg)                     
3. 在弹出的窗口中，输入名称，依据 EMR 集群所属 VPC，设置 VPC 网络类型和 VPC 网络名称。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5d11637c387b17091fc94f72d3b5e661.png" style="width: 50%;" />        
4. 选择创建好的权限组，单击**添加规则**，在授权地址中填入 EMR 集群所在的网段，配置访问模式和优先级。
![](https://qcloudimg.tencent-cloud.cn/raw/751229fe21486166b6677f64735c9631.jpg)
5. 重复执行步骤2 - 步骤4，配置另一个 VPC 的权限组。
![](https://qcloudimg.tencent-cloud.cn/raw/d9efa28efe51af9dc7717c7d45f5cdcc.jpg)        

### 步骤2：挂载点绑定权限组

1. 选择创建好的挂载点，单击**绑定权限组**。
![img](https://qcloudimg.tencent-cloud.cn/raw/7ac9e29bc08fef4c32f3572356141f58.jpg)        
2. 在弹出的窗口中，绑定 [步骤1](#step1) 创建的两个不同 VPC 的权限组。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9e9e637e09eed3c49cb0772a80671d2f.jpg" alt="img" style="zoom: 33%;" />        

### 步骤3：访问 CHDFS

1. 在配置好权限组和 [CHDFS 环境](https://cloud.tencent.com/document/product/1105/36368) 的 EMR 集群机器中，执行 `hadoop fs -ls` 命令，查看到文件列表，即表示挂载成功。   
![img](https://qcloudimg.tencent-cloud.cn/raw/4a3b1895729727c8ee91ad8381f3563b.jpg)        
2. 在另一台不同权限组的 EMR 集群机器中，重复执行步骤1，查看到文件列表，即表示挂载成功。                
![img](https://qcloudimg.tencent-cloud.cn/raw/034742dca0b3191000a836470c3bc328.jpg)        
使用一台权限组未添加权限规则的机器进行相同操作，挂载失败 ，显示**“*Permisson denied: No access rules matched*”** 错误。   
![img](https://qcloudimg.tencent-cloud.cn/raw/462d9e1d7234c61074214699eaeff5ed.jpg)        

