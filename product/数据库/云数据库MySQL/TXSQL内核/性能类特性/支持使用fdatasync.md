## 功能介绍
redo 日志文件目前采用 fsync 系统调用来落盘，包括文件元数据落盘和文件数据落盘。文件元数据信息包括最后修改时间等不是非常重要的信息，在一些 redo 落盘场景可以避免总是刷文件元数据到存储设备上（通过 fdatasync 系统调用），来减少开销。

## 支持版本
- 内核版本 MySQL 5.7 20201230 及以上
- 内核版本 MySQL 8.0 20201230 及以上

## 适用场景
主要适用于写入压力比较大的场景。

## 性能数据
在 sysbench-write-only 高并发持续写入场景下，TPS 性能有10%左右提升。

## 使用说明
通过设置参数 innodb_flush_redo_using_fdatasync=true/false 来控制是否用 fdatasync 来避免 redo 日志文件元数据实时落盘。缺省为 false。

| 参数名                            | 动态 | 类型 | 默认  | 参数值范围 | 说明                        |
| --------------------------------- | ---- | ---- | ----- | ---------- | --------------------------- |
| innodb_flush_redo_using_fdatasync | yes  | bool | false | true/false | 是否使用 fdatasync 方式刷 redo |

