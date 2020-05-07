## 操作场景
腾讯云容器服务开源版（Tencent Kubernetes Engine Stack，TKE Stack）是面向私有化环境的开源容器编排引擎。您可参考本文安装并创建容器服务开源版控制台，并通过控制台创建和管理容器集群，在集群内快速、弹性地部署服务。

## 前提条件
已具备4个可用节点，详细配置见下表。本文均以操作系统为 CentOS 7.6 的腾讯云云服务器为例，节点创建请参见 [创建实例](https://tcloud-doc.isd.com/document/product/213/4855)。

<table>
<tr>
<th>集群描述</th> <th>节点/集群</th> <th>CPU 核数</th>
<th>内存</th> <th>系统盘</th> <th>数量</th>
</tr>
<tr>
<td rowspan=2>Global 集群</td><td>Installer 节点</td><td>1</td>
<td>2G</td><td>50G</td><td>1</td>
</tr>
<tr>
<td>Global 集群</td><td>8</td>
<td>16G</td><td>100G</td><td>1</td>
</tr>
<tr>
<td rowspan=2>业务集群</td><td>Master & etcd</td><td>4</td>
<td>8G</td><td>100G</td><td>1</td>
</tr>
<tr>
<td>Node</td><td>8</td>
<td>16G</td><td>100G</td><td>1</td>
</tr>
</table>


## 步骤1：控制台安装
1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录已准备好的 installer 节点。
2. 执行以下命令，下载 tke-installer 安装器至 `/data` 目录下。
```
version=vx.x.x && wget https://tke-release-1251707795.cos.ap-guangzhou.myqcloud.com/tke-installer-x86_64-$version.run{,.sha256} && sha256sum --check --status tke-installer-x86_64-$version.run.sha256 && chmod +x tke-installer-x86_64-$version.run
```
>?
>- 例如，使用 v1.2.3 版本时进行安装时，则对应命令为 `version=v1.2.3`。您可查看 TKEStack [Release](https://github.com/tkestack/tke/releases) 按需选择版本进行安装，建议安装最新版本。
>- tke-installer 约为5GB，包含安装所需资源，请确保节点具备足够空间。
>
3. 执行以下命令，安装 tke-installer，请耐心等待安装完毕。
```
./tke-installer-x86_64-$version.run
```
4. 访问返回信息中给出的如下路径，开始控制台安装。
```
http://xxx.xxx.xx.xx:8080/index.html
```
1. 在 TKEStack “基本设置”页面，参考以下提示进行设置，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/c157649f5b2cd04290db5a2b9264d6b7.png)
	- **用户名**：TKEStack 控制台管理员名称。
	- **密码**：TKEStack 控制台管理员密码。
	- **高可用设置**：请按需进行配置，本文以【不设置】为例。
		- **TKE提供**：在所有 master 节点额外安装 Keepalived 完成 VIP 的配置与连接。
		- **使用已有**：对接已配置好的外部负载均衡实例。
		- **不设置**：访问第一台 master 节点的 APIServer。
2. 在“集群设置”页面，参考以下提示进行设置，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/241e2b3a22ab3c3506410f9efbc15cb5.png)
主要参数信息如下：
	- **网卡名称**：集群节点使用的网卡，请根据实际环境进行填写，默认为 `eth0`。
	- **GPU类型**：请按需进行配置，本文以【不使用】为例。
		- **不使用**：不安装 Nvidia GPU 相关驱动。
		- **Virtual**：自动为集群安装 [GPUManager](https://github.com/tkestack/docs/blob/master/features/gpumanager.md) 扩展组件。
		- **Physical**：自动为集群安装 [Nvidia-k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)。
	- **容器网络**：将为集群内容器分配在容器网络地址范围内的 IP 地址，您可以自定义三大私有网段作为容器网络。根据您选择的集群内服务数量的上限，自动分配适当大小的 CIDR 段用于 Kubernetes service。根据您选择 Pod 数量上限/节点，自动为集群内每台服务器分配一个适当大小的网段用于该主机分配 Pod 的 IP 地址。
		- **CIDR**：集群内 Service、Pod 等资源所在网段。
		- **Pod数量上限/节点**：分配给每个 Node 的 CIDR 大小。
		- **Service数量上限/集群**：分配给 Sevice 的 CIDR 大小。
	- **master节点**：
	 - **访问地址**：Master 节点的内网 IP，**请配置至少8核16G内存及以上的机型**。
	 - **SSH端口**：请确保目标机器安全组开放22端口和 ICMP 协议，否则无法远程登录和 PING 通。
	- **高级设置**：请按需自定义 Global 集群的 Docker、kube-apiserver、kube-controller-manager、kube-scheduler、kubelet 运行参数。
3. 在“认证设置”页面，参考以下提示选择 TKEStack 控制台认证信息，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/c838f9b7580fe8d98fcd05de65aa7b8e.png)
	- **认证方式**：请按需选择，本文以【TKE提供】为例。
		- **TKE提供**：使用 TKE 自带的认证方式。
		- **OIDC**：使用 OIDC 认证方式，详情请参见 [OIDC](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens)。
