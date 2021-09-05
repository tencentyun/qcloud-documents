>!数据库审计功能重构升级中，敬请期待；在此期间数据库新购实例不再开放审计功能。
>
数据库审计目前已经支持绝大多数 SQL 语句，如发现存在不足，请 [联系我们](https://cloud.tencent.com/about/connect) 反馈。
- 已支持 DCL、DDL、DML 语句的解析。
```
Insert,Replace,Select,Union,Update,Delete,CreateDatabase:,CreateEvent,CreateFunction,CreateIndex,CreateLog,
CreateTable,CreateServer,CreateProcedure,CreateTablespace,CreateTrigger,CreateView,CreateUDF,CreateUser,
ShowCharset,ShowCollation,ShowColumns,ShowCreate,ShowCreateDatabase,ShowDatabases,ShowEngines,ShowErrors,
ShowEvents,ShowFunction,ShowGrants,ShowLogEvents,ShowLogs,ShowProcedure,ShowOpenTables,ShowPlugins,
ShowProcessList,ShowMasterStatus,ShowPrivileges,ShowProfiles,ShowSlaveHosts,ShowSlaveStatus,ShowTableStatus,
ShowWarnings,ShowVariables,ShowStatus,ShowTriggers,Call,DropProcedure,DropDatabase,DropEvent,DropFunction,
DropIndex,DropLogfile,DropServer,DropTables,DropTablespace,DropTrigger,DropUser,DropView,AlterDatabase,
AlterEvent,AlterFunction,AlterLogfile,AlterProcedure,AlterServer,AlterTable,AlterTablespace,AlterUser,
AlterView,Rollback,Commit,Begin,Set,SetTrans,SetPassword,Release,Grant,RenameTable,RenameUser,Revoke,
Install,StopSlave,StartSlave,StartTrans,Use,DescribeTable,DescribeStmt,Flush,Load,LoadIndex,FlushTables,
Reset,CacheIndex,TruncateTable,Lock,Unlock,SavePoint,Help,Do,SubQuery,ShowTables,Execute,Deallocate,Binlog,
Kill,Partition,PrepareRepairXACheckCheckSumAnalyzeChangeOptimizePurgeHandlerSignalResignal
```
- 事务和存储过程可能被拆分为多条语句。
