数据湖计算 DLC 提供的 SQL 编辑器支持使用统一的 SQL 语句进行数据查询，兼容 SparkSQL，您使用标准 SQL 即可完成数据查询任务，详细语法说明可参见[ SQL 语法](https://cloud.tencent.com/document/product/1342/61734)。
您可以通过数据探索进入 SQL 编辑器，在编辑器内可完成简单的数据管理、多 Session 的数据查询、查询记录管理、下载记录管理。

## 数据管理
数据管理支持新增数据源、数据库管理及数据表管理。
### 新建数据目录
目前数据湖计算 DLC 支持管理 COS 及 EMR HIVE 的数据目录。操作步骤如下。
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域，登录角色需要管理员权限。
2. 进入数据探索，鼠标移入库表列表上方的![](https://qcloudimg.tencent-cloud.cn/raw/d963cf7b5aec5915e5369274e3b6939d.png)图标，单击**新建数据目录**即可进入新建流程。
![](https://qcloudimg.tencent-cloud.cn/raw/f2e49d5f8fb9e414942364286dea85eb.png)
详细操作指南可参见 [查询其他数据源](https://cloud.tencent.com/document/product/1342/66039)。

### 数据库管理
通过 SQL 编辑器，支持对数据库行进创建、删除、查看详情操作，详细操作指南可参见 [通过 SQL 管理数据库](https://cloud.tencent.com/document/product/1342/61666)。

### 数据表管理
通过 SQL 编辑器，支持对数据表进行创建、查询、查看详情操作，详细操作指南可参见 [数据表管理](https://cloud.tencent.com/document/product/1342/61870)。

### 默认数据库切换
使用 SQL 编辑器时，可以指定查询任务的默认数据库，指定后若在查询语句中未申明数据库，则查询将在默认数据库下执行。
1. 登录 [数据湖计算 DLC 控制台](https://console.cloud.tencent.com/dlc)，选择服务地域。
2. 进入数据探索，鼠标悬停需指定的数据库名称，单击![](https://qcloudimg.tencent-cloud.cn/raw/ca9b8841e37d3f8b444146c0f9d5208f.png)图标，单击**切换为默认数据库**即可将该数据库指定为默认数据库。
![](https://qcloudimg.tencent-cloud.cn/raw/930f3323d7f3bff988c13b4f98ab9f3e.png)
3. 或可以直接在默认数据库选择框切换。
![](https://qcloudimg.tencent-cloud.cn/raw/8146a8b39c5b120628acbcb427b80887.png)

## 数据查询
### Session 管理
SQL 编辑器支持多个 Session 进行数据查询，每个 Session 内的配置独立（默认数据库、使用的计算引擎、查询记录等），方便用户进行多个任务运行及管理。
- 您可以通过单击![](https://qcloudimg.tencent-cloud.cn/raw/c5576a8cc876cdde0ad4d5ea77e97c86.png)图标创建 Session，单击 tab 栏进行编辑器界面的切换。
![](https://qcloudimg.tencent-cloud.cn/raw/f0ebcc569fb84a5f19850a7902b0f5cc.png)
- 为了方便您的查询使用，常用的 Session 您可以点击保存按钮将 Session 进行保存，同时您可以通过点击![](https://qcloudimg.tencent-cloud.cn/raw/3b2fd07bb785b3f1affa9e98cb36556f.png)图标快速打开您已保存的 Session。
![](https://qcloudimg.tencent-cloud.cn/raw/85738c553ff158bb0049978ab5be1b2c.png)
- 针对已保存的 Session，您可以单击**刷新**按钮来更新同步已保存的信息，保证查询语句的准确性。
![](https://qcloudimg.tencent-cloud.cn/raw/a9d23bf01e8bb7cf4c5ec7fde8b80efa.png)
- 编辑器支持同时运行多个不同的 SQL 语句，单击**运行**按钮将会把编辑器内所有的 SQL 语句进行运行，同时拆分为多个 SQL 任务。
- 如需运行部分语句，可选中需运行的语句后单击**部分运行**。
![](https://qcloudimg.tencent-cloud.cn/raw/ed0696f8e96c3385f2fe217f5c95b388.png)

### 查询结果
通过 SQL 编辑器可直接查看查询结果，可以通过单击![](https://qcloudimg.tencent-cloud.cn/raw/1a1a6fab865faf251f9c2a88c72a3bf9.png)图表展开或收起查询结果的展示高度。
![](https://qcloudimg.tencent-cloud.cn/raw/99f60fb7526a9da293ce55fed7bae098.png)
- 控制台单个任务最多会返回1000条结果，如需更多结果可使用 API。API 相关操作说明可参见 [API 文档](https://cloud.tencent.com/document/product/1342/53787)。
- 查询结果在未指定 COS 存储路径情况下支持下载到本地，详细说明可参见 [获取任务结果](https://cloud.tencent.com/document/product/1342/61872)。

## 历史运行查询
每个 Session 可保存3个月内的运行历史，支持查看近24小时的查询结果。可通过运行历史快速查找过去执行的任务信息。详细操作可参见 [任务历史记录](https://cloud.tencent.com/document/product/1342/61874)。
## 下载历史管理
每个 Session 的下载任务可在**下载历史**中查看，可查询下载任务状态及相关参数信息。
![](https://qcloudimg.tencent-cloud.cn/raw/8a99c3cf804af13e6cbcb16a517c0383.png)
