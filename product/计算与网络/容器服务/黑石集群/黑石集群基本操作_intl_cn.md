## 黑石集群基本操作
### 创建黑石集群
前置条件： 已经至少2台可用黑石物理服务器。若无可用黑石物理服务器请前往[黑石物理服务器控制台](https://console.qcloud.com/cpm)新建。

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **黑石集群**，单击集群列表页的 【新建】。
![][1]
3. 设置集群的基本信息。

 - **集群名称**：要创建的集群的名称。不超过60个字符。
 - **集群版本**：选择创建的Kubernetes版本。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。可降低访问延迟，提高下载速度。
 - **可用区**：同地域内，内网互通；不同地域，内网不通。需要多个内网通信的用户须选择相同的地域。
 - **集群网络**：选择集群所在VPC网络，决定黑石物理服务器、集群内容器、Service的IP地址。参阅 [黑石集群网络详解][network]。
 - **容器网段**：为集群内容器分配在容器网络地址范围内的 IP 地址。参阅 [黑石集群网络详解][network]。
 - **Service网段**：为集群内service分配Service网络地址范围内的IP地址。参阅 [黑石集群网络详解][network]。
 - **集群备注**：创建集群的相关信息。
![][2]
4. 完成
5. 前往添加黑石物理服务器节点。

### 管理黑石集群节点
前置条件：已有黑石容器集群

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **黑石集群**， 点击右侧**添加节点**。
![][3]
3. 设置添加黑石节点的 **容器目录**、选择需要添加进黑石容器集群内的黑石物理服务器。
![][4]
4. 新添加的黑石容器节点将出现在 **ID/节点名** 列表中。
![][5]

### 连接黑石集群
前置条件：已有黑石容器集群

1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **黑石集群**， 选择需要连接的黑石集群进入详情页。
3. 点击查看集群凭证
![][6]
4. 根据[使用指引][]通过公网或内网连接到集群。
![][7]

您还可以直接登陆到黑石物理服务器节点直接通过Kubectl操作容器集群。

### 删除黑石集群
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的 **黑石集群**， 点击右侧**删除**。
![][8]

注：删除黑石集群仅移出黑石物理服务器，不销毁。


[1]: https://main.qcloudimg.com/raw/5721513777644435e3ef5c0007ea31d4.png
[2]: https://main.qcloudimg.com/raw/5c7cacbba5fcd0310464069b5abba746.png
[3]: https://main.qcloudimg.com/raw/464d07e282036fd80c22ca8fb122585f.png
[4]: https://main.qcloudimg.com/raw/76963ebc39c240070057f77c67c3a5e5.png
[5]: https://main.qcloudimg.com/raw/292300102120b529f046cb901529b397.png
[6]: https://main.qcloudimg.com/raw/55d2981a0db0d08964e07e8c7cca11fb.png
[7]: https://main.qcloudimg.com/raw/509d665d9728494921b5ffc2a46ad8fb.png
[8]: https://main.qcloudimg.com/raw/c30a9ac3d5777bd87ea9de3e10919e18.png




[network]:待补充
