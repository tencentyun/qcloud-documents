## 新增功能
- 增加hdfs冷备主动告警
- 增加增量备份脚本xtrabackup限速参数
- 增加安装过程zk连接重试
- 增加slowlog入es的功能：当全局开关agent@global中slowtoes=1时，agent将慢查询分析的结果以json格式写到agent/log下的jsonSlow.log中后续上报到es
- 增加安装工具生成es配置功能：
	- 新增一个模块，每个db机器常驻一个进程，类似于oc_agent，用于收集agent/proxy日志到es
	- 安装工具负责在每个实例新安装时写配置文件到该模块目录下，用于指定类型和收集路径
- 增加水平扩容删除range/list分区逻辑：对于新增的range/list分区，增加扩容清理逻辑
- 增加db的mc开关和gts变量设置
- 容灾补偿xa commit添加gts
- 安装工具增加网关mc配置项
- 增加groupshard指定gts回档功能
- 增加回档和安装过程中细化错误码
- 增加mariadb版本mysql.gtid_slave_pos表的自动清理
- 增加分离版本同版本网关安装
- 增加安装dcagent kafka单独地址配置



## 功能优化
- 支持回档过程中从多个历史冷备节点的binlog恢复数据: 避免从回档镜像产生时间到回档结束时间中间出现冷备角色切换，导致数据错误
- 回档结束后会等待心跳正常再返回任务结束: 避免回档结束后立即触发主备切换
- 调整回档并行复制参数: 将binlog伪造成relaylog回放，在遇到非自然切分binlog事件时会导致并行复制出错，调整参数规避
- 优化binlog001清理逻辑: 尽可能快的清理binlog001
- 优化percona检查relaylog回放判断为gtid集合比较
- 数据盘删除自动触发切换优化: percona5.7和mariadb10.1的版本在手动删除数据盘目录后可以自动切换
- 主备延迟上报优化: 
	- 3s内的延迟会被矫正忽略; 
	- 针对夏令时的场景可以正确处理
- binlog备份优化: 
	- 增加set级别的binlog冷备开关; 
	- 允许配置文件调整binlog冷备间隔时间
- 优化数据迁移: 支持oss接口配置数据迁移参数
- 优化slave_flag配置项
	- 增加slave_flag=2配置，优先选择备机，失败的情况下选择主机
	- slave_flag支持oss接口配置（zk配置有更高优先级）
- 支持kms表空间加密
- 默认关闭tdsqlsys_normal super权限
- 调大配置文件默认dcnlimit和coldbackuplimit到30MB，dcn建立优先从网卡获取限速
- 慢查询备份调整：
	- 扩大慢查询分析开关的控制范围，当关闭开关时，彻底不做备份避免io
	- 调整逐行读取写入的备份方式为dd append，降低io和cpu开销
- 回档镜像时间判断调整：将回档选取冷备镜像的时间由hdfs文件系统时间调整为文件名中记录的备份结束时间，可支持离线跨集群回档
- 历史会话输出调整：调整为纯json格式输出，processlist, explain, trace拆分为三种文件，便于es解析，同时避免清理不及时的问题
- 扩容删除分区过滤云平dts服务：云平new dts服务会影响水平扩容删分区流程，增加兼容逻辑
- 安装过程各模块标准输出重定向到/dev/null
- 调整历史会话默认开关为关闭
- 当主备切换备机也发生故障重启时，会由于db没有持久化master_pos导致agent上报同步位置异常。
- agent发现备机重启后会解析relaylog尝试获得正确的位置，并持久化到本地，即使在apply任务中
- relaylog被清理，也可以从缓存中正确拿到之前解析的位置
- 扩容只读任务条件判断调整
	- 由延迟检查调整为gtid检查，避免受时间误差影响
	- 调整只读超时时间
- cpu规格配置调整
	- 当购买cpu核数大于1核时不再自动x2
	- 上报cpu占用时用实际cpu配置
- alldump脚本grep参数去掉-P
- range/list水平扩容保留表结构
- 逻辑回档删除多余库表过滤xa库
- 支持指定优先的idc备机成为冷备节点


## BUG修复
- 修复cos备份binlog在来回切换冷备节点时，部分binlog备份不完整的问题
- 修复cos备份binlog可能的死循环问题
- 修复数据迁移长时间导致的myloader管道阻塞
- 修改清理binlog，配置overuse_flag默认值为2
- 修复过多ps进程问题（由14.54 R656引入)
	- R656版本开始有历史会话功能，为避免重复开启子进程获取processlist，引入了ps做互斥，但频率过高，实例过多的情况下cpu会占用很高
	- 新版本去掉了ps，换用文件锁做互斥
- 修复主备切换后errlog备份可能导致的io高问题
	- 旧版本只有主机处理errlog备份，当备机切换为主机后，积累的大量errlog开始备份导致io高
	- 新版本主备都会定时将errlog备份到本地的errorlog.date（不再用errlog.last），并定时清理4天前的errlog本地备份
- 修复水平扩容偶发的agent由于重连失效导致无法删除分区的问题
- 修复binlog位数溢出不能正常清理问题
- 修复keyring无法正常更新问题
- 修复逻辑扩容强制备机拉镜像的问题




