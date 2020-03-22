
如您需要阅读或下载全量开发文档，请参见 [TDSQL开发指南](https://cloud.tencent.com/document/product/557/7714)。

由于事务操作的数据通常跨多个物理节点，在分布式数据库中，类似方案即称为分布式事务。TDSQL（5.7或以上版本）默认支持分布式事务，并且对客户端透明，业务像使用单机事务一样使用。例如：
```
	begin; //开启事务
	delete
	update //操作数据，可以跨set
	select
	insert
	commit; //提交事务
```

为便于事务新增 sql 用于查询特定事务的信息：
- select gtid()，获取当前分布式事务的 gtid (事务的全局唯一性标识)，如果该事务不是分布式事务则返回空。
gtid 的格式：
‘网关id’-‘网关随机值’-‘序列号’-‘时间戳’-‘分区号’，例如 c46535fe-b6-dd-595db6b8-25
- select gtid_state(“gtid”)，获取“gtid”的状态，可能的结果有：
  - “COMMIT”，标识该事务已经或者最终会被提交。
  - “ABORT”，标识该事务最终会被回滚。
  - 空，由于事务的状态会在一个小时之后清除，因此有以下两种可能：
  a)一个小时之后查询，标识事务状态已经清除。
  b)一个小时以内查询，标识事务最终会被回滚。
当 commit 执行超时或者失败的时候，应该等待几秒之后再调用该接口来查询事务的状态。

- 运维命令：
	xa recover：向后端 set 发送 xa recover 命令，并进行汇总。
	xa lockwait：显示当前分布式事务的等待关系（可以使用 dot 命令将输出转化为等待关系图）。
	xa show：当前网关上正在运行的分布式事务。

#### 补充
TDSQL 分布式事务采用两阶段提交算法（2PC），隔离级别配置为 read committed, repeatable read，或者 serializable。
