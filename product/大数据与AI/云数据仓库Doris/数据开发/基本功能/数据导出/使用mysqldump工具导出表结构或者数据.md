Doris 在 0.15 之后的版本已经支持通过 `mysqldump` 工具导出数据或者表结构。

## 使用示例
### 导出
1. 导出 test 数据库中的 table1 表：`mysqldump -h127.0.0.1 -P9030 -uroot --no-tablespaces --databases test --tables table1`。
2. 导出 test 数据库中的 table1 表结构：`mysqldump -h127.0.0.1 -P9030 -uroot --no-tablespaces --databases test --tables table1 --no-data`。
3. 导出 test1，test2 数据库中所有表：`mysqldump -h127.0.0.1 -P9030 -uroot --no-tablespaces --databases test1 test2`。
4. 导出所有数据库和表 `mysqldump -h127.0.0.1 -P9030 -uroot --no-tablespaces --all-databases`。

更多的使用参数可以参考`mysqldump` 的使用手册。

### 导入
`mysqldump` 导出的结果可以重定向到文件中，之后可以通过 source 命令导入到 Doris 中 `source filename.sql`。

## 注意
1. 由于 Doris  中没有 mysql 里的 tablespace 概念，因此在使用 mysqldump 时要加上 `--no-tablespaces` 参数。
2. 使用 mysqldump 导出数据和表结构仅用于开发测试或者数据量很小的情况，请勿用于大数据量的生产环境。
