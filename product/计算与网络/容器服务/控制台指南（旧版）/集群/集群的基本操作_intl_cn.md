## 创建集群
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **集群**，单击集群列表页的 【新建】。
![](//mc.qcloudimg.com/static/img/3e20524b9aaa91e937bcfd02270d69c7/image.png)
3. 设置集群的基本信息。
 - **集群名称**：要创建的集群的名称。不超过60个字符。
 - **计费模式**：提供包年包月和按量计费两种计费模式，详细对比请查看 [计费模式说明](/doc/product/213/2180)。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。可降低访问延迟，提高下载速度。
 - **可用区**：同地域内，内网互通；不同地域，内网不通。需要多个内网通信的用户须选择相同的地域。
 - **节点网络**：为集群内主机分配在节点网络地址范围内的 IP 地址。参阅 [容器及节点网络设置](/doc/product/457/9083)。
 - **容器网络**：为集群内容器分配在容器网络地址范围内的 IP 地址。参阅 [容器及节点网络设置](/doc/product/457/9083)。
 - **集群描述**：创建集群的相关信息。该信息将显示在 **集群信息** 页面。
![Alt text](https://mc.qcloudimg.com/static/img/d52ff827c724c74c38a595d646cb0ca6/image.png)

4. 选择机型 (支持系统盘为云盘的所有机型)。
 - **系列**：提供 **系列 1** 和 **系列 2** 。详细对比参看 [实例类型概述](/doc/product/213/7153#.E5.8F.AF.E7.94.A8.E5.AE.9E.E4.BE.8B.E7.B1.BB.E5.9E.8B2) 。
 - **机型**：机型选择方案参看 [确定云服务器配置方案](/doc/product/213/2764#.E7.A1.AE.E5.AE.9A.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8.E9.85.8D.E7.BD.AE.E6.96.B9.E6.A1.88)。
![Alt text](https://mc.qcloudimg.com/static/img/e13c49f3333a1c482bbc158ffaff9653/image.png) 

5. 填写云主机配置。
 - **系统盘**：固定为 50G 。
 - **数据盘**：步长 10G ，最高为 4000G 。
 - **公网宽带**：提供两种计费模式，详细对比参看 [购买网络带宽](/doc/product/213/509)。
 - **带宽**：勾选 **免费分配公网 IP** ，系统将免费分配公网 IP ，若不需要，请选择带宽值为 0 。
 - **登录方式**：提供三种对应登录方式。
  i. **设置密码**：请根据提示设置对应密码。
	ii.**立即关联密钥**：密钥对是通过一种算法生成的一对参数，是一种比常规密码更安全的登录云服务器的方式。详细参阅    [SSH 密钥](/doc/product/213/503) 。
	iii.**自动生成密码**：自动生成的密码将通过站内信发送给您。
 - **安全组**：安全组具有防火墙的功能，用于设置云主机 CVM 的网络访问控制。参阅  [容器服务安全组设置](/doc/product/457/9084) 。
 - **云主机数量**：选择服务器数量。
![Alt text](https://mc.qcloudimg.com/static/img/eff41bd979d9572c773dd2dca6230261/image.png)

6. 创建完成的集群将出现在集群列表中。
![Alt text](https://mc.qcloudimg.com/static/img/e8224896e742266489f3e4f56c27b95e/image.png)

## 添加云主机
1. 在集群列表页中，单击右侧 **扩展节点**。
![](//mc.qcloudimg.com/static/img/630fefe69ca2d2bedd779246417f8c70/image.png)

2. 设置添加云主机的所属 **网络**、**机型** 和 **配置信息**。
   允许将主机创建在同一地域下不同可用区下的不同子网中。
![Alt text](https://mc.qcloudimg.com/static/img/e701af9583d1bae708ffd4d748adb3c6/image.png)

3. 新添加的云主机将出现在 **ID/节点名** 列表中。
![](//mc.qcloudimg.com/static/img/1707fa09977298f255c293aa62b1cc10/image.png)

## 销毁云主机
1. 在集群列表页中点击某集群的 **ID/名称**，进入如下界面，选择需销毁的云主机，单击右侧 **移出** 。
![](//mc.qcloudimg.com/static/img/cbb99d53f194ec9121fe29d840081ab7/image.png)

2. 弹出提示页面，显示要移出的节点信息，单击【确定】删除节点。
![](//mc.qcloudimg.com/static/img/e9194e2947562271931fcc429e5788f8/image.png)

## 查看节点信息

1. 在集群列表中集群的 **ID/名称** 。
2. 单击【节点列表】来查看集群节点列表信息。
![](//mc.qcloudimg.com/static/img/ad5db6f3a9071235e614f856c3ef7083/image.png)

## 登录到节点
当前节点支持腾讯云云主机，如何登录请查看 [登录到云主机](https://cloud.tencent.com/doc/product/213/5436) 。

## 创建集群 Namespace

1. 在集群列表页中选择某集群的 **ID/名称**。
2. 单击 **Namespace 列表** ，单击【新建 Namespace 】。
![](//mc.qcloudimg.com/static/img/9e6973758fdeec1a6cf6b5a7d6614ab8/image.png)
3. 填写信息并单击【提交】。
![](//mc.qcloudimg.com/static/img/c40e34d6235239ae4ef6ab39fbe775f0/image.png)

## 删除集群 Namespace

1. 在集群列表页中选择某集群的 **ID/名称**。
2. 单击 **Namespace 列表** ，选择需删除的 Namespace ，单击右侧【删除】。
![](//mc.qcloudimg.com/static/img/f327962fd0918f7030d01fa8c6c03735/image.png)
3. 弹出提示页面，显示要删除的 Namespace 信息，单击【确定】删除 Namespace 。
![](//mc.qcloudimg.com/static/img/b03914a11e8c6bfa5703eafe8017625e/image.png)
>**注意**： 
>删除 Namespace 将销毁 Namespace 下的所有资源，销毁后所有数据将被清除且不可恢复，清除前将请提前备份数据。
