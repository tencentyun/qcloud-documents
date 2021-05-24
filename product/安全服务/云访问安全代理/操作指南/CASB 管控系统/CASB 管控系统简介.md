
CASB 管控系统以免改造的方式，实现云环境下应用中结构化数据（包括实时数据和历史数据）的存储加密，提供多种加解密及脱敏策略，为公有云供应商提供方便快捷易于部署的数据安全解决方案。

### 拓扑结构
![](https://main.qcloudimg.com/raw/e43e546f840341ce43fca97a095bed51.png)

### 实现原理

CASB 管控系统由 CASB Plugin、CASB Client、CASB 管理平台组成。

- CASB Plugin：为数据安全插件，提供数据加密使用的密码算法，用于实时数据加解密。
- CASB Client：为客户端管理工具，是数据安全工具套件。由 Extractor 和 Processor 组成，Extractor 用于提取数据库表结构，Processor 用于数据库数据的全量加密和解密。
- CASB 管理平台：提供可视化的管理控制台，提供鉴权、权限管理、数据源管理、加解密策略管理等功能。