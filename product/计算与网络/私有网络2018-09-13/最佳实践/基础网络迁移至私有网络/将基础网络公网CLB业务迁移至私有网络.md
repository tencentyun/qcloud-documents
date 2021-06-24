本文介绍如何使用混访模式将公网 CLB 业务从基础网络平滑迁移至私有网络。
>?本示例仅供参考，实际迁移的场景可能较示例更复杂，请在迁移前仔细评估影响，谨慎地制定迁移方案。
>

### 迁移说明
如下图所示，基础网络的服务使用了 CLB、CVM、云数据库 MySQL、云数据库 Redis 四个产品，它们之间的依赖关系为：
- 公网 CLB 绑定了两台 CVM 作为后端服务器。
- 云数据库 MySQL、云数据库 Redis 为两台 CVM 上部署的服务提供数据库服务。
![](https://main.qcloudimg.com/raw/47306535fde541d174012cfa762ba746.png)

### 迁移步骤
1. 迁移云数据库，利用迁移后原有基础网络仍可访问的优势，保障数据库连接不中断，不影响服务提供，且在原有基础网络的访问的最长保持时间内，完成其他产品的迁移。
![](https://main.qcloudimg.com/raw/d3a4a990141bd75f162d62e6bebfe555.png)
2. 在云数据库迁移的私有网络内，新建两个 CVM，并部署对应的服务。完成后，测试 CVM 是否能正常访问云数据库。
![](https://main.qcloudimg.com/raw/ffe2eb1cbdb9cb860ca872fd3c251799.png)
3. 在云数据库迁移的私有网络内，新建一个公网 CLB，并绑定上述新建的两个 CVM，注意检查健康状态，避免因异常情况影响服务。
![](https://main.qcloudimg.com/raw/1025a688c01db399d3061a68d4d66c20.png)
4. 待所有服务完成迁移后，释放基础网络下留存的公网 CLB、CVM 资源，结束迁移。
![](https://main.qcloudimg.com/raw/6b0488e853bd84e0d424fd17120fef95.png)
