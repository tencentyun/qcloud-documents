当 NAT 网关绑定多个 EIP 时，可以通过[ 创建 SNAT 规则](#cjgz)，为不同业务分组的云服务器指定访问公网的 EIP。

例如，当 NAT 网关绑定了 EIP1、EIP2、EIP3、EIP4 等多个 EIP 时，则系统会在绑定的所有 EIP 中自动做负载均衡访问公网。如果将 EIP1、EIP2、EIP3 加入 SNAT 地址池，则系统使用 SNAT 地址池中的 EIP 访问公网，且自动在 SNAT 地址池中的 EIP 做负载均衡，没有配置 SNAT 规则的云服务器可以通过 NAT 上绑定的所有 EIP 访问公网。
>?
>- 当 CVM 实例负载激增时，1个 EIP 可能无法支撑巨大的访问量，可选择配置多个 EIP 分担访问量。
>- NAT 网关支持将同一个 EIP 同时用于配置 SNAT 规则和端口转发规则，端口转发规则的详细信息请参考[ 管理端口转发规则](https://cloud.tencent.com/document/product/552/53621)。
>


本文介绍如何创建和管理 SNAT 规则。

## SNAT 规则限制
- 当 NAT 网关解关联 EIP 时，若该 EIP 为 SNAT 规则的唯一 EIP，则同时删除此条 SNAT 规则；若该 EIP 为此 SNAT 规则的非唯一 EIP，则 SNAT 规则中删除此 EIP。
- SNAT 规则中使用的子网不存在时，联动删除该 SNAT 规则。
- SNAT 规则中使用的云服务器不存在时，联动从 SNAT 规则中删除该云服务器；若为 SNAT 规则中最后一台云服务器，则联动删除 SNAT 规则。
- 由于标准协议限制，对于同一协议/目的 IP/目的端口，连接数上限 = 绑定的 EIP 数 * 55000，如需提升连接数，请新增绑定 EIP 或调整目的 IP/端口。


## 前提条件
创建 SNAT 规则前，请确保子网所在的路由表需指向对应的 NAT 网关，详细操作请参见 [配置指向 NAT 网关的路由](https://cloud.tencent.com/document/product/552/19697)。


## 创建 SNAT 规则[](id:cjgz)
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 在列表中单击网关 ID 进入详情页。
3. 选择**SNAT 规则**标签页 ，进入 SNAT 规则管理界面。
4. 单击**新建**，弹出**新建 SNAT 规则**对话框。
5. 设置 SNAT 规则。
   + 源网段粒度：支持子网和云服务器粒度 。
     + 子网：当选择子网时，子网所关联的路由表必须指向该 NAT 网关，该子网内的云服务器均按照 SNAT 规则访问外网。
     + 云服务器：当选择云服务器时，云服务器所在子网所关联的路由表必须指向该 NAT 网关，只有选定的云服务器按照 SNAT 规则访问外网，没有配置 SNAT 规则的云服务器可以通过 NAT 上绑定的所有 EIP 访问公网。
   + 所属子网：选择子网，或云服务器所在子网。
   + 云服务器：仅当**源网段粒度**为**云服务器**时，需要指定云服务器，可添加多个云服务器。
   + 公网 IP：指定访问公网的弹性公网IP。
   + 描述：自定义描述信息，最多支持60个字符。
![](https://qcloudimg.tencent-cloud.cn/raw/5881eaa1ef888dc9db4b2b0c4a4b8d12.png)
6.  完成 SNAT 规则的参数设置后，单击**提交**。    

## 编辑 SNAT 规则
>?修改存量 SNAT 规则中的公网 IP，可能导致原有业务连接中断，重连后即可恢复，请谨慎操作。
>
1. 在 SNAT 规则标签页，单击 SNAT 规则条目右侧的**编辑**，进入编辑对话框。
![](https://qcloudimg.tencent-cloud.cn/raw/bc129e3317b4ae9b7b1c3ac261c1e0cb.png)
2. 修改 SNAT 规则中的公网IP地址或描述，然后单击**提交**完成修改。
3. 单击 SNAT 规则中的描述信息旁的编辑图标，直接进行修改。
    ![](https://main.qcloudimg.com/raw/64525964961cc447f448819213b0ff8e.png)

## 查询 SNAT 规则
1. 在 SNAT 规则标签页右上方的搜索框中，单击选择如下筛选条件，并在输入框中填写相应的参数值。
![](https://qcloudimg.tencent-cloud.cn/raw/9af33fd59cdb99eddfad12beeb15385a.png)
2. 单击搜索图标进行快速检索。
![](https://qcloudimg.tencent-cloud.cn/raw/f63bd2cb193115f281f320bb7c74ce1a.png)
3. 单击子网/云服务器 ID，可跳转到相应资源详情界面。


## 删除 SNAT 规则
如果您不需要为云服务器访问外网指定 EIP，可删除 SNAT 规则。
- **单条删除**
 1. 在 SNAT 规则标签页，单击 SNAT 规则条目右侧的**删除**。
 2. 单击**确认**，删除该条 SNAT 规则。
![](https://qcloudimg.tencent-cloud.cn/raw/0409fe10968ba576de4667821e7237b6.png)
- **批量删除**
 1. 在 SNAT 规则标签页，勾选多条 SNAT 规则，单击上方的**删除**。
![](https://qcloudimg.tencent-cloud.cn/raw/f75f3d94ba4e6b109625faf231ecea6c.png)
 2. 在弹出的提示框中，单击**删除**，完成批量删除。
![](https://qcloudimg.tencent-cloud.cn/raw/40b3f697fce8d6fad09be8b4f756bd50.png)
