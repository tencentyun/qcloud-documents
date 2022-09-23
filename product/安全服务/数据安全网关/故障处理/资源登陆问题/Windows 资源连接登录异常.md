## 现象描述
Windows 资源访问异常，提示无法连接到远程计算机，如下图所示：
![](https://main.qcloudimg.com/raw/614b95cb6726b22b6a1e8b89a575fe30.png)
![](https://qcloudimg.tencent-cloud.cn/raw/390d32a0deb9ec134519d6c349b9b483.png)

## 可能原因
SaaS 型堡垒机到资源 CVM 网络或者端口不通，导致堡垒机无法代理访问资源。

## 解决思路
1. 如果 SaaS 型堡垒机和资源不在同一个 VPC 则无法访问，需要购买多个服务或者打通 VPC 网络。
2. 若资源存在安全组限制，则堡垒机无法访问目标资源。需要放通资源安全组限制，允许堡垒机访问资源的远程协议端口。



## 处理步骤
#### 不在同一个 VPC 
1. 登录 [ SaaS 型堡垒机控制台](https://console.cloud.tencent.com/bh)，在左侧导航选择**开通服务**，进入开通服务页面。
2. 在开通服务页面，单击**购买**，购买多个服务。
>?也可使用私有网络打通 VPC 网络，详情请参见[ 连接其它 VPC](https://cloud.tencent.com/document/product/215/36698)。
>
![](https://main.qcloudimg.com/raw/69fcb15684fb73ddfa46c9e3aa5cbb62.png)

#### 安全组限制
1. 登录 [ SaaS 型堡垒机控制台](https://console.cloud.tencent.com/bh)，在左侧导航选择**开通服务**，进入开通服务页面。
2. 在开通服务页面，查看无法访问目标资源的堡垒机的内外网 IP，并记录内网 IP，用于加入到 [步骤6](#step6) 的入站规则中。
![](https://main.qcloudimg.com/raw/cb5b6e447b1c1c8f810f80d3ee97382f.png)
3. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，单击实例与镜像菜单下的**实例**，进入实例页面。
4. 在实例页面，单击需要绑定安全组的 CVM 实例 **ID/实例名** > **安全组** ，进入该实例详情的安全组页面。
![](https://main.qcloudimg.com/raw/df81eea452d7ebc60dfe82d1c4d91d2d.png)
5. 在安全组页面，单击**编辑规则**，进入私有网络的安全组规则的入站规则页面。
![](https://main.qcloudimg.com/raw/40254a33b9b9384566c93f229f8c4147.png)
6. 在入站规则页面，可增加或修改入站规则，允许堡垒机内网 IP 访问资源远程桌面端口。[](id:step6)
>?
>- 来源：根据实际情况，精确放通 IP。
>- 端口协议：输入远程桌端口。
> 
 - 增加：单击**添加规则**，配置相关参数，单击**完成**。
 ![](https://main.qcloudimg.com/raw/635c96a353d9b150250705474343a997.png)
 - 修改：单击**编辑**，修改来源 IP 和协议端口，单击**保存**。
 ![](https://main.qcloudimg.com/raw/a599198f286bea9c4243e8b6caee098a.png)
7. 在堡垒机的 [主机页面](https://console.cloud.tencent.com/bh/host)，单击**主机信息**，检查资源端口号配置，确认为在使用远程桌面端口，如果不正确请根据实际情况进行修改。
![](https://main.qcloudimg.com/raw/3ba9a08b77fc4378be3c414fbcd8c2cb.png)
