## 现象描述
同一 VPC 内的两台云服务器无法 ping 通。

## 可能原因
+ 云服务器安全组规则未放通。
+ 云服务器所在子网的网络 ACL 规则未放通。
+ 云服务器内存在容器路由。


## 处理步骤

### 检查云服务器实例关联的安全组规则
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 单击云服务器实例 ID，进入实例详情界面。
3. 单击**安全组**页签，查看是否有放通 ICMP 协议，及对应来源 IP/目的 IP 的出入站安全组规则。
 + 如无对应协议规则，或规则为**拒绝**，请单击**编辑**修改对应协议的安全组规则，然后尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查。
 + 如安全组出入站规则均正确，请继续排查。
	**异常示例**：
	![](https://qcloudimg.tencent-cloud.cn/raw/2c7a3bf9c7f88d6f1f96f56ffcf62fc2.png)
	**正常示例**：
	![](https://qcloudimg.tencent-cloud.cn/raw/d591b7590bdeb9c88cd290dd1b3f5bdc.png)
	
### 检查子网关联的网络 ACL 规则
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 单击云服务器实例 ID，进入实例详情界面。
3. 单击**ACL规则**页签，查看子网是否绑定了网络 ACL，且 ACL 出入站规则中，是否有拒绝 ICMP 协议，及来源/目标 IP 的规则。
  + 如绑定了 ACL，且 ACL 中 ICMP 规则为**拒绝**，或 ACL 中无 ICMP 规则，请单击 ACL ID，进入 ACL 界面，将对应协议，及来源/目标 IP 的规则修改为**允许**，并将该条规则移到第一条，确保规则优先匹配，然后尝试 ping 测试问题是否解决，解决则结束，未解决则继续排查。
  +  如未绑定 ACL，或 ACL 规则已允许相应协议及 IP，请继续排查。
   ![](https://qcloudimg.tencent-cloud.cn/raw/dff28d3b2825b35655084d21c7f03bd7.png)
	 
### 检查云服务器内是否存在容器路由
1. 进入[云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=16)，单击云服务器右侧的**登录**，按照界面提示输入密码或密钥，以 [标准方式登录云服务器](https://cloud.tencent.com/document/product/213/5436)，并执行 route 查看系统内部路由表。
    ![](https://qcloudimg.tencent-cloud.cn/raw/3b11c3b313ad0076f3c0d3c80d139701.png)
2. 查看系统内是否存在 docker 容器网段路由，且与被访问的云服务器所在子网网段相同。
  + 如存在容器网段路由，且容器网段与子网网段相同，容器网段路由与 VPC 系统内路由冲突，也可能导致此问题，可删除对应子网。
  + 如不存在，请记录问题，并联系 [售后在线支持](https://cloud.tencent.com/online-service)。
