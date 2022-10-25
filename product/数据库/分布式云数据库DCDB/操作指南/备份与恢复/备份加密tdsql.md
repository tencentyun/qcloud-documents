## 功能概述
分布式数据库 TDSQL MySQL版 提供透明数据加密（Transparent Data Encryption，TDE）功能，透明加密指数据的加解密操作对用户透明，支持对数据文件进行实时 I/O 加密和解密，在数据写入磁盘前进行加密，从磁盘读入内存时进行解密，可满足静态数据加密的合规性要求。

数据透明加密（TDE）当前仅支持 MySQL 8.0.24 版本和香港地区 Percona 5.7 版本，后续将陆续开放。您可以通过在 [TDSQL 控制台](https://console.cloud.tencent.com/tdsqld/instance-tdmysql) 的实例管理页的**数据安全性** > **数据加密**进行访问。

开启数据加密后，暂时不支持用备份文件在本地恢复数据库实例，推荐采用 [回档数据库](https://cloud.tencent.com/document/product/557/70277) 进行恢复。 
>?如需使用数据加密功能，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。


## 注意事项
- 目前实例 [开启密钥管理系统 KMS](https://cloud.tencent.com/document/product/573/38406) 后，不可创建灾备/只读实例。
- TDE 加密功能开通后无法关闭。
- 开启 TDE 加密功能后，可提高静态数据的安全性，但同时会影响访问加密数据库的读写性能，请结合实际情况选择开启 TDE 加密功能。
- 开启 TDE 加密功能后，会增加 CPU 资源的消耗，大约会影响5%左右的性能。
