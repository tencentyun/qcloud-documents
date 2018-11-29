Hive 默认查询如下：

``` sql
select * from tablename where a=’1’ limit 10;
```

默认查询不会启动计算任务，您可以通过添加如下参数 `set hive.fetch.task.conversion=none` 来开启分布式查询。
