本文为您介绍使用 TXRocks 的最佳实践 - 大量数据导入如何提升导入速度。

## 背景
- **场景**：将大量数据导入 TXRocks 引擎的数据库中，需对导入速度进行提升。
- **影响**：导入海量数据时，有可能出现 `Rows inserted during bulk load must not overlap existing rows` 错误。

## 处理方法1
1. 先删除二级索引（只保留主键索引）。
2. 根据规格和用户数据量调整内存相关参数。
>?需要根据规格和数据量，对参数 rocksdb_merge_buf_size 和 rocksdb_merge_combine_read_size 适当调大。
>
 - rocksdb_merge_buf_size 表示建索引过程中多路归并时每路数据量，rocksdb_merge_combine_read_size 表示多路归并时，各路占用总内存。
 - rocksdb_block_cache_size 表示 rocksdb_block_cache 大小，在多路归并时，建议临时调小。
3. bulk load 方式导数据。
```
SET session rocksdb_bulk_load_allow_unsorted=1;
SET session rocksdb_bulk_load=1;
...
导入数据
...
SET session rocksdb_bulk_load=0;
SET session rocksdb_bulk_load_allow_unsorted=0;
```
>?如果导入的数据本身有序，则不需要设置 rocksdb_bulk_load_allow_unsorted。
4. 重建二级索引，可以在全部数据导入完成后，逐个重建二级索引。
>!
>- 二级索引创建过程中涉及多路归并，rocksdb_merge_buf_size 为每路数据量大小，rocksdb_merge_combine_read_size 为合并过程中多路合并所使用的总内存大小。
>- 例如，建议 rocksdb_merge_buf_size 设置为64MB以上，rocksdb_merge_combine_read_size 设置为1GB以上，为避免 OOM，导入数据全部完成后务必改回原参数值。
>- 此外，每个二级索引创建过程都会消耗较多内存，建议不要同时创建较多的二级索引。

## 处理方法2
导入数据过程中，关闭 unique_check，可以提升导入性能。
```
set global unique_checks=OFF;
...
导入数据
...
set global unique_checks=ON;
```
>!处理完成后，务必将 unique_checks 改回 ON，否则后续正常事务写入的 insert 操作不会进行唯一性检查。
