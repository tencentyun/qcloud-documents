## 新增功能
- 几乎兼容原yun版本与mig版本的所有接口功能
- 提供一个接口删除manager由于磁盘满安装失败产生的告警
- group回档可以指定ip，并且提供一个接口能够获取回档前set列表，与之配套使用
- 自适应manager的运行模式（manager区分合并模式和分离模式）
- 提供一个能够修改group级别配置的接口
- 根据购买实例时的global_mc_enable决定是否开启一致性读
- 支持多源同步topic迁移功能
- string类型参数可以根据版本号指定合法值集合
- 支持几个数据库参数配置：
	- sql_require_primary_key
	- innodb_flush_log_at_trx_commit
	- sync-binlog


## 功能优化
- 分离模式下网关组迁移，支持同版本扩容、定时卸载旧端口、重置任务信息等
- 分离模式下提供sync信息给赤兔
- group回档支持gts参数
- 调用备份接口时，新购买的set冷备节点不完整，返回更加精确错误信息
- 数据库参数列表根据调用方过滤掉不想显示的配置项
- 支持修改账号读写(read_only)方式

