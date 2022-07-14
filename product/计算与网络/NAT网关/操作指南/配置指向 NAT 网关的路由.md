创建 NAT 网关后，需要配置路由规则，将子网流量指向 NAT 网关。
本文提供两种操作方式，您可以根据自己的需要选择任一操作方式。
- 方式一：从 **NAT 网关**控制台开始操作
- 方式二：从**路由表**控制台开始操作

## 操作步骤

### 方式一：从 NAT 网关控制台开始操作
1. 登录 [NAT 控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)。
2. 在 NAT 实例列表中，单击目标 NAT 实例所在行的私有网络 ID。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a14fb15efb8f54104eabdb8c88918ae8.png)
3. 在私有网络详细信息中，单击**子网**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/f80001ed29b7c8290fa67b70a434fbc9.png)
4. 在子网列表中，选择需要访问公网的子网所在行的路由表 ID。
5. 在路由表基本信息页面，单击**+新增路由策略**。
    ![](https://qcloudimg.tencent-cloud.cn/raw/ed02207b047f3164b950f73370ab9931.png)
6. 在**新增路由**弹框中，输入目的端（目的公网对应的 IP 地址段）、下一跳类型选择 **NAT 网关**、下一跳选择已创建的 NAT 网关 ID。
    ![](https://qcloudimg.tencent-cloud.cn/raw/df0ab60fa2824d4a8d61a7fe02585339.png)
7. 单击**创建**完成以上配置后，关联此路由表的子网内的云服务器访问公网的流量将指向该 NAT 网关。
   
 

### 方式二：从路由表控制台开始操作
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)，在左侧目录中单击**路由表**。
2. 在路由表列表中，单击需要访问公网的子网所关联的路由表 ID 进入详情页。
![](https://main.qcloudimg.com/raw/d9149a32b451867c5ccd4c171f58d963.png)
3. 在路由表基本信息页面，单击**+新增路由策略**。
4. 在**新增路由**弹框中，输入目的端（目的公网对应的 IP 地址段）、下一跳类型选择 **NAT 网关**、下一跳选择已创建的 NAT 网关 ID。
  ![](https://qcloudimg.tencent-cloud.cn/raw/63add142cdb650a1de47395439715af3.png)
5. 单击**创建**完成以上配置后，关联此路由表的子网内的云服务器访问公网的流量将指向该 NAT 网关。
