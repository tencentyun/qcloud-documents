Hive 默认如下查询：

``` sql
select * from tablename where a=’1’ limit 10;
```

是不会启动计算任务的，您可以通过添加如下参数 `set hive.fetch.task.conversion=none` 来开启分布式查询。
