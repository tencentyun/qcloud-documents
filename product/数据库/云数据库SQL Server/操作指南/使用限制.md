- 禁止通过 Microsoft SQL Server Management 执行创建、删除数据库、创建、删除或修改帐号操作，如有需要可登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver) 管理操作。通过 Microsoft SQL Server Management 管理数据库，系统可能提示“执行 Transact-SQL 预计或批处理时发生了异常”。

- 双机高可用版/集群版：考虑到可能存在入侵风险，默认不开放用户 sysadmin 角色，如果您业务必须使用 sysadmin  角色，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 获取解决方案。
通过 Microsoft SQL Server Management 管理数据库，系统可能提示“您必须是 sysadmin 角色成员才能执行此操作”。

- 基础版：可提供用户 sysadmin 角色，通过设计管理员帐号进行授权。
