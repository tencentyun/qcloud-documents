使用 Hue 之前，您首先需要通过 EMR 的快捷入口登录Hue，且 Hue 上的用户名建议是 hadoop。

进入 Hue 的 Hive 编辑模式，并选择对应的数据库

![选择数据库](https://mc.qcloudimg.com/static/img/c3e31e8338d7e6df80720becf819d2cd/5-8-1-1.png)

在 Hue 的 Hive SQL 编辑框里面输入 hive-SQL 创建表和导入数据

``` sql
drop table hive_test;
create table hive_test (a int, b string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ’,’;
load data local inpath "/usr/local/service/hadoop/bin/hive_test.data" into table hive_t
```

单击执行按钮如下图：

![执行](https://mc.qcloudimg.com/static/img/4e4de2b2e7cd5b7d67948b868582f508/5-8-1-2.png)

Hue 可以将查询结果以图表的方式展示，执行这个 SQL

``` sql
select * from hive_test limit 10;
```

执行完成后，结果数据如图所示：

![执行结果](https://mc.qcloudimg.com/static/img/8dadf3d5017f54cd98ab265034301bb4/5-8-1-3.png)

选择图例模式，在这里选择了"pie"，可以看到结果图

![结果图](https://mc.qcloudimg.com/static/img/d6df0d611093a07d841aad1376dc3a8b/5-8-1-4.png)
