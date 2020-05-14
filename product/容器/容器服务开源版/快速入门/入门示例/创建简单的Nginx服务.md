## 操作场景
本文档介绍如何快速创建一个基于容器服务开源版（TKE Stack）集群内的 Nginx 服务。


## 前提条件
- 已部署 TKEStack 控制台，详情请参见 [控制台安装](https://cloud.tencent.com/document/product/1205/43828#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AE.89.E8.A3.85)。
- 已创建集群，详情请参见 [新建独立集群](https://cloud.tencent.com/document/product/1205/43828#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E6.96.B0.E5.BB.BA.E7.8B.AC.E7.AB.8B.E9.9B.86.E7.BE.A4)。
- 由于 Master 节点的预设置，请参考 [添加节点](https://cloud.tencent.com/document/product/1205/43828#addNode) 步骤，向集群中增加节点后再创建服务。

## 操作步骤

### 创建 Nginx 服务

1. 登录 TKEStack 控制台，选择左侧导航栏中的【集群管理】。
2. 在“集群管理”列表页面，选择需创建服务的集群 ID。
3. 在集群的 “Deployment” 页面，单击【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/3199122e5925c79e020c8429488a0732.png)
4. 在 “新建Workload” 页面，根据以下提示，设置工作负载基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/cb89bcbd9bbcd5d11f584a485eb60a0b.png)
 - **工作负载名**：输入要创建的工作负载的名称，本文以 nginx 为例。
 - **描述**：填写工作负载的相关信息。
 - **标签**：key = value 键值对，本例中标签默认值为 k8s-app = **nginx**。
 - **命名空间**：根据实际需求进行选择。
 - **类型**：根据实际需求进行选择。
 - **数据卷**：根据实需求设置工作负载的挂载卷。
5. 在“实例内容器”中，参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/fe2ac9a5c76e55401395db600d43306f.png)
主要参数信息如下：
	- **名称**：输入实例内容器名称，本文以 nginx 为例。
	- **镜像**：输入镜像地址，本文以 nginx 为例。
	- **镜像版本（Tag）**：使用的镜像版本，本为以 `latest` 为例。
	其余参数请保持默认设置。
6. 在“实例数量”中，参考以下信息设置服务的实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/24fd3b152d94f5ca2f7170dc06e3eeda.png)
 - **手动调节**：设定实例数量，本文实例数量设置为1。可单击`+`或`-`控制实例数量。
 - **自动调节**：满足任一设定条件，则自动调节实例（pod）数目。
7. 根据以下提示，进行工作负载的访问设置。如下图所示：   
![](https://main.qcloudimg.com/raw/afda7a549dd4ebf554c9acbb5c9ea6a8.png)
 - **Service**：勾选“启用”。
 - **服务访问方式**：选择“主机端口访问”。
 - **端口映射**：选择 TCP 协议，容器端口和服务端口都设置为80 ，主机端口设置为30000。
 >!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。
 >
8. 单击【创建Workload】，完成 Nginx 服务的创建。


### 访问 Nginx 服务

可通过以下两种方式访问 Nginx 服务。

#### 通过主机节点端口访问 Nginx 服务

1. 单击左侧导航栏中【集群管理】，进入该集群的 “Deployment” 页面。
2. 选择左侧菜单栏中的【服务】>【Service】，进入 “Service” 页面。
3. 在 “Service” 页面，可查看 Nginx Service 正在运行，如下图所示：
![](https://main.qcloudimg.com/raw/549822715d1cd7eb35619570fadd9f87.png)
4. 在浏览器地址栏访问集群任意节点 IP 的30000端口即可访问服务。

#### 通过服务名称访问 Nginx 服务

集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 nginx 服务
服务创建成功，访问服务时直接进入 Nginx 服务器的默认欢迎页。如下图所示：
![](https://main.qcloudimg.com/raw/c2aa05dcabba7b9c8a9a49e258e65111.png)
