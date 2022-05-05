## 功能介绍
该功能主要用于删除数据文件很大的表，避免 IO 的抖动。

DROP TABLE 会将原数据库文件 (.ibd) 重命名为一个新的临时文件并返回成功，临时文件存放在 innodb-async-drop-tmp-dir 指定的目录下，并在后台分批次 truncate，每次 truncate 的文件大小由 innodb-async-truncate-size 控制；异步删表功能的开启由 innodb-async-drop-tmp-dir 参数控制，如果不为空，则开启。

该功能无需用户操作，由内核自动完成，其原理是在删除表时，为表的数据文件在另外一个目录中创建一个硬连接。当执行 drop table 后，删除的只是该文件的一个硬连接。之后后台线程扫描到硬连接目录中有需要删除的文件，自动在后台 truncate 前面 drop 掉表数据文件。

## 支持版本
- 内核版本 MySQL 5.6 20190203 及以上
- 内核版本 MySQL 5.7 20190203 及以上
- 内核版本 MySQL 8.0 20200630 及以上

## 适用场景
该功能适用于需要删除的表数据文件很大的场景。

## 使用说明
设置 innodb_async_truncate_work_enabled 为 ON，DROP TABLE 即会变成异步模式，默认值为 OFF。
每次 truncate 的文件大小由 innodb_async_truncate_size 控制。

| 参数名                             | 动态 | 类型   | 默认 | 参数值范围                        | 说明                            |
| ---------------------------------- | ---- | ------ | ---- | ------------------------- | ------------------------------ |
| innodb_async_truncate_work_enabled | Yes  | string |  OFF   | ON/OFF      | 是否开启异步清理大表          |
| innodb_async_truncate_size         | Yes  | int    | 5.7，20210630及其之前的版本，默认值128<br>5.7，20211030及其之后的版本，默认值64  | 5.7，20210630及其之前的版本，范围：128MB - 2048MB<br>5.7，20211030及其之后的版本，范围：16MB - 256MB | 异步 DROP TABLE 在后台每次 truncate 文件大小，单位MB |

