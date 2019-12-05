
> According to test, the database audit feature supports most SQL statements. If you encounter any problems, contact Tencent Cloud personnel or send an email to vitosu@tencent.com to provide feedback.
1. Resolution of DCL, DDL and DML statements is supported.
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
2. Transaction and storage process may be divided into multiple statements.

