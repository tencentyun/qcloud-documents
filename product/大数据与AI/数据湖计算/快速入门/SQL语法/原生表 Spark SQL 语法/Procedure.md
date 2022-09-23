## 基本句法
```
CALL catalog_name.system.procedure_name(arg_name_2 => arg_2, arg_name_1 => arg_1);
```

```
CALL catalog_name.system.procedure_name(arg_1, arg_2, ... arg_n);
```

## Snapshot 管理
### rollback_to_snapshot
回滚快照到指定版本。
输入参数：表名和版本号。
```
CALL `DataLakeCatalog`.`system`.rollback_to_snapshot('validation.dempts', 1);
```

### rollback_to_timestamp
回滚快照到指定时间戳。
输入参数：表名和时间戳。
```
CALL `DataLakeCatalog`.`system`.rollback_to_timestamp('validation.dempts', TIMESTAMP '2022-08-11 19:49:43.224');
```


### set_current_snapshot
设置当前快照版本。
输入参数：表名和版本号。
```
CALL `DataLakeCatalog`.`system`.set_current_snapshot('validation.dempts', 1);
```


### cherrypick_snapshot
从指定快照版本 cherrypick 到当前快照。
```
CALL `DataLakeCatalog`.`system`.cherrypick_snapshot('validation.dempts', 1);
CALL `DataLakeCatalog`.`system`.cherrypick_snapshot(snapshot_id => 1, table => 'my_table' )
```


## Metadata 管理
### expire_snapshots
清理过期快照，减少小文件数。
```
CALL `Catalog`.`system`.expire_snapshots(table_name, [older_than], [retain_last], [max_concurrent_deletes], [stream_results]);
```

示例：
```
CALL `DataLakeCatalog`.`system`.expire_snapshots('validation.dempts', TIMESTAMP '2021-06-30 00:00:00.000', 100);
```


### remove_orphan_files
移除不再被引用元数据文件。
```
CALL `Catalog`.`system`.remove_orphan_files(table_name, [older_than], [location], [dry_run], [max_concurrent_deletes]);
```

示例：
```
CALL `DataLakeCatalog`.`system`.remove_orphan_files(`table`=>'validation.dempts', dry_run=>TRUE);
CALL `DataLakeCatalog`.`system`.remove_orphan_files(`table`=>'validation.dempts', `location`=>'cosn://channingdata-1305424723/example2/');
CALL `DataLakeCatalog`.`system`.remove_orphan_files('validation.dempts', TIMESTAMP '2022-07-10 17:25:19.000');
```



### rewrite_data_files
数据文件合并重写，即小数据文件合并。
```
CALL `Catalog`.`system`.rewrite_data_files(table_name, [strategy], [sort_order], [options], [where]);
```

示例：
```
CALL `DataLakeCatalog`.`system`.rewrite_data_files('validation.dempts');
CALL `DataLakeCatalog`.`system`.rewrite_data_files(`table`=>'validation.dempts', `strategy`=>'sort', `sort_order`=>'id DESC NULLS LAST,data ASC NULLS FIRST');
CALL `DataLakeCatalog`.`system`.rewrite_data_files(`table`=>'validation.dempts', `options`=>map('min-input-files','2'));
CALL `DataLakeCatalog`.`system`.rewrite_data_files(`table`=>'validation.dempts', `where`=>'id = 3 and data = "foo"');
```


### rewrite_manifests
manifests 文件合并重写。
```
CALL `Catalog`.`system`.rewrite_manifests(table_name, [using_caching]);
```

示例：
```
CALL `DataLakeCatalog`.`system`.rewrite_manifests('validation.dempts');
CALL `DataLakeCatalog`.`system`.rewrite_manifests('validation.dempts', FALSE);
```


### ancestors_of
获取快照的血缘信息。
```
CALL `Catalog`.`system`.ancestors_of(table_name, [snapshot_id]);
```

示例：
```
CALL `DataLakeCatalog`.`system`.ancestors_of('validation.dempts');
CALL `DataLakeCatalog`.`system`.ancestors_of('validation.dempts', 1);
```