4. 在“镜像仓库设置”页面，参考以下提示设置镜像仓库，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/1413a363eb8b50b0120c0aa13cef87c1.png)
	- **镜像仓库类型**：请按需设置，本文以【TKE提供】为例。
		- **TKE提供**：使用 TKE 自带的镜像仓库。
		- **第三方仓库**：已配置好的外部镜像仓库。若选择【第三方仓库】，TKEStack 将不会再安装镜像仓库，而是使用您提供的镜像仓库作为默认镜像仓库服务。
5. 在“业务设置”页面，选择是否开启 TKEStack 控制台业务模块，建议开启，并单击【下一步】。
6. 在“监控设置”页面，参考以下提示进行设置，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/7236c01103b3fe9b02bc971b10e652b4.png)
	- **监控存储类型**：请按需设置，本文以【TKE提供】为例。
		- **TKE提供**：使用 TKE 自带的 Influxdb 作为存储。
		- **外部InfluxDB**：对接外部的 Influxdb 作为存储。
		- **外部ES**：对接外部的 Elasticsearch 作为存储。
		- **不使用**：不使用监控。
7. 在“控制台设置”页面，选择是否开启控制台，建议开启，并单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/11cf5c00c6697e1693b7c446855d5f84.png)
	- **证书类型**：请按需选择，本文以【自签名证书】为例。
		- **自签名证书**：使用 TKE 带有的自签名证书。
		- **指定服务端证书**：填写已备案域名的服务器证书。
