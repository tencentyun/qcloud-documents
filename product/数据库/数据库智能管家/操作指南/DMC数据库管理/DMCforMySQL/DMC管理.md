## 新建库表
1. 登录 [DMC 控制台](https://bj-dmc.cloud.tencent.com/v2/qcloudLogin/login)，在导航栏选择【新建】>【新建库】>【新增数据库】或【新建】>【新建表】。
2. 在弹出的对话框中，用户可以对新建的库表进行配置，配置完成后单击【提交】即可。
 - 新建库对话框：
![](https://main.qcloudimg.com/raw/258605b4ac20f2136672bab0381e0f3f.png)
 - 新建表对话框：
![](https://main.qcloudimg.com/raw/d2aec4106f019ff9d088be7c27737330.png)

## 实例会话管理
在导航栏单击【实例会话】进入实例会话管理页，用户可查看当前数据库中所有实例的会话详细信息，以及按照会话概览、用户、访问来源和数据库四个不同维度的信息展示。
DMC 提供 kill 会话的功能，方便用户对会话进行管理。
![](https://main.qcloudimg.com/raw/dd87caaefb78386484ebb58bfdbdc6e4.png)

## 数据库实时监控
在导航栏单击【实时监控】进入数据库实时监控页，数据库实时监控功能每4秒刷新一次，提供如下监控信息：

MySQL Status Information|  InnoDB Row Operation |   Thread   |Network
---|---|---|---
[qps] 表示每秒响应的查询次数 | [read] 表示 InnoDB 存储引擎表的读取记录行数 | [running] 表示活跃的连接数，即正在执行 sql 的连接 |[in(KB)] 表示进入实例的网络流量
[tps] 表示每秒处理的事务个数 | [insert] 表示 InnoDB 存储引擎表的写入记录行数| [connected] 表示连接在实例上的空闲连接，即未执行 sql 的连接| [out(KB)] 表示流出实例的网络流量
[ins] 表示 insert 语句每秒执行次数 | [update] 表示 InnoDB 存储引擎表的更新记录行数 |-  |- |
[upd] 表示 update 语句每秒执行次数 | [delete] 表示 InnoDB 存储引擎表的删除记录行数|- |- |
[del] 表示 delete 语句每秒执行次数 |- |- |- |
[sel] 表示 select 语句每秒执行次数 | -|- | - |
[hit%] 表示缓存命中率，主要指 innodb_buffer_pool 的命中率 | - | - |- |

## InnoDB 锁等待管理
在导航栏单击【InnoDB锁等待】进入 InnoDB 锁等待管理页，用户可以直观地查看持有锁及等待锁详情，并可以进行删除会话操作。如下图：
![](https://main.qcloudimg.com/raw/ea4ebed0ba1a6e8b804af1554c09d3e6.png)
![](https://main.qcloudimg.com/raw/746daa00522aa773c96c1248570a4537.png)

## 内嵌 phpMyAdmin
在导航栏单击【前往PMA】可进入腾讯 DMC 内置的 phpMyAdmin 进行相关数据库操作，phpMyAdmin 支持大多数 MySQL功能，包括：
- 浏览和删除数据库、表、视图、字段以及索引。
- 创建、复制、删除、重命名以及更改数据库、表、字段、索引。
- 维护服务器、数据库和表以及有关的服务器配置。
- 执行、编辑 SQL 语句。
- 管理存储过程和触发器。

## DBbrain 智能优化
在导航栏单击【DBbrain智能优化】可进入 DBbrain 控制台。
