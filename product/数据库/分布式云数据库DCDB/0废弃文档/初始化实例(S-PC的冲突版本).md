云数据库(TDSQL)在购买后，需要对实例进行（批量）初始化，初始化后方可正常使用实例，如下图
![](//mccdn.qcloud.com/static/img/7d6e94d91a4c132d70462029f1397ced/image.png)

目前需要初始化一下参数：

- 	支持字符集：character_set_server
- 	表名大小写敏感：lower_case_table_names
- 	INNODB引擎数据页大小：innodb_page_size（MySQL默认值为16K，修改该值将影响Innodb索引数据页长度，影响索引创建，但该值越小，性能越好。）