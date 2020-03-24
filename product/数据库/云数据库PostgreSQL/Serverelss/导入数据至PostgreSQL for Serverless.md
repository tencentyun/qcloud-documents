
当前支持通过 psql 导入从 pg_dump 备份下来的数据至 PostgreSQL for Serverless。

#### 操作流程
如您的数据已经在自建 PostgreSQL 上，可以使用 psql 命令将数据轻松的迁移至 PostgreSQL for Serverless 中。
迁移数据的工作主要分为两大部分：
1. 使用 pg_dump 命令进行逻辑备份，创建转储数据。
2. 将上一步的备份数据恢复至 PostgreSQL for Serverless 上。


准备操作：已完成 PostgreSQL for Serverless 实例的准备，如未完成，请参见 [购买实例](https://cloud.tencent.com/document/product/409/7550) 和 [连接实例](https://cloud.tencent.com/document/product/409/40429)。

### 步骤一：导出数据
使用 PostgreSQL 客户端连接本地数据库，执行如下命令，备份数据。
```
pg_dump -U username -h hostname -p port -O databasename -f filename
```
>?为避免执行权限问题，需要加入-O参数。

| 参数         | 说明                                |
| ------------ | ----------------------------------- |
| username     | 本地数据库用户名                    |
| hostname     | 本地数据库主机名                    |
| port         | 本地数据库端口号                    |
| databasename | 要备份的本地数据库名                |
| filename     | 要生成的备份文件名称，如 mydump.sql |


### 步骤二：导入数据至 PostgreSQL for Serverless
准备操作：先将备份好的数据上传至与 PostgreSQL for Serverless 实例同一私有网络的云服务器上，然后通过内网进行数据恢复，以保证网络的稳定和数据的安全。

登录云服务器后，在 PostgreSQL 客户端中，执行如下命令，恢复数据。
```
psql -U username -h hostname -d desintationdb -p port -f dumpfilename
```

>?在导入过程中，可能会存在部分报错，可根据报错原因分析具体原因，某些报错不影响数据导入。

| 参数          | 说明                                     |
| ------------- | ---------------------------------------- |
| username      | PostgreSQL for Serverless 的数据库用户名 |
| hostname      | PostgreSQL for Serverless 的数据库地址   |
| desintationdb | PostgreSQL for Serverless 的数据库名     |
| port          | PostgreSQL for Serverless 的数据库端口号 |
| dumpfilename  | 备份数据文件名，如 mydump.sql            |
