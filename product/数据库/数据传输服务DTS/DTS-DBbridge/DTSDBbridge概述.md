
## 概述
数据库应用服务迁移（DTS-DBbridge）是一款支持异构数据库和同构数据库之间迁移和同步的企业级产品。DTS-DBbridge 可以帮助企业实现完整数据库迁移（尤其是 Oracle 数据库），进而降低企业数据库 IT 成本和满足技术复杂度需求，适应企业多样化数据传输、数据汇聚、数据灾备等数据库架构和业务场景。

DTS-DBbridge 主要功能包括数据对象迁移评估、数据应用迁移评估、结构迁移、数据迁移、数据校验等全自动化平台功能，具有简单易用、自助操作、安全可靠的特点。

## 主要概念
- 迁移通道：指一个迁移项目，例如，您想完成一次从 Oracle 数据库到 TDSQL 的迁移，则需要先创建一个迁移通道。
- 数据源和数据端：指迁移通道连接的两端，数据流当前是单向流动的，即从数据源流向数据端。数据源即要准备迁移的数据库，数据端即要迁移到的目标数据库。
- 数据评估任务：执行数据评估所运行的任务，运行结束后产出数据对象评估报告和应用评估报告。
- 对象评估报告：数据库对象静态数据评估。
- 应用评估报告：数据库应用动态数据评估。
- 结构迁移任务：执行结构迁移所运行的任务。
- 全量数据迁移任务：执行全量数据迁移的任务，在一个迁移通道中可以重复执行多次全量数据迁移任务；如果存在迁移失败表，您可以针对单个表发起全量数据迁移。
- 数据校验任务：执行全量数据迁移后执行数据校验任务，在一个迁移通道中可以执行多次数据校验任务。
 
## 控制台功能
### 主要功能
- **数据迁移管理**
  - 新建迁移通道
  - 迁移评估
  - 结构迁移
  - 全量数据迁移
  - 数据校验
- **数据源端管理**
  - Oracle 数据源端管理
  - TDSQL 数据源端管理
  - TBase 数据源端管理
- **迁移规则管理**
- **规则模板管理**

### 辅助功能
- 系统配置管理
- 评估报告保留配置
- 用户与权限配置
- 批量抽取/装载配置