7. 在“配置预览”页面，确认 TKEStack 控制台所有配置正确后单击【安装】。
安装成功将返回如下信息：
![](https://main.qcloudimg.com/raw/83eee3292843650f62fae194d415671c.png)
8. 单击【查看指引】，根据弹出的“操作指引”窗口中的步骤配置域名，访问 TKEStack 控制台。

## 步骤2：新建独立集群

1. 登录 TKEStack 控制台，选择左侧导航栏中的【集群管理】。
2. 在“集群管理”列表页面，单击【新建独立集群】。
3. 在“新建独立集群”页面，参考以下提示设置集群基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/b333a31986c55cb4492d9f34cc6bdb25.png)
	- **集群名称**：支持中文，小于60字符。
	- **Kubernetes版本**：选择需要的 Kubernetes 版本。各版本特性对比请查看 [Supported Versions of the Kubernetes Documentation](https://kubernetes.io/docs/home/supported-doc-versions/)。
	- **网卡名称**： 最长63个字符，只能包含小写字母、数字及分隔符`-`，且必须以小写字母开头，数字或小写字母结尾。
	- **高可用类型**：请按需选择，本文以【不使用】为例。
		- **不使用**：访问第一台 master 节点的 APIServer。
		- **使用已有**：在用户自定义 VIP 情况下，VIP 后端需要绑定6443（kube-apiserver）端口。同时请确保该 VIP 有至少两个负载均衡后端（master），由于负载均衡自身路由问题，单负载均衡后端情况下存在集群不可用风险。
		- **TKE提供**：用户需要提供一个可用的 IP 地址，确保该 IP 和各 master 节点可以正常联通，TKE 会为集群部署 keepalived 并配置该 IP 为 VIP。
	- **GPU**：选择是否安装 GPU 相关依赖，本文以不安装为例。
	 - **pGPU**：自动为集群安装 [GPUManager](https://github.com/tkestack/docs/blob/master/features/gpumanager.md) 扩展组件。
	 - **vGPU**：自动为集群安装 [Nvidia-k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)。
	- **容器网络**：将为集群内容器分配在容器网络地址范围内的 IP 地址，您可以自定义三大私有网段作为容器网络。根据您选择的集群内服务数量的上限，自动分配适当大小的 CIDR 段用于 kubernetes service。根据您选择 Pod 数量上限/节点，自动为集群内每台云服务器分配一个适当大小的网段用于该主机分配 Pod 的 IP 地址。
		- **CIDR**： 集群内 Sevice、 Pod 等资源所在网段。
		- **Pod数量上限/节点**： 分配给每个 Node 的 CIDR 大小。
		- **Service数量上限/集群**：分配给 Sevice 的 CIDR 大小。
		- **目标机器**：Master&Etcd 节点的内网 IP，建议节点配置4核及以上机型。
		- **SSH端口**：请确保目标机器安全组放通22端口和 ICMP 协议，否则无法远程登录和 Ping 通。
		- **主机label**：设置主机 Label，可用于指定容器调度。
		- **认证方式**：
			- **密码认证**：目标机器密码。
			- **密钥认证**：
			   - **私钥**：目标机器私钥。
			   - **私钥密码**：目标机器私钥密码，可选填。
			- **GPU**：目标机器是否为 GPU 机型，使用 GPU 机器需提前安装驱动和 runtime。
				>?填写完目标机器信息后，请单击目标机器模块下方的【保存】。如【保存】为置灰不可选状态，请单击空白处，可选后再单击【保存】。
>
4. 单击【提交】即可在“集群管理”页面查看创建进度。

## （可选）步骤3：导入集群
1. 选择左侧导航栏中的【集群管理】，进入“集群管理”列表页面。
2. 在“集群管理”列表页面，单击【导入集群】。
3. 在“导入集群”页面，参考以下提示填写被导入集群的信息。如下图所示：
![](https://main.qcloudimg.com/raw/0ccb71d80959b790fc47a9b1f44ddecd.png)
 - **名称**：被导入集群的名称，最长60字符。
 - **API Server**： 输入要被导入集群的 API server 的 IP 和端口。
 - **CertFile**：输入被导入集群的 cert 文件内容。
 - **Token**：输入被导入集群创建时的 token 值。
4. 单击【提交】即可在“集群管理”页面查看进度。

## 步骤4：创建业务
1. 登录 TKEStack 控制台，选择左侧导航栏中的【业务管理】。
2. 在“业务管理”列表页面，单击【新建业务】。
3. 在“新建业务”页面，参考以下提示设置业务信息。如下图所示：
![](https://main.qcloudimg.com/raw/acdeddc50f4840da9fdccaea25f86569.png)
 - **业务名称**：自定义业务名称，不能超过63个字符。
 - **业务成员**：“用户管理”列表中已存在的用户。
 - **集群**：“集群管理”列表中已创建的集群。
 - **上级业务**：支持多级业务管理，可不选。
4. 单击【完成】即可创建业务。

## 步骤5：创建服务
>!由于 Master 节点的预设置，请参考 [添加节点](#addNode) 步骤，向集群中增加节点后再创建服务。
>
1. 选择左侧导航栏中的【集群管理】，进入“集群管理”列表页面。
2. 选择需创建服务的集群 ID，进入该集群 “Deployment” 页面并单击【新建】。
3. 在 “新建Workload” 页面，参考以下信息设置 Deployment 参数。如下图所示：
![](https://main.qcloudimg.com/raw/126e1db83a90ce4a7f560c6abb8991ca.png)
主要参数信息如下：
	- **工作负载名**：输入自定义名称，最长63个字符，只能包含小写字母、数字及分隔符 `-`，且必须以小写字母开头，数字或小写字母结尾。
	- **命名空间**：根据实际需求进行选择。
	- **类型**：选择【Deployment（可扩展的部署 Pod）】。
6. 如需指定容器挂载至指定路径时，单击【添加数据卷】，并根据以下信息设置。如下图所示：
![](https://main.qcloudimg.com/raw/2d971c8e615df80264849340ece5f64a.png)
	- **使用临时目录**：主机的临时目录，生命周期和 Pod 一致。
	- **使用主机路径**：主机的真实路径，可以重复使用，不会随 Pod 一起销毁。
	- **使用NFS盘**：挂载外部 NFS 到 Pod，用户需要指定相应 NFS 地址。例如，`127.0.0.1:/data`。
	- **使用已有PVC**：可选择在业务 Namespace 下的 PVC。
	- **使用ConfigMap**：可选择在业务 Namespace 下的 ConfigMap。
	- **使用Secret**：可选择在业务 Namespace 下的 Secret。
7. 根据实际需求，为 Deployment 的一个 Pod 设置一个或多个不同的容器。如下图所示：
![](https://main.qcloudimg.com/raw/a2b6b32ec9723bca7a53699719d63256.png)
主要参数信息如下：
 - **名称**：自定义名称，最长63个字符，只能包含小写字母、数字及分隔符 `-`，且不能以分隔符开头或结尾。
 - **镜像**：根据实际需求进行填写。
 - **镜像版本（Tag）**：根据实际需求进行填写。
 - **CPU/内存限制**：可根据 [Kubernetes 资源限制](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/) 进行设置 CPU 和内存的限制范围，提高业务的健壮性。
 - **显示高级设置**：可设置“工作目录”、“运行命令”、“运行参数”、“容器健康检查”和“特权级”等参数。
8. 参考以下信息设置实例数量。如下图所示：
![](https://main.qcloudimg.com/raw/43db545ddcdbd13752b18221550c269a.png)
 - **实例数量**：根据实际需求选择调节方式，设置实例数量。
	 - **手动调节**：直接设定实例个数。
	 - **自动调节**：根据设定的触发条件自动调节实例个数。目前支持根据 CPU、内存利用率和利用量出入带宽等调节实例个数。
 - **定时调节**：根据 Crontab 语法周期性设置实例个数。
9. 单击【显示高级设置】，并参考以下信息进行设置。如下图所示：
![](https://main.qcloudimg.com/raw/24e2289886c3187857a321b1e33a482d.png)
	- **imagePullSecrets**：镜像拉取密钥，用于拉取用户的私有镜像。
	- **节点调度策略**：根据配置的调度规则，将 Pod 调度到预期的节点。
	- **注释（Annotations）**：给 Pod 添加相应 Annotation，例如用户信息等。
	- **网络模式**：Pod 网络模式，根据以下信息进行设置：
	 - **OverLay（虚拟网络）**：基于 IPIP 和 Host Gateway 的 Overlay 网络方案。
	 - **FloatingIP（浮动 IP）**：支持容器、物理机和虚拟机在同一个扁平面中直接通过 IP 进行通信的 Underlay 网络方案。提供了 IP 漂移能力，支持 Pod 重启或迁移时 IP 不变。
	 - **NAT（端口映射）**：Kubernetes 原生 NAT 网络方案。
	 - **Host（主机网络）**：Kubernetes 原生 Host 网络方案。
10. 参考以下信息进行访问设置。如下图所示：
![](https://main.qcloudimg.com/raw/c56bb37f4510c9703ff87e8930647d05.png)
	- **Service**：勾选【启用】，配置负载端口访问。
	- **服务访问方式**：
	 - **仅在集群内访问**：将提供一个可以被集群内其他服务或容器访问的入口，支持 TCP/UDP 协议。数据库类服务如 MySQL 可选择此方式，来保证服务网络隔离性。
	 - **主机端口访问**：提供一个主机端口映射到容器的访问方式，支持 TCP/UDP 协议，可用于业务定制上层负载均衡转发到 Node。
	 - **Headless Service**：解析域名时返回相应 Pod IP 而不是 Cluster IP。**创建完成后不支持变更访问方式**。
	- **端口映射**：输入负载要暴露的端口并指定通信协议类型。
11. 单击【创建Workload】即可完成创建。
当运行数量=期望数量时，即表示 Deployment 下的所有 Pod 已创建完成。如下图所示：
![](https://main.qcloudimg.com/raw/7677b741d306407c74c082fa43c6c697.png)


## 相关操作
### 添加节点<span id="addNode"></span>
1. 登录 TKEStack 控制台，选择左侧导航栏中的【集群管理】。
2. 选择需创建服务的集群 ID，进入该集群 “Deployment” 页面。
3. 选择左侧菜单栏中的【节点管理】>【节点】，进入“节点列表”页面。
4. 在“节点列表”页面，选择【添加节点】。如下图所示：
![](https://main.qcloudimg.com/raw/922b1f24f8dba95c03105f0af32a0f58.png)
5. 在“添加节点页面”，参考以下信息进行设置。
	- **目标机器**：Master&Etcd 节点的内网 IP，建议节点配置4核及以上机型。
	- **SSH端口**：请确保目标机器安全组放通22端口和 ICMP 协议，否则无法远程登录和 Ping 通。
	- **主机label**：设置主机 Label，可用于指定容器调度。
	- **认证方式**：
		- **密码认证**：目标机器密码。
		- **密钥认证**：
			- **私钥**：目标机器私钥。
			- **私钥密码**：目标机器私钥密码，可选填。
	- **GPU**：目标机器是否为 GPU 机型，使用 GPU 机器需提前安装驱动和 runtime。
6. 单击【提交】即可在“节点列表”页面查看进度。
如下图所示，则为添加成功：
![](https://main.qcloudimg.com/raw/ad3bcb295cc717980b9aecfa86914985.png)

### 删除服务
1. 登录 TKEStack 控制台，选择左侧导航栏中的【集群管理】。
2. 在“集群管理”页面，选择需删除服务的集群 ID。
3. 在 “Deployment” 页面，选择左侧菜单栏中的【服务】>【Service】。
4. 在 “Service” 页面，选择需删除服务所在行右侧的【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/3d61c25bb4107ca33721972738ffcf80.png)
5. 在弹出的“删除资源”窗口中，单击【确定】即可。


### 删除集群
1. 选择左侧导航栏中的【集群管理】，进入“集群管理”页面。
2. 在“集群管理”页面中，选择需删除集群所在行右侧的【删除】。如下图所示：
![](https://main.qcloudimg.com/raw/44e326f84ad6ff929d10bf219905f492.png)
3. 在弹出的“删除集群”窗口中，单击【确定】即可。


