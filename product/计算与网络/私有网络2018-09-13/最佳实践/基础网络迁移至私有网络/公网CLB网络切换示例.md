本文介绍如何将公网CLB业务从基础网络平滑迁移至私有网络。
>?本示例仅供参考，实际迁移的场景可能较示例更复杂，请在迁移前仔细评估影响，谨慎地制定迁移方案。

### 迁移示例
基础网络中使用了 DNS、CLB、CVM、MySQL、Redis 产品。DNS 中访问域名映射为基础网络公网 CLB VIP，其中公网 CLB 绑定了两台云服务器 CVM1 和 CVM2 作为后端服务器，CVM1 和 CVM2 上部署了应用服务，应用服务会访问后端的云数据库服务 Rdeis 和 MySQL。
迁移要求：要求业务平滑切换至私有网络。
![](https://main.qcloudimg.com/raw/47306535fde541d174012cfa762ba746.png)


### 迁移步骤
1. 参见 [创建私有网络](https://cloud.tencent.com/document/product/215/36515) 创建 VPC 网络。
2. 参见 [更换 MySQL 的网络](https://cloud.tencent.com/document/product/236/35671) 和 [更换 Redis 的网络](https://cloud.tencent.com/document/product/239/30910?from=10680#.E6.9B.B4.E6.8D.A2-redis-.E7.BD.91.E7.BB.9C) 切换数据库网络。云数据库在网络切换时连接不中断，且切换后同时保持原基础网络和新 VPC 网络 IP，可确保迁移过程中不停服，在原有基础网络的访问的最长保持时间内，完成其他产品的迁移。
   ![](https://main.qcloudimg.com/raw/d3a4a990141bd75f162d62e6bebfe555.png)
3. 参见 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942) 在基础网络制作两台云服务器 CVM1 和 CVM2 的镜像，在私有网络内，参见 [通过镜像创建实例](https://cloud.tencent.com/document/product/213/44265) 创建两个 CVM。完成后，测试 CVM 是否能正常访问云数据库。
![](https://main.qcloudimg.com/raw/ffe2eb1cbdb9cb860ca872fd3c251799.png)
4. 在私有网络内，新建一个公网 CLB，并绑定上述新建的两个 CVM，注意检查健康状态，避免因异常情况影响服务。
![](https://main.qcloudimg.com/raw/1025a688c01db399d3061a68d4d66c20.png)
5. 为确保业务平滑切换，可直接切换 DNS IP 到 VPC 中公网 CLB 的 VIP。
6. 待所有服务完成迁移后，释放基础网络下留存的公网 CLB、CVM 资源，结束迁移。
![](https://main.qcloudimg.com/raw/6b0488e853bd84e0d424fd17120fef95.png)
