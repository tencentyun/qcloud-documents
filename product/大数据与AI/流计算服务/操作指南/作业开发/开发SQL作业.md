## 前提条件
流计算作业需运行于流计算独享集群，若还没有集群，请参考 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。

## 创建作业
在 [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus) 中选择**作业管理 > 新建作业**，在弹窗中选择作业类型、作业名称和运行集群，单击**确定**后即可在作业列表中看到新建的作业。
![](https://main.qcloudimg.com/raw/d098169a73fc7bfe9a9c8b67f76a0816.png)
创建 SQL 作业后，在作业管理中单击要进行开发的作业名称，然后单击**开发调试**，即可在草稿状态下进行作业开发。**版本管理（草稿）**后的“（草稿）”，即表示当前正处于可编辑的草稿状态下。

## 编写和调试 SQL
开发 SQL 作业需在 SQL 编辑器中输入 SQL 分析语句。单击**插入模板**可以快速在编辑器中插入常用的 Ckafka 或 JDBC 等数据流的定义语句。单击**库表引用**可以便捷地引用表，以及查看、编辑 DDL 语句。SQL 语句编辑完成后，单击**作业参数**，在页面右侧弹出的参数界面中设置参数值，具体可参考 [作业参数](#jump)。然后单击**保存**，保存 SQL 语句和作业参数。

SQL 语句的编写请参考 [SQL 开发指南](https://cloud.tencent.com/document/product/849/18030)。 
![](https://qcloudimg.tencent-cloud.cn/raw/00aa94bfe8dacd544d71534e466023c5.png)

[](id:jump)
## 作业参数
作业参数可以在**开发调试**页面中单击**作业参数**并在侧边弹出的参数界面中设置参数值，然后单击**确定**保存作业参数信息。下文会有各参数的详细介绍说明，以帮助您更好地配置各作业参数。
![](https://qcloudimg.tencent-cloud.cn/raw/eb02e793dabb56c1bffe0b184d44d441.png)

### 引用程序包
若 [SQL 开发指南](https://cloud.tencent.com/document/product/849/48242) 中提供的内置函数不满足需求，用户可以自行开发自定义函数，并以 JAR 包的形式在**依赖管理**中上传后，方可在此添加引用程序包，并选择版本。
程序包的上传和版本管理方式可参考 [依赖管理](https://cloud.tencent.com/document/product/849/48295)。

### Checkpoint
Checkpoint 即作业快照，开启 checkpoint 之后作业会按照设置的时间间隔自动保存作业快照，用于遇到故障时作业的恢复。可设置 checkpoint 的时间间隔，设置范围在30秒 - 3600秒。

### 运行日志采集
显示当前作业的运行日志的开启状态，默认为开启。作业的运行日志将自动采集到作业所在的集群绑定的日志集和日志主题，可在**日志**页面中查看。关闭或重新打开都需重启作业才能生效。

### 高级参数
支持部分 Flink 高级参数自定义，需按照 YML 语法，并以“key: value”的形式进行配置，详情可参考 [作业高级参数](https://cloud.tencent.com/document/product/849/53391)。 

### 规格配置
可以按需配置 JobManager 和 TaskManager 的规格大小，灵活运用资源，详情可参考 [作业资源配置](https://cloud.tencent.com/document/product/849/57772)。

### 算子默认并行度
当没有在 JAR 包中通过代码显式定义算子并行度时，作业将采用用户指定的算子默认并行度。并行度与 TaskManager 规格大小决定作业所占用的计算资源。1个并行度将占用1个 TaskManager 规格大小的 CU 计算资源（当 TaskManager 规格大小为1时，1个并行度将占用1 CU 计算资源。当 TaskManager 规格大小为0.5时，1个并行度将占用0.5 CU 计算资源）。

## 语法检查
编写并保存 SQL 语句后，可进行语法检查，以避免因语法错误而导致运行失败。单击 SQL 编辑器上方的**语法检查**，可对已保存 SQL 语句进行语法检查。若语法无误，将会在页面右上方提示“语法检查成功”；若有语法错误，将提示相应语法错误，请按照提示进行修改，直至语法检查通过。

## 调试
在 SQL 语句的语法检查通过，并且已在参数设置中选择了所需的引用程序包后，可以对 SQL 作业进行调试，即用样例数据作为输入，查看输出结果和调试日志，确认作业可以正常运行且输出数据符合预期。

单击 SQL 编辑器右上方的**调试**，即可进入调试界面。在**上传调试数据**中上传本地的调试数据，单击**上传**打开本地文件选择框，选择并上传该数据源对应的文件。若有多个数据源，则需要分别进行选择和上传。调试文件需注意满足以下条件：
1. 默认使用逗号区分。
2. 调试文件仅支持 UTF-8 格式。
3. 调试文件最大支持1MB或1千条记录。
4. 数值类型仅支持普通格式，不支持科学计数法。
![](https://qcloudimg.tencent-cloud.cn/raw/765df0ce48a87129febb8b60d33b98cd.png)
### 调试Demo_sql示例
```sql
--mysql cdc 源表Data_In
CREATE TABLE `Data_In` (
  `Id`     INT NOT NULL,
  `Str_A`   VARCHAR,
  `Str_B`   VARCHAR,
  PRIMARY KEY (`Id`) NOT ENFORCED
) WITH (
  'connector' = 'mysql-cdc',           -- 固定值 'mysql-cdc'
  'hostname' = 'YourHostName',         -- 数据库的 IP
  'port' = '3306',                     -- 数据库的访问端口
  'username' = 'YourUserName',         -- 数据库访问的用户名（需要提供 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD 权限）
  'password' = 'YourPassword',         -- 数据库访问的密码
  'database-name' = 'YourDatabase',    -- 需要同步的数据库
  'table-name' = 'YourTable'           -- 需要同步的数据表名     
);

--写入doris表Data_Out
CREATE TABLE `Data_Out` (
  `Id`       INT,
  `Str_A`     STRING,
  `Str_B`      STRING,
  PRIMARY KEY (`Id`) NOT ENFORCED
) WITH (
  'connector' = 'doris',                    -- 固定值 'doris'
  'fenodes' = 'FE_IP:FE_RESFUL_PORT',       -- Doris FE http 地址
  'table.identifier' = 'dbName.tableName',  -- Doris 表名 格式：db.tbl
  'username' = 'YourUserName',              -- 访问Doris的用户名，拥有库的写权限
  'password' = 'YourPassword',              -- 访问Doris的密码
  'sink.batch.size' = '500',                -- 单次写BE的最大行数
  'sink.batch.interval' = '1s'              -- flush 间隔时间，超过该时间后异步线程将 缓存中数据写入BE。 默认值为1秒，支持时间单位ms、s、min、h和d。设置为0表示关闭定期写入。
);

insert into Data_Out
select Id,Str_A,Str_B from Data_In;
```
### 调试文件示例
```text
1,Str_A_1,Str_B_1
2,Str_A_2,Str_B_2
3,Str_A_3,Str_B_3
4,Str_A_4,Str_B_4
5,Str_A_5,Str_B_5
```
调试文件中字段顺序与数据源表字段顺序一致。

上传调试数据后，单击**开始调试**即开始试运行作业，并将在1 - 2分钟内返回调试结果，同时在调试结果下方单击**调试日志**展示调试日志。若结果符合预期，则可以继续进行作业发布；若不符合预期，请检查数据源、SQL 语句和引用程序包设置等环节是否存在问题，调整后再重新进行调试。单击**结束调试**即可回到开发页面。
### 上传调试文件
![](https://qcloudimg.tencent-cloud.cn/raw/81cf741a3c019b2f9b096a5018df4b91.png)
### 开始调试
![](https://qcloudimg.tencent-cloud.cn/raw/fda747b2ce596c6a5a643047cff1bea9.png)
### 正在调试
![](https://qcloudimg.tencent-cloud.cn/raw/1323bdbac70d3aebdd36c471ee97ba8a.png)
### 调试结果
![](https://qcloudimg.tencent-cloud.cn/raw/1df61498790f89eedae72f6fabfd51cf.png)
### 调试日志
![](https://qcloudimg.tencent-cloud.cn/raw/99d1c3726c4556cc1d14e73888eb0f2d.png)
