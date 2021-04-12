本文指导您在本地数据中心完成 CDC 专用集群部署，确保计算、存储等资源可用后，如何快速配置 CDC 网络并启用 CDC 资源实例进行业务通信。

## 前提条件
[已在本地数据中心机房配置了 CDC 专用集群](https://cloud.tencent.com/document/product/1346/49917)

## 操作步骤

### 步骤1：创建 CDC 子网
1. 登录 CDC 集群控制台。
2. 选择 CDC 子网，单击创建 CDC 子网。
3. 在弹出的对话框中，选择您本地机房已部署的 CDC 集群，以及集群关联的 VPC，系统自动关联出可用区，路由表默认是 VPC 主路由表，如果创建多个子网请单击【添加子网】。
	![](https://main.qcloudimg.com/raw/d81e2e02af5afc641fd9024ca078fdc0.png)
4. 在配置完 CDC 子网后，单击【创建】完成操作，子网创建后，即可在子网中创建云服务器资源。
	![](https://main.qcloudimg.com/raw/8fd183549092a70809252c4bd29ed6e7.png)
5. （可选）如需更换路由表，可单击【更多】>【更换路由表】，可为 CDC 子网更换路由表。
	![](https://main.qcloudimg.com/raw/a039849dd23858734727d868bc702c4a.png)

### 步骤2：创建 CDC 本地网关
1. 单击 CDC 集群控制台下的 CDC 本地网关。
2. 在弹出的网关创建界面，填写网关名称，选择所属 CDC 集群和所属 VPC 网络。
 ![](https://main.qcloudimg.com/raw/81f47315a7347d62df99652c8e22ff22.png)
3. 单击【确定】，CDC 本地网关展示在列表中，目前1个 CDC 集群仅支持创建1个 CDC 本地网关。
   ![](https://main.qcloudimg.com/raw/b56d0a48e0d13dc6d9df87b3cbce3f27.png)

### 步骤3：创建路由策略
当 CDC 子网需要访问 IDC 网段时，可配置目标到本地网关的路由策略。CDC 默认关联主 Region 下 VPC 主路由表，可在路由表中增加路由策略，也可以[ 创建自定义路由表 ](https://cloud.tencent.com/document/product/215/36682)并增加路由策略。
1. 登录 [路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)。
2. 选择 CDC 子网关联路由表，单击路由表 ID 进入路由表详情界面。
3. 单击【新增路由】，当 CDC 子网访问 IDC 网段，可配置目的端为 IDC 网段，下一跳类型为 CDC 本地网关，下一跳为具体 CDC 网关实例。
  ![](https://main.qcloudimg.com/raw/9cfa0556cdbdc801a30b6252bbdcd913.png)
4. 单击【创建】完成路由策略的配置，路由表详情如下图所示。
    ![](https://main.qcloudimg.com/raw/7c5e837eb481b2db93499dfdf7193e66.png)
		
### 步骤4：（可选）绑定弹性IP
如果 CDC 子网中云服务器实例有访问公网的需求，可以为云服务器绑定 CDC 本地弹性 IP，该 IP 为内网 IP。
访问公网原理为：CDC 内云服务器通过弹性 IP 访问公网时，需要经过两次 NAT 转换，即当数据包出 CDC 时，由 CDC 内设备做第一次 NAT 转换为内网弹性 IP 地址，当数据包到达用户 IDC 时，由用户 IDC 内设备再做一次 NAT 转换为公网地址，最终云服务器通过该公网 IP 地址与公网通信。
>?
+ 仅支持 [标准账户](https://cloud.tencent.com/document/product/1199/49090#judge)
+ 主 Region 资源不能绑定 CDC 本地弹性IP
+ 暂不收取IP资源费和公网网络费用
+ 专有集群弹性 IP 暂不支持监控

1. 在 CDC 集群控制台，选择专有集群弹性 IP。
2. 单击申请弹性 IP。
3. 单击【更多】>【绑定】，绑定 CDC 子网中的云服务器实例。
4. 其他操作：如不再需要弹性 IP，可在更多中执行解绑、释放等操作。

### 步骤5：（可选）公网 CLB
目前 CDC 支持公网四、七层 CLB 功能，如有需要可在 CDC 本地配置公网 CLB。
>?
>+ 仅支持[ 标准账户](https://cloud.tencent.com/document/product/1199/49090#judge)
>+ 仅支持负载均衡（原“应用型负载均衡”），不支持传统型负载均衡
>+ CDC 内的本地公网CLB仅支持绑定同 CDC 集群内的云服务器，不能绑定同 VPC 内非 CDC 子网的云服务器
>+ CDC 的 CLB 暂不收费

1. 在 CDC 集群控制台下，选择创建 CLB。
2. 在创建界面，选择 CDC 所属 VPC，勾选本地专用集群，在 CDC 集群下拉框中，选择 CDC 集群。
    ![](https://main.qcloudimg.com/raw/9fadea3eed2cd1b1c1eda0f67f7c3177.png)
3. 配置完 CLB 参数后，单击立即购买完成 CLB 创建。
4. 单击配置监听器，新建监听器、配置监听器规则，并绑定后端云服务器实例。


### 步骤6：（可选）其他操作   
1. CDC 子网及子网中的云资源支持网络 ACL 和安全组，规则使用及配置与普通子网及云服务器无差异，具体操作请参考 [网络 ACL](https://cloud.tencent.com/document/product/215/20160) 和 [安全组](https://cloud.tencent.com/document/product/215/37888)。
2. CDC 支持网络流日志，具体请参考 [网络流日志](https://cloud.tencent.com/document/product/682/18935)。

## 测试连接
可通过如下方式测试网络连接：
1. 测试从用户 IDC 网络到 CDC 子网实例的连接，登录 IDC 中的服务器，并 ping CDC 子网中云服务器的 IP 地址。
2. 测试从 CDC 子网中实例到用户 IDC 网络的连接，登录 CDC 子网中的云服务器，并 ping 用户 IDC 网络中的服务器 IP。
3. 测试主 Region 公有云 VPC 中实例与 CDC 子网实例的连接，登录 CDC 子网中的云服务器，并 ping 主 Region VPC 中其他子网中某云服务器内网 IP。
有数据返回则表示已联通。
