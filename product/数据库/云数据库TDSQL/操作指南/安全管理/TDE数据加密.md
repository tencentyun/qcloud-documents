## 操作场景
云数据库 MariaDB 提供透明数据加密（Transparent Data Encryption，TDE）功能，透明加密指数据的加解密操作对用户透明，支持对数据文件进行实时 I/O 加密和解密，在数据写入磁盘前进行加密，从磁盘读入内存时进行解密，可满足静态数据加密的合规性要求。

本文为您介绍如何通过控制台开启数据加密功能，以及如何加密或解密数据。

## 限制条件
- TDE 加密功能当前仅支持 MySQL 8.0.24 及以上版本和 Percona 5.7 版本。
- 需开通 [密钥管理服务 KMS](https://cloud.tencent.com/document/product/573/38406)。如未开通，请根据 TDE 加密功能引导进行开通。
- 需获得 KMS 密钥权限。如未开通，请根据 TDE 加密功能引导进行开通。

## 注意事项
- 开启 KMS 后，可能产生密钥管理服务（KMS）费用，请参见 [KMS 购买指南](https://cloud.tencent.com/document/product/573/18809)。
- TDE 加密功能开通后无法关闭。
- 若已开通灾备/只读实例，暂时不支持 TDE 加密功能。
- 开启 TDE 加密功能后，暂时不支持创建灾备/只读实例。
- 开启 TDE 加密功能后，暂时不支持用备份文件在本地恢复数据库实例，推荐采用 [回档数据库](https://cloud.tencent.com/document/product/237/8719) 进行恢复。
- 开启 TDE 加密功能后，可提高静态数据的安全性，但同时会影响访问加密数据库的读写性能，请结合实际情况选择开启 TDE 加密功能。
- 开启 TDE 加密功能后，会增加 CPU 资源的消耗，大约会影响5%左右的性能。

## 操作步骤
1. 登录 [MariaDB 控制台](https://console.cloud.tencent.com/mariadb) ，单击实例 ID 或**操作**列的**管理**，进入实例管理页面。
2. 在实例管理页，选择**数据安全性** > **数据加密**，单击“加密状态”的开关。
![](https://qcloudimg.tencent-cloud.cn/raw/7a10a89a98252499de113656fb54f22a.png)
3. 在弹出的对话框，开通 KMS 服务和授予 KMS 密钥权限，选择密钥后，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/5e031edb1415f783a6fa5ee64bae9949.png)
4. 开启了数据加密之后，需要对数据库表进行 DDL 操作才能进行数据加密或者解密，具体做法如下：
 - 数据表创建时加密：
```
CREATE TABLE t1 (c1 INT) ENCRYPTION='Y'
```
 - 已创建数据表加密：
```
ALTER TABLE t1 ENCRYPTION='Y'
```
 - 数据表解密：
```
ALTER TABLE t1 ENCRYPTION='N'
```
