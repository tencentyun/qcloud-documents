使用数据湖 DLC，您仅需一分钟即可完成对象存储 COS 上的数据分析查询，目前支持 CSV、ORC、PARQUET、JSON、ARVO、文本文件等多个格式。
## 前置准备
### 设置必要 DLC 内部权限
>? 如果用户已经有权限，或者为主账户管理员，可忽略此步骤。

若您是首次登录的子账号，除了必要的 CAM 授权，还需要请任意 DLC 管理员或主账号管理员在 DLC 控制台左侧**权限管理**菜单，为您授予必要的 DLC 权限（详细权限说明参见 [DLC 权限概述](https://cloud.tencent.com/document/product/1342/61548)）：
1. 库表权限：可授予对应的 catalog、database、table，view 等读写操作权限。
2. 引擎权限：可授予计算引擎的使用、监控、修改等权限。

>? 系统会默认为每个用户开通基于 presto 内核的共享 public-engine，方便您可以快速试用，无需先购买独享集群。

详细权限授予步骤参见 [子账号权限管理](https://cloud.tencent.com/document/product/1342/61976)。

## 分析步骤
### 步骤1：创建数据库
如果您对 SQL 语句熟悉，可直接在查询中编写 create database 语句，跳过创建向导。
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择**服务地域**。
2. 左侧导航菜进入**数据探索**。
3. 选择**库表**，单击“+”，选择**创建数据库**进行数据库新建。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dd7c1a210e5a81a31dbd3cb54401efed.png)
4. 右上角选择执行引擎后，执行生成的 create database 语句，完成建库。
![](https://qcloudimg.tencent-cloud.cn/raw/d1254e5a6db8c587919ac7ed87d36988.png)
详细操作步骤及配置方式可参见 [数据库管理](https://cloud.tencent.com/document/product/1342/61666)。

### 步骤2：创建外表
如果您对 SQL 语句熟悉，可直接在查询中编写 create table 语句，跳过创建向导。
1. 登录[ 数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域。
2. 左侧导航菜进入**数据探索**。
3. 选择库表，选中当前创建的表后，右键单击，选择**创建外表向导**。

>? 外表一般指数据文件放到您自己账号下的 COS 桶，DLC 可以直接建立外表进行分析，无需额外加载数据。基于外表的特性，例如在执行 drop table 等动作时，DLC 并不会删除您的原始数据，只会删除 table 的元信息。

![](https://qcloudimg.tencent-cloud.cn/raw/bd8df9e5c2c7170e58187f5655756a16.png)

4. 按照向导生成创表语句，按照**基本信息 > 数据格式 > 编辑列 > 编辑分区**，完成各个步骤。
	- step1:  选择数据文件存放的 COS 路径（路径必须是 COS 桶下的目录，不能直接建立到 COS 桶），此处也提供快速上传文件到 COS 的快捷方式。操作需具备 COS 相关的权限。
![](https://qcloudimg.tencent-cloud.cn/raw/c485667a12424cc4ecdbcbea102f1885.png)
	- step2: 选择数据文件的格式，**高级选项**中可选择自动推断格式，后端将解析文件格式，自动生成表的列信息，快速完成列信息推断。
![](https://qcloudimg.tencent-cloud.cn/raw/e98374d1bcaa7e4f8ab8330125dde811.png)
>? 结构推断为建表辅助工具，不能保证100%正确，仍需您进行复查核对字段名、类型是否符合预期，根据实际情况编辑修改为正确的信息。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2c65ac96392d20eab9ab187fd596d1c7.png)
	- step3: 如果没有分区可以跳过此步骤，合理的分区可以帮助提升分析性能。详细分区信息可参见 [查询分区表](https://cloud.tencent.com/document/product/1342/61979)。
![](https://qcloudimg.tencent-cloud.cn/raw/6aa17596364cd2d0bae431271b3a3b1b.png)
5. 单击**完成**，会生成 SQL 建表语句，选择数据引擎后执行生成的语句即可完成建表。
![](https://qcloudimg.tencent-cloud.cn/raw/594e37c741e8501706147ccae3a9c98e.png)


### 步骤4：执行 sql 分析
数据准备完备后，您就可以开始书写 SQL 分析语句，选择合适的计算引擎，开始数据分析。
![](https://qcloudimg.tencent-cloud.cn/raw/433b56e9351557cb25fd1e23cb8e2d4a.png)

#### 示例
编写数据查询所有结果为 SUCCESS 记录的 SQL 语句，选择计算引擎后执行。
```
select * from `DataLakeCatalog`.`demo2`.`demo_audit_table` where _c5 = 'SUCCESS'

```
执行结果如下：
![](https://qcloudimg.tencent-cloud.cn/raw/ab60c721a3660daf3e9369b9ac673bd4.png)






