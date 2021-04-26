网络拓扑用于查看私有网络下包含的所有资源，以便您实时了解私有网络的资源部署及网络连接情况。

## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航中的【网络拓扑】，进入网络拓扑图的展示界面。
    ![](https://main.qcloudimg.com/raw/c7e8ecf743767784df696cf149413d75.png)
3. 选择地域、私有网络，可查看该私有网络中包含的云资源（如云服务器、负载均衡、云数据库、NoSQL），及网络拓扑关系。
  例如，如下图所示，该 VPC 包含两个子网，其中子网 test6 中包含2个负载均衡实例，该 VPC 通过 NAT 网关、公网 LB 与 Internet 通信，通过对等连接与对端 VPC 通信。
    ![](https://main.qcloudimg.com/raw/1cc6ff3a212bc7ef26b261ba8610cba5.png)
