创建 NAT 网关后，需要配置路由规则，将子网流量指向 NAT 网关。
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧目录中单击【路由表】。
2. 在路由表列表中，单击需要访问 Internet 的子网所关联的路由表 ID 进入详情页。
![](https://main.qcloudimg.com/raw/d9149a32b451867c5ccd4c171f58d963.png)
3. 单击【+新增路由策略】。
4. 在弹框中输入目的端（需访问的公网 IP 地址段），下一跳类型选择【NAT 网关】，下一跳选择已创建的 NAT 网关 ID。
![](https://main.qcloudimg.com/raw/668a7b0de070b67c9f42f264a0fca1f7.png)
5. 单击【创建】完成以上配置后，关联此路由表的子网内的云服务器访问 Internet 的流量将指向 NAT 网关。
