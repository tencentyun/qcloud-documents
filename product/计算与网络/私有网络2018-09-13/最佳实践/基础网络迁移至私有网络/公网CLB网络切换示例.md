本文介绍如何将公网 CLB 业务从基础网络平滑迁移至私有网络。
>?本示例仅供参考，实际迁移的场景可能较示例更复杂，请在迁移前仔细评估影响，谨慎地制定迁移方案。

### 迁移示例
假设用户基础网络业务使用如下产品：
+ DNS 中配置域名解析地址为基础网络公网 CLB VIP。
+ 公网 CLB 绑定了两台云服务器 CVM1 和 CVM2 作为后端服务器。
+ CVM1 和 CVM2 上部署了应用服务，应用服务会访问后端的云数据库服务 Redis 和 MySQL。

**迁移要求**：业务平滑切换至私有网络。

### 迁移流程
<dx-steps>
-准备私有网络环境
-切换云数据库网络
-新建 CVM 并部署应用
-新建公网 CLB 并绑定 CVM
-切换 DNS 域名解析 IP
-释放基础网络资源
</dx-steps>

### 迁移步骤
1. 参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515) 创建 VPC 网络环境。
![](https://main.qcloudimg.com/raw/ef2cbed4956063a439b14fc469fbec59.png)
2. 参见 [更换 MySQL 的网络](https://cloud.tencent.com/document/product/236/35671) 和 [更换 Redis 的网络](https://cloud.tencent.com/document/product/239/30910?from=10680#.E6.9B.B4.E6.8D.A2-redis-.E7.BD.91.E7.BB.9C) 切换数据库网络。
>?云数据库在网络切换时连接不中断，且切换后同时保持原基础网络和私有网络 IP，可确保迁移过程中不停服。在原有基础网络访问的最长保持时间内，请完成其他产品的迁移。
>
![](https://main.qcloudimg.com/raw/6b7d6bd05d075c2be6889e8eea737ca8.png)
3. 参见 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 在基础网络制作两台云服务器 CVM1 和 CVM2 的镜像，在私有网络内，参见 [通过镜像创建实例](https://cloud.tencent.com/document/product/213/44265) 创建两个 CVM。完成后，测试 CVM 是否能正常访问云数据库。
>?如您可以接受 CVM 切换时实例重启导致的业务停服，也可以选择在业务低峰时段直接切换 CVM 网络，具体请参见 [云服务器切换私有网络服务](https://cloud.tencent.com/document/product/213/20278)。
>
![](https://main.qcloudimg.com/raw/96d9e67836e4aa19b879369bbe0f0d50.png)
4. 参见 [负载均衡快速入门 ](https://cloud.tencent.com/document/product/214/8975#qrjkjc)，在私有网络内，新建一个公网 CLB，并绑定上述新建的两个 CVM，注意检查健康状态，避免因异常情况影响服务。
![](https://main.qcloudimg.com/raw/6b465520d036dd450e1d70e5d202a905.png)
5. 切换 DNS 域名解析地址为 VPC 中公网 CLB 的 VIP。
>?如您使用的是腾讯云 DNSPod，请参考 [修改解析记录](https://cloud.tencent.com/document/product/302/42168)。
>
![](https://main.qcloudimg.com/raw/c9a954b3e8a0aa5a61dd4305175d9440.png)
6. 待私有网络运行正常后，释放基础网络下留存的公网 CLB、CVM 资源，结束迁移。
>?云数据库的原基础网络 IP 过期后将自动释放。
>
![](https://main.qcloudimg.com/raw/2f22ab531342bae572bc2b5a7b2aace0.png)
