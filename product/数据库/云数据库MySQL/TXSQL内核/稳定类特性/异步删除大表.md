## 功能介绍
该功能主要用于删除数据文件很大的表，避免 IO 的抖动。
DROP TABLE 会将原 ibd 文件重命名为一个新的临时文件并返回成功，并在后台分批次 truncate。

## 支持版本
内核版本 MySQL 5.7 20190203 及以上

## 适用场景
该功能适用于需要删除的表数据文件很大的场景。

## 使用说明
设置 innodb_async_truncate_work_enabled 为 ON，DROP TABLE 即会变成异步模式，默认值为 OFF。
临时文件存放于 innodb_async_drop_tmp_dirr 指定的目录下，每次 truncate 的文件大小由 innodb_async_truncate_size 控制。

| 参数名                             | 动态 | 类型   | 默认 | 参数值范围                        | 说明                            |
| ---------------------------------- | ---- | ------ | ---- | ------------------------- | ------------------------------ |
| innodb_async_truncate_work_enabled | Yes  | string |  OFF   | ON/OFF      | 是否开启异步清理大表          |
| innodb_async_truncate_size         | Yes  | int    | 5.7，20210630及其之前的版本，默认值128<br>5.7，20211030及其之后的版本，默认值64  | 5.7，20210630及其之前的版本，范围：128MB - 2048MB<br>5.7，20211030及其之后的版本，范围：16MB - 256MB | 异步 DROP TABLE 在后台每次 truncate 文件大小，单位MB |

