## 如何开启 TKE 集群内网访问功能？

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在左侧导航栏中的**集群**，进入集群管理界面。
2. 单击需要连接的集群“ID/名称”，进入集群详情页。
3. 选择左侧导航栏中的**基本信息**，即可在基本信息页面中查看**集群APIServer信息**模块中该集群的访问地址、外网/内网访问状态、Kubeconfig 访问凭证内容等信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/863a8ebc868d5a8f4e3757ce4f253095.png)      
4. 单击**开启内网访问**。开启内网访问时，需配置一个子网，开启成功后将在已配置的子网中分配 IP 地址。
>!开启内网访问后，不能关闭，否则 API 网关会访问不到集群的 APIServer。



## 如何获取 TKE 集群 admin 角色？

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在左侧导航栏中的**集群**，进入集群管理界面。
2. 单击需要连接的集群"ID/名称"，进入集群详情页。
3. 选择左侧导航栏中的**授权管理** > **ClusterRole**，单击主界面的**获取集群admin角色**，即可获取集群 admin 角色。
![](https://qcloudimg.tencent-cloud.cn/raw/4749e3454b152bedf0c53c6c263aaa88.png)
4. 如果获取集群 admin 角色失败，一般是由于子账号没有 TKE 集群的 Cam 权限导致的，按照提示解决即可。
